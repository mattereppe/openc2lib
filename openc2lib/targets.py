import aenum
import openc2lib.targettypes
from openc2lib.datatypes import TargetEnum

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


Targets.add('ipv4_net', openc2lib.targettypes.IPv4Net, 13)
Targets.add('ipv4_connection', openc2lib.targettypes.IPv4Connection, 15)
