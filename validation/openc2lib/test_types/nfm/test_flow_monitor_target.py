import pytest
import parametrize_from_file
from openc2lib.types.base import ArrayOf, Array
from openc2lib.profiles.nfm.targets.monitor import FlowMonitor
from openc2lib.profiles.nfm.data.interface import Interface  # Assuming this path exists
from openc2lib.profiles.nfm.data.ie import IE  # Assuming this path exists
from openc2lib.types.data import Port  # Assuming Port is defined
from openc2lib.types.targets import IPv4Connection, IPv6Connection  # Updated to use Connections

@parametrize_from_file("parameters/test_flow_monitor_target.yml")
def test_good_flow_monitor(interfaces, information_elements, filter_v4, filter_v6):
    # Transforming the inputs into the corresponding types
    transformed_interfaces = ArrayOf(Interface)([Interface(name=iface["interface_name"]) for iface in interfaces])
    transformed_information_elements = ArrayOf(IE)([IE(ie["element_type"]) for ie in information_elements])
    
    # Converting to IPv4Connection and IPv6Connection
    transformed_filter_v4 = ArrayOf(IPv4Connection)([IPv4Connection(src_addr=ipv4["src_address"], 
                                                                  src_port=ipv4["src_port"], 
                                                                  dst_addr=ipv4["dst_address"], 
                                                                  dst_port=ipv4["dst_port"], 
                                                                  protocol=ipv4["protocol"]) 
                                                     for ipv4 in filter_v4])
    
    transformed_filter_v6 = ArrayOf(IPv6Connection)([IPv6Connection(src_addr=ipv6["src_address"], 
                                                                  src_port=ipv6["src_port"], 
                                                                  dst_addr=ipv6["dst_address"], 
                                                                  dst_port=ipv6["dst_port"], 
                                                                  protocol=ipv6["protocol"]) 
                                                     for ipv6 in filter_v6])
    
    # Create the FlowMonitor object
    obj = FlowMonitor(
        interfaces=transformed_interfaces,
        information_elements=transformed_information_elements,
        filter_v4=transformed_filter_v4,
        filter_v6=transformed_filter_v6
    )
    
    # Assert the object is of type FlowMonitor
    assert isinstance(obj, FlowMonitor)

@parametrize_from_file("parameters/test_flow_monitor_target.yml")
def test_bad_flow_monitor(bad_interfaces, bad_information_elements, bad_filter_v4, bad_filter_v6):
    # Handling bad input transformations and asserting that exceptions are raised
    
    with pytest.raises(Exception):
        # Attempting to create an Interface with invalid data (empty name)
        transformed_bad_interfaces = ArrayOf(Interface)([Interface(name=iface["interface_name"]) for iface in bad_interfaces]) if bad_interfaces else None
        
        transformed_bad_information_elements = ArrayOf(IE)([IE(ie["element_type"]) for ie in bad_information_elements]) if bad_information_elements else None
        
        # Converting bad filter inputs to IPv4Connection and IPv6Connection
        transformed_bad_filter_v4 = ArrayOf(IPv4Connection)([IPv4Connection(src_addr=ipv4["src_address"], 
                                                                      src_port=ipv4["src_port"], 
                                                                      dst_addr=ipv4["dst_address"], 
                                                                      dst_port=ipv4["dst_port"], 
                                                                      protocol=ipv4["protocol"]) 
                                                         for ipv4 in bad_filter_v4]) if bad_filter_v4 else None
        
        transformed_bad_filter_v6 = ArrayOf(IPv6Connection)([IPv6Connection(src_addr=ipv6["src_address"], 
                                                                      src_port=ipv6["src_port"], 
                                                                      dst_addr=ipv6["dst_address"], 
                                                                      dst_port=ipv6["dst_port"], 
                                                                      protocol=ipv6["protocol"]) 
                                                         for ipv6 in bad_filter_v6]) if bad_filter_v6 else None
        
        # Attempt to create a FlowMonitor object with possibly incorrect inputs
        FlowMonitor(
            interfaces=transformed_bad_interfaces,
            information_elements=transformed_bad_information_elements,
            filter_v4=transformed_bad_filter_v4,
            filter_v6=transformed_bad_filter_v6
        )
