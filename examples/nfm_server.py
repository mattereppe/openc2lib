#!../.oc2-env/bin/python3
# Example to use the OpenC2 library
#

import logging
import sys
import sqlite3
import openc2lib as oc2

from openc2lib.encoders.json import JSONEncoder
from openc2lib.transfers.http import HTTPTransfer
from openc2lib.actuators.nmf.nfm_flow_monitor import NFMActuator
import openc2lib.profiles.nfm as nfm

#logging.basicConfig(filename='consumer.log',level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout,level=logging.INFO)
logger = logging.getLogger('openc2')

def main():

# Instantiate the list of available actuators, using a dictionary which key
# is the assed_id of the actuator.
	actuators = {}
	actuators[(nfm.Profile.nsid,'x-nfm')]=NFMActuator()

	c = oc2.Consumer("testconsumer", actuators, JSONEncoder(),  HTTPTransfer("127.0.0.1", 8080))


	c.run()


if __name__ == "__main__":
	main()
