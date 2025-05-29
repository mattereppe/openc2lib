#!../.venv/bin/python3
# Example to use the OpenC2 library
#

import logging
import sys

import otupy as oc2

from otupy.encoders.json import JSONEncoder
from otupy.transfers.http import HTTPSTransfer
from otupy.actuators.iptables_actuator import IptablesActuator
import otupy.profiles.slpf as slpf

#logging.basicConfig(filename='consumer.log',level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout,level=logging.INFO)
logger = logging.getLogger('openc2')
	
def main():

# Instantiate the list of available actuators, using a dictionary which key
# is the assed_id of the actuator.
	actuators = {}
	actuators[(slpf.nsid,'iptables')]=IptablesActuator()

	c = oc2.Consumer("testconsumer", actuators, JSONEncoder(), HTTPSTransfer("127.0.0.1", 8080))


	c.run()


if __name__ == "__main__":
	main()
