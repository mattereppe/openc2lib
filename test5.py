# In questa versione, assumo ancora che sia ragionevole avere una unica lista di mapping tra nomi e 
# classi delle azioni. L'id lo si puo` recuperare indirettamente dalla classe (vedi esempio in fondo)
# La differenza rispetto all'esempio precedente consiste nell'utilizzare un decoratore per registrare
# in automatico ogni nuova classe che aggiungo (eliminando in questo modo errori dovuti alla
# estension "manuale".
from aenum import Enum, extend_enum

class Actions(Enum):
	pass

def register(cls):
	extend_enum(Actions, cls.name, cls)
	return cls

class Action:
	id = 0
	name = 'action'

	def run(self):
		print("Action")

	def to_json(self):
		return Actions(self.__class__).name

#@staticmethod
	def from_json(name):
		return Actions[name].value()	

@register
class Scan(Action):
	id = 1
	name = 'scan'

	def run(self):
		print("Scan")

@register
class Locate(Action):
	id = 2
	name = "locate"
	def run(self):
		print("Locate")

@register
class Query(Action):
	id = 3
	name = "query"

	def run(self):
		print("Query")


class_name = "scan"
s = Action.from_json(class_name)
s1 = Scan()
s2 = Scan()
l = Locate()
q = Query()
s.run()
print(s.id)
# Accedere all'id di una classe
print("Query id: ", Actions(Actions.query).value().id)
