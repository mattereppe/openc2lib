import rfc3987

class URI:
	""" OpenC2 URI

		Implements the `uri` target (Section 3.4.1.17). 
		A uniform resource identifier (URI) - RFC 3986.
	"""
		
	def __init__(self, uri):
		self.set(uri)

	def set(self, uri):
		""" Value must be an Uniform Resource Identifier (URI) as defined in [RFC3986] """
		if rfc3987.parse(uri, rule="URI_reference") is not None:
			self.__uri = str(uri)
		else:
			raise ValueError("Invalid URI -- not compliant to RFC 3986")

	def get(self):
		""" Returns the uri as string """
		return self.__uri

	def __str__(self):
		return self.__uri
