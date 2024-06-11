"""OpenC2 Actions

	This module defines the list of Actions defined by the Language Specification.
"""

import aenum 
from openc2lib.types.base import Enumerated

# TODO: Add full list of basic actions listed in Sec. 3.3.1
class Actions(Enumerated):
	"""OpenC2 Actions list

		This class enumerates the OpenC2 Actions listed in Sec. 3.3.1.1 of the Language Specification.
		The enumeration refers to the ID used in the Language Specification.
		
		OpenC2 Actions SHALL NOT be extended by Profiles.
	"""
	scan = 1
	locate = 2
	query = 3
	deny = 6
	allow = 8
	update = 16
	delete = 20


# DISABLED because not allowed by the Language Specification.
# New actions can be registered with the following syntax:
# Actions.add('<action_name>', <action_id>)
# <action_name> must be provided as a str
#	@classmethod
#	def add(cls, name, identifier):
#		aenum.extend_enum(Actions, name, identifier)

	def __repr__(self):
		return self.name

