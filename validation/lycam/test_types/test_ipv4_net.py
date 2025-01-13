import pytest
import parametrize_from_file

import ipaddress
from openc2.v10 import IPv4Address


@parametrize_from_file('parameters/test_ipv4_net.yml')
def test_good_nets(ip_address):
	assert type(IPv4Address(ipv4_net=ip_address)) == IPv4Address

@parametrize_from_file('parameters/test_ipv4_net.yml')
def test_bad_nets(ip_address):
	with pytest.raises(Exception) as ex:
		IPv4Address(ipv4_net=ip_address)
