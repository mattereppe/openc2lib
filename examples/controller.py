#!../.oc2-env/bin/python3
# Example to use the OpenC2 library
#

import logging
import sys

import openc2lib as oc2

from openc2lib.encoders.json import JSONEncoder
from openc2lib.transfers.http import HTTPTransfer

import openc2lib.profiles.slpf as slpf


#logging.basicConfig(filename='openc2.log',level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout,level=logging.INFO)
logger = logging.getLogger('openc2producer')

def main():
	logger.info("Creating Producer")
	p = oc2.Producer("producer.example.net", JSONEncoder(), HTTPTransfer("127.0.0.1", 8080))

	pf = slpf.slpf({'hostname':'firewall', 'named_group':'firewalls', 'asset_id':'iptables'})


	arg = slpf.Args({'response_requested': oc2.ResponseType.complete})
#	arg = slpf.Args({'response_requested': oc2.ResponseType.none})

	cmd = oc2.Command(oc2.Actions.query, oc2.Features([oc2.Feature.versions, oc2.Feature.profiles, oc2.Feature.pairs]), arg, actuator=pf)
#	cmd = oc2.Command(oc2.Actions.query, oc2.Features([oc2.Feature.rate_limit]), arg, actuator=pf)

	logger.info("Sending command: %s", cmd)
	resp = p.sendcmd(cmd)
	logger.info("Got response: %s", resp)


if __name__ == '__main__':
	main()
