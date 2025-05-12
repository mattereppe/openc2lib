""" RCLI validation rules

	This module defines specific RCLI constraints on the usable `Action`s and `Args` defined by the Language Specification.

"""

from openc2lib import Actions, StatusCode, ActionTargets, ActionArguments, TargetEnum, ResponseType

from openc2lib.profiles import rcli
from openc2lib.profiles.rcli.profile import Profile
from openc2lib.profiles.rcli.args import Args

AllowedActions = [ Actions.query, Actions.copy, Actions.start, Actions.stop, Actions.delete]
""" List of allowed `Action`s """

AllowedTargets = [ 'features','artifact', Profile.nsid+':files',Profile.nsid+':processes']
""" List of allowed `Target`s 

	 This is probably not strictly necessary
"""

AllowedStatusCode = [StatusCode.PROCESSING, StatusCode.OK, StatusCode.BADREQUEST, StatusCode.UNAUTHORIZED , StatusCode.FORBIDDEN, StatusCode.NOTFOUND, StatusCode.INTERNALERROR, StatusCode.NOTIMPLEMENTED, StatusCode.SERVICEUNAVAILABLE] 
""" List of allowed status code in `Response` """

AllowedCommandTarget = ActionTargets()
""" List of allowed `Target` for each `Action`

	 Command Matrix: valid Command/Target pairs
"""

AllowedCommandTarget[Actions.query] = [TargetEnum.features, TargetEnum[Profile.nsid+':files'], TargetEnum[Profile.nsid+':processes']]
AllowedCommandTarget[Actions.copy] = [TargetEnum.artifact]
AllowedCommandTarget[Actions.start] = [TargetEnum[Profile.nsid+':processes']]
AllowedCommandTarget[Actions.stop] = [TargetEnum[Profile.nsid+':processes']]
AllowedCommandTarget[Actions.delete] =  [TargetEnum[Profile.nsid+':files']]



AllowedCommandArguments = ActionArguments()
""" List of allowed `Args` for each `Action` 

"""

def fillin_allowed_command_arguments(AllowedCommandArguments, action, targets, args):
	""" Fill in the table for actions with multiple targets """
	for t in targets:
		AllowedCommandArguments[(action, t)]=args
	return AllowedCommandArguments

# TODO: complete the list (if necessary)
args = ['response_requested']
AllowedCommandArguments[(Actions.query, TargetEnum.features)] = ['response_requested']
AllowedCommandArguments[(Actions.query, TargetEnum[Profile.nsid+':processes'])] = ['response_requested']
AllowedCommandArguments[(Actions.query, TargetEnum[Profile.nsid+':files'])] = ['response_requested']
AllowedCommandArguments[(Actions.copy, TargetEnum.artifact)] = ['response_requested', 'storage']
AllowedCommandArguments[(Actions.start, TargetEnum[Profile.nsid+':processes'])] = ['response_requested', 'start_time', 'stop_time',  'duration']
AllowedCommandArguments[(Actions.stop, TargetEnum[Profile.nsid+':processes'])] = ['response_requested', 'stop_time',  'duration']
AllowedCommandArguments[(Actions.delete, TargetEnum[Profile.nsid+':files'])] = ['response_requested',]




def validate_command(cmd):
	""" Validate a `Command` 

		Helper function to check the `Target` in a `Command` are valid for the `Action` according
		to the RCLI profile.
		:param cmd: The `Command` class to validate.
	""" 
	
	try:
		print("--------------------------------------")
		print(cmd)
		print(cmd.action)
		print(AllowedActions)
		print(AllowedCommandTarget[cmd.action])
		print(TargetEnum[cmd.target.getName()] )
		if cmd.action in AllowedActions and \
			TargetEnum[cmd.target.getName()] in AllowedCommandTarget[cmd.action]:
			return True
		else:
			print(AllowedActions)
			print(AllowedCommandTarget(cmd.action))
			return False
	except Exception as e:
		print("------------NOO------------------")
		print(e)
		return False

def validate_args(cmd):
	""" Validate a `Command` 

		Helper function to check the `Args` in a `Command` are valid for the `Action` and `Target`  according
		to the RCLI profile.
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


