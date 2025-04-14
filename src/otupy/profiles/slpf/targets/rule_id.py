import otupy as oc2

from otupy.profiles.slpf.profile import Profile

@oc2.target(name='rule_number', nsid=Profile.nsid)
class RuleID(int):
	""" OpenC2 Rule-ID

		Rule identifier returned from allow or deny Command.
		See Sec. 2.1.3.2 of the SLPF Specification.

		The definition is rather trivial in this case, because the Specification
		defines this type as an integer.
	"""
	pass
