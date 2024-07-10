import pytest
import parametrize_from_file

import ipaddress
from openc2lib import IPv6Net


@parametrize_from_file
def test_good_nets(ip_address):
	assert type(IPv6Net(ip_address)) == IPv6Net

@parametrize_from_file
def test_bad_nets(ip_address):
	with pytest.raises(Exception) as ex:
		IPv6Net(ip_address)
	assert ex.type == ipaddress.AddressValueError or ex.type == ipaddress.NetmaskValueError or ex.type == ValueError
