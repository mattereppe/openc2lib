
class Nsid(str):
	""" OpenC2 Namespace Identifier

		Namespace identifiers are described in Sec. 3.1.4. This class implements the required
			controls on the string length.
	"""
	def __init__(self, nsid):
		""" Initialize `Nsid`

			:param nsid: Text string (must be more than 1 and less than 16 characters.
		"""
		if len(nsid) > 16 or len(nsid) < 1:
			raise ValueError("Nsid must be between 1 and 16 characters")
		self = nsid

	@classmethod
	def fromdict(cls, name, e):
		""" Create `Nsid` instance

			Create `Nsid` instance from string.
			This method is provided to deserialize an OpenC2 message according to the openc2lib approach.
			This method should only be used internally the openc2lib.
			:param name: Text string with the namespace identifier..
			:param e: `Encoder` instance to be used (only included to be compliance with the function footprint.
			:return: `Version` instance.
		"""
		return Nsid(name)
	
