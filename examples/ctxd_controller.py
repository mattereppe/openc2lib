#!../.oc2-env/bin/python3
# Example to use the OpenC2 library
#

import logging
import os
import sys

import otupy as oc2

from otupy.encoders.json import JSONEncoder
from otupy.transfers.http import HTTPTransfer
import otupy.profiles.ctxd as ctxd
from otupy.profiles.ctxd.data.name import Name
from otupy.types.base.array_of import ArrayOf
from otupy.core.register import Register
from otupy.types.base.choice import Choice
from otupy.types.data.hostname import Hostname
from otupy.types.base.array import Array

logger = logging.getLogger()
# Ask for 4 levels of logging: INFO, WARNING, ERROR, CRITICAL
logger.setLevel(logging.INFO)
# Create stdout handler for logging to the console 
stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(oc2.LogFormatter(datetime=True,name=True))
hdls = [ stdout_handler ]
# Add both handlers to the logger
logger.addHandler(stdout_handler)

def main():
	logger.info("Creating Producer")

	p = oc2.Producer("producer.example.net", JSONEncoder(), HTTPTransfer("127.0.0.1", 8080))

	#pf = ctxd.Specifiers({'domain':'example_domain', 'asset_id':'example_asset_id'})
	#pf = ctxd.Specifiers({})
	pf = ctxd.Specifiers({'asset_id': 'x-ctxd'})
	#pf.fieldtypes['asset_id'] = 'ciao'  # I have to repeat a second time to have no bugs

	arg = ctxd.Args({'name_only': False})

	services = ArrayOf(Name)()
	links = ArrayOf(Name)()
	
	services.append('example_service')
	services.append(Name(Hostname('servizio2.com')))
	links.append('link_1')

	#context = ctxd.Context(services=services, links=links)
	#context = ctxd.Context() #expected heartbeat
	context = ctxd.Context(services= ArrayOf(Name)(), links= ArrayOf(Name)()) #expected all services and links

	cmd = oc2.Command(action = oc2.Actions.query, target = context, args = arg, actuator = pf)
	#cmd = oc2.Command(oc2.Actions.query, oc2.Features([oc2.Feature.versions, oc2.Feature.profiles, oc2.Feature.pairs]), actuator = pf)



	logger.info("Sending command: %s", cmd)
	resp = p.sendcmd(cmd)
	logger.info("Got response: %s", resp)


if __name__ == '__main__':
	main()
