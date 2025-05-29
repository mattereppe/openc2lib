from otupy.types.base.openc2_type import Openc2Type

class Array(Openc2Type, list):
	""" OpenC2 Array

		Implements OpenC2 Array:
		>An ordered list of unnamed fields with positionally-defined semantics. 
		Each field has a position, label, and type.
		However, position does not matter in this implementation.

		Array can be initialized with both a list, an Array, or a scalar. In the last case, an Array with
		a single value is created. Note that this overrides the typical behaviour of `list` (for
		instance, a `str` is not converted to an `list` of characters). 

		Derived classes must provide a `fieldtypes` dictionary that associate each field name
		to its class. This is strictly required in order to instantiate the object at
		deserialization time. However, no check is performed when new items are inserted.
	"""
	fieldtypes = None
	""" Field types

		A `dictionary` which keys are field names and which values are the corresponding classes.
		Must be provided by any derived class.
	"""

	def __init__(self, args=[]):
		""" `Array` initialization

			`Array`s are initialized the same way as lists. They only take as input an interable (`list`, `tuple`,
			`dict`, or another `Array`/`ArrayOf`). Initialization with scalars is not allowed. In this case, 
			a `tuple` must be used (mind to add the trailing comma even with a single value!)
			:param args: The `list`, `tuple`, `Array`, `ArrayOf` used to initialize. May be empty.
		"""

		if isinstance(args, str):
			# Overwrites the default initialization, which gives undesired behaviour
			# (e.g., strings are converted to array of characters, int fails)
			args = [ args ]
		super().__init__(args)

	def validate(self, num_min=0, num_max=None):
		""" Validate the size of the array

			Validation is successfull if the number of elements is in the given range
			:param num_min: Minimun number of elements in the array (Default to: 0).
			:param num_max: Maximun number of elements in the array (Default: no limit).
			:return: `True` if the size in within the given range, a `ValueError` Exception otherwise.
		"""
		if not num_max:
			valid =  len(self) >= num_min
		else:
			valid =  num_min <= len(self) <= num_max

		if not valid:
			raise(ValueError("Invalid number of elements in Array"))

		return True


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

