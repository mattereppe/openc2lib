import uuid

import otupy as oc2


class myuuid(uuid.UUID):
	def __init__(self, u):
		if isinstance(u, uuid.UUID):
			self = u
		else:
		 	self = uuid.UUID(u)

@oc2.actuator(nsid='x-acme')
class Specifiers(oc2.Map):
	fieldtypes = {'endpoint_id': str, 'asset_id': myuuid}
	nsid = 'x-acme'
