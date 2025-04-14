"""OpenC2 Command structure

This module defines the OpenC2 Command structure, as defined
in Sec. 3.2 of the Language Specification.

"""

import dataclasses

from otupy.types.base import Record
from otupy.core.content import MessageType, Content
from otupy.core.actions import Actions 
from otupy.core.target import Target
from otupy.core.args import Args
from otupy.core.actuator import Actuator


# Init and other standard methods are automatically created
@dataclasses.dataclass
class Command(Content, Record):
	"""OpenC2 Command

	This class defines the structure of the OpenC2 Command. The name, meaning, and restrictions for
	the fields are described in Sec. 3.3.1 of the Specification.

	The `target` object is implicitely initialized by passing any valid `Target`.
	"""
	action: Actions
	target: Target
	args: Args = None
	actuator: Actuator = None
	command_id: str = None
	msg_type = MessageType.command

	# Mind that the __post_init__ hides Exceptions!!!! 
	# If something fails in its code, it returns with no errors but does 
	# not complete the code
	def __post_init__(self):
		if not isinstance(self.action, Actions):
			raise TypeError("Invalid action")
		if not isinstance(self.target, Target):
			self.target = Target(self.target)
		if not isinstance(self.actuator, Actuator) and self.actuator is not None:
			self.actuator = Actuator(self.actuator)


