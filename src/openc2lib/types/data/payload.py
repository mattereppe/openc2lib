import openc2.types.base
from openc2lib.types.data import Binary, URI


class Payload(openc2.types.base.Choice):
	""" OpenC2 Payload

		Choice of literal content or URL (Sec. 3.4.2.13).
	"""
	register = {'bin': Binary, 'url': URI}

