import openc2lib.args
from openc2lib.profile import Profile
from openc2lib.profiles.slpf.profile import profile_name
from openc2lib.profiles.slpf.datatypes import DropProcess, Direction, RuleID

class ExtArgs(openc2lib.args.Args):
	extend = openc2lib.args.Args
	fieldtypes = openc2lib.args.Args.fieldtypes.copy()
	fieldtypes['drop_process']=DropProcess
	fieldtypes['persistent']=bool
	fieldtypes['direction']=Direction
	fieldtypes['insert_rule']=RuleID
	nsid = profile_name

