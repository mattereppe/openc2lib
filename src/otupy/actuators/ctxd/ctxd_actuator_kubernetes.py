""" Skeleton `Actuator` for CTXD profile

	This module provides an example to create an `Actuator` for the CTXD profile.
	It only answers to the request for available features.
"""

import socket
import subprocess
import json
import os
import logging
import sys

import docker
from otupy.profiles import slpf
from otupy.profiles.ctxd.data.application import Application
from otupy.profiles.ctxd.data.openc2_endpoint import OpenC2Endpoint
from otupy.types.data.ipv4_addr import IPv4Addr
import requests
from kubernetes import config, client
from kubernetes.client.rest import ApiException

from otupy.actuators.ctxd.ctxd_actuator import CTXDActuator
from otupy.profiles.ctxd.data.cloud import Cloud
from otupy.profiles.ctxd.data.consumer import Consumer
from otupy.profiles.ctxd.data.container import Container
from otupy.profiles.ctxd.data.encoding import Encoding
from otupy.profiles.ctxd.data.link_type import LinkType
from otupy.profiles.ctxd.data.network import Network
from otupy.profiles.ctxd.data.network_type import NetworkType
from otupy.profiles.ctxd.data.os import OS
from otupy.profiles.ctxd.data.peer import Peer
from otupy.profiles.ctxd.data.peer_role import PeerRole
from otupy.profiles.ctxd.data.server import Server
from otupy.profiles.ctxd.data.service_type import ServiceType
from otupy.profiles.ctxd.data.transfer import Transfer
from otupy.profiles.ctxd.data.vm import VM
from otupy.types.data.hostname import Hostname
from otupy.types.data.l4_protocol import L4Protocol



from otupy import ArrayOf, Nsid, Version,Actions, Response, StatusCode, StatusCodeDescription, Features, ResponseType, Feature
import otupy.profiles.ctxd as ctxd

from otupy.profiles.ctxd.data.name import Name
from otupy.profiles.ctxd.data.service import Service
from otupy.profiles.ctxd.data.link import Link

logger = logging.getLogger(__name__)

OPENC2VERS=Version(1,0)
""" Supported OpenC2 Version """

MY_IDS = {
	'domain': None,
	'asset_id': None
}

