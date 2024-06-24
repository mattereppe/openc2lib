import base64

from openc2lib.types.base.binary import Binary

class Binaryx(Binary):
	""" OpenC2 Binary HEX data

		Binary data that are expected to be encoded with hex 
		as defined in [RFC4648], Section 8 (Sec. 3.1.5).
	"""

	def __str__(self):
		""" Returns base64 encoding """
		if self._data is not None:
			return base64.b16encode(self._data).decode('ascii')
		else:
			return ""
			
	def todict(self, e):
		""" Encodes with base64 """
		return base64.b16encode(self._data).decode('ascii')	

	@classmethod
	def fromdict(cls, dic, e):
		""" Builds from base64encoding """
		print("binary16 decoder")
		print("cls: ", cls)
		print("dic: ", dic)
		print("e: ", e)
		try:
			print("value: ", dic)
			print("ascii: ", dic.encode('ascii'))
			return cls( base64.b16decode(dic.encode('ascii')) )
		except:		
			raise TypeError("Unexpected b16 value: ", dic)
