import aenum 
import openc2lib.basetypes

# New actions can be registered with the following syntax:
# Actions.add('<action_name>', <action_id>)
# <action_name> must be provided as a str
# TODO: Add full list of basic actions listed in Sec. 3.3.1
class Actions(openc2lib.basetypes.Enumerated):
	scan = 1
	locate = 2
	query = 3

	@classmethod
	def add(cls, name, identifier):
		aenum.extend_enum(Actions, name, identifier)

	def __repr__(self):
		return self.name

