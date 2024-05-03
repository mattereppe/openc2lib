import openc2lib as oc2

from openc2lib.profiles.slpf.profile import profile_name
from openc2lib.profiles.slpf.datatypes import DropProcess, Direction, RuleID

class Args(oc2.Args):
	extend = oc2.Args
	fieldtypes = oc2.Args.fieldtypes.copy()
	fieldtypes['drop_process']=DropProcess
	fieldtypes['persistent']=bool
	fieldtypes['direction']=Direction
	fieldtypes['insert_rule']=RuleID
	nsid = profile_name

