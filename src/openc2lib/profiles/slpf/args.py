""" SLPF Arguments
	
	This module extends the Args defined by the Language Specification
	(see Sec. 2.1.3.2 of the SLPF Specification).
"""
import openc2lib as oc2

from openc2lib.profiles.slpf.profile import Profile
from openc2lib.profiles.slpf.data import DropProcess, Direction
from openc2lib.profiles.slpf.targets import RuleID

@oc2.extension(nsid=Profile.nsid)
class Args(oc2.Args):
	""" SLPF Args

		This class extends the Args defined in the Language Specification.
		The extension mechanism is described in the 
		[Developing extensions](https://github.com/mattereppe/openc2lib/blob/main/docs/developingextensions.md#developing-extensions) Section of the main documentation.

		Note that the same name is used as the base class, to make it simpler to 
		remember. The recommended way to use in the code is to import the whole
		slpf module as `slpf` and refer to this class as `slpf.Args`.

	"""
	fieldtypes = {'drop_process': DropProcess, 'persistent': bool, 'direction': Direction, 'insert_rule': RuleID}
	""" Extension with SLPF specific arguments (Sec. 2.1.3.2 of the SLPF Specification) """

