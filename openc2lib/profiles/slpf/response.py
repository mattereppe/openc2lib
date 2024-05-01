import openc2lib.response 
from openc2lib.profiles.slpf.profile import profile_name
from openc2lib.profiles.slpf.datatypes import RuleID

class Results(openc2lib.response.Results):
	extend = openc2lib.response.Results
	fieldtypes = openc2lib.response.Results.fieldtypes.copy()
	fieldtypes['rule_number']=RuleID
	nsid = profile_name

