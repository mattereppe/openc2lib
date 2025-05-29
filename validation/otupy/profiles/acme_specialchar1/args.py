import uuid

import otupy as oc2

@oc2.extension(nsid='xacm&e')
class Args(oc2.Args):
	fieldtypes = {'firewall_status': str }

