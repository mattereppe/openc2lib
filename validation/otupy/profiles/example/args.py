import uuid

import otupy as oc2

class myuuid(uuid.UUID):

	def __init__(self, u):
		if isinstance(u, uuid.UUID):
		 	super().__init__(str(u))
		else:
			super().__init__(u)

@oc2.extension(nsid='x-example')
class Args(oc2.Args):
	fieldtypes = {'async': bool, 'webhook_id': myuuid}

