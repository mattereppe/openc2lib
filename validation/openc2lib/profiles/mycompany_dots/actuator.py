import uuid

import openc2lib as oc2

@oc2.actuator(nsid='x-mycompany.example.com')
class Specifiers(oc2.Map):
	fieldtypes = {'asset_id': uuid.UUID}
	nsid = 'x-mycompany.example.com'
