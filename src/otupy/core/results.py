""" OpenC2 Response Results

	This class defines the basic structure for Results carried in a Response.
	This class can be extended by profiles definitions with additional fields.
	See the main project documentation to learn more about extensions.
"""

from otupy.types.base import Map, ArrayOf
from otupy.types.data import Version, ActionTargets, Nsid
from otupy.core.extensions import extensible


@extensible
class Results(Map):
	""" OpenC2 Response Results

		This class implements the definition in Sec. 3.3.2.2 of the Language Specification. The `Results` carry
		the output of an OpenC2 Command. This definition only includes basic fields and it is expected to
		be extended for each `Profile`.

		Extensions must be declared with the `@extension` decorator, including the Namespace Identifier.
		Extensions must define the additional fields envisioned by the Profile specification in the `fieldtypes` 
		dictionary.
	"""
	fieldtypes = dict(versions= ArrayOf(Version), profiles= ArrayOf(Nsid), pairs= ActionTargets, rate_limit= int)
	""" Field types
	
		This is the definition of the fields beard by the `Results`. This definition is for internal use only,
		to parse OpenC2 messages. Extensions must include these fields and add additional definitions.
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
