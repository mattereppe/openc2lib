#!../.venv/bin/python3
# Example to use the OpenC2 library
#

import logging
import sys

import openc2lib as oc2

from openc2lib.encoders.json_encoder import JSONEncoder
from openc2lib.transfers.http_transfer import HTTPTransfer

import openc2lib.profiles.slpf as slpf


#logging.basicConfig(filename='openc2.log',level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout,level=logging.INFO)
logger = logging.getLogger('openc2producer')

def main():
	logger.info("Creating Producer")
	p = oc2.Producer("producer.example.net", JSONEncoder(), HTTPTransfer("127.0.0.1", 8080))

	pf = slpf.slpf({'hostname':'abete', 'named_group':'firewalls', 'asset_id':'iptables'})


	arg = slpf.ExtArgs({'start_time': oc2.DateTime(), 'duration': 3000,'persistent': True, 'direction': slpf.Direction.ingress})

	cmd = oc2.Command(oc2.Actions.query, oc2.Features(), actuator=pf)

	logger.info("Sending command: %s", cmd)
	resp = p.sendcmd(cmd,consumers=["firewall.example.net"])
	logger.info("Got response: %s", resp)


if __name__ == '__main__':
	main()
