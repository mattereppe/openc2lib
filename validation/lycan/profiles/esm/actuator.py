import openc2


@openc2.v10.CustomActuator(
    "x-esm",
    [
		("asset_id", openc2.properties.StringProperty()),
    ],
)
class MyCompanyActuator(object):
    pass

