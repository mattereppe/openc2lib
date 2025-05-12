from openc2lib.types.base import Record
from openc2lib.profiles.nfm.data.flow_format import FlowFormat

class ExportOptions(Record):
    """
    ExportOptions Class

    Represents optional export configuration settings.
    - `sampling`: Optional sampling rate (e.g., 1 means every packet, 10 means every 10th).
    - `aggregate`: Optional aggregation mode (may indicate level or method of aggregation).
    - `buffer`: Optional size of the UDP buffer for collectors.
    - `timeout`: Optional UDP timeout duration (in seconds or milliseconds).
    """

    sampling: int = None
    """ Sampling rate """

    aggregate: int = None
    """ Aggregation mode """

    buffer: int = None
    """ Collector UDP buffer """

    timeout: int = None
    """ Collector UDP timeout """
    
    format: FlowFormat = None
    """ Flow export format (e.g., NetFlow v5, v9, IPFIX) """
    def __init__(self, sampling: int = None, aggregate: int = None, buffer: int = None, timeout: int = None, format: FlowFormat = None):
        super().__init__()
        self.sampling = sampling
        self.aggregate = aggregate
        self.buffer = buffer
        self.timeout = timeout
        self.format = format
        self.validate_fields()

    def __repr__(self):
        return (
            f"ExportOptions(sampling={self.sampling}, aggregate={self.aggregate}, "
            f"buffer={self.buffer}, timeout={self.timeout}, format={self.format})"
        )

    def __str__(self):
        return (
            f"ExportOptions(sampling={self.sampling}, aggregate={self.aggregate}, "
            f"buffer={self.buffer}, timeout={self.timeout}, format={self.format})"
        )

    def validate_fields(self):
        if self.sampling is not None and not isinstance(self.sampling, int):
            raise TypeError(f"Expected 'sampling' to be int, got {type(self.sampling)}")
        if self.aggregate is not None and not isinstance(self.aggregate, int):
            raise TypeError(f"Expected 'aggregate' to be int, got {type(self.aggregate)}")
        if self.buffer is not None and not isinstance(self.buffer, int):
            raise TypeError(f"Expected 'buffer' to be int, got {type(self.buffer)}")
        if self.timeout is not None and not isinstance(self.timeout, int):
            raise TypeError(f"Expected 'timeout' to be int, got {type(self.timeout)}")
        if self.format is not None and not isinstance(self.format, FlowFormat):
            raise TypeError(f"Expected 'format' to be FlowFormat, got {type(self.format)}")
        
    def get(self, key, default=None):
        """ Mimics dictionary get method """
        return getattr(self, key, default)
