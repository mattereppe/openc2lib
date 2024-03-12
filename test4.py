# Estensione dinamica dell'enum.
# Questo esempio usa un unico Enum per la lista delle action (Actions), nel quale viene salvato sia l'id che l'implementazione di riferimento.
# Usando "aenum", e` possibile estendere le azioni in altri file
from aenum import Enum, extend_enum


class Action:
	def run(self):
		print("Action")

	def to_json(self):
		for e in Actions:
			if e.value['impl'] == self.__class__:
				return e.name
		return ""
	
	def from_json(name):
		return Actions[name].value["impl"]()	

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
	scan = {"id": 1, "impl": Scan}
	locate = {"id": 2, "impl": Locate}
	query = {"id": 3, "impl": Query}


class_name = "scan"
s = Action.from_json(class_name)
s.run()

# In un altro ipotetico file:
# from openc2_actions import *
#
#class Allow(Action):
#	def run(self):
#		print("Allow")
#
#extend_enum(Actions, 'allow', {"id": 8, "impl": Allow})
