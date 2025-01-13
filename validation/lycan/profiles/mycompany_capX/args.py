import openc2
import stix2
import mycompany_capX.properties

#@oc2.extension(nsid='X-mycompany')
#class Args(oc2.Args):
#	fieldtypes = {'debug_logging': bool }

#@openc2.CustomArgs("whatever-who-cares", [("custom_args", CustomTargetProperty())])
#class CustomArgs(object):
#    pass

@openc2.v10.CustomArgs(
		"whatever-it-cares",
		[
			("X-mycompany", mycompany_capX.properties.DebugArgsProperty())
		]
)
class MyCompanyArgs(object):
    pass

