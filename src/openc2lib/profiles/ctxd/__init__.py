""" Context Discovery profile

	This module collects all public definition that are exported as part of the CTXD profile.
	All naming follows as much as possible the terminology in the CTXD Specification, by
	also applying generic openc2lib conventions.

	This definition also registers all extensions defined in the SLPF profile (`Args`, `Target`, `Profile`, `Results`).

"""

from openc2lib.profiles.ctxd.profile import Profile
from openc2lib.profiles.ctxd.actuator import *

from openc2lib import TargetEnum
from openc2lib.profiles.ctxd.data import *
from openc2lib.profiles.ctxd.targets import Context


# According to the standard, extended targets must be prefixed with the nsid
from openc2lib.profiles.ctxd.args import Args
from openc2lib.profiles.ctxd.results import Results
from openc2lib.profiles.ctxd.validation import AllowedCommandTarget, AllowedCommandArguments, validate_command, validate_args
