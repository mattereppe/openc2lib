#__all__ = [ "actuator" , "targettypes" ]
#from . import *

from openc2lib.profile import Profiles
from openc2lib.profiles.slpf.profile import *

nsid = profile_name
Profiles.add(nsid, slpf, 1024)

from openc2lib.targets import Targets
from openc2lib.profiles.slpf.datatypes import RuleID, Direction
from openc2lib.datatypes import TargetEnum

Targets.add('rule_number', RuleID, 1024, nsid)
print(Targets)
print([e.name for e in TargetEnum])

# According to the standard, extended targets must be prefixed with the nsid
from openc2lib.args import ExtendedArguments
from openc2lib.profiles.slpf.args import ExtArgs

ExtendedArguments.add(nsid, ExtArgs)

from openc2lib.response import ExtendedResults
from openc2lib.profiles.slpf.response import Results

ExtendedResults.add(nsid, Results)

from openc2lib.profiles.slpf.validation import AllowedCommandTarget
