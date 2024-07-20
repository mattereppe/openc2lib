import openc2lib as oc2


class Mode(oc2.Map):
	fieldtypes = {'output': str, 'supported': oc2.ArrayOf(str)}

class Battery(oc2.Map):
	fieldtypes = {'capacity': float, 'charged_at': int, 'status': int, 'mode': Mode, 'visible_on_display': bool}


@oc2.extension(nsid="x-esm")
class Results(oc2.Results):
   fieldtypes = {'battery': Battery, 'asset_id': str}

