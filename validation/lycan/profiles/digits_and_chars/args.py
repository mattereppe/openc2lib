import openc2
import stix2
import digits_and_chars.properties

@openc2.v10.CustomArgs(
		"whatever-it-cares",
		[
			("x-0123456789_ABCDEFG_abcdefg___", digits_and_chars.properties.DebugArgsProperty())
		]
)
class MyArgs(object):
    pass

