""" CTXD Response extensions

"""
import otupy as oc2

from otupy.profiles.ctxd.profile import Profile
from otupy.types.base.array_of import ArrayOf
from otupy.profiles.ctxd.data.name import Name
from otupy.profiles.ctxd.data.service import Service
from otupy.profiles.ctxd.data.link import Link


@oc2.extension(nsid=Profile.nsid)
class Results(oc2.Results):
	""" CTXD Results

		Extensions to the base class `otupy.core.response.Results`.
		 
		[Developing extensions](https://github.com/mattereppe/otupy/blob/main/docs/developingextensions.md#developing-extensions) Section of the main documentation.

	"""
	fieldtypes = {'services': ArrayOf(Service), 'links': ArrayOf(Link), 'service_names': ArrayOf(Name), 'link_names': ArrayOf(Name)}

