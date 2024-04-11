from openc2lib.basetypes import EnumeratedID, Map, ArrayOf
from openc2lib.datatypes import Version, ActionTargets, Nsid

class StatusCode(EnumeratedID):
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

class Results(Map):
	fieldtypes = dict(versions= Version, profiles= ArrayOf(Nsid), pairs= ActionTargets, rate_limit= int)
