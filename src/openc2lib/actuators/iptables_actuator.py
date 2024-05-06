from openc2lib import ArrayOf,ActionTargets, TargetEnum, Nsid, Version,Actions, Command, Response, StatusCode, StatusCodeDescription

import openc2lib.profiles.slpf as slpf 


OPENC2VERS=Version(1,0)

# An implementation of the slpf profile. 
class IptablesActuator:
	profile = slpf


	def run(self, cmd):
		if not slpf.validate_command(cmd):
			return Response(status=StatusCode.NOTIMPLEMENTED, status_text='Invalid Action/Target pair')

		if not slpf.validate_args(cmd):
			return Response(status=StatusCode.NOTIMPLEMENTED, status_text='Option not supported')

		match cmd.action:
			case Actions.query:
				r = self.query(cmd)
			case _:
				r = self.__notimplemented(cmd)	

		return r

	def query(self, cmd):
		at = ActionTargets()
		pf = ArrayOf(Nsid)()
		pf.append(Nsid('slpf'))
		res = slpf.Results(versions=ArrayOf(Version)([OPENC2VERS]), 
				profiles=pf, pairs=slpf.AllowedCommandTarget)
		r = Response(status=StatusCode.OK, status_text=StatusCodeDescription[StatusCode.OK], results=res)

		return r

	def allow(self, cmd):
		pass

	def deny(self, cmd):
		pass

	def update(self, cmd):
		pass

	def __notimplemented(self, cmd):
		return Response(status=StatusCode.NOTIMPLEMENTED, status_text='Command not implemented')
