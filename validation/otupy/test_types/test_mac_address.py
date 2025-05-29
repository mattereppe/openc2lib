import pytest
import parametrize_from_file

import ipaddress
from otupy import MACAddr


@parametrize_from_file('parameters/test_mac_address.yml')
def test_good_nets(address):
	assert type(MACAddr(address)) == MACAddr

@parametrize_from_file('parameters/test_mac_address.yml')
def test_bad_nets(address):
	with pytest.raises(Exception):
		MACAddr(address)
