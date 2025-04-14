import uuid

import otupy as oc2

@oc2.actuator(nsid='X-mycompany')
class Specifiers(oc2.Map):
	fieldtypes = {'asset_id': uuid.UUID}
	nsid = 'X-mycompany'
