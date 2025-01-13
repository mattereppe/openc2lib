import openc2
import stix2
import acme_underscore_first1.properties

@openc2.v10.CustomArgs(
		"whatever-who-cares",
		[
			("x-_acme", acme_underscore_first1.properties.AcmeProperty())
		]
)
class AcmeArgs(object):
    pass

