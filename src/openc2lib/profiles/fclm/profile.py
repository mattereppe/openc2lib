""" File Collection Log Monitor namespace

	This module defines the nsid and unique name for the FCLM profile.
	No explicit values are used anywhere in the rest of the code.
"""

import openc2lib as oc2

nsid = 'x-fclm'

@oc2.extension(nsid = nsid)
class Profile(oc2.Profile):
	""" FCLM Profile

		Defines the namespace identifier and the name of the FCLM Profile.
	"""
	nsid = nsid
	name = 'File Collecion Log Monitoring'
