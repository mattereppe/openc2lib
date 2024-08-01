#!../.oc2-env/bin/python3
# Example to use the OpenC2 library
#

import logging
import sys
import datetime

import openc2lib as oc2


from openc2lib.encoders.json import JSONEncoder
from openc2lib.transfers.http import HTTPTransfer
from openc2lib.actuators.iptables_actuator import IptablesActuator
import openc2lib.profiles.slpf as slpf
import openc2lib.profiles.dumb as dumb
from openc2lib.actuators.dumb_actuator import DumbActuator

#logging.basicConfig(filename='consumer.log',level=logging.DEBUG)
#logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)
#logger = logging.getLogger('openc2:'+__name__)
# Declare the logger name
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
file_handler = logging.FileHandler("server.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(oc2.LogFormatter(datetime=True,name=True, datefmt='%t'))
logger.addHandler(file_handler)
# ?????
hdls = [ stdout_handler , file_handler]
	
def main():

# Instantiate the list of available actuators, using a dictionary which key
# is the assed_id of the actuator.
	actuators = {}
	actuators[(slpf.Profile.nsid,'iptables')]=IptablesActuator()
	actuators[('x-dumb','dumb')]=DumbActuator()

	c = oc2.Consumer("testconsumer", actuators, JSONEncoder(), HTTPTransfer("127.0.0.1", 8080))

	c.run()


if __name__ == "__main__":
	main()
