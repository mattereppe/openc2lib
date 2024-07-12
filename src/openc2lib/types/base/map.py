import logging
import typing

from openc2lib.types.base.openc2_type import Openc2Type

logger = logging.getLogger(__name__)

class Map(Openc2Type, dict):
	""" OpenC2 Map

		Implements OpenC2 Map:
		>An unordered map from a set of specified keys to values with semantics 
			bound to each key. Each field has an id, name and type.

		However, the id is not considered in this implementation.

		The implementation follows a similar logic than `Array`. Each derived class
		is expected to provide a `fieldtypes` class attribute that associate field names 
		with their class definition. 
		
		Additionally, according to the Language Specification, `Map`s may be extended by
		Profiles. Such extensions must use the `base` and `register` class attributes to 
		bind to the base element they extend and the `Profile` in which they are defined.

		For derived types that are recursive (i.e., they need to hold an instance of their same
		type internally), declare the type of the recursive field as `typing.Self`, and 
		use the `@make_recursive` decorator in front of the class definition.
		(See also (recursive definitions)[https://github.com/mattereppe/openc2lib/blob/main/docs/developingextensions.md#recursive-definitions] in the documentation)
	"""
	fieldtypes: dict = None
	""" Field types

		A `dictionary` which keys are field names and which values are the corresponding classes.
		Must be provided by any derived class.
	"""
	base = None
	""" Base class

		Data types defined in the Language Specification shall not set this field. Data types defined in
		Profiles that extends a Data Type defined in the Language Specification, must set this field to
		the corresponding class of the base Data Type.

		Note: Extensions defined in the openc2lib context are recommended to use the same name of the base
		Data Type, and to distinguish them through appropriate usage of the namespacing mechanism.
	"""
	register = None
	""" Registered extensions

		Classes that implement a Data Type defined in the Language Specification will use this field to
		register extensions defined by external Profiles. Classes that define extensions within Profiles
		shall register themselves according to the specific documentation of the base type class, but 
		shall not modify this field.
	"""

	def __init__(self, *args, **kwargs):
		""" Create and validate objects

			Store the map and convert the fields to appropriate types, whenever possible.
			It accepts both plain dictionaries (as first arguments) and keyword arguments (last elements)
			and automatically merges them. Keyword arguments take precedence over non-keyword
			arguments.

			:param args: One or more dictionaries or maps used to initialize this object.
			:param kwargs: keyword arguments used to initialize this object.
		"""
		raw = {}

		for arg in args:
			raw.update(arg)
		# This step is indeed not strictly necessary, but used to give keyword arguments
		# precedence over non-keyword arguments.
		raw.update(kwargs)
		for k,v in raw.items():
			self[k] = self.fieldtypes[k](v)


	def validate_fields(self, min_num=1):
		""" Check whether field names are valid
	
			Check if supplied field names are compliant with the `fieldtypes` list. Only check the name 
			and number of fields, but does not perform any type checking.
	
			:param min_num: Check that at list min_num fields are supplied (usually, at least 1 field must 
					be supplied to create a valid object). Default to 1.
			:return: True if validity check is passed, raise a ValueError exception otherwise.
		"""
		count = 0
		for x in self.keys():
			if x in self.fieldtypes:
				count += 1
			else:
				logger.error("Invalid field: %s", str(x))	
				raise TypeError("Invalid field")
			if not isinstance(self[x], self.fieldtypes[x]):
				raise TypeError("Invalid field type for: " + x)
		if count >= min_num:
			return True
		else:
			raise ValueError("Too few fields provided")
		
	@staticmethod
	def make_recursive(cls):
		""" Make this class recursive

			This method can be used as a decorator to make a Map-derived class recurive, namely to hold objects
			of the same type in `fieldtypes`. To use this function, just declare the field that must be of the same
			type as the class as `typing.Self`, and use the `@make_recursive` decorator at declaration time.
			:param: No arguments must be specified when using this method as a decorator.
			:return: A new instance of the class, where all types in `fieldtypes` marked as `typing.Self` are replaced
		  		with the class instance.
		"""	
		for k,v in cls.fieldtypes.items():
			if v == typing.Self:
				cls.fieldtypes[k] = cls

		return cls

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
		newdic=dict()

		# This is necessary because self.base.fieldtypes does
		# not exist for non-extended classes
		if self.base is None:
			return e.todict(dict(self))
			
		for k,v in self.items():
			if k not in self.fieldtypes:
				raise ValueError('Unknown field: ', k)
			if k in self.base.fieldtypes:
				newdic[k] = v
			else:
				if self.nsid not in newdic:
					newdic[self.nsid]={}
				newdic[self.nsid][k]=v
			
		return e.todict(newdic)

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
		objdic = {}
		extension = None
		logger.debug('Decoding %s from %s in Map', cls, dic)
		try:
			for k,v in dic.items():
				if k in cls.fieldtypes:
					objdic[k] = e.fromdict(cls.fieldtypes[k], v)
				elif k in cls.register:
					logger.debug('   Using profile %s to decode: %s', k, v)
					extension = cls.register[k]
					for l,w in v.items():
						objdic[l] = e.fromdict(extension.fieldtypes[l], w)
				else:
					raise TypeError("Unexpected field: ", k)
		except TypeError:
			logger.error("Unable to decode. Ill-formed object: %s", cls.__name__)
		

		if extension is not None:
			cls = extension

		try:
			logger.debug("Building %s with %s", clstype, objdic)
			return  cls(objdic)
		except Exception as e:
			logger.ERROR("Unable to instantiate %s from %s", cls, objdic)
			raise TypeError("Unable to instantiate class " + cls)

