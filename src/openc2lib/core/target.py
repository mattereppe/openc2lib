""" OpenC2 Target

	This module implements the Target types defined in Sec. 3.4.1 [OpenC2 Languate specification].
"""

import aenum

from openc2lib.types.basetypes import Choice
from openc2lib.types.datatypes import TargetEnum


class Target(Choice):
	""" OpenC2 Target in `Command`

		This is the definition of the `target` carried in OpenC2 `Command`.
	"""

	def __init__(self, target):
		""" Creates a new `Target`

			Objects used as Target must be registered in advance in the `Targets` dictionary.

			:arg target: An object among those defined as `targettypes`.
		"""
		self.obj = target
		""" Keeps the instance of the target object"""
	# Throw exception if the class is not a valid target
		self.choice = Targets.getName(target.__class__)
		""" Keeps the identifier that the Language Specification associates to each target type"""
	
	def getTarget(self):
		""" Returns the objet instance embedded in the `Target`."""
		return self.obj
	
	def getName(self):
		""" Returns the identifier associated to the Target type."""
		return self.choice

	@staticmethod
	def getClass(name: str):
		""" Target object class

			Returns the class that implements a given target type identifier.
			:param name: the identifier of the target type in a `Target` object
			:return: a class object
		"""
		return Targets.get(name)

	def __str__(self):
		return self.choice

	def __repr__(self):
		return str(self.obj)



class Targets:
	""" List of `Target`s
	
		This class registers all available `Target`s, both provided by the openc2lib and by Profiles.
		The class is meant to be used internally with class methods only without creating any instance.
	"""
	
	_targets = {}

	@classmethod
	def add(cls, name: str, target, identifier, nsid=None):
		""" Add a new `Target`
	
			Register a new `Target` and make it available within the system. This method is expected to
			be called by any `Profile` that defines additional `Target`s.
			
			This method throw an Exception if the `Target` is already registered.

			:param name: The name used for the `Target`.
			:param target: The class that defines the `Target`.
			:param identifier: A numeric value associated to the standard by the Specification.
			:param nsid: The Namespace Identifier where the `Target` is defined. It is prepended to the target `name`.
			:return: None
		"""
		if nsid is not None:
			name = nsid + ':' + name
		try:
			list(cls._targets.keys())[list(cls._targets.values()).index(target)]
		except ValueError:
			# The item is not in the list
			cls._targets[name] = target
			aenum.extend_enum(TargetEnum, name, identifier)
			return
		raise ValueError("Target already registered")

	@classmethod
	def get(cls, name: str):
		""" Get `Target` by name

			Throws an exception if the given name does not correspond to any registered `Target`.

			:param name: The name of the `Target` to return.
			:return: The class `Target` corresponding to the given name.
		"""
		return cls._targets[name]

	@classmethod
	def getName(cls, target):
		""" Get the name of a `Target`

			Given a class `Target`, this method returns its name (the name it was registered with. 
			Note that the returned name include the namespace prefix.

			Throws an exception if the given `Target` is not registered.

			:param target: The class `Target` to look for.
			:return: A string with the name of the `Target`.
		"""
		return list(cls._targets.keys())[list(cls._targets.values()).index(target)]



