#!../../.oc2-env/bin/python3
# Example to use the OpenC2 library
#

import logging
import sys

import openc2lib as oc2

from openc2lib.encoders.json import JSONEncoder
from openc2lib.transfers.http import HTTPTransfer

import openc2lib.profiles.slpf as slpf
import openc2lib.profiles.dumb as dumb

from helpers import load_json

#logging.basicConfig(filename='openc2.log',level=logging.DEBUG)
#logging.basicConfig(stream=sys.stdout,level=logging.INFO)
#logger = logging.getLogger('openc2producer')
logger = logging.getLogger()
# Ask for 4 levels of logging: INFO, WARNING, ERROR, CRITICAL
logger.setLevel(logging.INFO)
# Add file logger
file_handler = logging.FileHandler("controller.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(oc2.LogFormatter(datetime=True,name=True, datefmt='%t'))
logger.addHandler(file_handler)

command_path_good = "openc2-commands-good"
NUM_TESTS = 100

def main():
	logger.info("Creating Producer")

	p = oc2.Producer("producer.example.net", JSONEncoder(), HTTPTransfer("127.0.0.1", 8080))


	cmd_list = load_json(command_path_good) 
	for i in range(1, NUM_TESTS+1):
		print("Running test #", i)
		for c in cmd_list:
			cmd = oc2.Encoder.decode(oc2.Command, c)
	
			logger.info("Sending command: %s", cmd)
			resp = p.sendcmd(cmd)
			logger.info("Got response: %s", resp)


if __name__ == '__main__':
	main()
