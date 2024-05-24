""" OpenC2 structures

	Definition of the base types (structures) in the OpenC2 DataModels (Sec. 3.1.1)
	Each OpenC2 object must derive from these classes, which
	affects serialization operations

"""

import aenum
import inspect
import logging

logger = logging.getLogger('openc2lib')
""" openc2lib logger """


class Openc2Type():
	""" OpenC2 Language Element
		
		This class is currently unused and is only provided to have a common ancestor for all
		OpenC2 basic types. It may be used in the future to implement common methods or arguments.
	"""
	pass


#@register_basetype
class Record(Openc2Type):
	""" OpenC2 Record

		Implements OpenC2 Record: 
			>An ordered map from a list of keys with positions to values with 
			positionally-defined semantics. Each key has a position and name, 
			and is mapped to a type.

		It expect keys to be public class attributes. All internal attributes 
		must be kept private by prefixing it with an '_'.

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
		objdic = vars(self)

		dic = {}
		for k,v in objdic.items():
			# Fix keywords corresponding to variable names that clash with Python keywords
			if isinstance(k, str) and k.endswith('_'):
				k = k.rstrip('_')
			# Remove empty and private elements; do not include non-string keys
			if not v is None and not k.startswith('_') and isinstance(k, str):
				dic[k] = v	

		return e.todict(dic)

	@classmethod
	def fromdict(clstype, dic, e):
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
		# Retrieve class type for each field in the dictionary
		fielddesc = None
		for tpl in inspect.getmembers(clstype):
			if tpl[0] == '__annotations__':
				fielddesc = tpl[1]

		for k,v in dic.items():
			if k not in fielddesc:
				raise Exception("Unknown field '" + k + "' from message")
			objdic[k] = e.fromdict(fielddesc[k], v)

		# A record should always have more than one field, so the following statement 
		# should not raise exceptions
		return clstype(**objdic)



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
			return e.fromdict(objtype, v)

class Enumerated(Openc2Type, aenum.Enum):
	""" OpenC2 Enumerated

		Implements OpenC2 Enumerated:
		>A set of named integral constants. The API value is a name.

		The constants may be anything, including strings, integers, classes.
	"""

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

			It is used during deserialization to create an openc2lib instance from the text message.
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
		try:
			return cls(int(dic))
		except:
			raise TypeError("Unexpected enum value: ", dic)

class Array(Openc2Type, list):
	""" OpenC2 Array

		Implements OpenC2 Array:
		>An ordered list of unnamed fields with positionally-defined semantics. 
		Each field has a position, label, and type.

		However, position does not matter in this implementation.

		Derived classes must provide a `fieldtypes` dictionary that associate each field name
		to its class. This is strictly required in order to instantiate the object at
		deserialization time. However, no check is performed when new items are inserted.
	"""
	fieldtypes = None
	""" Field types

		A `dictionary` which keys are field names and which values are the corresponding classes.
		Must be provided by any derived class.
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
		lis = []
		for i in self:
			lis.append = e.todict(i)
		return lis

	def fromdict(cls, dic, e):
		""" !!! WARNING !!!
			Currently not implemented because there are no examples of usage of this
			type (only Array/net, which is not clear)
		"""
		raise Exception("Function not implemented")

class ArrayOf:
	""" OpenC2 ArrayOf

		Implements OpenC2 ArrayOf(*vtype*):
		>An ordered list of fields with the same semantics. 
		Each field has a position and type *vtype*.

		It extends the `Array` type. However, to make its usage simpler and compliant 
		to the description given in the
		Language Specification, the implementation is quite different.
		Note that in many cases `ArrayOf` is only used to create arrays without the need
		to derive an additional data type.
	"""

	def __new__(self, fldtype):
		""" `ArrayOf` builder

			Creates a unnamed derived class from `Array`, which `fieldtypes` is set to `fldtype`.
			:param fldtype: The type of the fields stored in the array (indicated as *vtype* in 
					the Language Specification.
			:return: A new unnamed class definition.
		"""
		class ArrayOf(Array):
			""" OpenC2 unnamed `ArrayOf`

				This class inherits from `Array` and sets its `fieldtypes` to a given type.
		
				One might like to check the type of the elements before inserting them.
				However, this is not the Python-way. Python use the duck typing approach:
				https://en.wikipedia.org/wiki/Duck_typing
				We ask for the type of objects just to keep this information according to
				the OpenC2 data model.

				Note: no `todict()` method is provided, since `Array.todict()` is fine here.
			"""
			fieldtype = fldtype
			""" The type of values stored in this container """

			@classmethod
			def fromdict(cls, lis, e):
				""" Builds instance from dictionary 
		
					It is used during deserialization to create an openc2lib instance from the text message.
					It takes an `Encoder` instance that is used to recursively build instances of the inner
					objects (the `Encoder` provides standard methods to create instances of base objects like
					strings, integers, boolean).
		
					:param lis: The intermediary dictionary representation from which the object is built.
					:param e: The `Encoder that is being used.
					:return: An instance of this class initialized from the dictionary values.
				"""
				objlis = cls()
				logger.debug('Building %s from %s in ArrayOf', cls, lis)
				logger.debug('-> instantiating: %s', cls.fieldtype)
				for k in lis:
					objlis.append(e.fromdict(cls.fieldtype, k))
		
				return objlis
			
			# This is the code if I would like to do type checking
			# when inserting data
