""" RCLI Response extensions

"""
import openc2lib as oc2

from openc2lib.profiles.rcli.profile import Profile
from openc2lib.profiles.rcli.targets import Processes , Files
from openc2lib.types.targets.file import File
#from openc2lib.profiles.rcli.data.extended_process import Process
from openc2lib.profiles.rcli.data.process import Process

from openc2lib.types.base.array_of import ArrayOf


@oc2.extension(nsid=Profile.nsid)
class Results(oc2.Results):
	""" RCLI Results

		Extensions to the base class `openc2lib.core.response.Results`.
		 
		[Developing extensions](https://github.com/mattereppe/openc2lib/blob/main/docs/developingextensions.md#developing-extensions) Section of the main documentation.

	"""
	#fieldtypes = {'clicommands' : ArrayOf(Process)}
	#fieldtypes = dict(clicommands = ArrayOf(Process))

	fieldtypes = {'clicommands': Processes, 'process_status': Processes, 'file_status': Files}


