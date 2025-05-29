""" Context Discovery namespace

	This module defines the nsid and unique name for the CTXD profile.
	No explicit values are used anywhere in the rest of the code.
"""

import otupy as oc2

nsid = 'x-ctxd'

@oc2.extension(nsid = nsid)
class Profile(oc2.Profile):
	""" CTXD Profile

		Defines the namespace identifier and the name of the SLPF Profile.
	"""
	nsid = nsid
	name = 'Context Discovery'
