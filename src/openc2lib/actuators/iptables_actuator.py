""" Skeleton `Actuator` for SLPF profile

	This module provides an example to create an `Actuator` for the SLPF profile.
	It only answers to the request for available features.
"""
import logging

from openc2lib import ArrayOf,ActionTargets, TargetEnum, Nsid, Version,Actions, Command, Response, StatusCode, StatusCodeDescription, Features, ResponseType, Feature
from openc2lib.actuators.SQLDatabase import SQLDatabase
from openc2lib.actuators.iptables_manager import IptablesManager
from openc2lib.core.actions import Actions
import openc2lib.profiles.slpf as slpf 

logger = logging.getLogger(__name__)

OPENC2VERS=Version(1,0)
""" Supported OpenC2 Version """

MY_IDS = {'hostname': None,
			'named_group': None,
			'asset_id': 'iptables',
			'asset_tuple': None }

# An implementation of the slpf profile. 
class IptablesActuator:
	""" Iptables SLPF implementation

		This class provides an implementation of the SLPF `Actuator` for iptables.
	"""
	
	def __init__(self, args=None,db_name = "openc2_commands.db"):
		self.db = SQLDatabase(db_name)
		self.db.init_db()

	def run(self, cmd):


		# Check if the Command is compliant with the implemented profile
		if not slpf.validate_command(cmd):
			return Response(status=StatusCode.NOTIMPLEMENTED, status_text='Invalid Action/Target pair')
		if not slpf.validate_args(cmd):
			return Response(status=StatusCode.NOTIMPLEMENTED, status_text='Option not supported')

		# Check if the Specifiers are actually served by this Actuator
		try:
			if not self.__is_addressed_to_actuator(cmd.actuator.getObj()):
				return Response(status=StatusCode.NOTFOUND, status_text='Requested Actuator not available')
		except AttributeError:
			# If no actuator is given, execute the command
			pass
		except Exception as e:
			return Response(status=StatusCode.INTERNALERROR, status_text='Unable to identify actuator')

		return Response(status=StatusCode.NOTFOUND, status_text='Fake response for local testing')

		try:
			match cmd.action:
				case Actions.query:
					response = self.query(cmd)
				case Actions.allow:
					response = self.allow(cmd)
				case Actions.deny:
					response = self.deny(cmd)
				case Actions.update:
					response = self.update(cmd)
				case Actions.delete:
					response = self.delete(cmd)
				case _:
					response = self.__notimplemented(cmd)
		except Exception as e:
			return self.__servererror(cmd, e)

		return response

	# def action_mapping(self, action, target):
	# 	action_method = getattr(self, f"{action}", None)
	# 	return action_method(target, self.args)

	def __is_addressed_to_actuator(self, actuator):
		""" Checks if this Actuator must run the command """
		if len(actuator) == 0:
			# Empty specifier: run the command
			return True

		for k,v in actuator.items():
			try:
				if v == MY_IDS[k]:
					return True
			except KeyError:
				pass

		return False
		

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
					pf.append(Nsid(slpf.Profile.nsid))
					features[Feature.profiles.name]=pf
				case Feature.pairs:
					features[Feature.pairs.name]=slpf.AllowedCommandTarget
				case Feature.rate_limit:
					return Response(status=StatusCode.NOTIMPLEMENTED, status_text="Feature 'rate_limit' not yet implemented")
				case _:
					return Response(status=StatusCode.NOTIMPLEMENTED, status_text="Invalid feature '" + f + "'")

		res = None
		try:
			res = slpf.Results(features)
		except Exception as e:
			return __servererror(cmd, e)

		return  Response(status=StatusCode.OK, status_text=StatusCodeDescription[StatusCode.OK], results=res)


	# def action_mapping(self, action, target):
	# 	action_method = getattr(self, f"{action}", None)
	# 	return action_method(target, self.args)

	def insert_handler(self, target, args, action, rule_number=None):
		error, cmd = IptablesManager.insert_rule(target, action)
		rule_number = self.db.insert_command(cmd, rule_number)

		if error is not 200:
			return Response(status=StatusCode.INTERNALERROR, status_text="Internal error")
		elif rule_number < 0:
			return Response(status=StatusCode.INTERNALERROR, status_text="Internal error")
		else:
			res = slpf.Results(rule_number=slpf.RuleID(rule_number))
			return Response(status=StatusCode.OK, status_text="OK", results=res)
				
		return error, rule_number 

	def allow(self, cmd):
		target = cmd.target.getObj()
		args = cmd.args
		return self.insert_handler(target, args, "ACCEPT")

	def deny(self, cmd):
		target = cmd.target.getObj()
		args = cmd.args
		return self.insert_handler(target, args, "DROP")

	def update(self, cmd):
		target = cmd.target.getObj()
		args = cmd.args
		rule_number = int(cmd.target.getObj())
		delete_result = self.delete_handler(target, args, rule_number)
		iptables_target = cmd.args.get('iptables_target')
		return self.insert_handler(target, args, iptables_target, rule_number)

	def delete(self, cmd):
		target = cmd.target.getObj()
		args = cmd.args
		rule_number = int(target)
		cmd_data = self.db.get_command_from_rule_number(rule_number)
		if cmd_data is None:
			return Response(status=StatusCode.INTERNALERROR, status_text="Internal error")
		modified_cmd = IptablesManager.modify_command_for_deletion(cmd_data[0])
		err_code = IptablesManager.delete_rule(modified_cmd)
		if err_code is 200:
			err_db = self.db.delete_command_by_rule_number(rule_number)
			if err_db >= 0:
				return Response(status=StatusCode.OK, status_text="OK")
			
		return Response(status=StatusCode.INTERNALERROR, status_text="Internal error")
				
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
		logger.warn("Returning details of internal exception")
		logger.warn("This is only meant for debugging: change the log level for production environments")
		if(logging.root.level < logging.INFO):
			return Response(status=StatusCode.INTERNALERROR, status_text='Internal server error: ' + str(e))
		else:
			return Response(status=StatusCode.INTERNALERROR, status_text='Internal server error')
