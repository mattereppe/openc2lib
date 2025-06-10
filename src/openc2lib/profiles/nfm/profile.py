""" Netflow Monitor namespace

	This module defines the nsid and unique name for the NFM profile.
	No explicit values are used anywhere in the rest of the code.
"""

import openc2lib as oc2

nsid = 'x-nfm'

@oc2.extension(nsid = nsid)
class Profile(oc2.Profile):
	""" NFM Profile

		Defines the namespace identifier and the name of the NFM Profile.
	"""
	nsid = nsid
	name = 'Netflow Monitor'
