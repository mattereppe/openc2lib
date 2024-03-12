from enum import Enum

class Actions(Enum):
	scan = 1
	locate = 2
	query = 3

class Action:
	def run(self): pass
	def to_json(self):
		return ActionsMappings.action_to_json(self.__class__)

class Scan(Action):
	def run(self):
		print("Scan action")

class Locate(Action):
	def run(self):
		print("Locate action")

class Query(Action):
	def run(self):
		print("Query action")

class ActionsMappings:
	__mappings = { Actions.scan: Scan, Actions.locate: Locate, Actions.query: Query }
	
	def action_to_json(classptr):
		for e in ActionsMappings.__mappings:
			if ActionsMappings.__mappings[e] == classptr: return e.name
		raise Exception()
	
	def classname_to_action(class_name):
		for e in ActionsMappings.__mappings:
			if e.name == class_name: return ActionsMappings.__mappings[e]
		raise Exception()

class_name = "scan"
class_ptr = ActionsMappings.classname_to_action(class_name)
print('cn: '+class_name)
if not class_ptr is None:
	class_obj = class_ptr()
	class_obj.run()

#s = eval(class_name.capitalize())
