import openc2
import stix2
import acme_noprofile.properties

@openc2.v10.CustomArgs(
		"whatever-who-cares",
		[
			("", acme_noprofile.properties.AcmeProperty())
		]
)
class AcmeArgs(object):
    pass

