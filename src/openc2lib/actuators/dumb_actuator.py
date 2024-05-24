""" Dumb `Actuator`

	This module provides a dumb actuator that always answer with a fixed 
	message. Use it for testing only.
"""
from openc2lib import ArrayOf,ActionTargets, TargetEnum, Nsid, Version,Results, StatusCode, StatusCodeDescription, Actions, Command, Response

# A dumb actuator that does not implement any function but can
# be used to test the openc2 communication.
class DumbActuator:
	def run(self, cmd):

		at = ActionTargets()
		at[Actions.scan] = [TargetEnum.ipv4_net]
		at[Actions.query] = [TargetEnum.ipv4_net, TargetEnum.ipv4_connection]
		pf = ArrayOf(Nsid)()
		pf.append(Nsid('slpf'))
		res = Results(versions=Version(1,0), profiles=pf, pairs=at,rate_limit=3)
		r = Response({'status': StatusCode.OK, 'status_code': StatusCodeDescription[StatusCode.OK], 'results': res})

		return r
