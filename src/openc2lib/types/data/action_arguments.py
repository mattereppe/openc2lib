from openc2lib.core.actions import Actions
from openc2lib.types.base import MapOf, ArrayOf

class ActionArguments(MapOf(Actions, ArrayOf(str))):
	""" OpenC2 Action-Arguments mapping

		Map of each action supported by an actuator to the list of arguments applicable to
		that action. 
		This is not defined in the Language Specification, but used e.g., by the SLPF Profile.
	"""
	pass
