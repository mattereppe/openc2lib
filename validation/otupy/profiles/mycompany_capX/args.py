import otupy as oc2

@oc2.extension(nsid='X-mycompany')
class Args(oc2.Args):
	fieldtypes = {'debug_logging': bool }

