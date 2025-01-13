import openc2
import stix2
import example.properties

@openc2.v10.CustomArgs(
		"whatever-it-cares",
		[
			("x-example", example.properties.ArgsProperty())
		]
)
class MyCompanyArgs(object):
    pass

