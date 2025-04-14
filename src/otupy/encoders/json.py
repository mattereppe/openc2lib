""" JSON Encoding

	This module provides the code for encoding OpenC2 messages with JSON.
"""
import json

from otupy import Encoder, register_encoder


@register_encoder
class JSONEncoder(Encoder):
	""" JSON Encoder
	
		This class implements the `Encoder` interface for the JSON format. It leverages
		the intermediary dictionary representation.

		The `JSONEncoder` can be used to create an OpenC2 stack in `Consumer` and `Producer`.
	"""
	encoder_type = 'json'
	""" The label that is used to identify this `Encoder` in OpenC2 messages. """

	@staticmethod
	def encode(obj):
		""" Encode an OpenC2 object

			This method is used to encode an otupy object, which usually is a `Command` or `Message`. 
			The implementation leverages the intermediary dictionary representation and it is
			therefore agnostic of otupy clases.

			:param obj: A valid otupy object.
			:return: A string with the json representation of the `obj`.

		"""
		return json.dumps(Encoder.todict(obj), indent=3)

	@staticmethod
	def decode(msg, msgtype=None):
		""" Decode an OpenC2 message

			This method is used to create an otupy object of type `msgtype` from a json record. 
			The otupy class `msgtype` corresponding to the json record `msg` must be explicitly provided,
			since parsing and automatically inferring the `msgtype` is not currently implemented.

			The implementation leverages the intermediary dictionary representation and it is
			therefore agnostic of otupy classes.

			:param msg: The json record to decode.
			:param msgtype: The otupy class to convert the json to.
			:return: An `msgtype` class initialized according to the json content.
		"""
		if msgtype == None:
			return json.loads(msg)

		if isinstance(msg, str):
			return Encoder.decode(msgtype, json.loads(msg))
		else:
			return Encoder.decode(msgtype, msg)

