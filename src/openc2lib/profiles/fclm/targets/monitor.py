import openc2lib as oc2
from openc2lib.profiles.fclm.profile import Profile  # Assuming this exists
from openc2lib.types.base import ArrayOf, Array
from openc2lib.types.targets import File, URI
from openc2lib.profiles.fclm.data.socket import Socket
from openc2lib.types.base import Choice
from openc2lib.types.data.hostname import  Hostname
from openc2lib.types.targets.ipv4_connection import IPv4Connection
from openc2lib.core.register import Register
# Target for LogMonitor Configuration
@oc2.target(name='monitor', nsid=Profile.nsid)
class LogMonitor(Choice):
    """
    LogMonitor

    Represents a file log monitoring system. Suitable for agents that collect logs
    from files, URIs, or sockets and attach metadata.
    """

    register = Register({'file': File, 'URI': URI, 'socket': Socket})