# TODO: Merge this definition in target.py

import aenum

from openc2lib.types.targettypes import Features, IPv4Net, IPv4Connection
from openc2lib.types.datatypes import TargetEnum

TargetObjects = {}

class TargetsDict(dict):
	def add(self, name: str, target, identifier, nsid=None):
		if nsid is not None:
			name = nsid + ':' + name
		try:
			list(TargetObjects.keys())[list(TargetObjects.values()).index(target)]
		except ValueError:
			# The item is not in the list
			self[name] = target
			aenum.extend_enum(TargetEnum, name, identifier)
			return
		raise ValueError("Target already registered")
	
Targets = TargetsDict()


# TODO: Move to __init__
Targets.add('features', Features, 9)
Targets.add('ipv4_net', IPv4Net, 13)
Targets.add('ipv4_connection', IPv4Connection, 15)
