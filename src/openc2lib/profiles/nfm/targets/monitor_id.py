import openc2lib as oc2
from openc2lib.profiles.nfm.profile import Profile  # Assuming this exists

# Target for Monitor-ID (Monitoring Agent ID)
@oc2.target(name='monitor_id', nsid=Profile.nsid)
class MonitorID(str):
    """ MonitoringAgentID
    Represents a monitoring agent ID as an OpenC2 target.
    This extends the base MonitorID class.
    """

    def __new__(cls, value):
        if not isinstance(value, str):
            raise TypeError(f"MonitorID must be a string, got {type(value).__name__}")
        return str.__new__(cls, value)