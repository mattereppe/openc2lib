""" FCLM Arguments
	
	This module extends the Args defined by the Language Specification
	(see Sec. 'Command Arguments Unique to FCLM').
"""
import openc2lib as oc2

from openc2lib.profiles.fclm.profile import Profile
from openc2lib import TargetEnum
from openc2lib.profiles.fclm.data.exporter import Exporter
from openc2lib.profiles.fclm.data.import_options import ImportOptions
from openc2lib.profiles.fclm.data.ef import EF



@oc2.extension(nsid=Profile.nsid)
class Args(oc2.Args):
	""" FCLM Args

		This class extends the Args defined in the Language Specification.
		The extension mechanism is described in the 
		[Developing extensions](https://github.com/mattereppe/openc2lib/blob/main/docs/developingextensions.md#developing-extensions) Section of the main documentation.


	"""
	fieldtypes = {'log_exporter': Exporter,'export_fields':oc2.ArrayOf(EF), 'import_controls': ImportOptions}
