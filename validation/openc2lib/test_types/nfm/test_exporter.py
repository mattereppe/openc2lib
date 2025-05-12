import pytest
import parametrize_from_file
from openc2lib.profiles.nfm.data.exporter import Exporter
from openc2lib.profiles.nfm.data.collector import Collector
from openc2lib.types.targets.file import File
from openc2lib.types.base import ArrayOf
from openc2lib.types.data import IPv4Addr, Port
from openc2lib.profiles.nfm.data.flow_format import FlowFormat

@parametrize_from_file("parameters/test_exporter.yml")
def test_good_exporter(storage, collectors):
    # Transforming the inputs into the corresponding types
    transformed_storage = File(**storage) if storage else None
    transformed_collectors = ArrayOf(Collector)([
        Collector(
            address=IPv4Addr(c.get("address")) if c.get("address") else None,
            port=Port(c.get("port")) if c.get("port") else None,
        ) for c in collectors]) if collectors else None

    # Create the Exporter object
    obj = Exporter(storage=transformed_storage, collectors=transformed_collectors)

    # Assert the object is of type Exporter
    assert isinstance(obj, Exporter)


@parametrize_from_file("parameters/test_exporter.yml")
def test_bad_exporter(storage, collectors):
    with pytest.raises(Exception):
        transformed_storage = File(**storage) if isinstance(storage, dict) else storage
        transformed_collectors = ArrayOf(Collector)([
                Collector(
                    address=IPv4Addr(c.get("address")) if c.get("address") else None,
                    port=Port(c.get("port")) if c.get("port") else None,
                ) for c in collectors]) if collectors else None
        Exporter(storage=transformed_storage, collectors=transformed_collectors)
