import logging

from openc2lib.types.datatypes import DateTime, ResponseType

from openc2lib.core.encoder import Encoder
from openc2lib.core.transfer import Transfer
from openc2lib.core.message import Message, Response
from openc2lib.core.response import StatusCode, StatusCodeDescription

logger = logging.getLogger('openc2')

class Consumer:
	def __init__(self, consumer, actuators=None, encoder: Encoder = None, transfer: Transfer = None):
		self.consumer = consumer
		self.encoder = encoder
		self.transfer = transfer
		self.actuators = actuators

		# TODO: Read configuration from file

	def run(self, encoder: Encoder = None, transfer: Transfer = None):
		if not encoder: encoder = self.encoder
		if not transfer: transfer = self.transfer
		if not transfer: raise ValueError('Missing transfer object')

		transfer.receive(self.dispatch, self.encoder)


	def dispatch(self, msg):
		#TODO: The logic to select the actuator that matches the request
		# OC2 Architecture, Sec. 2.1:
		# The Profile field, if present, specifies the profile that defines the function 
		# to be performed. A Consumer executes the command if it supports the specified 
		# profile, otherwise the command is ignored. The Profile field may be omitted and 
		# typically will not be included in implementations where the functions of the 
		# recipients are unambiguous or when a high- level effects-based command is 
		# desired and tactical decisions on how the effect is achieved is left to the 
		# recipient. If Profile is omitted and the recipient supports multiple profiles, 
		# the command will be executed in the context of each profile that supports the 
		# command's combination of action and target.
		try:
			profile = msg.content.actuator.getName()
		except AttributeError:
			# For a packet filter-only consumer, the following may apply:
			# profile = slpf.nsid
			# Default: execute in the context of multiple profiles
			profile = None
			# TODO: how to mix responses from multiple actuators?
			# Workaround: strictly require a profile to be present
			response = Response(status=StatusCode.BADREQUEST, status_text='Missing profile')
			return self.__respmsg(msg, response)

		try:
			asset_id = msg.content.actuator.getTarget()['asset_id']
		except KeyError:
			# assed_id = None means the default actuator that implements the required profile
			asset_id = None

		try:
			if profile == None:
				# Select all actuators
				actuator = list(self.actuators.values())
			elif asset_id == None:
				# Select all actuators that implement the specific profile
				actuator = list(dict(filter(lambda p: p[0][0]==profile, self.actuators.items())).values())
			else:
				# Only one instance is expected to be present in this case
				actuator = [self.actuators[(profile,asset_id)]]
		except KeyError:
			response = Response(status=StatusCode.NOTFOUND, status_text='No actuator available')
			return self.__respmsg(msg, response)

		response_content = None
		if msg.content.args:
			if 'response_requested' in msg.content.args.keys():
				match msg.content.args['response_requested']:
					case ResponseType.none:
						response_content = None
					case ResponseType.ack:
						response_content = Response(status=StatusCode.PROCESSING, status_text=StatusCodeDescription[StatusCode.PROCESSING])
						# TODO: Spawn a process to run the process offline
						logger.warn("Command: %s not run! -- Missing code")
					case ResponseType.status:
						response_content = Response(status=StatusCode.PROCESSING, status_text=StatusCodeDescription[StatusCode.PROCESSING])
						# TODO: Spawn a process to run the process offline
						logger.warn("Command: %s not run! -- Missing code")
					case ResponseType.complete:
						response_content = self.__runcmd(msg, actuator)
					case _:
						response_content = Response(status=StatusCode.BADREQUEST, status_text="Invalid response requested")

		if not response_content:
			# Default: ResponseType == complete. Return an answer after the command is executed.
			response_content = self.__runcmd(msg, actuator)
					
		logger.debug("Actuator %s returned: %s", actuator, response_content)

		# Add the metadata to be returned to the Producer
		return self.__respmsg(msg, response_content)

	def __runcmd(self, msg, actuator):
		# Run the command and collect the response
		# TODO: Define how to manage concurrent execution from more than one actuator
		try:
			# TODO: How to merge multiple responses?
			# for a in actuators.items(): 
			response_content = actuator[0].run(msg.content) 
		except (IndexError,AttributeError):
			response_content = Response(status=StatusCode.NOTFOUND, status_text='No actuator available')

		return response_content

	def __respmsg(self, msg, response):
		if response:
			respmsg = Message(response)
			respmsg.from_=self.consumer
			respmsg.to=msg.from_
			respmsg.content_type=msg.content_type
			respmsg.request_id=msg.request_id
			respmsg.created=int(DateTime())
			respmsg.status=response['status']
		else:
			respmsg = None
		logger.debug("Response to be sent: %s", respmsg)

		return respmsg



# TODO: Add main to load configuration from file
