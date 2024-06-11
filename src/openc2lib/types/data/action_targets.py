from openc2lib.core.actions import Actions
from openc2lib.types.base import MapOf, ArrayOf
from openc2lib.types.data.target_enum import TargetEnum


class ActionTargets(MapOf(Actions, ArrayOf(TargetEnum))):
	""" OpenC2 Action-Targets

		Map of each action supported by an actuator to the list of targets applicable to 
		that action (Sec. 3.4.2.1).
		They must be defined by each Profile.
	"""
	pass

