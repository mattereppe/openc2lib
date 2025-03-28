import logging

from openc2lib.types.base.openc2_type import Openc2Type
from openc2lib.types.base.array import Array

logger = logging.getLogger(__name__)

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
			
			def validate(self, types: bool=True, num_min: int = 0, num_max: int = None):
				""" Validate the list 
		
					Validation checks the types of the item and the size of the array. By properly combining the options,
					validation may include only a specific aspect.
					:param types: Set to `True` to validate the types of element in the list (Default: `True`).
					:param num_min: Set to the minimun number of elements; 0 to disable (Default: 0).
					:param num_max: Set to the maximun number of elements; None to disable (Default: None).
					:return: True if every required condition is satisfied. Otherwise, a `ValueError` Exception is raised.
				"""
				for i in self:
					if types and not isinstance(i, self.fieldtype):
						raise ValueError("Invalid field type")

					 	
				return super().validate(num_min, num_max)
			
			# This is the code if I would like to do type checking
			# when inserting data
			def __to_fldtype(self, item):
				return item if type(item)==self.fieldtype else self.fieldtype(item)

			def __init__(self, args=[]):

				super().__init__(args)

				converted_items = []
				for idx, val in enumerate(self):
					self[idx] = (self.__to_fldtype(val))

				
			def append(self, item):
				item = self.__to_fldtype(item)
				super().append(item)
			
			def insert(self, index, item):
				item = self.__to_fldtype(item)
				super().insert(index, item)
			
			def __add__(self, item):
				item = self.__to_fldtype(item)
				super().__add__(item)
			
			def __iadd__(self, item):
				item = self.__to_fldtype(item)
				super().__iadd__(item)

		return ArrayOf



