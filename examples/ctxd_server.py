#!../.oc2-env/bin/python3
# Example to use the OpenC2 library
#

import logging
import os 
import sys
import datetime
import uuid

from otupy.profiles.ctxd.data.application import Application
from otupy.profiles.ctxd.data.cloud import Cloud
from otupy.profiles.ctxd.data.container import Container
from otupy.profiles.ctxd.data.iot import IOT
from otupy.profiles.ctxd.data.network import Network
from otupy.profiles.ctxd.data.network_type import NetworkType
from otupy.profiles.ctxd.data.web_service import WebService
from otupy.types.data.uri import URI

import otupy as oc2

from otupy.encoders.json import JSONEncoder
from otupy.transfers.http import HTTPTransfer
from otupy.actuators.ctxd.ctxd_actuator import CTXDActuator
import otupy.profiles.ctxd as ctxd
from otupy.actuators.iptables_actuator import IptablesActuator
from otupy.profiles import slpf
from otupy.profiles.ctxd.data.link import Link
from otupy.profiles.ctxd.data.service import Service
from otupy.types.base.array_of import ArrayOf
from otupy.profiles.ctxd.data.consumer import Consumer
from otupy.profiles.ctxd.data.transfer import Transfer
from otupy.profiles.ctxd.data.encoding import Encoding
from otupy.profiles.ctxd.data.link_type import LinkType
from otupy.profiles.ctxd.data.name import Name
from otupy.profiles.ctxd.data.openc2_endpoint import OpenC2Endpoint
from otupy.profiles.ctxd.data.os import OS
from otupy.profiles.ctxd.data.peer import Peer
from otupy.profiles.ctxd.data.peer_role import PeerRole
from otupy.profiles.ctxd.data.server import Server
from otupy.profiles.ctxd.data.service_type import ServiceType
from otupy.profiles.ctxd.data.vm import VM
from otupy.types.data.hostname import Hostname
from otupy.types.data.ipv4_addr import IPv4Addr
from otupy.types.data.l4_protocol import L4Protocol
from otupy.types.data.version import Version
from otupy.types.data.nsid import Nsid



# Declare the logger name
logger = logging.getLogger()
# Ask for 4 levels of logging: INFO, WARNING, ERROR, CRITICAL
logger.setLevel(logging.ERROR)
# Create stdout handler for logging to the console 
stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(logging.ERROR)
stdout_handler.setFormatter(oc2.LogFormatter(datetime=True,name=True))
hdls = [ stdout_handler ]
# Add both handlers to the logger
logger.addHandler(stdout_handler)
	
def main():

# Instantiate the list of available actuators, using a dictionary which key
# is the assed_id of the actuator.
	ex_vm = VM(description='vm', id='123456', hostname=Hostname('My-virtualbox'), os = OS(name='ubuntu', version='22.04.3', family='debian', type='linux'))
	array_link = ArrayOf(Name)()
	array_link.append('link_1')
	array_subservice = ArrayOf(Name)()
	array_subservice.append('example_subservice')
	array_security_functions = ArrayOf(OpenC2Endpoint)()
	array_security_functions.append(OpenC2Endpoint(actuator=Nsid(slpf.Profile.nsid),
												consumer = Consumer(server = Server(IPv4Addr('192.168.0.2')), 
																	port=80, 
																	protocol=L4Protocol(6),
																	endpoint='/.well-known/openc2',
																	transfer=Transfer(1),
																	encoding=Encoding(1))))
	ex_consumer = Consumer(server = Server(IPv4Addr('192.168.0.2')), 
							port=80, 
							protocol=L4Protocol(6),
							endpoint='/.well-known/openc2',
							transfer=Transfer(1),
							encoding=Encoding(1))
	
	service1 = Service(name = Name('example_service'), type = ServiceType(ex_vm),links=array_link, subservices=array_subservice,
					 owner = 'Mario Rossi', release='1.0', security_functions=array_security_functions,
					 actuator= ex_consumer)

	ex_application = Application(description="application", name="iptables", version="1.8.10", owner="Netfilter", app_type="Packet Filtering")
	ex_container = Container(description="container", id="123456", hostname="container_name", runtime="docker", os = OS(name='ubuntu', version='22.04.3', family='debian', type='linux'))
	ex_web_service = WebService(description="web_service", server= Server(IPv4Addr('192.168.0.3')), port = 80, endpoint='/.well-known/openc2', owner = "Google")
	ex_cloud = Cloud(description="cloud", id="123456", name="aws", type="lambda")
	ex_network = Network(description="network", name="The Things Network", type=NetworkType("lorawan")) #remember that NetworkType is not completely defined
	ex_iot = IOT(description="IoT", name="Azure IoT", type="sensor")

	service_application = Service(name = Name(Hostname('serviceApplication')), type=ServiceType(ex_application), owner = 'Luigi Bianchi')
	service_container = Service(name = Name(URI('service_container.com')), type=ServiceType(ex_container))
	service_web_service = Service(name = Name(uuid.UUID('e3c4e5a8-52f2-4f60-b3d1-8f8dbf8d8be9')), type=ServiceType(ex_web_service))
	service_cloud = Service(name = Name(Hostname('serviceCloud')), type=ServiceType(ex_cloud))
	service_network = Service(name = Name(Hostname('serviceNetwork')), type=ServiceType(ex_network))
	service_iot = Service(name = Name(Hostname('serviceIoT')), type=ServiceType(ex_iot))
	my_services = [service1, service_application, service_container, service_web_service, service_cloud, service_network, service_iot]
	
	array_versions = ArrayOf(Version)()
	array_versions.append('1.0')
	array_peers = ArrayOf(Peer)()
	array_peers.append(Peer(service_name=Name(Hostname('com.example-connected-consumer')),
						 role=PeerRole(4),
						 consumer = Consumer(server = Server(IPv4Addr('192.168.0.3')), 
											port=80, 
											protocol=L4Protocol(6),
											endpoint='/.well-known/openc2',
											transfer=Transfer(1),
											encoding=Encoding(1))))
	
	array_security_functions_links = ArrayOf(OpenC2Endpoint)()
	array_security_functions_links.append(OpenC2Endpoint(actuator=Nsid(slpf.Profile.nsid),
												consumer = Consumer(server = Server(IPv4Addr('192.168.0.4')), 
																	port=80, 
																	protocol=L4Protocol(6),
																	endpoint='/.well-known/openc2',
																	transfer=Transfer(1),
																	encoding=Encoding(1))))
	
	link1 = Link(name = Name('link_1'), description = 'description1', versions=array_versions, link_type= LinkType(2)
			  , peers = array_peers, security_functions = array_security_functions_links)
	link2 = Link(name = Name('link2'), description = 'description2')
	my_links = [link1, link2]

	actuators = {}
	actuators[(ctxd.Profile.nsid,'x-ctxd')] = CTXDActuator(services=ArrayOf(Service)(my_services), links=ArrayOf(Link)(my_links), domain=None, asset_id='x-ctxd')
	c = oc2.Consumer("testconsumer", actuators, JSONEncoder(), HTTPTransfer("127.0.0.1", 8080))
	

	c.run()

if __name__ == "__main__":
	main()
