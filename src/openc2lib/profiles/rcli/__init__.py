""" Remote CLI profile

	This module collects all public definition that are exported as part of the RCLI profile.
	All naming follows as much as possible the terminology in the RCLI Specification, by
	also applying generic openc2lib conventions.

	This definition also registers all extensions defined in the RCLI profile (`Args`, `Target`, `Profile`, `Results`).

"""

from openc2lib.profiles.rcli.profile import Profile
from openc2lib.profiles.rcli.actuator import *

from openc2lib import TargetEnum
from openc2lib.profiles.rcli.data import *
from openc2lib.profiles.rcli.targets import Processes
from openc2lib.profiles.rcli.targets import Files



# According to the standard, extended targets must be prefixed with the nsid
from openc2lib.profiles.rcli.args import Args
from openc2lib.profiles.rcli.results import Results
from openc2lib.profiles.rcli.validation import AllowedCommandTarget, AllowedCommandArguments, validate_command, validate_args