# An implementation of the ctxd profile (it implements my5gtestbed). 
class CTXDActuator_kubernetes(CTXDActuator):
	""" CTXD implementation

		This class provides an implementation of the CTXD `Actuator`.
	"""

	my_services: ArrayOf(Service) = None # type: ignore
	""" Name of the service """
	my_links: ArrayOf(Link) = None # type: ignore
	"""It identifies the type of the service"""
	domain : str = None
	asset_id : str = None
	actuators: any = None
	hostname: any = None
	ip: any = None
	port: any = None
	protocol: any = None
	endpoint: any = None
	transfer: any = None
	encoding: any = None
	namespace = [] #it contains only the name of the namespaces
	api_client : any = None #api client for kubernetes
	config_file : any = None #configuration file path
	kube_context : any = None #kubernetes context

	def __init__(self, domain, asset_id, actuators, hostname, ip, port, protocol, endpoint, transfer, encoding, namespace, config_file, kube_context):
		MY_IDS['domain'] = domain
		MY_IDS['asset_id'] = asset_id
		self.domain = domain
		self.asset_id = asset_id
		self.actuators = actuators
		self.hostname = hostname
		self.ip = ip
		self.port = port
		self.protocol = protocol
		self.endpoint = endpoint
		self.transfer = transfer
		self.encoding = encoding
		self.namespace = namespace
		self.config_file = config_file
		self.kube_context = kube_context

		self.connect_to_kubernetes()

		self.namespace = self.get_name_namespace()
		self.my_links = self.get_links()
		self.my_services = self.get_services()
		self.get_connected_actuators(actuators)

	def get_name_namespace(self):
		if len(self.namespace) == 0: #devo controllare tutti i namespaces attivi -> estraggo solo i nomi
			#process = subprocess.Popen('kubectl get namespaces --field-selector=status.phase=Active -o json', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			#stdout, stderr = process.communicate()
			api_namespaces = self.api_client.list_namespace(field_selector="status.phase=Active")
			return [namespace.metadata.name for namespace in api_namespaces.items]
		
		return self.namespace		

	def get_name_links(self, links):
		
		name_links = ArrayOf(Name)()
		
		for link in links:
			name_links.append(link.name.obj)
			
		return name_links

	def get_services(self):

		kubernetes = Cloud(description='cloud', id= None, name=self.asset_id, type= None)
			

		kubernetes_service = Service(name= Name(self.asset_id), type=ServiceType(kubernetes), links=self.get_name_links(self.my_links),
									 subservices=None, owner= None, release=None, security_functions=None,
									 actuator=Consumer(server=Server(Hostname(self.asset_id)), 
													   port=self.port,
													   protocol= L4Protocol(self.protocol),
													   endpoint=self.endpoint,
													   transfer=Transfer(self.transfer),
													   encoding=Encoding(self.encoding)))
        
	
		return ArrayOf(Service)([kubernetes_service])

	def get_links(self):
		#process = subprocess.Popen('kubectl get nodes -o json', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		#stdout, stderr = process.communicate()
		api_nodes = self.api_client.list_node()
		vms = api_nodes.items
		array_vms = ArrayOf(VM)()

		#definisco il link control tra kubernetes e vm
		links = ArrayOf(Link)()
		
		for vm in vms:
			tmp_vm = VM(description='vm', 
							id= vm.metadata.uid, 
							hostname= Hostname(vm.metadata.name), 
							os= OS(family=vm.status.node_info.operating_system, name=vm.status.node_info.os_image))

			array_vms.append(tmp_vm)
			
			tmp_peer = Peer(service_name= Name('vm\n' + vm.status.addresses[0].address), 
							role= PeerRole(9), #VM is controlled by kubernetes
							consumer=Consumer(server=Server(Hostname(vm.metadata.name)),
												port=self.port,
												protocol= L4Protocol(self.protocol),
											    endpoint=self.endpoint,
												transfer=Transfer(self.transfer),
												encoding=Encoding(self.encoding)))

			links.append(Link(name = Name(vm.metadata.uid), link_type=LinkType(4), peers=ArrayOf(Peer)([tmp_peer])))

		#i link per trovare i namespace collegato al cloud kubernetes
		try:
			for it_namespace in self.namespace:

				#process = subprocess.Popen('kubectl get namespace ' + it_namespace +' -o json', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				#stdout, stderr = process.communicate()
				#namespace = json.loads(stdout.decode())
				namespace = self.api_client.read_namespace(name=it_namespace)

		
				namespace_peer = Peer(service_name= Name(namespace.metadata.name), 
        	        	            role= PeerRole(3),
            	        	        consumer=Consumer(server=Server(Hostname(namespace.metadata.name)),
                	        	                        port=self.port,
														protocol= L4Protocol(self.protocol),
													    endpoint=self.endpoint,
														transfer=Transfer(self.transfer),
														encoding=Encoding(self.encoding)))
			
				links.append(Link(name=Name(namespace.metadata.name), #the name of the link is the name of the namespace
            		                       description= 'namespace',
                		                   versions=None,
                    		               link_type=LinkType(2),
                        		           peers=ArrayOf(Peer)([namespace_peer]),
                            		       security_functions=None))
		except Exception as e:
			print(f"An error occurred: {e}")

		#create a dumb slpf peer
		slpf_peer = Peer(service_name= Name('slpf'), 
						role= PeerRole(3), #The slpf controls the vm
						consumer=Consumer(server=Server(Hostname('kube-fw')),
											port=self.port,
											protocol= L4Protocol(self.protocol),
											endpoint= self.endpoint,
											transfer=Transfer(self.transfer),
											encoding=Encoding(self.encoding)))
				
		links.append(Link(name = Name('kube-fw'), description="slpf", link_type=LinkType(2), peers=ArrayOf(Peer)([slpf_peer])))
		#end creation of dumb slpf

		return links

	def get_connected_actuators(self, actuators):
		#create dumb slpf actuators
		actuators[(ctxd.Profile.nsid,str('os-fw'))] = self.getDumbSLPF(name='os-fw')
		actuators[(ctxd.Profile.nsid,str('kube-fw'))] = self.getDumbSLPF(name='kube-fw')
		#end creation of dumb slpf actuators

		for link in self.my_links: #explore link between kubernetes and vm
			if(link.description == "namespace" ): #but if the description = namespace -> find namespace and not vm
				actuators[(ctxd.Profile.nsid,str(link.name.obj))] = CTXDActuator(services= self.get_namespace_service(str(link.name.obj)),
                                                                            	links= ArrayOf(Link)(),
                                                                                domain=None,
                                                                                asset_id=str(link.name.obj))
			elif(link.description != "slpf"):
				for vm in link.peers: #explore vm (kube0, kube1, kube2)
					actuators[(ctxd.Profile.nsid,str(vm.consumer.server.obj._hostname))] = CTXDActuator(services= self.get_vm_service(vm.consumer.server.obj._hostname),
                                                                                                        links= self.get_vm_links(vm.consumer.server.obj._hostname),
                                                                                                        domain=None,
                                                                                                        asset_id=str(vm.consumer.server.obj._hostname))
                    
					for vm_link in actuators[(ctxd.Profile.nsid,str(vm.consumer.server.obj._hostname))].my_links: #explore link between vm and container
						if(vm_link.description != "kubernetes" and vm_link.description != "slpf"):
							for container in vm_link.peers: #explore containers connect to a vm
								actuators[(ctxd.Profile.nsid,str(container.consumer.server.obj._hostname))] = CTXDActuator(services= self.get_container_service(container.consumer.server.obj._hostname),
																														links=self.get_container_links(str(container.consumer.server.obj._hostname)),
																														domain=None,
																														asset_id=str(container.consumer.server.obj._hostname))

	def get_vm_service(self, asset_id):
		#process = subprocess.Popen('kubectl get nodes '+ str(asset_id) +' -o json', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		#stdout, stderr = process.communicate()
		node_name = str(asset_id)
		vm = self.api_client.read_node(name=node_name)

		tmp_vm = VM(description='vm', 
                        id= vm.metadata.uid, 
                        hostname= Hostname(vm.metadata.name), 
                        os= OS(family=vm.status.node_info.operating_system, name=vm.status.node_info.os_image))
		
		vm_service = Service(name= Name(node_name), type=ServiceType(tmp_vm), links= self.get_name_links(self.get_vm_links(asset_id)),
                                         subservices=None, owner='openstack', release=None, security_functions=None,
                                         actuator=Consumer(server=Server(Hostname(vm.metadata.name)),
                                                            port=self.port,
															protocol= L4Protocol(self.protocol),
											    			endpoint=self.endpoint,
															transfer=Transfer(self.transfer),
															encoding=Encoding(self.encoding))) 

		return ArrayOf(Service)([vm_service])
	
	def get_vm_links(self, asset_id):
		#trovo i container collegati alla VM per ogni namespace
		links = ArrayOf(Link)()
		for it_namespace in self.namespace:
			try:
				#process = subprocess.Popen('kubectl get pods -n ' + it_namespace +' --field-selector spec.nodeName=' +str(asset_id)+ ' -o json', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				#stdout, stderr = process.communicate()
				pods = self.api_client.list_namespaced_pod(namespace=str(it_namespace), field_selector="spec.nodeName=" + str(asset_id))
				containers = pods.items

				for it_container in containers:
					tmp_peer_container = Peer(service_name= Name('container\n'+ it_container.status.pod_ip),
            	    	                          role= PeerRole(3),
                	    	                      consumer=Consumer(server=Server(Hostname(it_container.metadata.name)),
                    	    	                                    port=self.port,
																	protocol= L4Protocol(self.protocol),
													    			endpoint=self.endpoint,
																	transfer=Transfer(self.transfer),
																	encoding=Encoding(self.encoding)))
					links.append(Link(name=Name(it_container.metadata.uid),
                    	                     	link_type=LinkType(2),
                        	                 	peers=ArrayOf(Peer)([tmp_peer_container])))
			except Exception as e:
				continue
		
		#trovo il link tra vm e kubernetes solo per il master del cluster (role = control-plane)
		#process = subprocess.Popen('kubectl get nodes -l node-role.kubernetes.io/control-plane -o json', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		#stdout, stderr = process.communicate()
		label_selector = "node-role.kubernetes.io/control-plane"
		control_plane_nodes = self.api_client.list_node(label_selector=label_selector)
		array_masters = control_plane_nodes.items
		is_master = False

		for it_master in array_masters:
			if(str(it_master.metadata.name) == str(asset_id)):
				is_master = True
		
		if(is_master is True): #solo per il master aggiungo il link
			tmp_peer_kubernetes = Peer(service_name= Name('kubernetes'),
                                          	role= PeerRole(3),
                                          	consumer=Consumer(server=Server(Hostname(self.asset_id)),
                                                            	port=self.port,
																protocol= L4Protocol(self.protocol),
											    				endpoint=self.endpoint,
																transfer=Transfer(self.transfer),
																encoding=Encoding(self.encoding)))

			links.append(Link(name=Name('kubernetes'),
							description='kubernetes',
                            link_type=LinkType(2),
                            peers=ArrayOf(Peer)([tmp_peer_kubernetes])))

		#create a dumb slpf peer
		slpf_peer = Peer(service_name= Name('slpf'), 
						role= PeerRole(8), #The slpf controls the vm
						consumer=Consumer(server=Server(Hostname('os-fw')),
											port=self.port,
											protocol= L4Protocol(self.protocol),
											endpoint= self.endpoint,
											transfer=Transfer(self.transfer),
											encoding=Encoding(self.encoding)))
				
		links.append(Link(name = Name('os-fw'), description="slpf", link_type=LinkType(5), peers=ArrayOf(Peer)([slpf_peer])))
		#end creation of dumb slpf

		#create a link to docker service if it is active
		if(str(asset_id) == self.get_hostname_if_docker_active()):
			docker_peer = Peer(service_name= Name('docker'),
					  			role= PeerRole(3), #docker is hosted on the vm
								consumer=Consumer(server=Server(Hostname('docker')),
								port=self.port,
								protocol= L4Protocol(self.protocol),
								endpoint=self.endpoint,
								transfer=Transfer(self.transfer),
								encoding=Encoding(self.encoding)))
			links.append(Link(name = Name('docker'), description="docker", link_type=LinkType(2), peers=ArrayOf(Peer)([docker_peer])))
		#end creation link to docker

		return links
	
	def get_container_service(self, asset_id):
		array_container = ArrayOf(Service)()
		for it_namespace in self.namespace:
			try:
				#process = subprocess.Popen('kubectl get pod '+ asset_id +' -n ' + it_namespace +' -o json', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				#stdout, stderr = process.communicate()
				container = self.api_client.read_namespaced_pod(name=str(asset_id), namespace=str(it_namespace) )
				

				tmp_container = Container(description='container',
                	              id=container.metadata.uid,
                    	          hostname=Hostname(container.metadata.name),
                        	      runtime = None,
                            	  os=None)

				service_container = Service(name= Name(container.metadata.name), type=ServiceType(tmp_container), links= ArrayOf(Name)([]),
            		                             subservices=None, owner='openstack', release=None, security_functions=None,
                		                         actuator=Consumer(server=Server(Hostname(container.metadata.name)),
                    		                                        port=self.port,
																	protocol= L4Protocol(self.protocol),
													    			endpoint=self.endpoint,
																	transfer=Transfer(self.transfer),
																	encoding=Encoding(self.encoding)))
				array_container.append(service_container)
			except Exception as e:
					continue
		return array_container
	
	def get_container_links(self, asset_id):
		links = ArrayOf(Link)()

		#each container is connected to a namespaces
		for it_namespace in self.namespace:
			try:
				#process = subprocess.Popen('kubectl get pod ' + asset_id +' --namespace=' + it_namespace +' -o json', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				#stdout, stderr = process.communicate()
				pod = self.api_client.read_namespaced_pod(name=str(asset_id), namespace=str(it_namespace))

				if(pod.metadata.name == asset_id):
					#process = subprocess.Popen('kubectl get namespace '  + it_namespace + ' -o json', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
					#stdout, stderr = process.communicate()
					namespace = self.api_client.read_namespace(name=str(it_namespace))

					namespace_peer = Peer(service_name= Name(namespace.metadata.name), 
            			                role= PeerRole(3),
                			            consumer=Consumer(server=Server(Hostname(namespace.metadata.name)),
                    			                			            port=self.port,
																		protocol= L4Protocol(self.protocol),
														    			endpoint=self.endpoint,
																		transfer=Transfer(self.transfer),
																		encoding=Encoding(self.encoding)))
					links.append(Link(name=Name(namespace.metadata.name),
            		                       description=None,
                		                   versions=None,
                    		               link_type=LinkType(3),
                        		           peers=ArrayOf(Peer)([namespace_peer]),
                            		       security_functions=None))
			except Exception as e:
				continue
		
		#create a dumb slpf peer
		slpf_peer = Peer(service_name= Name('slpf'), 
						role= PeerRole(8), #The slpf controls the vm
						consumer=Consumer(server=Server(Hostname('kube-fw')),
											port=self.port,
											protocol= L4Protocol(self.protocol),
											endpoint= self.endpoint,
											transfer=Transfer(self.transfer),
											encoding=Encoding(self.encoding)))
				
		links.append(Link(name = Name('kube-fw'), description="slpf", link_type=LinkType(5), peers=ArrayOf(Peer)([slpf_peer])))
		#end creation of dumb slpf

		return links

	def get_namespace_service(self, namespace_name):
		#process = subprocess.Popen('kubectl get namespace '  + namespace_name + ' -o json', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		#stdout, stderr = process.communicate()
		namespace = self.api_client.read_namespace(name=str(namespace_name))
        
		namespace_network = Network(description='network',
                                      name=Name(namespace.metadata.name),
                                      type=NetworkType('wan'))
        
		namespace_service = Service(name=Name(namespace.metadata.name),
                                      type=ServiceType(namespace_network),
                                      links= ArrayOf(Name)(),
                                      subservices=None,
                                      owner=None,
                                      release=None,
                                      security_functions=None,
                                      actuator=None)
        
	
		return ArrayOf(Service)([namespace_service])
	
	def connect_to_kubernetes(self):
		try:
			if self.config_file is not None:
				if self.kube_context is not None:
					config.load_kube_config(config_file= self.config_file, context= self.kube_context)
				else:	
					config.load_kube_config(config_file= self.config_file)
			else:
				# Load the kubeconfig file (by default it loads from ~/.kube/config)
				if self.kube_context is not None:
					config.load_kube_config(context=self.kube_context)
				else:
					config.load_kube_config()
			# Create an API client
			self.api_client = client.CoreV1Api()
		except Exception as e:
			print(f"Failed to connect to kubernetes: {e}")
			return Exception("Failed to connect to kubernetes")
		
	def getDumbSLPF(self, name):
		ex_application = Application(description="slpf", name=name, app_type="Packet Filtering")
		array_security_functions = ArrayOf(OpenC2Endpoint)()
		array_security_functions.append(OpenC2Endpoint(actuator=Nsid(slpf.Profile.nsid),
												consumer = Consumer(server=Server(Hostname(name)),
                    			                			            port=self.port,
																		protocol= L4Protocol(self.protocol),
														    			endpoint=self.endpoint,
																		transfer=Transfer(self.transfer),
																		encoding=Encoding(self.encoding))))
		ex_consumer = Consumer(server=Server(Hostname(name)),
                    			port=self.port,
								protocol= L4Protocol(self.protocol),
								endpoint=self.endpoint,
								transfer=Transfer(self.transfer),
								encoding=Encoding(self.encoding))
			
		slpf_service = Service(name = Name(name), 
						 type = ServiceType(ex_application),
						 links=None, 
						 security_functions=array_security_functions,
						 actuator= ex_consumer)
		
		return CTXDActuator(services= ArrayOf(Service)([slpf_service]),
                            links= ArrayOf(Link)([]),
                            domain=None,
                        	asset_id=str(name))

	def get_hostname_if_docker_active(self):
		try:
			client = docker.from_env()
			client.ping()  # This will raise an exception if Docker isn't running
			return socket.gethostname()
		except Exception as e:
			print(f"Docker is not running or not accessible: {e}")
			return None
