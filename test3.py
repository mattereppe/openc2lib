from enum import Enum


class Action:
	def run(self):
		print("Action")

	def to_json(self):
		return Actions(self.__class__).name
	
	def from_json(name):
		return Actions[name].value()	

class Scan(Action):
	def run(self):
		print("Scan")

class Locate(Action):
	def run(self):
		print("Locate")

class Query(Action):
	def run(self):
		print("Query")

class Actions(Enum):
	scan = Scan
	locate = Locate
	query = Query


class_name = "scan"
s = Action.from_json(class_name)
s.run()
