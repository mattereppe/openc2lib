import uuid

import otupy as oc2

@oc2.extension(nsid='x-acme')
class Args(oc2.Args):
	fieldtypes = {'firewall_status': str }

