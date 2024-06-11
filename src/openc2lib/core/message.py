"""OpenC2 Message structures

This module defines the OpenC2 Message structure and its content type, as defined
in Sec. 3.2 of the Language Specification.

The definition include: `Message`, `Content`, `Command`, and `Response`.
"""


import enum
import dataclasses
import uuid

from openc2lib.types.data import DateTime, Version
from openc2lib.types.base import Record, Map

from openc2lib.core.actions import Actions 
from openc2lib.core.target import Target
from openc2lib.core.response import StatusCode, Results
from openc2lib.core.args import Args

from openc2lib.core.actuator import Actuator

_OPENC2_CONTENT_TYPE = "openc2"
_OPENC2_VERSION = Version(1,0)

class MessageType(enum.Enum):
	"""OpenC2 Message Type
	
	Message type can be either `command` or `response`.
	"""
	command = 1
	response = 2


class Content:
	""" Content of the OpenC2 Message

		A content is the base class to derive either a `Command` or a `Response`. 
	"""
	msg_type: MessageType = None
	"The type of Content (`MessageType`)"

	def getType(self):
		""" Returns the Content type """
		return self.msg_type

@dataclasses.dataclass
class Message:
	"""OpenC2 Message
	
	The Message class embeds all Message fields that are defined in Table 3.1 of the
	Language Specification. It is just an internal structure that is not automatically
	serialized, since the use of the fields depends on the specific transport protocol.
	"""
	content: Content
	""" Message body as specified by `content_type` and `msg_type`. """
	content_type: str = _OPENC2_CONTENT_TYPE
	""" Media Type that identifies the format of the content, including major version."""
	msg_type: MessageType = None
	"""The type of OpenC2 Message."""
	status: int = None
	"""Populated with a numeric status code in Responses."""
	request_id: str = None
	"""A unique identifier created by the Producer and copied by Consumer into all Responses."""
	created: int = None
	"""Creation date/time of the content."""
	from_: str = None
	"""Authenticated identifier of the creator of or authority for execution of a message. 

	This field is named `from` in the Specification.
	"""
	to: [] = None
	""" Authenticated identifier(s) of the authorized recipient(s) of a message."""
	version: Version = _OPENC2_VERSION
	"""OpenC2 version used to encode the `Message`.

	This is is an additional field not envisioned by the Language Specification.
	"""
	encoding: object = None
	"""Encoding format used to serialize the `Message`.

	This is is an additional field not envisioned by the Language Specification.
	"""
	
	def __post_init__(self ):
		self.request_id = str(uuid.uuid4()) 
		self.created = int(DateTime())
		try:
			self.msg_type = self.content.msg_type
		except AttributeError:
			pass

#todo
	def todict(self):
		""" Serialization to dictionary."""
#dict = {"headers
		dic = self.__dict__
		return dic


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
		if not isinstance(self.target, Target):
			self.target = Target(self.target)
		if not isinstance(self.actuator, Actuator) and self.actuator is not None:
			self.actuator = Actuator(self.actuator)


class Response(Content, Map):
	"""OpenC2 Response

		This class defines the structure of the OpenC2 Response. According to the definition
			in Sec. 3.3.2 of the Language Specification, the `Response` contains a list of
		  <key, value> pair. This allows for extensions by the Profiles.

			Extensions to `Response` must extend `fieldtypes` according to the allowed field
	 		names and types. `fieldtypes` is used to parse incoming OpenC2 messages and to build
		   and initialize	the
			correct Python objects for each \<key, value\> pair.		
	"""
		
	fieldtypes = dict(status= StatusCode, status_text= str, results= Results)
	"""The list of allowed \<key,value\> pair expected in a `Response`"""
	msg_type = MessageType.response

