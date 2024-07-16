import uuid

import openc2lib as oc2


@oc2.target(name='conta$iner', nsid='x-acme')
class Container(oc2.Map):
	fieldtypes = {'container_id': uuid.UUID}
