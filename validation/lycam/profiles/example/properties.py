import openc2
import stix2
import uuid


class UuidProperty(openc2.properties.Property):
	def __init__(self, **kwargs):
		super(UuidProperty, self).__init__(**kwargs)

	def clean(self, value):
		if not isinstance(value, uuid.UUID):
			return uuid.UUID(value)
		return value

@openc2.properties.CustomProperty(
    "x-example",
    [
        ("async", stix2.properties.BooleanProperty()),
        ("webhook_id", openc2.properties.StringProperty()),
    ],
)
class ArgsProperty(object):
    pass
