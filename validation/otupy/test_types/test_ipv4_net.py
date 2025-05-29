import pytest
import parametrize_from_file

import ipaddress
from otupy import IPv4Net


@parametrize_from_file('parameters/test_ipv4_net.yml')
def test_good_nets(ip_address):
	assert type(IPv4Net(ip_address)) == IPv4Net

@parametrize_from_file('parameters/test_ipv4_net.yml')
def test_bad_nets(ip_address):
	with pytest.raises(Exception) as ex:
		IPv4Net(ip_address)
	assert ex.type == ipaddress.AddressValueError or ex.type == ipaddress.NetmaskValueError or ex.type == ValueError
