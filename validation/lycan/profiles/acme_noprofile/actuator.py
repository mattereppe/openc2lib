import openc2

@openc2.v10.CustomActuator(
    "",
    [
	 	("endpoint_id", openc2.properties.StringProperty()),
		("asset_id", openc2.properties.StringProperty()),
    ],
)
class AcmeActuator(object):
    pass
