""" OpenC2 Target

	This module implements the Target types defined in Sec. 3.4.1 [OpenC2 Languate specification].
"""

import aenum

from otupy.types.base import Choice
from otupy.types.data import TargetEnum
from otupy.core.register import Register
from otupy.core.extensions import Extensions


class TargetRegister(Register):
	""" Target registration
	
		This class registers all available `Target`s, both provided by the otupy and by Profiles.
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
			if identifier is None:
				aenum.extend_enum(TargetEnum, name)
			else:
				aenum.extend_enum(TargetEnum, name, identifier)
			return
		raise ValueError("Target already registered")

Extensions['Targets'] = TargetRegister()
""" List of available `Target`s

	Include base Targets defined by the Language Specification and additional Targets defined by Profiles.
"""

def target(name, nsid=None):
	""" The `@target` decorator

		Use this decorator to declare a `Target` in otupy extensions.
		:param name: The name of the target, as provided by the corresponding specification.
		:param nsid: The Profile NameSpace identifier (must be the same as defined by the corresponding Profile specification.
		:result: The following class definition is registered as valid `Target` in otupy.
	"""
	def target_register(cls):
		Extensions['Targets'].add(name, cls, None, nsid)
		return cls
	return target_register

class Target(Choice):
	""" OpenC2 Target in `Command`

		This is the definition of the `target` carried in OpenC2 `Command`.
	"""
	register = Extensions['Targets']
	""" Keeps the list of registered `Target`s 
	
		For internal use only. Do not delete or modify.
	"""



