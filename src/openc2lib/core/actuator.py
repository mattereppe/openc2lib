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




