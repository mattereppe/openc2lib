""" NFM validation rules

	This module defines specific NFM constraints on the usable `Action`s and `Args` defined by the Language Specification.

"""

from openc2lib import Actions, StatusCode, ActionTargets, ActionArguments, TargetEnum, ResponseType

from openc2lib.profiles.nfm.profile import Profile
from openc2lib.profiles.nfm.args import Args

AllowedActions = [ Actions.query, Actions.start, Actions.stop]
""" List of allowed `Action`s """

AllowedTargets = ['features', Profile.nsid+':monitor', Profile.nsid+':monitor_id']
""" List of allowed `Target`s 

	 This is probably not strictly necessary
"""

AllowedStatusCode = [StatusCode.PROCESSING, StatusCode.OK, StatusCode.BADREQUEST, StatusCode.UNAUTHORIZED , StatusCode.FORBIDDEN, StatusCode.NOTFOUND, StatusCode.INTERNALERROR, StatusCode.NOTIMPLEMENTED, StatusCode.SERVICEUNAVAILABLE] 
""" List of allowed status code in `Response` """

AllowedCommandTarget = ActionTargets()
""" List of allowed `Target` for each `Action`

	 Command Matrix: valid Command/Target pairs
"""

AllowedCommandTarget[Actions.query] = [TargetEnum.features]
AllowedCommandTarget[Actions.start] = [TargetEnum[Profile.nsid+':monitor']]
AllowedCommandTarget[Actions.stop] = [TargetEnum[Profile.nsid+':monitor_id']]



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
AllowedCommandArguments[(Actions.start, TargetEnum[Profile.nsid+':monitor'])] = ['response_requested', 'start_time', 'stop_time',  'duration', 'exporter', 'exporter_options']
AllowedCommandArguments[(Actions.stop, TargetEnum[Profile.nsid+':monitor_id'])] = ['response_requested', 'stop_time',  'duration']




def validate_command(cmd):
	""" Validate a `Command` 

		Helper function to check the `Target` in a `Command` are valid for the `Action` according
		to the nfm profile.
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
		to the nfm profile.
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


