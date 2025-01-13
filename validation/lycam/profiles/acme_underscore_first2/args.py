import openc2
import stix2
import acme_underscore_first2.properties

@openc2.v10.CustomArgs(
		"whatever-who-cares",
		[
			("x-acme", acme_underscore_first2.properties.AcmeProperty())
		]
)
class AcmeArgs(object):
    pass

