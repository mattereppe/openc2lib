import pytest
import parametrize_from_file

import ipaddress
from openc2lib import IPv4Net


#@pytest.mark.parametrize("ip_address",["192.168.10.1", "130.251.4.7", "15.0.7.0/24", "10.0.0.0/8"])
@parametrize_from_file
def test_good_nets(ip_address):
	assert type(IPv4Net(ip_address)) == IPv4Net

#@pytest.mark.parametrize("ip_address",["10.0"])
@parametrize_from_file
def test_bad_nets(ip_address):
	with pytest.raises(Exception) as ex:
		IPv4Net(ip_address)
	assert ex.type == ipaddress.AddressValueError or ex.type == ipaddress.NetmaskValueError or ex.type == ValueError
