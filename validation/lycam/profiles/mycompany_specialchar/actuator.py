import openc2
import mycompany_specialchar.properties


@openc2.v10.CustomActuator(
    "x-mycompany/foo;bar",
    [
		("asset_id", openc2.properties.StringProperty()),
    ],
)
class MyCompanyActuator(object):
    pass
