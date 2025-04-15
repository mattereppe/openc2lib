""" Skeleton `Actuator` for CTXD profile

	This module provides an example to create an `Actuator` for the CTXD profile.
	It only answers to the request for available features.
"""
import docker
import socket
import subprocess
import json
import os
import logging
import sys
from openc2lib.profiles import slpf
from openc2lib.profiles.ctxd.data.application import Application
from openc2lib.profiles.ctxd.data.openc2_endpoint import OpenC2Endpoint
from openc2lib.types.data.ipv4_addr import IPv4Addr
import requests
from kubernetes import config, client
from kubernetes.client.rest import ApiException

from openc2lib.actuators.ctxd.ctxd_actuator import CTXDActuator
from openc2lib.profiles.ctxd.data.cloud import Cloud
from openc2lib.profiles.ctxd.data.consumer import Consumer
from openc2lib.profiles.ctxd.data.container import Container
from openc2lib.profiles.ctxd.data.encoding import Encoding
from openc2lib.profiles.ctxd.data.link_type import LinkType
from openc2lib.profiles.ctxd.data.network import Network
from openc2lib.profiles.ctxd.data.network_type import NetworkType
from openc2lib.profiles.ctxd.data.os import OS
from openc2lib.profiles.ctxd.data.peer import Peer
from openc2lib.profiles.ctxd.data.peer_role import PeerRole
from openc2lib.profiles.ctxd.data.server import Server
from openc2lib.profiles.ctxd.data.service_type import ServiceType
from openc2lib.profiles.ctxd.data.transfer import Transfer
from openc2lib.profiles.ctxd.data.vm import VM
from openc2lib.types.data.hostname import Hostname
from openc2lib.types.data.l4_protocol import L4Protocol



from openc2lib import ArrayOf, Nsid, Version,Actions, Response, StatusCode, StatusCodeDescription, Features, ResponseType, Feature
import openc2lib.profiles.ctxd as ctxd

from openc2lib.profiles.ctxd.data.name import Name
from openc2lib.profiles.ctxd.data.service import Service
from openc2lib.profiles.ctxd.data.link import Link

logger = logging.getLogger(__name__)

OPENC2VERS=Version(1,0)
""" Supported OpenC2 Version """

MY_IDS = {
	'domain': None,
	'asset_id': None
}

