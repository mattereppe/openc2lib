import openc2
import stix2
import mycompany_specialchar.properties

@openc2.v10.CustomArgs(
		"whatever-who-cares",
		[
			("x-mycompany/foo;bar", mycompany_specialchar.properties.DebugArgsProperty())
		]
)
class MyCompanyArgs(object):
    pass

