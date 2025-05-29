import aenum

from otupy.types.base.openc2_type import Openc2Type

class Enumerated(Openc2Type, aenum.Enum):
	""" OpenC2 Enumerated

		Implements OpenC2 Enumerated:
		>A set of named integral constants. The API value is a name.

		The constants may be anything, including strings, integers, classes.
	"""

	@classmethod
	def extend(cls, name, value=None):
		""" Extends the Enumarated 
	
			Extends the definition with a new <name, value> pair.
			:param name: The name (tag) used to identify a new element in the Enumeration.
			:param value: The numeric index associated to the Enumerated (optional).
			:return: None
		"""
		if value is None:
			aenum.extend_enum(cls, name)
		else:
			aenum.extend_enum(cls, name, value)

	# Convert enumerations to str
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
		return self.name

	@classmethod
	def fromdict(cls, dic, e):
		""" Builds instance from dictionary 

			It is used during deserialization to create an otupy instance from the text message.
			It takes an `Encoder` instance that is used to recursively build instances of the inner
			objects (the `Encoder` provides standard methods to create instances of base objects like
			strings, integers, boolean).

			:param dic: The intermediary dictionary representation from which the object is built.
			:param e: The `Encoder that is being used.
			:return: An instance of this class initialized from the dictionary values.
		"""
		try:
			return cls[str(dic)]
		except:
			raise TypeError("Unexpected enum value: ", dic)
	
	def __str__(self):
		return self.name
