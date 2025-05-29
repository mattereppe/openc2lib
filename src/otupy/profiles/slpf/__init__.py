""" StateLess Packet Filter profile

	This module collects all public definition that are exported as part of the SLPF profile.
	All naming follows as much as possible the terminology in the SLPF Specification, by
	also applying generic otupy conventions.

	This definition also registers all extensions defined in the SLPF profile (`Args`, `Target`, `Profile`, `Results`).

	The SLPF profile extends the language specification with the following elements:
	- `otupy.core.profile.Profile`:
		- `otupy.profiles.slpf.profile.slpf` profile is defined for all Actuators that will implement it;
		- `otupy.profiles.slpf.nsid.nsid` is defined as Namespace identifier for the SLPF profile;
	- `otupy.types.data`:
		- `otupy.profiles.slpf.data.Direction` is used to specify the rule applies to incoming, outgoing, or both kinds of packets;
	- `otupy.types.targets`:
		- `otupy.profiles.slpf.targets.RuleID` identifies a rule identifier to distinguish firewalling rules;
	- `otupy.core.target.Targets`:
		- `otupy.profiles.slpf.targets.RuleID` is the identifier of an SLPF rule;
	- `otupy.core.args.Args`:
		- `otupy.profiles.slpf.args.Args` is extended with `drop_process`, `persistent`, `direction`, and `insert_rule` arguments;
	- `otupy.core.response.Results`:
		- `otupy.profiles.slpf.response.Results` is extended with the `rule_id` field;
	- validation:
		- `otupy.profiles.slpf.validation.AllowedCommandTarget` contains all valid `otupy.core.target.Target` for each `otupy.core.actions.Actions`;
		- `otupy.profiles.slpf.validation.AllowedCommandArguments` contains all valid `otupy.core.args.Args` for each `otupy.core.actions.Actions`/`otupy.core.target.Target` pair;
	- helper functions:
		- `otupy.profiles.slpf.validation.validate_command` checks a `otupy.core.target.Target`-otupy.core.actions.Actions` pair in a `otupy.core.message.Command` is present in `otupy.profiles.slpf.validation.AllowedCommandTarget`;
	   - `otupy.profiles.slpf.validation.validate_args` checks a `otupy.core.args.Args`-`otupy.core.actions.Actions`-`otupy.core.target.Target` triple in a `otupy.core.message.Command` is present in `otupy.profiles.slpf.validation.AllowedCommandArguments`.	
"""


from otupy.profiles.slpf.profile import Profile, nsid
from otupy.profiles.slpf.actuator import *

from otupy import TargetEnum
from otupy.profiles.slpf.data import Direction
from otupy.profiles.slpf.targets import RuleID


# According to the standard, extended targets must be prefixed with the nsid
from otupy.profiles.slpf.args import Args
from otupy.profiles.slpf.results import Results
from otupy.profiles.slpf.validation import AllowedCommandTarget, AllowedCommandArguments, validate_command, validate_args
