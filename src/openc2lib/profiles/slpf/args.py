""" SLPF Arguments
	
	This module extends the Args defined by the Language Specification
	(see Sec. 2.1.3.2 of the SLPF Specification).
"""
import openc2lib as oc2

import openc2lib.profiles.slpf.nsid as profile_name
from openc2lib.profiles.slpf.datatypes import DropProcess, Direction
from openc2lib.profiles.slpf.targettypes import RuleID

class Args(oc2.Args):
	""" SLPF Args

		This class extends the Args defined in the Language Specification.
		The extension mechanism is described in the 
		[Developing extensions](https://github.com/mattereppe/openc2lib/blob/main/docs/developingextensions.md#developing-extensions) Section of the main documentation.

		Note that the same name is used as the base class, to make it simpler to 
		remember. The recommended way to use in the code is to import the whole
		slpf module as `slpf` and refer to this class as `slpf.Args`.

	"""
	extend = oc2.Args
	""" The class to extend (`openc2lib.core.args.Args` defined in the core section). """
	fieldtypes = oc2.Args.fieldtypes.copy()
	""" Copy all `fieldtypes` defined in the base class. """
	fieldtypes['drop_process']=DropProcess
	""" Extension with SLPF specific arguments (Sec. 2.1.3.2 of the SLPF Specification) """
	fieldtypes['persistent']=bool
	""" Extension with SLPF specific arguments (Sec. 2.1.3.2 of the SLPF Specification) """
	fieldtypes['direction']=Direction
	""" Extension with SLPF specific arguments (Sec. 2.1.3.2 of the SLPF Specification) """
	fieldtypes['insert_rule']=RuleID
	""" Extension with SLPF specific arguments (Sec. 2.1.3.2 of the SLPF Specification) """
	nsid = profile_name
	""" Namespace identifier to distinguish extensions """

