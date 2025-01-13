import openc2
import mycompany_dots.properties


@openc2.v10.CustomActuator(
    "x-mycompany.example.com",
    [
#	("asset_id", mycompany_dots.properties.UuidProperty()), >>> Does not work, because UuidProperty is not serializable!
		("asset_id", openc2.properties.StringProperty()),
    ],
)
class MyCompanyActuator(object):
    pass
