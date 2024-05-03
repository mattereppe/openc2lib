import aenum 
from openc2lib.types.basetypes import Enumerated

# New actions can be registered with the following syntax:
# Actions.add('<action_name>', <action_id>)
# <action_name> must be provided as a str
# TODO: Add full list of basic actions listed in Sec. 3.3.1
class Actions(Enumerated):
	scan = 1
	locate = 2
	query = 3
	deny = 6
	allow = 8
	update = 16
	delete = 20

	@classmethod
	def add(cls, name, identifier):
		aenum.extend_enum(Actions, name, identifier)

	def __repr__(self):
		return self.name

