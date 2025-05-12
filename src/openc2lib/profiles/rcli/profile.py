""" Remote CLI namespace

	This module defines the nsid and unique name for the RCLI profile.
	No explicit values are used anywhere in the rest of the code.
"""

import openc2lib as oc2

nsid = 'x-rcli'

@oc2.extension(nsid = nsid)
class Profile(oc2.Profile):
	""" RCLI Profile

		Defines the namespace identifier and the name of the RCLI Profile.
	"""
	nsid = nsid
	name = 'Remote CLI'
