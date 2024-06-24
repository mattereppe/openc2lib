import uritools

class URI:
	""" RFC 3986 compliant URI

		This class is used to hold and check URI according to RFC 3986. For the purpose of OpenC2,
		URIs are just seen as plain strings, so no parsing function is provided.
	"""

	def __init__(self, uri: str):
		""" Initialize an URI

			'URI' can be initialized only with strings that corresponds to RFC 3968 valid URIs.
		"""
		if uritools.isuri(uri):
			self._uri = uri
		else:
		 	raise ValueError("Invalid URI")

	def get(self):
		""" Returns the content of the URI """
		return self._uri


	def __str__(self):
		return self._uri
