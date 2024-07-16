import openc2lib as oc2

@oc2.extension(nsid='x-0123456789_ABCDEFG_abcdefg___')
class Args(oc2.Args):
	fieldtypes = {'debug_logging': bool }

