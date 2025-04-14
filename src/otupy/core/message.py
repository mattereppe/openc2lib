"""OpenC2 Message structure

This module defines the OpenC2 Message structure, as defined
in Sec. 3.2 of the Language Specification.

"""

import dataclasses
import uuid

from otupy.types.data import DateTime, Version

from otupy.core.content import MessageType, Content
from otupy.core.version import _OPENC2_VERSION
from otupy.core.content_type import _OPENC2_CONTENT_TYPE	

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


