import uuid
import openc2

class UuidProperty(openc2.properties.Property):
	def __init__(self, **kwargs):
		super(UuidProperty, self).__init__(**kwargs)

	def clean(self, value):
		if not isinstance(value, uuid.UUID):
			return uuid.UUID(value)
		return value

@openc2.properties.CustomProperty(
    "x-acme",
    [
        ("firewall_status", openc2.properties.StringProperty()),
        ("container_id", openc2.properties.StringProperty()),
        ("features", openc2.properties.EnumProperty(allowed=["versions", "profiles", "schema"])),
    ],
)
class AcmeProperty(object):
    pass

