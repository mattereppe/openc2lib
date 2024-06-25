""" Dumb `Actuator`

	This module provides a dumb actuator that always answer with a fixed 
	message. Use it for testing only.
"""
from openc2lib import ArrayOf,ActionTargets, TargetEnum, Nsid, Version,Results, StatusCode, StatusCodeDescription, Actions, Command, Response, ResponseType, Feature, Features
import openc2lib.profiles.slpf as slpf
import openc2lib.profiles.dumb as dumb 

OPENC2VERS=Version(1,0)
""" Supported OpenC2 Version """

# A dumb actuator that does not implement any function but can
# be used to test the openc2 communication.
class DumbActuator:
	def run(self, cmd):

		print("Helpme!!!")

		match cmd.action:
			case Actions.query:
				result = self.query(cmd)
			case Actions.allow:
				result = self.allow(cmd)
			case Actions.deny:
				result = self.deny(cmd)
#			case Actions.update:
#				result = self.update(cmd)
#			case Actions.delete:
#				result = self.delete(cmd)
			case Actions.copy:
				result = self.copy(cmd)
			case Actions.scan:
				result = self.scan(cmd)
			case _:
				print("Not implemented")
				result = self.__notimplemented(cmd)

		return result

	def query(self, cmd):
		""" Query action

			This method implements the `query` action.
			:param cmd: The `Command` including `Target` and optional `Args`.
			:return: A `Response` including the result of the query and appropriate status code and messages.
		"""
		
		# Sec. 4.1 Implementation of the 'query features' command
		if cmd.args is not None:
			if ( len(cmd.args) > 1 ):
				return Response(satus=StatusCode.BEDREQUEST, statust_text="Invalid query argument")
			if ( len(cmd.args) == 1 ):
				try:
					if cmd.args['response_requested'] != ResponseType.complete:
						raise KeyError
				except KeyError:
					return Response(status=StatusCode.BADREQUEST, status_text="Invalid query argument")

		if ( cmd.target.getObj().__class__ == Features):
			r = self.query_feature(cmd)
		else:
			return Response(status=StatusCode.BADREQUEST, status_text="Querying " + cmd.target.getName() + " not supported")

		return r

	def query_feature(self, cmd):
		""" Query features

			Implements the 'query features' command according to the requirements in Sec. 4.1 of the Language Specification.
		"""
		features = {}
		for f in cmd.target.getObj():
			match f:
				case Feature.versions:
					features[Feature.versions.name]=ArrayOf(Version)([OPENC2VERS])	
				case Feature.profiles:
					pf = ArrayOf(Nsid)()
					pf.append(Nsid("dumb"))
					features[Feature.profiles.name]=pf
				case Feature.pairs:
					features[Feature.pairs.name]=[]
				case Feature.rate_limit:
					return Response(status=StatusCode.NOTIMPLEMENTED, status_text="Feature 'rate_limit' not yet implemented")
				case _:
					return Response(status=StatusCode.NOTIMPLEMENTED, status_text="Invalid feature '" + f + "'")

		res = Results(features)
		r = Response(status=StatusCode.OK, status_text=StatusCodeDescription[StatusCode.OK], results=res)

		return r
	
	def allow(self, cmd):
		""" Allow IPv4Net/IPv4Connection

			Do nothing, but return a `rule_number` just for testing response.
		"""
		res = slpf.Results({'rule_number': slpf.RuleID(1234)})
		r = Response(status=StatusCode.OK, status_text=StatusCodeDescription[StatusCode.OK], results=res)
		return r

	def deny(self, cmd):
		""" Deny IPv4Net/IPv4Connection

			Do nothing, but return a `rule_number` just for testing response.
		"""
		res = Results({'rule_number': 1234})
		r = Response(status=StatusCode.OK, status_text=StatusCodeDescription[StatusCode.OK], results=res)
		return r


	def copy(self, cmd):
		return  Response(status=StatusCode.OK, status_text=StatusCodeDescription[StatusCode.OK])

	def scan(self, cmd):
		return  Response(status=StatusCode.OK, status_text=StatusCodeDescription[StatusCode.OK])

	def __notimplemented(self, cmd):
		""" Default response

			Default response returned in case an `Action` is not implemented.
			The `cmd` argument is only present for uniformity with the other handlers.
			:param cmd: The `Command` that triggered the error.
			:return: A `Response` with the appropriate error code.

		"""
		return Response(status=StatusCode.NOTIMPLEMENTED, status_text='Command not implemented')
