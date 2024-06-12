"""OpenC2 Command content

This module defines the content of an OpenC2 Message, as defined
in Sec. 3.2 of the Language Specification.

"""

import enum

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

