""" StateLess Packet Filter profile

	This module collects all public definition that are exported as part of the SLPF profile.
	All naming follows as much as possible the terminology in the SLPF Specification, by
	also applying generic openc2lib conventions.

	This definition also registers all extensions defined in the SLPF profile (`Args`, `Target`, `Profile`, `Results`).

	The SLPF profile extends the language specification with the following elements:
	- `openc2lib.core.profile.Profile`:
		- `openc2lib.profiles.slpf.profile.slpf` profile is defined for all Actuators that will implement it;
		- `openc2lib.profiles.slpf.nsid.nsid` is defined as Namespace identifier for the SLPF profile;
	- `openc2lib.types.datatypes`:
		- `openc2lib.profiles.slpf.datatypes.Direction` is used to specify the rule applies to incoming, outgoing, or both kinds of packets;
	- `openc2lib.types.targettypes`:
		- `openc2lib.profiles.slpf.targettypes.RuleID` identifies a rule identifier to distinguish firewalling rules;
	- `openc2lib.core.target.Targets`:
		- `openc2lib.profiles.slpf.targettypes.RuleID` is the identifier of an SLPF rule;
	- `openc2lib.core.args.Args`:
		- `openc2lib.profiles.slpf.args.Args` is extended with `drop_process`, `persistent`, `direction`, and `insert_rule` arguments;
	- `openc2lib.core.response.Results`:
		- `openc2lib.profiles.slpf.response.Results` is extended with the `rule_id` field;
	- validation:
		- `openc2lib.profiles.slpf.validation.AllowedCommandTarget` contains all valid `openc2lib.core.target.Target` for each `openc2lib.core.actions.Actions`;
		- `openc2lib.profiles.slpf.validation.AllowedCommandArguments` contains all valid `openc2lib.core.args.Args` for each `openc2lib.core.actions.Actions`/`openc2lib.core.target.Target` pair;
	- helper functions:
		- `openc2lib.profiles.slpf.validation.validate_command` checks a `openc2lib.core.target.Target`-openc2lib.core.actions.Actions` pair in a `openc2lib.core.message.Command` is present in `openc2lib.profiles.slpf.validation.AllowedCommandTarget`;
	   - `openc2lib.profiles.slpf.validation.validate_args` checks a `openc2lib.core.args.Args`-`openc2lib.core.actions.Actions`-`openc2lib.core.target.Target` triple in a `openc2lib.core.message.Command` is present in `openc2lib.profiles.slpf.validation.AllowedCommandArguments`.	
"""


from openc2lib import Profile, Profiles

from openc2lib.profiles.slpf.nsid import nsid
from openc2lib.profiles.slpf.profile import *

Profiles.add(nsid, slpf, 1024)

from openc2lib import Targets
from openc2lib import TargetEnum
from openc2lib.profiles.slpf.datatypes import Direction
from openc2lib.profiles.slpf.targettypes import RuleID

Targets.add('rule_number', RuleID, 1024, nsid)

# According to the standard, extended targets must be prefixed with the nsid
from openc2lib import ExtendedArguments
from openc2lib.profiles.slpf.args import Args

ExtendedArguments.add(nsid, Args)

from openc2lib import ExtendedResults
from openc2lib.profiles.slpf.response import Results

ExtendedResults.add(nsid, Results)

from openc2lib.profiles.slpf.validation import AllowedCommandTarget, AllowedCommandArguments, validate_command, validate_args
