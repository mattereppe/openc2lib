# This module implements the Target types defined in Sec. 3.4.1 [OpenC2 Languate specification]
#
import aenum

from openc2lib.types.language import Choice
from openc2lib.core.targets import Targets


class Target(Choice):

	def __init__(self, target):
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

