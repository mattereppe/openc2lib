import enum
import dataclasses
from openc2.actions import Actions 
from openc2.target import Target
from openc2.response import * # This should be made safer by defining __all__ in openc2.targets
from openc2.args import Args
from openc2.actuator import Actuator
import openc2.actuators
import openc2.basetypes
from openc2.datatypes import DateTime

_OPENC2_CONTENT_TYPE = "application/openc2"
_OPENC2_VERSION = "version=1.0"

class MessageType(enum.Enum):
	command = 1
	response = 2

class Content:
	msg_type: str = None

@dataclasses.dataclass
class Message:
	content: Content
	content_type: str = _OPENC2_CONTENT_TYPE
	msg_type: int = None
	status: int = None
	request_id: str = None
	created: int = None
	from_: str = None
	to: [] = None
	version = _OPENC2_VERSION
	
	def __post_init__(self ):
		self.request_id = "" # TODO: Fill in with random string
		self.created = int(DateTime())
		self.msg_type = self.content.msg_type

#todo
	def todict(self):
#dict = {"headers
		dic = self.__dict__
		return dic


# Init and other standard methods are automatically created
@dataclasses.dataclass
class Command(Content, openc2.basetypes.Record):
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
		if not isinstance(self.target, Target):
			self.target = Target(self.target)


# Init and other standard methods are automatically created
@dataclasses.dataclass
class Response(Content):
	status: StatusCode
	status_text: str = None
	results: Results = None
	msg_type = MessageType.response
