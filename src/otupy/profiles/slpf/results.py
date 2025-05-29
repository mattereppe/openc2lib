""" SLPF Response extensions

	This module defines SLPF-specific extensions to OpenC2 Response.
	See Sec. 2.2 of the SLPF Specification.
"""
import otupy as oc2

from otupy.profiles.slpf.profile import Profile
from otupy.profiles.slpf.targets import RuleID

@oc2.extension(nsid=Profile.nsid)
class Results(oc2.Results):
	""" SLPF Results

		Extensions to the base class `otupy.core.response.Results`.
		See Sec. 2.2.2 of the SLPF Specification.
		The extension mechanism is described in the 
		[Developing extensions](https://github.com/mattereppe/otupy/blob/main/docs/developingextensions.md#developing-extensions) Section of the main documentation.

		Note that the same name is used as the base class, to make it simpler to 
		remember. The recommended way to use in the code is to import the whole
		slpf module as `slpf` and refer to this class as `slpf.Results`.
	"""
	fieldtypes = {'rule_number': RuleID}
	""" Extension with SLPF specific arguments (Sec. 2.2.2 of the SLPF Specification) """

