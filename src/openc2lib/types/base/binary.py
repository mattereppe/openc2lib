import base64

from openc2lib.types.base.openc2_type import Openc2Type

class Binary(Openc2Type):
	""" OpenC2 Binary data

		Binary data that are expected to be encoded with base64 
		as defined in [RFC4648], Section 5 (Sec. 3.1.5).
	"""

	def __init__(self, b=None):
		""" Initializes from bytes or null """
		if b is None:
			b = b''
		self.set(b)			

	def set(self, b):
		self._data = bytes(b)
	
	def get(self):
		return self._data
	
	def __str__(self):
		""" Returns base64 encoding """
		if self._data is not None:
			return base64.b64encode(self._data).decode('ascii')
		else:
			return ""
			
	def todict(self, e):
		""" Encodes with base64 """
		return base64.b64encode(self._data).decode('ascii')	

	@classmethod
	def fromdict(cls, dic, e):
		""" Builds from base64encoding """
		try:
			return cls( base64.b64decode(dic.encode('ascii')) )
		except:		
			raise TypeError("Unexpected b64 value: ", dic)
