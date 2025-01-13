import openc2
import mycompany_capX.properties


@openc2.v10.CustomActuator(
    "X-mycompany",
    [
#	("asset_id", mycompany_capX.properties.UuidProperty()), >>> Does not work, because UuidProperty is not serializable!
		("asset_id", openc2.properties.StringProperty()),
    ],
)
class MyCompanyActuator(object):
    pass
