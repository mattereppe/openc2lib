from otupy.types.base import Enumerated

class Transfer(Enumerated):

	http=1
	https=2
	mqtt=3

#OpenC2 can be layered over any standard transport protocol (Architecture Specification 2.4)