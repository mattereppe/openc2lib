import json

from openc2lib import Encoder, register_encoder


@register_encoder
class JSONEncoder(Encoder):
	encoder_type = 'json'

	@staticmethod
	def encode(obj):
		return json.dumps(Encoder.todict(obj))

	@staticmethod
	def decode(msg, msgtype=None):
		if msgtype == None:
			return json.loads(msg)

		if isinstance(msg, str):
			return Encoder.decode(msgtype, json.loads(msg))
		else:
			return Encoder.decode(msgtype, msg)

