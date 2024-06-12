""" OpenC2 Response Results

	This class defines the basic structure for Results carried in a Response.
	This class can be extended by profiles definitions with additional fields.
	See the main project documentation to learn more about extensions.
"""

from openc2lib.types.base import Map, ArrayOf
from openc2lib.types.data import Version, ActionTargets, Nsid

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
