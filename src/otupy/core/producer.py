""" OpenC2 Producer functions

	This module provides the `Producer` class for implementing an OpenC2 Producer.

"""
from otupy.core.message import Message
from otupy.core.command import Command
from otupy.core.encoder import Encoder
from otupy.core.transfer import Transfer

class Producer:
	"""
		OpenC2 Producer

		An OpenC2 Producer sends Commands and receives Responses. The `Producer` is an intermediary to 
		deal with OpenC2-related issues, but does not implement any control logic. A `Producer` instance
		is used to create an OpenC2 stack with an `Encoder` and a `Transfer` protocol. The `Producer`
		is associated to an identifier to distinguish its messages.	

		Note that the actuator instance is only known to the consumer, which runs it. The producer 
		 knows the profile of the actuator, which embeds the an identifier for the actual
		 actuator run by the consumer.
		"""
	def __init__(self, producer: str, encoder: Encoder =None, transfer: Transfer =None):
		""" Initialize an OpenC2 stack

			Creates a `Producer` communication stack made of an identifier, an Encoding format, and a 
			Transfer protocol. This will be used as the "default" stack if no otherwise overwritten
			when sending the message.
			Both the Encoding and Transfer class must be derived from the base `Encoder` and `Transfer` definition.

			:param producer: A string that identifies the `Producer`.
			:param encoder: An instance of an Encoding class derived from base `Encoder`.
			:param transfer: An instnace of a Transfer protocol derived from base `Transfer`.
		"""
		if not isinstance(producer, str):
			raise TypeError('Only strings are allowed for producer identifier')
		self.producer = producer
		self.encoder = encoder
		self.transfer = transfer

	def sendcmd(self, cmd: Command, encoder: Encoder =None, transfer: Transfer =None, consumers: [] =None):
		""" Send an OpenC2 message

			Sends an otupy `Command`. The default communication stack is used, if a different one is not specified. 
			This method internally creates the `Message` metadata that will be encoded and traferred.
			
			The option to
			create a different stack is given to manage the presence of multiple `Consumer` with different stacks.
			However, it is recommended to create different `Producer`s in this case.
			Note that the `consumer` argument is meant for internal use of a `Consumer` only, because the
			endpoint of the message is always identified by the `Transfer` definition.


			:param cmd: The `Command` to be sent.
			:param encoder: An instance of an Encoding class derived from base `Encoder`.
			:param transfer: An instnace of a Transfer protocol derived from base `Transfer`.
			:param consumers: An optional list of strings that identify multiple intended recipients of the
				message.
			:return: The `Response` to the `Command`.
		"""
		if not encoder: encoder = self.encoder
		if not transfer: transfer = self.transfer
		if not transfer: raise ValueError('Missing transfer object')
		if not encoder: raise ValueError('Missing encoder object')
		
		msg = Message(cmd)
		msg.from_=self.producer
		msg.to=consumers

		return transfer.send(msg, encoder)



