from openc2lib import Args

from openc2lib.profiles.slpf.profile import profile_name
from openc2lib.profiles.slpf.datatypes import DropProcess, Direction, RuleID

class ExtArgs(Args):
	extend = Args
	fieldtypes = Args.fieldtypes.copy()
	fieldtypes['drop_process']=DropProcess
	fieldtypes['persistent']=bool
	fieldtypes['direction']=Direction
	fieldtypes['insert_rule']=RuleID
	nsid = profile_name

