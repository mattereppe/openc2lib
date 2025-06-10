from openc2lib.types.base import Record
from openc2lib.types.data import Port
from openc2lib.types.targets import IPv4Net
from openc2lib.profiles.fclm.data.file_format import FileFormat

class Collector(Record):
    """
    Collector Class

    Represents a flow collector configuration.
    - `address`: Optional IPv4 address of the collector.
    - `port`: Optional port number used by the collector.
    - `format`: Optional flow export format used by the collector.
    """

    address: IPv4Net = None
    """ IP address of the collector """

    port: Port = None
    """ Port of the collector """

    format: FileFormat = None
    """ Flow export file format (e.g., JSON, YAML, etc.) """

    def __init__(
        self,
        address: IPv4Net = None,
        port: Port = None,
        format: FileFormat = None
    ):
        super().__init__()
        self.address = address
        self.port = port
        self.format = format
        self.validate_fields()

    def __repr__(self):
        return f"Collector(address={self.address}, port={self.port}, format={self.format})"

    def __str__(self):
        return f"Collector(address={self.address}, port={self.port}, format={self.format})"

    def validate_fields(self):
        if self.address is not None and not isinstance(self.address, IPv4Net):
            raise TypeError(f"Expected 'address' to be IPv4Addr, got {type(self.address)}")
        if self.port is not None and not isinstance(self.port, Port):
            raise TypeError(f"Expected 'port' to be Port, got {type(self.port)}")
        if self.format is not None and not isinstance(self.format, FileFormat):
            raise TypeError(f"Expected 'format' to be FileFormat, got {type(self.format)}")
