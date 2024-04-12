import logging
import sys
from openc2lib.consumer import Consumer
from openc2lib.encoders.json_encoder import JSONEncoder
from openc2lib.encoder import Encoder
from openc2lib.transfers.http_transfer import HTTPTransfer
from openc2lib.transfer	import Transfer
from openc2lib.message import Response
from openc2lib.datatypes import *
from openc2lib.actuators.dumb_actuator import DumbActuator
import openc2lib.response

#logging.basicConfig(filename='consumer.log',level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)
logger = logging.getLogger('openc2')
	
def main():

	c = Consumer("testconsumer", [DumbActuator()], JSONEncoder(), HTTPTransfer("acme.com", 8080))

	c.run()



#print(msg)
#print(msg.content)
#
##print(type(msg.content.target))
#
#print("Creating response")
#
#
#print(r)
#
#c.reply(r)
#
#logger.debug('debug')
#logger.warn('warn')
#logger.error('error')

if __name__ == "__main__":
	main()
