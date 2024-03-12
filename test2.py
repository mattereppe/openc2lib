from enum import Enum

class Actions(Enum):
	scan = 1
	locate = 2
	query = 3

class Action:
	def run(self):
		print("Action")

	def to_json(self):
		return ActionsMappings.action_to_json(self.__class__)

class Scan(Action):
	def run(self):
		print("Scan")

class Locate(Action):
	def run(self):
		print("Locate")

class Query(Action):
	def run(self):
		print("Query")



class ActionsMappings:
	__mappings = { Actions.scan: Scan, Actions.locate: Locate, Actions.query: Query }
	
	def action_to_json(classptr):
		for e in ActionsMappings.__mappings:
			if ActionsMappings.__mappings[e] == classptr: return e.name
		raise Exception()


	def classname_to_action(class_name):
		for e in ActionsMappings.__mappings:
			if e.name == class_name: return ActionsMappings.__mappings[e]
	

class_name = "scan"
s = eval(class_name.capitalize())
# <class 'test2.Scan'>

