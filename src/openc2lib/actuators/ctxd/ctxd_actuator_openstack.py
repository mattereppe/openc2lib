""" Skeleton `Actuator` for CTXD profile

	This module provides an example to create an `Actuator` for the CTXD profile.
	It only answers to the request for available features.
"""

import json
import subprocess
import os
import logging
import sys
import openstack

from openc2lib.actuators.ctxd.ctxd_actuator import CTXDActuator
from openc2lib.profiles.ctxd.data.cloud import Cloud
from openc2lib.profiles.ctxd.data.consumer import Consumer
from openc2lib.profiles.ctxd.data.container import Container
from openc2lib.profiles.ctxd.data.encoding import Encoding
from openc2lib.profiles.ctxd.data.link_type import LinkType
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

# An implementation of the ctxd profile. 
class CTXDActuator_openstack(CTXDActuator):
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
	file_enviroment_variables : any = None
	conn : any = None #connection to openstack
	
	def __init__(self, domain, asset_id, hostname, ip, port, protocol, endpoint, transfer, encoding, file_enviroment_variables):
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
		self.file_enviroment_variables = file_enviroment_variables

		self.connect_to_openstack()
		self.my_links = self.get_links()
		self.my_services = self.get_services()


		
	def get_services(self):
		#process = subprocess.Popen('openstack service list -f json', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		#stdout, stderr = process.communicate()
		cloud_services = self.openstack_service_list()
		array_cloud_services = ArrayOf(Cloud)()

		for service in cloud_services:
			if(service['name'] == 'nova'):
				array_cloud_services.append(Cloud(description='cloud', id=service['id'], name=service['id'], type=service['type']))

		openstack_service = Service(name= Name('openstack'), type=ServiceType(array_cloud_services[0]), links=self.get_name_links(self.my_links),
									 subservices=None, owner= self.asset_id, release=None, security_functions=None,
									 actuator=Consumer(server=Server(Hostname(self.hostname)), 
													   port=self.port,
													   protocol= L4Protocol(self.protocol),
													   endpoint= self.endpoint,
													   transfer=Transfer(self.transfer),
													   encoding=Encoding(self.encoding)))
		return ArrayOf(Service)([openstack_service])


	def get_links(self):
		#process = subprocess.Popen('openstack server list --status ACTIVE -f json', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		#stdout, stderr = process.communicate()
		vms = self.openstack_server_list()
		array_vms = ArrayOf(VM)()

		#definisco il link control tra cloud e vm
		links = ArrayOf(Link)()
		for vm in vms:
			tmp_vm = VM(description='vm', 
							id= vm['id'], 
							hostname= Hostname(vm['name']),
							os = OS(name=self.openstack_server_os(vm['image']['id'])))

			array_vms.append(tmp_vm)
			
			tmp_peer = Peer(service_name= Name('vm\n'+ vm['addresses']['Net01'][0]['addr']), 
							role= PeerRole(9), #VM is controlled by Openstack
							consumer=Consumer(server=Server(Hostname(vm['name'])),
												port=self.port,
												protocol= L4Protocol(self.protocol),
												endpoint= self.endpoint,
												transfer=Transfer(self.transfer),
												encoding=Encoding(self.encoding)))

			links.append(Link(name = Name(vm['id']), link_type=LinkType(4), peers=ArrayOf(Peer)([tmp_peer])))

		#create a dumb slpf peer
		slpf_peer = Peer(service_name= Name('slpf'),
						role= PeerRole(3), #The slpf is hosted by Openstack
						consumer=Consumer(server=Server(Hostname('os-fw')),
											port=self.port,
											protocol= L4Protocol(self.protocol),
											endpoint= self.endpoint,
											transfer=Transfer(self.transfer),
											encoding=Encoding(self.encoding)))
				
		links.append(Link(name = Name('os-fw'), link_type=LinkType(2), peers=ArrayOf(Peer)([slpf_peer])))
		#end creation of dumb slpf
		
		return links
	
	
	def get_name_links(self, links):
		
		name_links = ArrayOf(Name)()
		
		for link in links:
			name_links.append(link.name.obj)
			
		return name_links
	

	def connect_to_openstack(self):
		#load enviroment variables into linux OS to connect to openstack
		if(self.file_enviroment_variables is not None): #if it is none, it will use the enviroment variables already present in the system
			with open(self.file_enviroment_variables, 'r') as f:
				for line in f:
					line = line.strip()
					if line.startswith('export '):  # Only process lines starting with 'export'
						# Remove 'export ' and split on the first '='
						line = line[len('export '):]
						if '=' in line:
							key, value = line.split('=', 1)
							# Strip quotes around the value if they exist (handle the case of values like "SreX1$")
							value = value.strip('"').strip("'")
							os.environ[key] = value
		
		try:
		# Initialize the OpenStack connection using environment variables
			self.conn = openstack.connect()

        # Get the token from the connection object (it will automatically handle authentication)
			token = self.conn.authorize()

        # Verify successful authentication by checking token
			if token:
				print("Authentication successful!")
				print(f"Token: {token}")
			else:
				print("Authentication failed.")
    
		except Exception as e:
			print(f"An error occurred: {e}")

	
	def openstack_service_list(self):
		if not self.conn:
			print("Connection to OpenStack is not established.")
			return
		
		try:
		    # List services available in OpenStack
			services = self.conn.identity.services()
		
			# Format the response as a JSON-like structure for pretty printing
			services_list = []
			for service in services:
				service_data = {key: value for key, value in service.to_dict().items()}
				services_list.append(service_data)
			# Return the formatted services list
			return services_list
		
		except Exception as e:
			print(f"Failed to retrieve service list: {e}")
			return Exception("Failed to retrieve service list")
		
	def openstack_server_list(self):
		if not self.conn:
			print("Connection to OpenStack is not established.")
			return

		try:
			# Use the OpenStack client to list active servers
			servers = self.conn.compute.servers(details=True, status="ACTIVE")

			# Format the response as a JSON-like structure for pretty printing
			server_list = []
			for server in servers:
				server_data = {key: value for key, value in server.to_dict().items()}
				server_list.append(server_data)

        	# Return the formatted server list as a pretty-printed JSON string
			return server_list

		except Exception as e:
			print(f"Failed to retrieve server list: {e}")
			return Exception("Failed to retrieve server list")
		

	def openstack_server_os(self, image_id):
		try:
        # Get image details using the OpenStack client
			image = self.conn.compute.get_image(image_id)

        # Check if the image is found and return the operating system name
			if image:
				return image.name  # Return the name of the image (OS name)
			else:
				print(f"Image with ID {image_id} not found.")
				return None
		except Exception as e:
			print(f"Failed to retrieve OS for image ID {image_id}: {e}")
			return None