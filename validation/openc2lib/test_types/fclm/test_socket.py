import pytest
import parametrize_from_file
from openc2lib.profiles.fclm.data.socket import Socket
from openc2lib.types.data import IPv4Addr, Port
from openc2lib.types.data.l4_protocol import L4Protocol

@parametrize_from_file("parameters/test_socket.yml")
def test_good_socket(host, port, protocol):
    # Transforming the inputs into the corresponding types
    transformed_host = IPv4Addr(host)
    transformed_port = Port(port)
    transformed_protocol = L4Protocol[str(protocol)]  # Transform string to enum
    
    # Create the Socket object
    obj = Socket(host=transformed_host, port=transformed_port, protocol=transformed_protocol)
    
    # Assert the object is of type Socket
    assert isinstance(obj, Socket)
    

@parametrize_from_file("parameters/test_socket.yml")
def test_bad_socket(bad_host, bad_port, bad_protocol):
    # Handling bad input transformations
    with pytest.raises(Exception):
        # Attempt to create a Socket object with possibly incorrect inputs
        transformed_bad_host = IPv4Addr(bad_host) if bad_host else None
        transformed_bad_port = Port(bad_port) if bad_port else None
        transformed_bad_protocol = L4Protocol[str(bad_protocol)] if bad_protocol else None
        
        Socket(host=transformed_bad_host, port=transformed_bad_port, protocol=transformed_bad_protocol)
