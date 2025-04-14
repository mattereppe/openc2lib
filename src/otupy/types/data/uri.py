import rfc3987

class URI:
	""" OpenC2 URI

		Implements the `uri` target (Section 3.4.1.17). 
		A uniform resource identifier (URI) - RFC 3986.

		Note that the standard define the URI type as part of targets, but
		it is also used in the Payload, which is a data type. This breaks 
		the assumption of otupy that `target`s uses `data` and not vice-versa.
		Therefore, a data.URI type is defined, which is used to create the target.
		Users must be aware to distinguish between the two types, namely using 
		`target.URI` as a Target, and `data.URI` as a data type.

		otupy only binds `URI` to `target.URI`. If you need to use `data.URI` to build
		a payload, call it as `types.data.URI`.
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
