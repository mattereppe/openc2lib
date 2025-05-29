""" Context Discovery profile

	This module collects all public definition that are exported as part of the CTXD profile.
	All naming follows as much as possible the terminology in the CTXD Specification, by
	also applying generic otupy conventions.

	This definition also registers all extensions defined in the SLPF profile (`Args`, `Target`, `Profile`, `Results`).

"""

from otupy.profiles.ctxd.profile import Profile
from otupy.profiles.ctxd.actuator import *

from otupy import TargetEnum
from otupy.profiles.ctxd.data import *
from otupy.profiles.ctxd.targets import Context


# According to the standard, extended targets must be prefixed with the nsid
from otupy.profiles.ctxd.args import Args
from otupy.profiles.ctxd.results import Results
from otupy.profiles.ctxd.validation import AllowedCommandTarget, AllowedCommandArguments, validate_command, validate_args
