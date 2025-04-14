import rfc3987

from otupy.core.target import target

@target('iri')
class IRI:
	""" OpenC2 IRI

		Implements the `iri` target (Section 3.4.1.13). 
		Internationalized Resource Identifier, [RFC3987].
	"""
		
	def __init__(self, iri):
		self.set(iri)

	def set(self, iri):
		""" Value must be an Internationalized Resource Identifier (IRI) as defined in [RFC3987] """
		if rfc3987.match(iri, rule='IRI_reference') is not None:
			self.__iri = str(iri)
		else:
			raise ValueError("Invalid IRI -- not compliant to RFC 3987")

	def get(self):
		""" Returns the iri as string """
		return self.__iri

	def __str__(self):
		return self.__iri
