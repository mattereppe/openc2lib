""" SLPF additional data types

	This modules defines additional data types specific for the SLPF profile.
"""

from openc2lib import Targets

from openc2lib.profiles.slpf.nsid import nsid
from openc2lib.profiles.slpf.targets.rule_id import RuleID

Targets.add('rule_number', RuleID, 1024, nsid)
