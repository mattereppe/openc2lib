from openc2lib.types.basetypes import EnumeratedID, Map, ArrayOf
from openc2lib.types.datatypes import Version, ActionTargets, Nsid

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

class ExtResultsDict(dict):
	def add(self, profile: str, extresults):
		if profile in self:
			raise ValueError("ExtResults already registered")
		self[profile] = extresults
	
ExtendedResults = ExtResultsDict()

class Results(Map):
	fieldtypes = dict(versions= ArrayOf(Version), profiles= ArrayOf(Nsid), pairs= ActionTargets, rate_limit= int)
	extend = None
	extns = ExtendedResults

	def set(self, version=None, profiles=None, pairs=None, rate_limit=None):
		self['version']=version
		self['profiles']=profiles
		self['pairs']=pairs
		self['rate_limit']=rate_limit
