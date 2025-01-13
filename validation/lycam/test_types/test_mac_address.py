import pytest
import parametrize_from_file

import ipaddress
from openc2.v10 import MACAddress


@parametrize_from_file('parameters/test_mac_address.yml')
def test_good_nets(address):
	assert type(MACAddress(mac_addr=address)) == MACAddress

@parametrize_from_file('parameters/test_mac_address.yml')
def test_bad_nets(address):
	with pytest.raises(Exception):
		MACAddress(mac_addr=address)
