import openc2
import stix2
import digits.properties

@openc2.v10.CustomArgs(
		"whatever-it-cares",
		[
			("x-395", digits.properties.DebugArgsProperty())
		]
)
class MyArgs(object):
    pass

