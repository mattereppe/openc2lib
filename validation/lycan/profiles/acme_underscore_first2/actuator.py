import openc2

@openc2.v10.CustomActuator(
    "x-acme",
    [
	 	("endpoint_id", openc2.properties.StringProperty()),
		("asset_id", openc2.properties.StringProperty()),
    ],
)
class AcmeActuator(object):
    pass
