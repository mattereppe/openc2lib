""" OpenC2 Profile management

	This module defines the concept of Profile and keeps a list of available `Profiles` 
	registered within the system.
"""

class Profile:
	"""OpenC2 Profile
	
		This is the openc2lib interpretation of the Profile concept. It basically defines
		a Profile namespace and the language extensions that are defined for that namespace.

		A `Profile` is fully transparent to concrete implementation for controlling specific
		security functions, which in openc2lib terminology is named `Actuator`.

		Each Profile defined for openc2lib must inherit from this class.
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

class _ProfilesDict(dict):
	def add(self, name: str, profile, identifier ):
		if name in self:
			raise ValueError("Profile already registered")
		self[name] = profile
	
Profiles = _ProfilesDict()
"""List of registered `Profile`s

	This is a dictionary of available `Profile`s within the system. When a new `Profile` is defined,
	it must be registered in openc2lib before being used.

	Multiple registration of the same Profile will raise a `ValueError` Excepction.

	Methods
	- **add(name: str, profile, identifier)**: Add a new profile

	:param name: the name used to identify the profile (commonly set to its nsid)
	:param profile: the class the extend the basic `Profile` definition
	:param identifier: the numeric identifier assigned by the OpenC2 specification
"""

