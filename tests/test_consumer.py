import logging
import sys
sys.path.insert(0,'/Users/matteo/Progetti/OpenC2/openc2/src')

import otupy as oc2

from otupy.encoders.json_encoder import JSONEncoder
from otupy.transfers.http_transfer import HTTPTransfer
from otupy.actuators.dumb_actuator import DumbActuator
from otupy.actuators.iptables_actuator import IptablesActuator
import otupy.profiles.slpf as slpf

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
