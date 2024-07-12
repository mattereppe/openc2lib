import base64

from openc2lib.types.base.binary import Binary

class Binaryx(Binary):
	""" OpenC2 Binary HEX data

		Binary data that are expected to be encoded with hex 
		as defined in [RFC4648], Section 8 (Sec. 3.1.5).
	"""

	def set(self, b):
		""" Set the value internally and covert it, if necessary. Accepted data: bytes, hex strings, Binary, Binaryx."""
		if isinstance(b, bytes):
			self._data = bytes(b)
		elif  isinstance(b, Binaryx) or isinstance(b, Binary):
			self._data = b.get()
		elif isinstance(b, str): 
		# Assume this is a hex-encoded string
			self._data = base64.b16decode(b.upper())
		else:
			raise ValueError("Binary type needs binary value")
	
	def __str__(self):
		""" Returns base64 encoding """
		if self._data is not None:
			return base64.b16encode(self._data).decode('ascii')
		else:
			return ""
			
	def todict(self, e=None):
		""" Encodes with base64 """
		return base64.b16encode(self._data).decode('ascii')	

	@classmethod
	def fromdict(cls, dic, e=None):
		""" Builds from base64encoding """
		try:
			return cls( base64.b16decode(dic.encode('ascii').upper()) )
		except:		
			raise TypeError("Unexpected b16 value: ", dic)
