""" HTTP Message
	
	This module defines the HTTP definition of the abstract OpenC2 Message data.
	See Sec. 3.3.2 of the HTTP Specification.
"""
import dataclasses
import logging
import copy

import otupy as oc2


class Headers(oc2.Map):
	""" HTTP Message Headers (see Sec. 3.3.2 of the Specification) 
		
		Note: the Specification defines `to` as "String [0..*]", but it should be an `ArrayOf(str)`. Using
		a plain Python list does not work with the current otupy implementation.
	"""
	fieldtypes = {'request_id': str, 'created': oc2.DateTime, 'from': str, 'to': oc2.ArrayOf(str)}
	extend = None
	regext = {}


OpenC2Contents = oc2.Register()
""" List allowed OpenC2-Content (see Sec. 3.3.2 of the Specification) """
OpenC2Contents.add('request', oc2.Command, 1)
OpenC2Contents.add('response', oc2.Response, 2)
# Event is not currently defined in the Language Specification
# and there is not indication how to manage it.
# OpenC2Contents.add('notification', oc2.Event, 3)

class OpenC2Content(oc2.Choice):
	""" HTTP Message OpenC2-Content (see Sec. 3.3.2 of the Specification) """
	register = OpenC2Contents

Bodies = oc2.Register()
""" List allowed objects in Body (see Sec. 3.3.2 of the Specification) """
Bodies.add('openc2',OpenC2Content, 1)

class Body(oc2.Choice):
	""" HTTP Message Body (see Sec. 3.3.2 of the Specification) """
	register = Bodies

@dataclasses.dataclass
class Message(oc2.Record):
	""" HTTP Message representation

		This class implements the HTTP-specific representation of the 
		OpenC2 Message metadata. The OpenC2 Message metadata are described in 
		Table 3.1 of the Language Specification as message elements, but they are not
		framed in a concrete structure. The HTTP Specification defines such structure 
		in Sec. 3.3.2, and this class is its implementation.

		The methods of this class are meant to translate back and for the otupy
		`Message` class.
	"""
	headers: Headers = None
	""" Contains the `Message` metadata """
	body: Body = None # This is indeed not optional, but the default argument is set to preserve ordering
	""" Contains the `Content` """
	signature: str = None
	""" Not used (the Specification does not define its usage """

	def set(self, msg: oc2.Message):
		""" Create HTTP `Message` from otupy `Message` 
			
			:param msg: An otupy `Message`.
			:return: An HTTP `Message`
		"""
		self.headers = {}
		self.headers['request_id'] = msg.request_id
		self.headers['created'] = msg.created
		self.headers['from'] = msg.from_
		self.headers['to'] = msg.to

		self.body = Body(OpenC2Content(msg.content))

		
	def get(self):
		""" Create an otupy `Message` from HTTP `Message` 
			
			:param msg: An otupy `Message`.
			:return: An HTTP `Message`
		"""
		msg = oc2.Message(self.body.getObj().getObj())
		msg.request_id = self.headers['request_id'] if 'request_id' in self.headers.keys() else None
		msg.created = self.headers['created'] if 'created' in self.headers.keys() else None
		msg.from_ = self.headers['from'] if 'from' in self.headers.keys() else None
		msg.to = self.headers['to'] if 'to' in self.headers.keys() else None
		msg.msg_type = msg.content.getType()

		return msg

