import pytest
import parametrize_from_file
from openc2lib.profiles.fclm.targets.monitor import LogMonitor
from openc2lib.types.targets import File, URI
from openc2lib.profiles.fclm.data.socket import Socket
from openc2lib.types.data.hostname import Hostname
from openc2lib.types.targets.ipv4_connection import IPv4Connection

@parametrize_from_file("parameters/test_log_monitor_target.yml")
def test_log_monitor_target(monitor_type, monitor_value):
    # Transform the input into the corresponding types
    if monitor_type == "file":
        transformed_monitor = File(**monitor_value)
    elif monitor_type == "URI":
        transformed_monitor = URI(**monitor_value)
    elif monitor_type == "socket":
        transformed_monitor = Socket(**monitor_value)
    else:
        raise ValueError("Unsupported monitor type")

    # Create the LogMonitor object
    obj = LogMonitor(transformed_monitor)

    # Assert the object is of type LogMonitor
    assert isinstance(obj, LogMonitor)

@parametrize_from_file("parameters/test_log_monitor_target.yml")
def test_bad_log_monitor_target(bad_monitor_type, bad_monitor_value):
    # Handling bad input transformations
    with pytest.raises(Exception):
        if bad_monitor_type == "file":
            transformed_bad_monitor = File(**bad_monitor_value)
        elif bad_monitor_type == "URI":
            transformed_bad_monitor = URI(**bad_monitor_value)
        elif bad_monitor_type == "socket":
            transformed_bad_monitor = Socket(**bad_monitor_value)
        else:
            raise ValueError("Unsupported monitor type")

        # Attempt to create a LogMonitor object with possibly incorrect inputs
        LogMonitor(transformed_bad_monitor)
