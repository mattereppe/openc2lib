#__all__ = [ "actuator" , "targettypes" ]
#from . import *

from openc2lib import Profile, Profiles
from openc2lib.profiles.slpf.profile import *

nsid = profile_name
Profiles.add(nsid, slpf, 1024)

from openc2lib import Targets
from openc2lib import TargetEnum
from openc2lib.profiles.slpf.datatypes import RuleID, Direction

Targets.add('rule_number', RuleID, 1024, nsid)

# According to the standard, extended targets must be prefixed with the nsid
from openc2lib import ExtendedArguments
from openc2lib.profiles.slpf.args import Args

ExtendedArguments.add(nsid, Args)

from openc2lib import ExtendedResults
from openc2lib.profiles.slpf.response import Results

ExtendedResults.add(nsid, Results)

from openc2lib.profiles.slpf.validation import AllowedCommandTarget
