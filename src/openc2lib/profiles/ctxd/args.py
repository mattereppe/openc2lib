""" CTXD Arguments
	
	This module extends the Args defined by the Language Specification
	(see Sec. 'Command Arguments Unique to CTXD').
"""
import openc2lib as oc2

from openc2lib.profiles.ctxd.profile import Profile


@oc2.extension(nsid=Profile.nsid)
class Args(oc2.Args):
	""" CTXD Args

		This class extends the Args defined in the Language Specification.
		The extension mechanism is described in the 
		[Developing extensions](https://github.com/mattereppe/openc2lib/blob/main/docs/developingextensions.md#developing-extensions) Section of the main documentation.


	"""
	fieldtypes = {'name_only': bool}

