from otupy.core.actions import Actions
from otupy.types.base import MapOf, ArrayOf

class ActionArguments(MapOf(Actions, ArrayOf(str))):
	""" OpenC2 Action-Arguments mapping

		Map of each action supported by an actuator to the list of arguments applicable to
		that action. 
		This is not defined in the Language Specification, but used e.g., by the SLPF Profile.
	"""
	pass
