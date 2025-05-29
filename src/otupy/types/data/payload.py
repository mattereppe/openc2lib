from otupy.types.base import Choice, Binary
from otupy.types.data.uri import  URI
from otupy.core.register import Register


class Payload(Choice):
	""" OpenC2 Payload

		Choice of literal content or URL (Sec. 3.4.2.13).
	"""
	register = Register({'bin': Binary, 'url': URI})

