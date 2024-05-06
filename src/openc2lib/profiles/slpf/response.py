import openc2lib as oc2

import openc2lib.profiles.slpf.nsid as profile_name
from openc2lib.profiles.slpf.targettypes import RuleID

class Results(oc2.Results):
	extend = oc2.Results
	fieldtypes = oc2.Results.fieldtypes.copy()
	fieldtypes['rule_number']=RuleID
	nsid = profile_name

