import pytest
import parametrize_from_file
from openc2lib.types.base import ArrayOf
from openc2lib.types.targets import IPv4Net, IPv6Net, MACAddr
from openc2lib.profiles.nfm.data.iface_type import IfaceType  # Assuming this path exists
from openc2lib.profiles.nfm.data.interface import Interface  # Assuming this path exists

@parametrize_from_file("parameters/test_interface.yml")
def test_good_interface(name, description, if_id, ipv4_net, ipv6_net, mac_addr, iface_type, active):
    # Transforming inputs into the corresponding types
    transformed_ipv4_net = ArrayOf(IPv4Net)([IPv4Net(ipv4) for ipv4 in ipv4_net])
    transformed_ipv6_net = ArrayOf(IPv6Net)([IPv6Net(ipv6) for ipv6 in ipv6_net])
    transformed_mac_addr = MACAddr(mac_addr) if mac_addr else None
    transformed_iface_type = IfaceType(iface_type) if iface_type else None
    
    # Create the Interface object
    obj = Interface(
        name=name,
        description=description,
        if_id=if_id,
        ipv4_net=transformed_ipv4_net,
        ipv6_net=transformed_ipv6_net,
        mac_addr=transformed_mac_addr,
        iface_type=transformed_iface_type,
        active=active
    )
    
    # Assert the object is of type Interface
    assert isinstance(obj, Interface)

@parametrize_from_file("parameters/test_interface.yml")
def test_bad_interface(bad_name, bad_description, bad_if_id, bad_ipv4_net, bad_ipv6_net, bad_mac_addr, bad_iface_type, bad_active):
    # Handling bad input transformations and asserting that exceptions are raised
    with pytest.raises(Exception):
        # Attempting to create an Interface with invalid data (e.g., empty name, invalid IPv4 address)
        transformed_bad_ipv4_net = ArrayOf(IPv4Net)([IPv4Net(ipv4) for ipv4 in bad_ipv4_net]) if bad_ipv4_net else None
        transformed_bad_ipv6_net = ArrayOf(IPv6Net)([IPv6Net(ipv6) for ipv6 in bad_ipv6_net]) if bad_ipv6_net else None
        transformed_bad_mac_addr = MACAddr(bad_mac_addr) if bad_mac_addr else None
        transformed_bad_iface_type = IfaceType(bad_iface_type) if bad_iface_type else None
        
        # Attempt to create an Interface object with invalid inputs
        Interface(
            name=bad_name,
            description=bad_description,
            if_id=bad_if_id,
            ipv4_net=transformed_bad_ipv4_net,
            ipv6_net=transformed_bad_ipv6_net,
            mac_addr=transformed_bad_mac_addr,
            iface_type=transformed_bad_iface_type,
            active=bad_active
        )