# An implementation of the ctxd profile (it implements my5gtestbed). 
class CTXDActuator_docker(CTXDActuator):
	""" CTXD implementation

		This class provides an implementation of the CTXD `Actuator`.
	"""

	my_services: ArrayOf(Service) = None # type: ignore
	""" Name of the service """
	my_links: ArrayOf(Link) = None # type: ignore
	"""It identifies the type of the service"""
	domain : str = None
	asset_id : str = None
	hostname: any = None
	ip: any = None
	port: any = None
	protocol: any = None
	endpoint: any = None
	transfer: any = None
	encoding: any = None
	actuators: any = None
	conn : any = None #connection to docker

	def __init__(self, domain, asset_id, hostname, ip, port, protocol, endpoint, transfer, encoding, actuators):
		MY_IDS['domain'] = domain
		MY_IDS['asset_id'] = asset_id
		self.domain = domain
		self.asset_id = asset_id
		self.hostname = hostname
		self.ip = ip
		self.port = port
		self.protocol = protocol
		self.endpoint = endpoint
		self.transfer = transfer
		self.encoding = encoding
		self.actuators = actuators
		
		self.connect_to_docker()

		self.my_links = self.get_links()
		self.my_services = self.get_services()
		self.get_connected_actuators()


	def connect_to_docker(self):
		try:
			self.conn = docker.from_env()
		except Exception as e:
			print(f"An error occurred while connecting to docker: {e}")
	
	def get_services(self):

		docker = self.conn.info()

		docker_application = Application(description='docker', name= docker['ID'], version=docker['ServerVersion'], owner='Docker, Inc.', app_type=None)
			

		docker_service = Service(name= Name('docker'), type=ServiceType(docker_application), links=self.get_name_links(self.my_links),
									 subservices=None, owner= 'Docker, Inc.', release=docker['ServerVersion'], security_functions=None,
									 actuator=Consumer(server=Server(Hostname(self.asset_id)), 
													   port=self.port,
													   protocol= L4Protocol(self.protocol),
													   endpoint=self.endpoint,
													   transfer=Transfer(self.transfer),
													   encoding=Encoding(self.encoding)))

		return ArrayOf(Service)([docker_service])



	def get_name_links(self, links):
		
		name_links = ArrayOf(Name)()
		
		for link in links:
			name_links.append(link.name.obj)
			
		return name_links
	
	def get_links(self):

		links = ArrayOf(Link)()

		#--------------FIND the vm where the docker application is running-------------------
		#it only works if the vm is running on one vm
		vm_hostname = socket.gethostname()
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("8.8.8.8", 80)) # Finta connessione a un IP pubblico per ottenere l'indirizzo IP 192.168.0.X
		vm_ip = s.getsockname()[0]

		#if the vm is already created, I don't create a link otherwise I create link, service and actuator
		if(any(item[1] == vm_hostname for item in self.actuators) == False):
			vm_hosting_peer = Peer(service_name= Name('vm\n' + vm_ip), 
							role= PeerRole(4), #VM hosts docker
							consumer=Consumer(server=Server(Hostname(vm_hostname)),
												port=self.port,
												protocol= L4Protocol(self.protocol),
											    endpoint=self.endpoint,
												transfer=Transfer(self.transfer),
												encoding=Encoding(self.encoding)))

			links.append(Link(name = Name(vm_hostname), link_type=LinkType(2), peers=ArrayOf(Peer)([vm_hosting_peer])))

			self.actuators[(ctxd.Profile.nsid,str(vm_hostname))] = CTXDActuator(services= self.get_services_hosting_vm(),
																	   links= ArrayOf(Link)(),
																	   domain=None,
																	   asset_id=str(vm_hostname))



		#-------------END CREATION LINK TO HOSTING VM------------------------------------

		#now create a link for each active container
		containers = self.conn.containers.list() #only active containers

		for container in containers:
			tmp_container = Peer(service_name=(Name('container\n' + container.attrs['NetworkSettings']['IPAddress'])),
								role= PeerRole(9), #Docker controls the container
								consumer=Consumer(server=Server(Hostname(container.attrs['Name'].lstrip('/'))), #remove / 
								port=self.port,
								protocol= L4Protocol(self.protocol),
								endpoint=self.endpoint,
								transfer=Transfer(self.transfer),
								encoding=Encoding(self.encoding)))
			links.append(Link(name = Name(container.attrs['Name'].lstrip('/')), link_type=LinkType(4), peers=ArrayOf(Peer)([tmp_container])))

		return links
	
	def get_container_service(self, name):
		array_container = ArrayOf(Service)()
		#now create a service for each active container
		container = self.conn.containers.get(name) #only active containers

		tmp_container = Container(description='container',
            		   	              id=container.attrs['Id'],
                   			          hostname=Hostname(container.attrs['Name'].lstrip('/')),
                        		      runtime = None,
                            		  os=None)

		service_container = Service(name= Name(container.attrs['Name'].lstrip('/')), type=ServiceType(tmp_container), links= ArrayOf(Name)([]),
            		                             subservices=None, owner='Docker, Inc.', release=None, security_functions=None,
                		                         actuator=Consumer(server=Server(Hostname(container.attrs['Name'].lstrip('/'))),
                    		                                        port=self.port,
																	protocol= L4Protocol(self.protocol),
													    			endpoint=self.endpoint,
																	transfer=Transfer(self.transfer),
																	encoding=Encoding(self.encoding)))
		array_container.append(service_container)
		return array_container

	def get_connected_actuators(self):

		for link in self.my_links: #explore link between docker and managed containers
			if(link.link_type.name == "control"): #only the controlled containers
				self.actuators[(ctxd.Profile.nsid,str(link.name.obj))] = CTXDActuator(services= self.get_container_service(str(link.name.obj)),
                                                                            	links= ArrayOf(Link)(),
                                                                                domain=None,
                                                                                asset_id=str(link.name.obj))

	def get_services_hosting_vm(self):
		docker = self.conn.info()
		tmp_vm = VM(description='vm', 
                        id= docker['ID'], 
                        hostname= Hostname(docker['Name']), 
                        os= OS(family=docker['Operating System'], name=docker['OSType']))
		
		vm_service = Service(name= Name(docker['Name']), type=ServiceType(tmp_vm), links= ArrayOf(Link)([]),
                                         subservices=None, release=None, security_functions=None,
                                         actuator=Consumer(server=Server(Hostname(docker['Name'])),
                                                            port=self.port,
															protocol= L4Protocol(self.protocol),
											    			endpoint=self.endpoint,
															transfer=Transfer(self.transfer),
															encoding=Encoding(self.encoding)))
		return ArrayOf(Service)([vm_service])

