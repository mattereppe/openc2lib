from openc2lib.basetypes import ArrayOf
from openc2lib.datatypes import ActionTargets, TargetEnum, Nsid, Version
from openc2lib.actions import Actions
from openc2lib.message import Command, Response
from openc2lib.response import Results, StatusCode, StatusCodeDescription
from openc2lib.profiles.slpf import slpf

# An implementation of the slpf profile. 
class IptablesActuator:
	profile = slpf

	def run(self, cmd):

		at = ActionTargets()
		at[Actions.scan] = [TargetEnum.ipv4_net]
		at[Actions.query] = [TargetEnum.ipv4_net, TargetEnum.ipv4_connection]
		pf = ArrayOf(Nsid)()
		pf.append(Nsid('slpf'))
		res = Results(versions=Version(1,0), profiles=pf, pairs=at,rate_limit=3)
		r = Response(StatusCode.OK, StatusCodeDescription[StatusCode.OK], res)

		return r
