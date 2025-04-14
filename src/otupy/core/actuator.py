"""OpenC2 Actuator

This module defines the `Actuator` element used in Commands. It does not include any element concerning the concrete
implementation of Actuators for specific security functions.
"""

import aenum

from otupy.types.base  import Choice
from otupy.core.extensions import Extensions, Register

Extensions['Actuators'] = Register()

class Actuator(Choice):
	"""OpenC2 Actuator Profile
	
	The `Actuator` carries the Profile to which the Command applies, according to the definition in Sec. 3.3.1.3 of the 
	Language Specification. The `Actuator` is fully transparent to the concrete implementation of the Profile for a specific
	security functions.
	"""
	register = Extensions['Actuators']
	""" Registry of available `Actuator`

		For internal use only. Do not change or alter.
	"""


def actuator(nsid):
	""" The `@actuator` decorator

		Use this decorator to declare an `Actuator` in otupy extensions.
		:param nsid: The Profile NameSpace identifier (must be the same as defined by the corresponding Profile specification.
		:result: The following class definition is registered as valid `Actuator` in otupy.
	"""
	def actuator_registration(cls):
		Extensions['Actuators'].add(nsid, cls)
		return cls
	return actuator_registration





