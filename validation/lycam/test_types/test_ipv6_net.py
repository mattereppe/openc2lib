import pytest
import parametrize_from_file

import ipaddress
from openc2.v10 import IPv6Address


@parametrize_from_file('parameters/test_ipv6_net.yml')
def test_good_nets(ip_address):
	assert type(IPv6Address(ipv6_net=ip_address)) == IPv6Address

@parametrize_from_file('parameters/test_ipv6_net.yml')
def test_bad_nets(ip_address):
	with pytest.raises(Exception) as ex:
		IPv6Address(ipv6_net=ip_address)
