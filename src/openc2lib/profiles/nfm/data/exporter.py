from openc2lib.types.base import Record, ArrayOf, Array
from openc2lib.types.targets.file import File
from openc2lib.profiles.nfm.data.collector import Collector  # Assuming this path

class Exporter(Record):
    """
    Exporter

    Represents a system component responsible for exporting flow data.
    """

    storage: File = None
    """ Location and filename to store logs (with possible error reporting) """

    collectors: ArrayOf(Collector) = None  # type: ignore
    """ Systems that receive and process flow data from the exporter """

    def __init__(self, storage: File = None, collectors: ArrayOf = None):  # type: ignore
        if isinstance(storage, Exporter):
            self._init_from_exporter(storage)
        else:
            self._init_from_params(storage, collectors)
        self.validate_fields()

    def _init_from_exporter(self, exporter):
        self.storage = exporter.storage
        self.collectors = exporter.collectors

    def _init_from_params(self, storage, collectors):
        self.storage = storage
        self.collectors = collectors

    def __repr__(self):
        return f"Exporter(storage={self.storage}, collectors={self.collectors})"

    def __str__(self):
        return self.__repr__()

    def validate_fields(self):
        if not any([self.storage, self.collectors]):
            raise ValueError("At least one field must be set in Exporter (Record{1..*})")

        if self.storage is not None and not isinstance(self.storage, File):
            raise TypeError(f"'storage' must be File, got {type(self.storage)}")
        if self.collectors is not None and not isinstance(self.collectors, Array):
            raise TypeError(f"'collectors' must be ArrayOf(Collector), got {type(self.collectors)}")
    def get(self, key, default=None):
        """ Mimics dictionary get method """
        return getattr(self, key, default)
