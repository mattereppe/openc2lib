
from openc2lib.types.base.record import Record
from openc2lib.types.targets.ipv4_net import IPv4Net
from openc2lib.types.data.port import Port
from openc2lib.types.data.l4_protocol import L4Protocol

class Socket(Record):
    """OpenC2 Socket

    A socket connection with IPv4 address, port, and protocol details.
    """
    host: IPv4Net
    """ IPv4 address of the host """
    port: Port = None
    """ Port number """
    protocol: L4Protocol = None
    """ L4 protocol (e.g., TCP or UDP) """

    def __init__(self, host, port=None, protocol=None):
        if host is None:
            raise ValueError("host must be provided")
        self.host = IPv4Net(host)
        self.port = Port(port) if port is not None else None
        self.protocol = L4Protocol[str(protocol)] if protocol is not None else None

    def __repr__(self):
        return (f"Socket(host='{self.host}', port={self.port}, "
                f"protocol='{self.protocol}')")

    def __str__(self):
        return f"Socket(" \
               f"host={self.host}, " \
               f"port={self.port}, " \
               f"protocol={self.protocol})"
