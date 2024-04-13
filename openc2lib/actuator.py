from openc2lib.basetypes import Choice

class Actuator(Choice):

	def __init__(self, actuator):
		self.obj = target
	# Throw exception if the class is not a valid target
		self.choice = list(Targets.keys())[list(Targets.values()).index(target.__class__)]
	
	def getTarget(self):
		return self.obj
	
	def getName(self):
		return self.choice

	@staticmethod
	def getClass(name: str):
		return Targets[name]

	def __str__(self):
		return self.choice

	def __repr__(self):
		return str(self.obj)

	def run(self, command):
		raise NotImplementedError("Actuator not implemented!")
