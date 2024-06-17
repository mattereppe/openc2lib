from openc2lib.types.base import Choice, Binary
from openc2lib.types.data.uri import  URI
from openc2lib.core.register import Register


class Payload(Choice):
	""" OpenC2 Payload

		Choice of literal content or URL (Sec. 3.4.2.13).
	"""
	register = Register({'bin': Binary, 'url': URI})

