""" OpenC2 Response elements

	This module defines the elements beard by a `Response`.
"""
from openc2lib.types.base import EnumeratedID, Map, ArrayOf
from openc2lib.types.data import Version, ActionTargets, Nsid

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

class ExtResultsDict(dict):
	""" Extended Results

		This class is used to extend the basic `Results` definition. If follows the same logic as 
		other extended class in the openc2lib. 
	"""
	def add(self, profile: str, extresults):
		""" Add extension

			Add a new extension for a given `Profile`. The extension must be registered only once.
			:param profile: The name of the profile for which the extension is registered.
			:param extresults: The Extension to be registered.
			:return: None
		"""
		if profile in self:
			raise ValueError("ExtResults already registered")
		self[profile] = extresults
	
ExtendedResults = ExtResultsDict()
""" List of Extended Results

	List of registered extensions to `Results`. It is only used internally the openc2lib to correctly
	parse incoming Rensponses.
"""

class Results(Map):
	""" OpenC2 Response Results

		This class implements the definition in Sec. 3.3.2.2 of the Language Specification. The `Results` carry
		the output of an OpenC2 Command. This definition only includes basic fields and it is expected to
		be extended for each `Profile`.

		Extensions must be derived class that define the following member:
			- `fieldtypes`
			- `extend`
			- `nsid`
		`nsid` must be set to the profile name.
	"""
	fieldtypes = dict(versions= ArrayOf(Version), profiles= ArrayOf(Nsid), pairs= ActionTargets, rate_limit= int)
	""" Field types
	
		This is the definition of the fields beard by the `Results`. This definition is for internal use only,
		to parse OpenC2 messages. Extensions must include these fields and add additional definitions.
	"""
	extend = None
	""" Extension

		This field must be set to None in the base class, and to `Results` in the derived class that defines an extension.
	"""
	regext = ExtendedResults
	""" Extended NameSpace

		This field is for internal use only and must not be set by any derived class.
	"""

	def set(self, versions=None, profiles=None, pairs=None, rate_limit=None):
		""" Set values

			This function may be used to set specific values of the `Results`, with a key=value syntax.
			:param version: List of OpenC2 Versions supported by the Actuator.
			:param profiles: List of OpenC2 Profiles supported by the Actuator.
			:param pairs: List of `Targets` applicable to each supported `Action`.
			:param rate_limit: Maximum number of requests per minute supported by design or policy.
			:return: None
		"""
		self['versions']=versions
		self['profiles']=profiles
		self['pairs']=pairs
		self['rate_limit']=rate_limit
