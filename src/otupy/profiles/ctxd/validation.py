""" CTXD validation rules

	This module defines specific CTXD constraints on the usable `Action`s and `Args` defined by the Language Specification.

"""

from otupy import Actions, StatusCode, ActionTargets, ActionArguments, TargetEnum, ResponseType

from otupy.profiles import ctxd
from otupy.profiles.ctxd.profile import Profile
from otupy.profiles.ctxd.targets import Context
from otupy.profiles.ctxd.args import Args

AllowedActions = [ Actions.query]
""" List of allowed `Action`s """

AllowedTargets = [ 'features', Profile.nsid+':context']
""" List of allowed `Target`s 

	 This is probably not strictly necessary
"""

AllowedStatusCode = [StatusCode.PROCESSING, StatusCode.OK, StatusCode.BADREQUEST, StatusCode.UNAUTHORIZED , StatusCode.FORBIDDEN, StatusCode.NOTFOUND, StatusCode.INTERNALERROR, StatusCode.NOTIMPLEMENTED, StatusCode.SERVICEUNAVAILABLE] 
""" List of allowed status code in `Response` """

AllowedCommandTarget = ActionTargets()
""" List of allowed `Target` for each `Action`

	 Command Matrix: valid Command/Target pairs
"""

AllowedCommandTarget[Actions.query] = [TargetEnum.features, TargetEnum[Profile.nsid+':context']]


AllowedCommandArguments = ActionArguments()
""" List of allowed `Args` for each `Action` 

"""

def fillin_allowed_command_arguments(AllowedCommandArguments, action, targets, args):
	""" Fill in the table for actions with multiple targets """
	for t in targets:
		AllowedCommandArguments[(action, t)]=args
	return AllowedCommandArguments

# TODO: complete the list (if necessary)
args = ['response_requested', 'name_only']
AllowedCommandArguments[(Actions.query, TargetEnum.features)] = ['response_requested']
AllowedCommandArguments[(Actions.query, TargetEnum[Profile.nsid+':context'])] = ['name_only']

def validate_command(cmd):
	""" Validate a `Command` 

		Helper function to check the `Target` in a `Command` are valid for the `Action` according
		to the CTXD profile.
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
		to the CTXD profile.
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


