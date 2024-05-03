import aenum

from openc2lib.types.language import Choice
from openc2lib.core.profile import Profiles

class Actuator(Choice):

	# According to the specification, the actuator is embedded within an actuator profile. 
	# The actuator instance is only known to the consumer, which runs it. The producer only
	# knows the profile of the actuator, which embeds the an identifier for the actual
	# actuator run by the consumer.
	def __init__(self, profile):
		self.obj = profile
	# Throw exception if the class is not a valid actuator
		self.choice = list(Profiles.keys())[list(Profiles.values()).index(profile.__class__)]
	
	def getTarget(self):
		return self.obj
	
	def getName(self):
		return self.choice

	@staticmethod
	def getClass(name: str):
		return Profiles[name]

	def __str__(self):
		return self.choice

	def __repr__(self):
		return str(self.obj)

	def run(self, command):
		raise NotImplementedError("Actuator not implemented!")

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


