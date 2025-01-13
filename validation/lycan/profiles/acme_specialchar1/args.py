import openc2
import stix2
import acme_specialchar1.properties

@openc2.v10.CustomArgs(
		"whatever-who-cares",
		[
			("x-acm&e", acme_specialchar1.properties.AcmeProperty())
		]
)
class AcmeArgs(object):
    pass

