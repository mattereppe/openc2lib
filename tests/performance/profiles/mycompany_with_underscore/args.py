import uuid

import openc2lib as oc2

@oc2.extension(nsid='x-mycompany_with_underscore')
class Args(oc2.Args):
	fieldtypes = {'debug_logging': bool }

