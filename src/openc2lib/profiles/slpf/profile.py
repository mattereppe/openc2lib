""" Statless Packet Filter namespace

	This module defines the nsid and unique name for the SLPF profile.
	No explicit values are used anywhere in the rest of the code.
"""

import openc2lib as oc2

nsid = 'slpf'

@oc2.extension(nsid = nsid)
class Profile(oc2.Profile):
	""" SLPF Profile

		Defines the namespace identifier and the name of the SLPF Profile.
	"""
	nsid = nsid
	name = 'http://docs.oasis-open.org/openc2/oc2slpf/v1.0/oc2slpf-v1.0.md'
