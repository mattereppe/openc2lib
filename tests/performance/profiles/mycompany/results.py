import openc2lib as oc2


class Stuff(oc2.Map):
	fieldtypes = {'some': int, 'values': oc2.ArrayOf(bool), 'defined': str}


@oc2.extension(nsid="x-mycompany")
class Results(oc2.Results):
   fieldtypes = {'stuff': Stuff}

