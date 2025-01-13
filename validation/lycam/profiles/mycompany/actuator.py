import openc2
import mycompany.properties


@openc2.v10.CustomActuator(
    "x-mycompany",
    [
		("asset_id", openc2.properties.StringProperty()),
    ],
)
class MyCompanyActuator(object):
    pass
