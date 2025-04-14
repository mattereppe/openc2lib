import otupy as oc2

@oc2.actuator(nsid='x-esm')
class Specifiers(oc2.Map):
	fieldtypes = {'asset_id': str}
	nsid = 'x-esm'
