import openc2
import acme.properties

@openc2.v10.CustomActuator(
    "x-acme",
    [
	 	("endpoint_id", openc2.properties.StringProperty()),
#	("asset_id", openc2.properties.StringProperty()),
		("asset_id", acme.properties.UuidProperty()),
    ],
)
class AcmeActuator(object):
    pass
