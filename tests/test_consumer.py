import logging
import sys
sys.path.insert(0,'/Users/matteo/Progetti/OpenC2/openc2/src')

import openc2lib as oc2

from openc2lib.encoders.json_encoder import JSONEncoder
from openc2lib.transfers.http_transfer import HTTPTransfer
from openc2lib.actuators.dumb_actuator import DumbActuator
from openc2lib.actuators.iptables_actuator import IptablesActuator
import openc2lib.profiles.slpf as slpf

#logging.basicConfig(filename='consumer.log',level=logging.DEBUG)
#logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout,level=logging.INFO)
logger = logging.getLogger('openc2')
	
def main():

# Instantiate the list of available actuators, using a dictionary which key
# is the assed_id of the actuator.
	actuators = {}
	actuators[('slpf','iptables')]=IptablesActuator()

	c = oc2.Consumer("testconsumer", actuators, JSONEncoder(), HTTPTransfer("127.0.0.1", 8080))


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
