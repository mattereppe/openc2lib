from aenum import Enum, extend_enum
from abc import ABC,abstractmethod 

class Actions(Enum):
	pass

def register_action(cls):
	extend_enum(Actions, cls.getName(), cls)
	return cls

#class Action(ABC):
class Action:
	id: int = 0
	action: str = 'action'

	def __init__(self):
		self.action = self.__class__.action

	@abstractmethod
	def run(self):
		print("Action")

	# This is not really necessary
	@classmethod
	def getId(self):
		return self.id
	
	# This is not really necessary
	@classmethod
	def getName(self):
		return self.action

	def __str__(self):
		return Actions(self.__class__).action

	def __new__(cls, name=None):
		if( name is None ):
			return super().__new__(cls)
		else:
			return Actions[name].value()	

@register_action
class Scan(Action):
	id = 1
	action = 'scan'

	def run(self):
		print("Scan")

@register_action
class Locate(Action):
	id = 2
	action = "locate"
	def run(self):
		print("Locate")

@register_action
class Query(Action):
	id = 3
	action = "query"

	def run(self):
		print("Query")


