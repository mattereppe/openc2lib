#__all__ = [ "actuator" , "targettypes" ]
#from . import *
from openc2lib.targets import Targets
from openc2lib.profile import Profiles
from openc2lib.args import ExtendedArguments
from openc2lib.profiles.slpf.profile import *
from openc2lib.profiles.slpf.datatypes import RuleID
from openc2lib.profiles.slpf.args import ExtArgs

nsid = 'slpf'

Profiles.add(nsid, slpf, 1024)
# According to the standard, extended targets must be prefixed with the nsid
Targets.add('rule_number', RuleID, 1024, nsid)
ExtendedArguments.add(nsid, ExtArgs)
