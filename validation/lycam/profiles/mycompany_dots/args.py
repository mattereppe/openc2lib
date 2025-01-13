import openc2
import stix2
import mycompany_dots.properties

@openc2.v10.CustomArgs(
		"whatever-who-cares",
		[
			("x-mycompany.example.com", mycompany_dots.properties.DebugArgsProperty())
		]
)
class MyCompanyArgs(object):
    pass

