# Validation rules according to SLPF specification

from openc2lib.actions import Actions

AllowedActions = [ Actions.query, Actions.deny, Actions.allow, Actions.deny, Actions.update, Actions.delete]

# This is probably not strictly necessary
AllowedTargets = [ 'feature', 'file', 'ipv4_net', 'ipv6_net', 'ipv4_connection', 'ipv6_connection' , 'rule_number']

#AllowedArguments = [ 'start_time', 'stop_time', 'duration', 'response_requested', 


