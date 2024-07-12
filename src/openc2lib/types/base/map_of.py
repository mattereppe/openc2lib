import logging

from openc2lib.types.base.openc2_type import Openc2Type
from openc2lib.types.base.map import Map

logger = logging.getLogger(__name__)

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
			fieldtypes = {'key': ktype, 'value': vtype}
			""" The type of values stored in this container """

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
					self[self.fieldtypes['key'](k)] = self.fieldtypes['value'](v)
		


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
					objk = e.fromdict(cls.fieldtypes['key'], k)
					objdic[objk] = e.fromdict(cls.fieldtypes['value'], v)
				return objdic

		return MapOf
