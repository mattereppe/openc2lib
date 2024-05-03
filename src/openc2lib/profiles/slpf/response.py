import openc2lib as oc2

from openc2lib.profiles.slpf.profile import profile_name
from openc2lib.profiles.slpf.datatypes import RuleID

class Results(oc2.Results):
	extend = oc2.Results
	fieldtypes = oc2.Results.fieldtypes.copy()
	fieldtypes['rule_number']=RuleID
	nsid = profile_name

