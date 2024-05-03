import enum
import dataclasses
import uuid

from openc2lib.types.datatypes import DateTime, Version
from openc2lib.types.basetypes import Record, Map

from openc2lib.core.actions import Actions 
from openc2lib.core.target import Target
from openc2lib.core.response import StatusCode, Results
from openc2lib.core.args import Args

from openc2lib.core.actuator import Actuator

_OPENC2_CONTENT_TYPE = "openc2"
_OPENC2_VERSION = Version(1,0)

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
	version: Version = _OPENC2_VERSION
	encoding: object = None
	
	def __post_init__(self ):
		self.request_id = str(uuid.uuid4()) 
		self.created = int(DateTime())
		try:
			self.msg_type = self.content.msg_type
		except AttributeError:
			pass

#todo
	def todict(self):
#dict = {"headers
		dic = self.__dict__
		return dic


# Init and other standard methods are automatically created
@dataclasses.dataclass
class Command(Content, Record):
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
		if not isinstance(self.actuator, Actuator) and self.actuator is not None:
			self.actuator = Actuator(self.actuator)


class Response(Content, Map):
	fieldtypes = dict(status= StatusCode, status_text= str, results= Results)
	msg_type = MessageType.response

