import pytest
import parametrize_from_file
from openc2lib.types.base import ArrayOf
from openc2lib.profiles.fclm.data.exporter import Exporter
from openc2lib.profiles.fclm.data.collector import Collector
from openc2lib.types.targets.file import File
from openc2lib.types.data import IPv4Addr, Port
from openc2lib.profiles.fclm.data.file_format import FileFormat


@parametrize_from_file('parameters/test_exporter.yml')
def test_good_exporters(storage, collectors):
    exporter = Exporter(
        storage=File(**storage) if storage else None,
        collectors=ArrayOf(Collector)([Collector(
            address=IPv4Addr(c.get("address")) if c.get("address") else None,
            port=Port(c.get("port")) if c.get("port") else None,
            format=FileFormat[c.get("format")] if c.get("format") else None
        ) for c in collectors]) if collectors else None
    )
    assert isinstance(exporter, Exporter)


@parametrize_from_file('parameters/test_exporter.yml')
def test_bad_exporters(storage, collectors):
    with pytest.raises(Exception):
        storage_val = File(**storage) if isinstance(storage, dict) else storage
        collectors_val=ArrayOf(Collector)([Collector(
            address=IPv4Addr(c.get("address")) if c.get("address") else None,
            port=Port(c.get("port")) if c.get("port") else None,
            format=FileFormat[c.get("format")] if c.get("format") else None
        ) for c in collectors]) # Might be non-list to trigger failure
        Exporter(storage=storage_val, collectors=collectors_val)
