import openc2
import mycompany_nox.properties


@openc2.v10.CustomActuator(
    "mycompany",
    [
		("asset_id", openc2.properties.StringProperty()),
    ],
)
class MyCompanyActuator(object):
    pass
