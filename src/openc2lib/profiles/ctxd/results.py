""" CTXD Response extensions

"""
import openc2lib as oc2

from openc2lib.profiles.ctxd.profile import Profile
from openc2lib.types.base.array_of import ArrayOf
from openc2lib.profiles.ctxd.data.name import Name
from openc2lib.profiles.ctxd.data.service import Service
from openc2lib.profiles.ctxd.data.link import Link


@oc2.extension(nsid=Profile.nsid)
class Results(oc2.Results):
	""" CTXD Results

		Extensions to the base class `openc2lib.core.response.Results`.
		 
		[Developing extensions](https://github.com/mattereppe/openc2lib/blob/main/docs/developingextensions.md#developing-extensions) Section of the main documentation.

	"""
	fieldtypes = {'services': ArrayOf(Service), 'links': ArrayOf(Link), 'service_names': ArrayOf(Name), 'link_names': ArrayOf(Name)}

