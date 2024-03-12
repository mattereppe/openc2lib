# This module implements the Target types defined in Sec. 3.4.1 [OpenC2 Languate specification]
#
import openc2.targets


class Target(openc2.basetypes.Choice):

	def __init__(self, target):
		self.obj = target
	# Throw exception if the class is not a valid target
		self.choice = list(openc2.targets.Targets.keys())[list(openc2.targets.Targets.values()).index(target.__class__)]
	
	def getTarget(self):
		return self.obj
	
	def getName(self):
		return self.choice

	@staticmethod
	def add(name: str, target):
		try:
			list(openc2.targets.Targets.keys())[list(openc2.targets.Targets.values()).index(target)]
		except ValueError:
			# The item is not in the list
			openc2.targets.Targets[name] = target
			return
		raise ValueError("Target already registered")

	@staticmethod
	def getClass(name: str):
		return openc2.targets.Targets[name]

	def __str__(self):
		return self.choice

	def __repr__(self):
		return str(self.obj)

