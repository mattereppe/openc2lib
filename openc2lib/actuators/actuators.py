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

