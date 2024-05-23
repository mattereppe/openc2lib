"""OpenC2 Actuator

This module defines the `Actuator` element used in Commands. It does not include any element concerning the concrete
implementation of Actuators for specific security functions.
"""

import aenum

from openc2lib.types.basetypes  import Choice
from openc2lib.core.profile import Profiles

class Actuator(Choice):
	"""OpenC2 Actuator Profile
	
	The `Actuator` carries the Profile to which the Command applies, according to the definition in Sec. 3.3.1.3 of the 
	Language Specification. The `Actuator` is fully transparent to the concrete implementation of the Profile for a specific
	security functions.
	"""
	register = Profiles

	# According to the specification, the actuator is embedded within an actuator profile. 
	def __init__(self, profile):
		"""Instantiates an `Actuator` with a specific `Profile`. 

		The openc2lib is fully transparent to the structure and syntax of Profiles, which specifiers are defined by external modules 
		(although such modules can be collected in the `/profiles` subfolder. The `Actuator`  takes a `Profile` object as input.
		 """
		self.obj = profile
	# Throw exception if the class is not a valid actuator
		self.choice = Profiles.getName(profile.__class__)
	
	def getTarget(self):
		"""Returns the Profile

			Returns an instance of the `Profile` that was used to create the `Actuator`.
		"""
		return self.obj
	
	def getName(self):
		"""Returns the name of the `Profile`.

			Returns the name of `Profile`, which is the selector carried by the `Actuator` element. This does not include the object itself.
			The `name` is automatically extracted from the `Profile` at creation time.
		"""
		return self.choice

#	@staticmethod
#	def getClass(name: str):
#		"""Returns the class of the `Profile`.
#
#			Returns the class associated to a given  `Actuator` Profile name.  This is used inside the core 
#			library to instantiate the object from an OpenC2 message.
#		"""
#		return Profiles.get(name)

	def __str__(self):
		return self.choice

	def __repr__(self):
		return str(self.obj)