#			def append(self, item):
#				if isinstance(item, self.fieldtype):
#					super().append(item)
#				else:
#					raise ValueError(self.fieldtype,' allowed only')
#			
#			def insert(self, index, item):
#				if isinstance(item, self.fieldtype):
#					super().insert(index, item)
#				else:
#					raise ValueError(self.fieldtype,' allowed only')
#			
#			def __add__(self, item):
#				if isinstance(item, self.fieldtype):
#					super().__add__(item)
#				else:
#					raise ValueError(self.fieldtype,' allowed only')
#			
#			def __iadd__(self, item):
#				if isinstance(item, self.fieldtype):
#					super().__iadd__(item)
#				else:
#					raise ValueError(self.fieldtype,' allowed only')

		return ArrayOf


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
		Profiles. Such extensions must use the `extend` and `regext` class attributes to 
		bind to the base element they extend and the `Profile` in which they are defined.
	"""
	fieldtypes: dict = None
	""" Field types

		A `dictionary` which keys are field names and which values are the corresponding classes.
		Must be provided by any derived class.
	"""
	extend = None
	""" Base class

		Data types defined in the Language Specification shall not set this field. Data types defined in
		Profiles that extends a Data Type defined in the Language Specification, must set this field to
		the corresponding class of the base Data Type.

		Note: Extensions defined in the openc2lib context are recommended to use the same name of the base
		Data Type, and to distinguish them through appropriate usage of the namespacing mechanism.
	"""
	regext = {}
	""" Registered extensions

		Classes that implement a Data Type defined in the Language Specification will use this field to
		register extensions defined by external Profiles. Classes that define extensions within Profiles
		shall register themselves according to the specific documentation of the base type class, but 
		shall not modify this field.
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
		newdic=dict()

		# This is necessary because self.extend.fieldtypes does
		# not exist for non-extended classes
		if self.extend is None:
			return e.todict(dict(self))
			
		for k,v in self.items():
			if k not in self.fieldtypes:
				raise ValueError('Unknown field: ', k)
			if k in self.extend.fieldtypes:
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
		logger.debug('Building %s from %s in Map', cls, dic)
		for k,v in dic.items():
			if k in cls.fieldtypes:
				objdic[k] = e.fromdict(cls.fieldtypes[k], v)
			elif k in cls.regext:
				logger.debug('   Using profile %s to decode: %s', k, v)
				extension = cls.regext[k]
				for l,w in v.items():
					objdic[l] = e.fromdict(extension.fieldtypes[l], w)
			else:
				raise TypeError("Unexpected field: ", k)

		if extension is not None:
			cls = extension

		return cls(objdic)

class MapOf:
	""" OpenC2 MapOf

		Implements OpenC2 MapOf(*ktype, vtype*):
		>An unordered set of keys to values with the same semantics. 
			Each key has key type *ktype* and is mapped to value type *vtype*.

		It extends `Map` with the same approach already used for `ArrayOf`.
		`MapOf` for specific types are created as anonymous classes by passing
		`ktype` and `vtype` as arguments.

		Note: `MapOf` implementation currently does not support extensins!.
	"""

	def __new__(self,ktype, vtype):
		""" `MapOf` builder

			Creates a unnamed derived class from `Map`, which `fieldtypes` is set to a single value
		 	`ktype: vtype`.
			:param ktype: The key type of the items stored in the map.
			:param vtype: The value type of the items stored in the map.
			:return: A new unnamed class definition.
		"""
		class MapOf(Map):
			""" OpenC2 unnamed `MapOf`

				This class inherits from `Map` and sets its `fieldtypes` to a given type.
		
				Note: no `todict()` method is provided, since `Map.todict()` is fine here.
			"""
			fieldtypes = {ktype: vtype}
			""" The type of values stored in this container """

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
				logger.debug('Building %s from %s in MapOf', cls, dic)
				for k,v in dic.items():
					kclass = list(cls.fieldtypes)[0]
					objk = e.fromdict(kclass, k)
					objdic[objk] = e.fromdict(cls.fieldtypes[kclass], v)
				return objdic

		return MapOf

