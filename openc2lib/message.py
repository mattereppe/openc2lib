import enum
import dataclasses
import uuid
from openc2lib.actions import Actions 
from openc2lib.target import Target
from openc2lib.response import * # This should be made safer by defining __all__ in openc2.targets
from openc2lib.args import Args
from openc2lib.actuator import Actuator
import openc2lib.actuators
import openc2lib.basetypes
from openc2lib.datatypes import DateTime

_OPENC2_CONTENT_TYPE = "application/openc2lib"
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
class Command(Content, openc2lib.basetypes.Record):
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


class Response(Content, openc2lib.basetypes.Map):
	fieldtypes = dict(status= StatusCode, status_text= str, results= Results)
	msg_type = MessageType.response

	def __init__(self, status, status_text = None, results = None):
		self['status'] = status
		if not status_text is None:
			self['status_text'] = status_text
		if not results is None:
			self['results'] = results
