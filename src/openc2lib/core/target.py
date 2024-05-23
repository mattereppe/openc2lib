""" OpenC2 Target

	This module implements the Target types defined in Sec. 3.4.1 [OpenC2 Languate specification].
"""

import aenum

from openc2lib.types.basetypes import Choice
from openc2lib.types.datatypes import TargetEnum
from openc2lib.core.register import Register


class TargetRegister(Register):
	""" Target registration
	
		This class registers all available `Target`s, both provided by the openc2lib and by Profiles.
		The extension of the base class `Register` is necessary to add the nsid prefix in front of the
		`Target` name.
	"""
	
	def add(self, name: str, target, identifier=None, nsid=None):
		""" Add a new `Target`
	
			Register a new `Target` and make it available within the system. This method is expected to
			be called by any `Profile` that defines additional `Target`s. Additionally, the name is added 
			to the Target enumeration `TargetEnum`.
			
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
			list(self.keys())[list(self.values()).index(target)]
		except ValueError:
			# The item is not in the list
			self[name] = target
			aenum.extend_enum(TargetEnum, name, identifier)
			return
		raise ValueError("Target already registered")

Targets = TargetRegister()
""" List of available `Target`s

	Include base Targets defined by the Language Specification and additional Targets defined by Profiles.
"""

class Target(Choice):
	""" OpenC2 Target in `Command`

		This is the definition of the `target` carried in OpenC2 `Command`.
	"""
	register = Targets
	""" Keeps the list of registered `Target`s """

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

#	@staticmethod
#	def getClass(name: str):
#		""" Target object class
#
#			Returns the class that implements a given target type identifier.
#			:param name: the identifier of the target type in a `Target` object
#			:return: a class object
#		"""
#		return Targets.get(name)

	def __str__(self):
		return self.choice

	def __repr__(self):
		return str(self.obj)



