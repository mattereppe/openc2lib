""" Dumb `Actuator`

	This module provides a dumb actuator that always answer with a fixed 
	message. Use it for testing only.
"""
import logging

from otupy import ArrayOf,ActionTargets, TargetEnum, Nsid, Version,Results, StatusCode, StatusCodeDescription, Actions, Command, Response, ResponseType, Feature, Features
import otupy.profiles.slpf as slpf
import otupy.profiles.dumb as dumb 

logger = logging.getLogger(__name__)

OPENC2VERS=Version(1,0)
""" Supported OpenC2 Version """

# A dumb actuator that does not implement any function but can
# be used to test the openc2 communication.
class DumbActuator:
	def run(self, cmd):

		try:
			match cmd.action:
				case Actions.query:
					response = self.query(cmd)
				case Actions.allow:
					response = self.allow(cmd)
				case Actions.deny:
					response = self.deny(cmd)
	#			case Actions.update:
	#				response = self.update(cmd)
	#			case Actions.delete:
	#				response = self.delete(cmd)
				case Actions.copy:
					response = self.copy(cmd)
				case Actions.scan:
					response = self.scan(cmd)
				case _:
					response = self.__notimplemented(cmd)
		except Exception as e:
			return self.__servererror(cmd, e)

		return response

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
					pf.append(dumb.Profile.nsid)
					pf.append(slpf.Profile.nsid)
					features[Feature.profiles.name]=pf
				case Feature.pairs:
					features[Feature.pairs.name]=[]
				case Feature.rate_limit:
					return Response(status=StatusCode.NOTIMPLEMENTED, status_text="Feature 'rate_limit' not yet implemented")
				case _:
					return Response(status=StatusCode.NOTIMPLEMENTED, status_text="Invalid feature '" + str(f) + "'")

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

	def __servererror(self, cmd, e):
		""" Internal server error

			Default response in case something goes wrong while processing the command.
			:param cmd: The command that triggered the error.
			:param e: The Exception returned.
			:return: A standard INTERNALSERVERERROR response.
		"""
		if(logging.root.level < logging.INFO):
			logger.warn("Returning details of internal exception")
			logger.warn("This is only meant for debugging: change the log level for production environments")
			return Response(status=StatusCode.INTERNALERROR, status_text='Internal server error: ' + str(e))
		else:
			return Response(status=StatusCode.INTERNALERROR, status_text='Internal server error')


