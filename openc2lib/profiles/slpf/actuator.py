from openc2lib.actuators import Actuators
from openc2lib.profiles.slpf.profile import slpf

class Actuator:
	pass

Actuators.add(slpf.name, Actuator, 1024)
