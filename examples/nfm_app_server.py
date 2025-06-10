#!../.oc2-env/bin/python3
# Example to use the OpenC2 library
#

import logging
import sys
import sqlite3
import openc2lib as oc2

from openc2lib.encoders.json import JSONEncoder
from openc2lib.transfers.http import HTTPTransfer
from openc2lib.actuators.nmf import NprobeActuator, PacketbeatActuator

import openc2lib.profiles.nfm as nfm

#logging.basicConfig(filename='consumer.log',level=logging.DEBUG)
'''logging.basicConfig(stream=sys.stdout,level=logging.INFO)
logger = logging.getLogger('openc2')'''
logger = logging.getLogger()
# Ask for 4 levels of logging: INFO, WARNING, ERROR, CRITICAL
logger.setLevel(logging.INFO)
# Create stdout handler for logging to the console 
stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(logging.INFO)
stdout_handler.setFormatter(oc2.LogFormatter(datetime=True,name=True))
# Add both handlers to the logger
logger.addHandler(stdout_handler)
# Add file logger
file_handler = logging.FileHandler("server_nfm_app_probe_y.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(oc2.LogFormatter(datetime=True,name=True, datefmt='%t'))
logger.addHandler(file_handler)
hdls = [ stdout_handler , file_handler]
def main():

# Instantiate the list of available actuators, using a dictionary which key
# is the assed_id of the actuator.
	actuators = {}
	actuators[(nfm.Profile.nsid,'probe_x')]=NprobeActuator(asset_id="probe_x")
	actuators[(nfm.Profile.nsid,'probe_y')]=PacketbeatActuator(asset_id="probe_y")
	

	c = oc2.Consumer("testconsumer", actuators, JSONEncoder(),  HTTPTransfer("127.0.0.1", 8080))


	c.run()

if __name__ == "__main__":
	main()
