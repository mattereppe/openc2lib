""" Skeleton `Actuator` for SLPF profile

	This module provides an example to create an `Actuator` for the SLPF profile.
	It only answers to the request for available features.
"""
from openc2lib import ArrayOf,ActionTargets, TargetEnum, Nsid, Version,Actions, Command, Response, StatusCode, StatusCodeDescription

import openc2lib.profiles.slpf as slpf 


OPENC2VERS=Version(1,0)
""" Supported OpenC2 Version """

# An implementation of the slpf profile. 
class IptablesActuator:
	""" Dumb SLPF implementation

		This class provides a skeleton for implementing an `Actuator` according to the openc2lib approach.
	"""
	profile = slpf


	def run(self, cmd):
		""" Process `Command`

			The `run` method executes an OpenC2 `Command` and returns a `Response`.
		"""
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
		""" Query action

			This method implements the `query` action.
			:param cmd: The `Command` including `Target` and optional `Args`.
			:return: A `Response` including the result of the query and appropriate status code and messages.
		"""
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
		""" Default response

			Default response returned in case an `Action` is not implemented.
			The `cmd` argument is only present for uniformity with the other handlers.
			:param cmd: The `Command` that triggered the error.
			:return: A `Response` with the appropriate error code.

		"""
		return Response(status=StatusCode.NOTIMPLEMENTED, status_text='Command not implemented')
