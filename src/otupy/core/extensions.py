""" OpenC2 Extensions

	This module defines internal structures to register extensions defined by additional profiles.
	It also includes helper functions to be used as decorators to manage the registration of the
	extensions.

	Classes that can be extended must allocate an item to keep track of all
	extensions registered in Profiles.
	This class must not be instantiated. Just use its class methods as decorators for both
	base and extended classes.

	Each item in `Extensions` includes:
	- the name of the class to be extended as the key;
	- a `Register` object as value, which will contain all the extensions.

	Usage:
	- Define a class as extensible by using the `@extensible` decorator;
	- Register extensions by using the `@extension` decorator for classes that define an extension.
"""
import copy

from otupy.core.register import Register

Extensions = dict()
""" Extensions

	This is the registry that keeps track of all extensions to the core otupy data and
	structures. 
"""

def extensible(cls):
	""" The `@extensible` decorator

		The `@extensible` decorator makes Map-based class extensible. It adds internal class methods
		that are used in the encoding/decondig processes to manage extensions.
		This decorator must be used in front of all classes that can be extended in Profiles.
	"""
	if cls.__name__ not in Extensions:
		Extensions[cls.__name__]=Register()
	setattr(cls, 'register' , Extensions[cls.__name__])
	setattr(cls, 'base', None)
	return cls

def extension(nsid):
	""" @extends decorator

		This decorator must be used in front of all extensions to Map-based classes.

		@cls: The class which is being extended (no need to specify)
		@base: The base class to extend
		@nsid: The profile name
		@return: The class definition that is now registered and usable in otupy.
	"""
	def extend_wrapper(cls):
		setattr(cls, 'base', cls.__base__)
		setattr(cls, 'nsid', nsid)
		Extensions[cls.__base__.__name__].add(nsid, cls)
		cls.fieldtypes.update(copy.deepcopy(cls.__base__.fieldtypes))
		return cls
	return extend_wrapper


