""" FCLM Response extensions

"""
import openc2lib as oc2

from openc2lib.profiles.fclm.profile import Profile
from openc2lib.profiles.fclm.data.ef import EF
from openc2lib.profiles.fclm.targets.monitor_id import MonitorID

from openc2lib.types.base.array_of import ArrayOf


@oc2.extension(nsid=Profile.nsid)
class Results(oc2.Results):
	""" FCLM Results

		Extensions to the base class `openc2lib.core.response.Results`.
		 
		[Developing extensions](https://github.com/mattereppe/openc2lib/blob/main/docs/developingextensions.md#developing-extensions) Section of the main documentation.

	"""

	fieldtypes = {'export_fields': ArrayOf(EF), 'monitor_id': MonitorID, 'exports_config':ArrayOf(str), 'imports_config':ArrayOf(str), 'import_controls':ArrayOf(str)}


