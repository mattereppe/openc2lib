""" Transfer protocol

	Interface that defines the basic behavior of the Transfer Protocols.
"""

class Transfer:
	""" Transfer protocol

		This is the base class for all implementation of Transfer protocols.
	"""

	def send(self, msg, encoder,token):
		""" Sends a Message

			Encodes, sends a message, and returns the response.

			:arg msg: an otupy `Message` to send
			:arg encoder: the `Encoder` to be used 
			:return: An otupy `Message` that contains the `Response` to the sent Message.
		"""
		pass

	def receive(self, callback, encoder):
		""" Receives a Message
			
			Listen for incoming `Message`s and dispatches them to the `Actuator`. This method may
			be blocking or non-blocking. 

			:arg callback: the `Consumer.dispatch` function that contains the logic to dispatch a `Message`
				to one or more `Actuator`
			:arg encode: the default `Encoder` instance to encode/decode Messages. Implementations might
				use the information carried within OpenC2 Messages to derive the `Encoder` instance 
				(retrieved from the `Encoders` variable.
			:return: None
		"""
		pass
