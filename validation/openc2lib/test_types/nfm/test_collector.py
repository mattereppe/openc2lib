import pytest
import parametrize_from_file
from openc2lib.profiles.nfm.data.collector import Collector
from openc2lib.types.data import IPv4Addr, Port
from openc2lib.profiles.nfm.data.flow_format import FlowFormat  # Assuming FlowFormat is defined

@parametrize_from_file("parameters/test_collector.yml")
def test_good_collector(address, port):
    # Transforming the inputs into the corresponding types
    transformed_address = IPv4Addr(address)
    transformed_port = Port(port)
    
    # Create the Collector object
    obj = Collector(address=transformed_address, port=transformed_port)
    
    # Assert the object is of type Collector
    assert isinstance(obj, Collector)

@parametrize_from_file("parameters/test_collector.yml")
def test_bad_collector(bad_address, bad_port):
    # Handling bad input transformations
    with pytest.raises(Exception):
        transformed_bad_address = IPv4Addr(bad_address) if bad_address else None
        transformed_bad_port = Port(bad_port) if bad_port else None
        
        # Attempt to create a Collector object with possibly incorrect inputs
        Collector(address=transformed_bad_address, port=transformed_bad_port)
