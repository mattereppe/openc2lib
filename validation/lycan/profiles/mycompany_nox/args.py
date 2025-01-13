import openc2
import stix2
import mycompany_nox.properties

@openc2.v10.CustomArgs(
		"whatever-who-cares",
		[
			("mycompany", mycompany_nox.properties.DebugArgsProperty())
		]
)
class MyCompanyArgs(object):
    pass

