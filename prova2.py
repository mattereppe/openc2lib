class Action:
	_id = 0
	def __init__(self):
		self.attr = "action"
	def name(self):
		return self.attr
	def id(self):
		return self._id

class Scan(Action):
	_id = 1
	def __init__(self):
		self.attr = "scan"
