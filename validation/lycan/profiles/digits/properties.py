import openc2
import stix2


@openc2.properties.CustomProperty(
    "x-395",
    [
        ("debug_logging", stix2.properties.BooleanProperty()),
    ],
)
class DebugArgsProperty(object):
    pass

