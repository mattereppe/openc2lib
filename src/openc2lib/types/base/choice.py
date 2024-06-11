from openc2lib.types.base.openc2_type import Openc2Type

class Choice(Openc2Type):
	""" OpenC2 Choice
		Implements the OpenC2 Choice:
		>One field selected from a set of named fields. The API value has a name and a type.

		It expect all allowed values to be provided in a `Register` class, which must be defined
		as class attribute `register` in all derived classes (see `Target` and `Actuator` as examples).
	"""
	register = None
	""" List of registered name/class options available """

	def __init__(self, obj):
		""" Initialize the `Choice` object

			Objects used as `Choice` must be registered in advance in the `register` dictionary.

			:arg obj: An object among those defined in the `register`.
		"""
		self.choice: str = self.register.getName(obj.__class__)
		""" Selected name for the `Choice` """
		self.obj = obj
		""" Class corresponding to the `choice` """

	def getObj(self):
		""" Returns the objet instance embedded in the `register`."""
		return self.obj
	
	def getName(self):
		"""Returns the name of the choice

			Returns the name of object, which is the selector carried by the `Choice` element. 
			This does not include the object itself.
		"""
		return self.choice

	@classmethod
	def getClass(cls, choice):
		""" Get the class corresponding to the current `choice` 
			
			It may be implemented by any derived class, if a different logic than the `Register` class 
			is followed to store the name/class bindings.
			:param choice: The name of the alternative that is being looked for.
			:return: The class corresponding to the provided `choice`.
		"""
		return cls.register.get(choice)

	def __str__(self):
		return self.choice

	def __repr__(self):
		return str(self.obj)

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
		# In case of Choice, the specific choice may be the implementation of an additional type,
		# which affects its representation. So, first of all, get the representation of the inner
		# data type
		dic = {}
		dic[self.choice] = e.todict(self.obj)
		return dic

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
		if not len(dic) == 1:
			raise ValueError("Unexpected dict: ", dic)

		for k, v in dic.items():
			# Expected to run one time only!
			objtype = cls.getClass(k)
			return cls(e.fromdict(objtype, v))

