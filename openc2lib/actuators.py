import aenum

ActuatorTypes = {}

class ActuatorsDict(dict):
	def add(self, name: str, actuator, identifier):
		try:
			list(ActuatorTypes.keys())[list(ActuatorTypes.values()).index(actuator)]
		except ValueError:
			# The item is not in the list
			self[name] = actuator
			return
		raise ValueError("Actuator already registered")
	
Actuators = ActuatorsDict()


#Targets.add('ipv4_net', openc2lib.targettypes.IPv4Net, 13)
#Targets.add('ipv4_connection', openc2lib.targettypes.IPv4Connection, 15)
