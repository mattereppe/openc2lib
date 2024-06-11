""" SLPF Response extensions

	This module defines SLPF-specific extensions to OpenC2 Response.
	See Sec. 2.2 of the SLPF Specification.
"""
import openc2lib as oc2

import openc2lib.profiles.slpf.nsid as profile_name
from openc2lib.profiles.slpf.targets import RuleID

class Results(oc2.Results):
	""" SLPF Results

		Extensions to the base class `openc2lib.core.response.Results`.
		See Sec. 2.2.2 of the SLPF Specification.
		The extension mechanism is described in the 
		[Developing extensions](https://github.com/mattereppe/openc2lib/blob/main/docs/developingextensions.md#developing-extensions) Section of the main documentation.

		Note that the same name is used as the base class, to make it simpler to 
		remember. The recommended way to use in the code is to import the whole
		slpf module as `slpf` and refer to this class as `slpf.Results`.
	"""
	extend = oc2.Results
	""" The class to extend (`openc2lib.core.response.Results` defined in the core section). """
	fieldtypes = oc2.Results.fieldtypes.copy()
	""" Copy all `fieldtypes` defined in the base class. """
	fieldtypes['rule_number']=RuleID
	""" Extension with SLPF specific arguments (Sec. 2.2.2 of the SLPF Specification) """
	nsid = profile_name
	""" Namespace identifier to distinguish extensions """

