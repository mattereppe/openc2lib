from otupy.types.base import Enumerated

class L4Protocol(Enumerated):
	""" OpenC2 L4 Protocol

		This is an enumeration for all known transport protocols. The numeric identifier
		is set to the protocol number defined for IP.
	"""
	icmp = 1
	tcp = 6
	udp = 17
	sctp = 132

