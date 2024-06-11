from openc2lib.types.base.openc2_type import Openc2Type
from openc2lib.types.base.logger import logger

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

