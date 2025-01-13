import openc2
import stix2
import acme.properties

@openc2.v10.CustomArgs(
		"whatever-who-cares",
		[
			("x-acme", acme.properties.AcmeProperty())
		]
)
class AcmeArgs(object):
    pass

