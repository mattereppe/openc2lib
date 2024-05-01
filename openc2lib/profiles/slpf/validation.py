# Validation rules according to SLPF specification

from openc2lib import Actions, StatusCode, ActionTargets, ActionArguments, TargetEnum

from openc2lib.profiles.slpf.profile import profile_name

AllowedActions = [ Actions.query, Actions.deny, Actions.allow, Actions.deny, Actions.update, Actions.delete]

# This is probably not strictly necessary
AllowedTargets = [ 'feature', 'file', 'ipv4_net', 'ipv6_net', 'ipv4_connection', 'ipv6_connection' , profile_name+':rule_number']

AllowedStatusCode = [StatusCode.PROCESSING, StatusCode.OK, StatusCode.BADREQUEST, StatusCode.INTERNALERROR, StatusCode.NOTIMPLEMENTED ] 

# Command Matrix (Table 2.3.1): valid Command/Target pairs
# TODO: complete (replace with commented lines) after defining all targets
AllowedCommandTarget = ActionTargets()
AllowedCommandTarget[Actions.allow] = [TargetEnum.ipv4_connection, TargetEnum.ipv4_net]
#AllowedCommandTarget[Actions.allow] = [TargetEnum.ipv4_connection, TargetEnum.ipv6_connection,
#	TargetEnum.ipv4_net, TargetEnum.ipv6_net]
AllowedCommandTarget[Actions.deny] = [TargetEnum.ipv4_connection, TargetEnum.ipv4_net]
#AllowedCommandTarget[Actions.deny] = [TargetEnum.ipv4_connection, TargetEnum.ipv6_connection,
#	TargetEnum.ipv4_net, TargetEnum.ipv6_net]
AllowedCommandTarget[Actions.query] = [TargetEnum.features]
AllowedCommandTarget[Actions.delete] = [TargetEnum[profile_name+':rule_number']]
#AllowedCommandTarget[Actions.update] = [TargetEnum.file]

# Command Arguments Matrix (Table 2.3.2): valid Command/Arguments pairs.
# An argument value of 'None' means the argument is valid for any supported target (see Table 2.3.1).
# See Sec. 2.3.1-2.3.5 for the behaviour to be implemented in the actuators.
AllowedCommandArguments = ActionArguments()
AllowedCommandArguments[(Actions.allow, None)] = ['response_requested', 'start_time', 'stop_time',
	'duration','persistent','direction','insert_rule']
AllowedCommandArguments[(Actions.deny, None)] = ['response_requested', 'start_time', 'stop_time',
	'duration','persistent','direction','insert_rule','drop_process']
AllowedCommandArguments[(Actions.query, TargetEnum.features)] = ['response_requested']
AllowedCommandArguments[(Actions.delete, TargetEnum[profile_name+':rule_number'])] = ['response_requested', 'start_time']
#AllowedCommandArguments[(Actions.update, TargetEnum.file)] = ['response_requested', 'start_time']



