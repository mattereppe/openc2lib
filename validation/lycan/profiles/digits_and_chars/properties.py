import openc2
import stix2


@openc2.properties.CustomProperty(
    "x-0123456789_ABCDEFG_abcdefg___",
    [
        ("debug_logging", stix2.properties.BooleanProperty()),
    ],
)
class DebugArgsProperty(object):
    pass

