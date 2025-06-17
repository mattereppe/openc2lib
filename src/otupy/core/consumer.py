"""OpenC2 Consumer

The `Consumer` implements the expected behaviour of an OpenC2 Consumer server that dispatches OpenC2 Commands
to the Actuators.
"""

import logging

from otupy.types.data import DateTime, ResponseType

from otupy.core.encoder import Encoder
from otupy.core.transfer import Transfer
from otupy.core.message import Message
from otupy.core.response import Response, StatusCode, StatusCodeDescription

logger = logging.getLogger(__name__)

class Consumer:
	"""OpenC2 Consumer

		The `Consumer` is designed to dispatch OpenC2 `Message`s to the relevant `Actuator`. 
		The current implementation receives the configuration at initialization time. It is therefore
		not conceived to be runned itself as a service, but to be integrated in an external component 
		that reads the relevant configuration from file and passes it to the Consumer.

		The `Consumer` has two main tasks:
		- creating the OpenC2 stack to process Messages (namely the combination of an Encoding format and
				a Transfer protocol);
		- dispatching incoming `Command`s to the relevant `Actuator`.

		Each `Consumer` will only run a single `Transfer` protocol. All registered `Encoder`s can be used,
		and a default `Encoder` is explicitely given that will be used when no other selection is available 
		(e.g., to answer Messages that the Consumer does not understand).
		
	"""
	def __init__(self, consumer: str, actuators: [] =None, encoder: Encoder = None, transfer: Transfer = None):
		""" Create a `Consumer`
			:param consumer: This is a string that identifies the `Consumer` and is used in `from` 
				and `to` fields of the OpenC2 `Message` (see Table 3.1 of the Language Specification.
			:param actuators: This must be a list of available `Actuator`s. The list contains the
				`Actuator` instances that will be used by the `Consumer`.
			:param encoder: This is an instance of the `Encoder` that will be used by default.
			:param transfer: This is the `Transfer` protocol that will be used to send/receive `Message`s.
		"""
		self.consumer = consumer
		self.encoder = encoder
		self.transfer = transfer
		self.actuators = actuators

		# TODO: Read configuration from file

	# TODO: Manage non-blocking implementation of the Transfer.receive() function
	def run(self, encoder: Encoder = None, transfer: Transfer = None):
		"""Runs a `Consumer`

			This is the entry point of the `Consumer`. It must be invoked to start operation of the `Consumer`.
			This method may be blocking, depending on the implementation of the `receive()` method of the 
			used `Transfer`.

			The arguments of this method can be used to create multiple OpenC2 stacks (e.g., using 
			different `Encoder`s and `Transfer`s). This feature clearly requires the `Transfer` 
			implementation to be non-blocking.

			:param encoder: A different `Encoder` that might be passed to overwrite what set at initialization time. 
			:param transfer: A different `Transfer` that might be passed to overwrite what set at initialization time.
			:return: None.
		"""
		if not encoder: encoder = self.encoder
		if not transfer: transfer = self.transfer
		if not transfer: raise ValueError('Missing transfer object')

		transfer.receive(self.dispatch, self.encoder)


	def dispatch(self, msg):
		""" Dispatches Commands to Actuators

			This method scans the actuator profile carried in the `Command` and select one or more
			`Actuator`s that will process the `Command`. 
			
			The current implementation is only meant to be used within the
			implementation of `Transfer` protocols as a callback for returning control to the main code.
			This approach is motivated by those Transfer protocols that replies to messages on the same 
			TCP connection, so to avoid errors with NAT and firewalls 
			(if a Command were passed back from the `Transfer.receive()` and processed within the `Consumer.run()`, 
			 the following `Transfer.send() would use a different TCP connection).
			
			:param msg: The full otupy `Message` that embeds the `Command` to be processed.
			:return: A `Message` that embeds the `Response` (from the `Actuator` or elaborated by the `Consumer` in
					case of errors).
		"""
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
			asset_id = msg.content.actuator.getObj()['asset_id']
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
			logger.info("Dispatching command to: %s", actuator[0])
			response_content = actuator[0].run(msg.content) 
		except (IndexError,AttributeError):
			response_content = Response(status=StatusCode.NOTFOUND, status_text='No actuator available')

		return response_content

	def __respmsg(self, msg, response):
		if response:
			respmsg = Message(response)
			respmsg.from_=self.consumer
			respmsg.to=[msg.from_]
			respmsg.content_type=msg.content_type
			respmsg.request_id=msg.request_id
			respmsg.created=int(DateTime())
			respmsg.status=response['status']
		else:
			respmsg = None
		logger.debug("Response to be sent: %s", respmsg)

		return respmsg


# TODO: Add main to load configuration from file
