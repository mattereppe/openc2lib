""" OpenC2 Response elements

	This module defines the elements beard by a `Response`.
"""

from otupy.types.base import EnumeratedID, Map
from otupy.core.content import Content, MessageType
from otupy.core.results import Results

class StatusCode(EnumeratedID):
	""" Status codes

		Status codes provide indication about the processing of the OpenC2 Command.
		They follow the same logic and values of HTTP status code, since they are copied
		in HTTP headers.
"""
	PROCESSING = 102
	OK = 200
	BADREQUEST = 400
	UNAUTHORIZED = 401
	FORBIDDEN = 403
	NOTFOUND = 404
	INTERNALERROR =500
	NOTIMPLEMENTED = 501
	SERVICEUNAVAILABLE = 503

StatusCodeDescription = {StatusCode.PROCESSING: 'Processing', 
										StatusCode.OK: 'OK',
										StatusCode.BADREQUEST: 'Bad Request',
										StatusCode.UNAUTHORIZED: 'Unauthorized',
										StatusCode.FORBIDDEN: 'Forbidden',
										StatusCode.NOTFOUND: 'Not Found',
										StatusCode.INTERNALERROR: 'Internal Error',
										StatusCode.NOTIMPLEMENTED: 'Not Implemented',
										StatusCode.SERVICEUNAVAILABLE: 'Service Unavailable'}
""" Status code description

	Human-readable description of `StatusCode`s. The values are only provided as base values, since any `Actuator`
	can freely use different descriptions.
"""

class Response(Content, Map):
	""" OpenC2 Response

		This class defines the structure of the OpenC2 Response. According to the definition
			in Sec. 3.3.2 of the Language Specification, the `Response` contains a list of
		  <key, value> pair. This allows for extensions by the Profiles.

			Extensions to `Response` must extend `fieldtypes` according to the allowed field
	 		names and types. `fieldtypes` is used to parse incoming OpenC2 messages and to build
		   and initialize	the
			correct Python objects for each <key, value> pair.		
	"""
		
	fieldtypes = dict(status= StatusCode, status_text= str, auth_endpoint=str, results= Results)
	""" The list of allowed <key,value> pair expected in a `Response`"""
	msg_type = MessageType.response

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.validate_fields()

	def validate_fields(self):
		""" Check the `status` field is present """
		if not 'status' in self:
			raise ValueError("A Response must contain the status field")







