""" NFM Response extensions

"""
import openc2lib as oc2

from openc2lib.profiles.nfm.profile import Profile
from openc2lib.profiles.nfm.data.ie import IE
from openc2lib.profiles.nfm.data.interface import Interface
from openc2lib.profiles.nfm.targets.monitor_id import MonitorID

from openc2lib.types.base.array_of import ArrayOf


@oc2.extension(nsid=Profile.nsid)
class Results(oc2.Results):
	""" NFM Results

		Extensions to the base class `openc2lib.core.response.Results`.
		 
		[Developing extensions](https://github.com/mattereppe/openc2lib/blob/main/docs/developingextensions.md#developing-extensions) Section of the main documentation.

	"""

	fieldtypes = {'interfaces' : ArrayOf(Interface),'information_elements': ArrayOf(IE), 'monitor_id': MonitorID, 'exports':ArrayOf(str), 'export_options':ArrayOf(str), 'flow_format':ArrayOf(str), 'filters':ArrayOf(str)}


