from otupy import Enumerated

class Direction(Enumerated):
	""" Direction enumeration

		The packet direction to which a rule applies.
		Defined in Sec. 2.1.3.2 of the SLPF Specification.
	"""
	both=1
	""" Apply rules to all traffic """
	ingress=2
	""" Apply rules to incoming traffic only """
	egress=3
	""" Apply rules to outgoing traffic only """

