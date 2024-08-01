#!../.oc2-env/bin/python3
# Example to use the OpenC2 library
#

import logging
import sys

import openc2lib as oc2

from openc2lib.encoders.json import JSONEncoder
from openc2lib.transfers.http import HTTPTransfer

import openc2lib.profiles.slpf as slpf
import openc2lib.profiles.dumb as dumb


#logging.basicConfig(filename='openc2.log',level=logging.DEBUG)
#logging.basicConfig(stream=sys.stdout,level=logging.INFO)
#logger = logging.getLogger('openc2producer')
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
# Add file logger
file_handler = logging.FileHandler("controller.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(oc2.LogFormatter(datetime=True,name=True, datefmt='%t'))
logger.addHandler(file_handler)

def main():
	logger.info("Creating Producer")

	p = oc2.Producer("producer.example.net", JSONEncoder(), HTTPTransfer("127.0.0.1", 8080))
#	p = oc2.Producer("producer.example.net", JSONEncoder(), HTTPTransfer("172.17.0.11", 8080))

	pf = slpf.Specifiers({'hostname':'firewall', 'named_group':'firewalls', 'asset_id':'iptables'})
#	pf = dumb.dumb({'hostname':'mockup', 'named_group':'testing', 'asset_id':'dumb'})


#	arg = oc2.Args({'response_requested': oc2.ResponseType.complete})
#	arg = slpf.Args({'response_requested': oc2.ResponseType.none})
	arg = slpf.Args({'response_requested': oc2.ResponseType.complete, 'direction': slpf.Direction.ingress})

	cmd = oc2.Command(oc2.Actions.query, oc2.Features([oc2.Feature.versions, oc2.Feature.profiles, oc2.Feature.pairs]), arg, actuator=pf)
#	cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Net("172.19.0.0/24"), arg, actuator=pf)
#	cmd = oc2.Command(oc2.Actions.delete, slpf.RuleID(1), arg, actuator=pf)
#cmd = oc2.Command(oc2.Actions.allow, slpf.RuleID(24), arg, actuator=pf)
#	cmd = oc2.Command(oc2.Actions.query, oc2.Features([oc2.Feature.rate_limit]), arg, actuator=pf)

	logger.info("Sending command: %s", cmd)
	resp = p.sendcmd(cmd)
	logger.info("Got response: %s", resp)


if __name__ == '__main__':
	main()
