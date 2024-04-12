import logging
from openc2lib.encoder import Encoder
from openc2lib.transfer import Transfer
from openc2lib.message import Message, Response

logger = logging.getLogger('openc2')

class Consumer:
	def __init__(self, consumer, actuators=None, encoder: Encoder = None, transfer: Transfer = None):
		self.consumer = consumer
		self.encoder = encoder
		self.transfer = transfer
		self.actuators = actuators

	def run(self, encoder: Encoder = None, transfer: Transfer = None):
		if not encoder: encoder = self.encoder
		if not transfer: transfer = self.transfer
		if not transfer: raise ValueError('Missing transfer object')

#transfer.run(dispatch, actuators)
		transfer.run(self.dispatch)


	def dispatch(self, msg):
		#TODO: The logic to select the actuator that matches the request
#		for a in actuators:
		actuator = self.actuators[0]

		# Run the command and collect the response
		response = actuator.run(msg.content) 
		logger.debug("Actuator %s returned: %s", actuator, response)

		# Add the metadata to be returned to the Producer

		respmsg = Message(response)
		respmsg.from_=self.consumer
		respmsg.to=msg.from_
		respmsg.content_type=msg.content_type
		respmsg.request_id=msg.request_id
		respmsg.status=response['status']
		logger.debug("Response to be sent: %s", respmsg)

		return respmsg




# TODO: Add main to load configuration from file
