import openc2
import stix2
import mycompany.properties

@openc2.v10.CustomArgs(
		"whatever-it-cares",
		[
			("x-mycompany", mycompany.properties.DebugArgsProperty())
		]
)
class MyCompanyArgs(object):
    pass

