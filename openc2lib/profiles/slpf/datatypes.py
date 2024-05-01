from openc2lib import Enumerated

class DropProcess(Enumerated):
	none=1
	reject=2
	false_ack=3

class Direction(Enumerated):
	both=1
	ingress=2
	egress=3

class RuleID(int):
	pass
