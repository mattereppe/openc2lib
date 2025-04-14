import otupy as oc2

@oc2.extension(nsid="x-acme")
class Results(oc2.Results):
   fieldtypes = {'status_detail': str}

