import uuid

import otupy as oc2


@oc2.target(name='container', nsid='')
class Container(oc2.Map):
	fieldtypes = {'container_id': uuid.UUID}
