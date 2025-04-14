""" CTXD Arguments
	
	This module extends the Args defined by the Language Specification
	(see Sec. 'Command Arguments Unique to CTXD').
"""
import otupy as oc2

from otupy.profiles.ctxd.profile import Profile


@oc2.extension(nsid=Profile.nsid)
class Args(oc2.Args):
	""" CTXD Args

		This class extends the Args defined in the Language Specification.
		The extension mechanism is described in the 
		[Developing extensions](https://github.com/mattereppe/otupy/blob/main/docs/developingextensions.md#developing-extensions) Section of the main documentation.


	"""
	fieldtypes = {'name_only': bool}

