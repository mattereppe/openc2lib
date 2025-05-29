"""OpenC2 Actions

	This module defines the list of Actions defined by the Language Specification.
"""

import aenum 
from otupy.types.base import Enumerated

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
	contain = 7
	allow = 8
	start = 9
	stop = 10
	restart = 11
	cancel = 14
	set = 15
	update = 16
	redirect = 18
	create = 19
	delete = 20
	detonate = 22
	restore = 23
	copy = 28
	investigate = 30
	remediate = 32


# DISABLED because not allowed by the Language Specification.
# New actions can be registered with the following syntax:
# Actions.add('<action_name>', <action_id>)
# <action_name> must be provided as a str
#	@classmethod
#	def add(cls, name, identifier):
#		aenum.extend_enum(Actions, name, identifier)

	def __repr__(self):
		return self.name

