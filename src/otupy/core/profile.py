""" OpenC2 Profile management

	This module defines the concept of Profile and keeps a list of available `Profiles` 
	registered within the system.
"""

from otupy.core.extensions import extensible

@extensible
class Profile:
	"""OpenC2 Profile
	
		This is the otupy interpretation of the Profile concept. It basically defines
		a Profile namespace and the language extensions that are defined for that namespace.

		A `Profile` is fully transparent to concrete implementation for controlling specific
		security functions, which in otupy terminology is named `Actuator`.

		Each Profile defined for otupy must inherit from this class.
	"""
	fieldtypes = {'nsid': str, 'name': str}
	""" Types of fields

		The `fieldtypes` definition is not used in the current implementation. It is only provided
		for compatibility with the extensibility mechanism. It might be used in the future.
	"""
	def __init__(self, nsid, name):
		""" Creates the Profile

			A Profile is identified by its namespace identifier and unique name.
			:param nsid: the Profile NameSpace IDentifier
			:param name: the Profile Unique Name (typically a URL)
		"""
		self.nsid = nsid
		"""Namespace Identifier"""
		self.name = name
		"""Unique Name"""

	def __str__(self):
		return self.nsid

