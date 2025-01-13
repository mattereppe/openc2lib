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
    "x-mycompany",
    [
        ("debug_logging", stix2.properties.BooleanProperty()),
    ],
)
class DebugArgsProperty(object):
    pass

