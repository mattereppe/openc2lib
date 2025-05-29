""" Dumb profile for testing

"""

import otupy as oc2

@oc2.extension(nsid = 'x-dumb')
class Profile(oc2.Profile):
	""" Dumb Profile

		Defines the namespace identifier and the name of the SLPF Profile.
	"""
	nsid = 'x-dumb'
	name = 'dumb-profile-for-testing'
