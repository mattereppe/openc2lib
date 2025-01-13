import openc2
import stix2
import mycompany_with_underscore.properties

@openc2.v10.CustomArgs(
		"whatever-it-cares",
		[
			("x-mycompany_with_underscore", mycompany_with_underscore.properties.DebugArgsProperty())
		]
)
class MyCompanyArgs(object):
    pass

