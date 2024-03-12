import json
from enum import Enum

class Action(Enum):
	scan = 1
	locate = 2
	query = 3
#	...

class ActionsMappings:
# Add missing mappings
	__mappings = { Action.scan:Scan, Action.query:Query }
	def action_to_json(classptr):
		for e in ActionsMappings.__mappings:
			if ActionsMappings.__mappings[e] === classptr: return ActionsMappings.__mappings[e].name
		raise Exception()

class ActionImplementation:
    def to_json(self):
        return ActionsMappings.action_to_json(self.__class__)



class Query(ActionImplementation):
	pass


# Rename to ActionImplementation
#class Deny(Action):
#    def __init__(self, action_type, target):
#        super().__init__(action_type)
#        self.target = target
#
#    def validate(self):
#        if not self.target or not isinstance(self.target, str):
#            raise ValueError("The target must be a non-empty string representing an IP address.")
#
#    def __str__(self):
#        return f"DenyAction(Type: {self.action_type}, Target: {self.target})"
#
#    def to_json(self):
#        base_json = json.loads(super().to_json())
#        base_json['target'] = self.target
#        return json.dumps(base_json, indent=4)
#
#
#class Allow(Action):
#    def __init__(self, action_type, target):
#        super().__init__(action_type)
#        self.target = target
#
#    def validate(self):
#        if not self.target or not isinstance(self.target, str):
#            raise ValueError("The target must be a non-empty string representing an IP address.")
#
#    def __str__(self):
#        return f"AllowAction(Type: {self.action_type}, Target: {self.target})"
#
#    def to_json(self):
#        base_json = json.loads(super().to_json())
#        base_json['target'] = self.target
#        return json.dumps(base_json, indent=4)
#
#
#class Update(Action):
#    def __init__(self, action_type, file_path, file_name):
#        super().__init__(action_type)
#        self.file_path = file_path
#        self.file_name = file_name
#
#    def validate(self):
#        pass
#
#    def __str__(self):
#        return f"UpdateAction(Type: {self.action_type}, File: {self.file_path}/{self.file_name})"
#
#    def to_json(self):
#        base_json = json.loads(super().to_json())
#        base_json['file_path'] = self.file_path
#        base_json['file_name'] = self.file_name
#        return json.dumps(base_json, indent=4)
#
#
#class Delete(Action):
#    def __init__(self, action_type, target):
#        super().__init__(action_type)
#        self.target = target
#
#    def validate(self):
#        return True
#
#    def __str__(self):
#        return f"DeleteAction(Type: {self.action_type}, Target: {self.target})"
#
#    def to_json(self):
#        base_json = json.loads(super().to_json())
#        base_json['target'] = self.target
#        return json.dumps(base_json, indent=4)
#
#
#
#"""
#nprobe service action
#
#"""
#
#class start(Action): # nprobe-action
#    pass
#
#class stop(Action): # nprobe-action
#    pass
#
#class restart(Action): # nprobe-action
#    pass
#
#class set(Action): # nprobe-action, change a value, configuration of service.
#    pass
#
#
#"""
#Do not need implement action
#
#"""
#
#class detonate(Action):
#    pass
#
#class restore(Action):
#    pass
#
#class copy(Action):
#    pass
#
#class investigate(Action):
#    pass
#
#class remediate(Action):
#    pass
#
#class cancel(Action):
#    pass
#
#class redirect(Action):
#    pass
#
#class create(Action):
#    pass
#
#class contain(Action):
#    pass
#
#class scan(Action):
#    pass
#
#class locate(Action):
#    pass
#
#


