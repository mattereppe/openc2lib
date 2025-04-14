from otupy import Enumerated

class DropProcess(Enumerated):
	""" Drop-Process enumeration

		The action to be performed in case the packet is dropped.
		Defined in Sec. 2.1.3.2 of the SLPF Specification.
	"""
	none=1
	""" Drop the packet and do not send a notification to the source of the packet """
	reject=2
	""" Drop the packet and send an ICMP host unreachable (or equivalent) to the source of the packet """
	false_ack=3
	""" Drop the traffic and send a false acknowledgment """

