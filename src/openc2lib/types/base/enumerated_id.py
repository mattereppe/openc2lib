from openc2lib.types.base.openc2_type import Openc2Type
from openc2lib.types.base.enumerated import Enumerated

# This class should check the names are integers.
# The enum syntax only allows to define <str = int> pairs,
# so to use this class it is necessary to define mnemonic label
# TODO: Test this code
class EnumeratedID(Enumerated):
	""" OpenC2 EnumeratedID

		Implements OpenC2 EnumeratedID: 
		>A set of unnamed integral constants. The API value is an id.

		The current implementation does not check the values to be integer.
		However, coversion to/from integer is explicitly done during the
		intermediary dictionary serialization, hence throwing an Exception if
		the IDs are not integers.
	"""


	def todict(self, e):
		""" Converts to dictionary 
		
			It is used to convert this object to an intermediary representation during 
			serialization. It takes an `Encoder` argument that is used to recursively
			serialize inner data and structures (the `Encoder` provides standard methods
			for converting base types to dictionaries).. 

			:param e: The `Encoder` that is being used.
			:return: A dictionary compliants to the Language Specification's serialization
			rules.
		"""
		return int(self.value)

	@classmethod
	def fromdict(cls, dic, e):
		""" Builds instance from dictionary 

			It is used during deserialization to create an openc2lib instance from the text message.
			It takes an `Encoder` instance that is used to recursively build instances of the inner
			objects (the `Encoder` provides standard methods to create instances of base objects like
			strings, integers, boolean).

			:param dic: The intermediary dictionary representation from which the object is built.
			:param e: The `Encoder that is being used.
			:return: An instance of this class initialized from the dictionary values.
		"""
		if not isinstance(dic, int):
			raise ValueError("EnumeratedID must be int type")
		try:
			return cls(int(dic))
		except:
			raise TypeError("Unexpected enum value: ", dic)

