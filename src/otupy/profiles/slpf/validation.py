""" SLPF validation rules

	This module defines specific SLPF constraints on the usable `Action`s and `Args` defined by the Language Specification.
	See Sec. 2.3 of the SLPF Specification.
"""

from otupy import Actions, StatusCode, ActionTargets, ActionArguments, TargetEnum

from otupy.profiles.slpf.profile import Profile

AllowedActions = [ Actions.query, Actions.deny, Actions.allow, Actions.deny, Actions.update, Actions.delete]
""" List of allowed `Action`s """

AllowedTargets = [ 'feature', 'file', 'ipv4_net', 'ipv6_net', 'ipv4_connection', 'ipv6_connection' , Profile.nsid+':rule_number']
""" List of allowed `Target`s 

	 This is probably not strictly necessary
"""

AllowedStatusCode = [StatusCode.PROCESSING, StatusCode.OK, StatusCode.BADREQUEST, StatusCode.INTERNALERROR, StatusCode.NOTIMPLEMENTED ] 
""" List of allowed status code in `Response` """

AllowedCommandTarget = ActionTargets()
""" List of allowed `Target` for each `Action`

	 Command Matrix (Table 2.3.1): valid Command/Target pairs
"""
# TODO: complete (replace with commented lines) after defining all targets
AllowedCommandTarget[Actions.allow] = [TargetEnum.ipv4_connection, TargetEnum.ipv4_net]
#AllowedCommandTarget[Actions.allow] = [TargetEnum.ipv4_connection, TargetEnum.ipv6_connection,
#	TargetEnum.ipv4_net, TargetEnum.ipv6_net]
AllowedCommandTarget[Actions.deny] = [TargetEnum.ipv4_connection, TargetEnum.ipv4_net]
#AllowedCommandTarget[Actions.deny] = [TargetEnum.ipv4_connection, TargetEnum.ipv6_connection,
#	TargetEnum.ipv4_net, TargetEnum.ipv6_net]
AllowedCommandTarget[Actions.query] = [TargetEnum.features]
AllowedCommandTarget[Actions.delete] = [TargetEnum[Profile.nsid+':rule_number']]
AllowedCommandTarget[Actions.update] = [TargetEnum.file]

AllowedCommandArguments = ActionArguments()
""" List of allowed `Args` for each `Action` 

	Command Arguments Matrix (Table 2.3.2): valid Command/Arguments pairs.
	An argument value of 'None' means the argument is valid for any supported target (see Table 2.3.1).
	See Sec. 2.3.1-2.3.5 for the behaviour to be implemented in the actuators.
"""
def fillin_allowed_command_arguments(AllowedCommandArguments, action, targets, args):
	""" Fill in the table for actions with multiple targets """
	for t in targets:
		AllowedCommandArguments[(action, t)]=args
	return AllowedCommandArguments

# TODO: complete the list (if necessary)
args = ['response_requested', 'start_time', 'stop_time', 'duration','persistent','direction','insert_rule','drop_process']
AllowedCommandArguments = fillin_allowed_command_arguments(AllowedCommandArguments, Actions.allow, AllowedCommandTarget[Actions.allow], args)
AllowedCommandArguments = fillin_allowed_command_arguments(AllowedCommandArguments, Actions.deny, AllowedCommandTarget[Actions.deny], args)
AllowedCommandArguments[(Actions.query, TargetEnum.features)] = ['response_requested']
AllowedCommandArguments[(Actions.delete, TargetEnum[Profile.nsid+':rule_number'])] = ['response_requested', 'start_time']
AllowedCommandArguments[(Actions.update, TargetEnum.file)] = ['response_requested', 'start_time']

def validate_command(cmd):
	""" Validate a `Command` 

		Helper function to check the `Target` in a `Command` are valid for the `Action` according
		to the SLPF profile.
		:param cmd: The `Command` class to validate.
	""" 
	try:
		if cmd.action in AllowedActions and \
			TargetEnum[cmd.target.getName()] in AllowedCommandTarget[cmd.action]:
			return True
		else:
			return False
	except:
		return False

def validate_args(cmd):
	""" Validate a `Command` 

		Helper function to check the `Args` in a `Command` are valid for the `Action` and `Target`  according
		to the SLPF profile.
		:param cmd: The `Command` class to validate.
	"""
	try:
		if cmd.args is None: 
			return True
		for k,v in cmd.args.items():
			if k not in AllowedCommandArguments[cmd.action, TargetEnum[cmd.target.getName()]]:
				return False
		return True
	except:
	  return False


