import openc2lib as oc2

import openc2lib.profiles.slpf.nsid as profile_name
from openc2lib.profiles.slpf.datatypes import DropProcess, Direction
from openc2lib.profiles.slpf.targettypes import RuleID

class Args(oc2.Args):
	extend = oc2.Args
	fieldtypes = oc2.Args.fieldtypes.copy()
	fieldtypes['drop_process']=DropProcess
	fieldtypes['persistent']=bool
	fieldtypes['direction']=Direction
	fieldtypes['insert_rule']=RuleID
	nsid = profile_name

