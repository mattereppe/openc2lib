import pytest
import parametrize_from_file

import ipaddress
from openc2lib import MACAddr


@parametrize_from_file
def test_good_nets(address):
	assert type(MACAddr(address)) == MACAddr

@parametrize_from_file
def test_bad_nets(address):
	with pytest.raises(Exception):
		MACAddr(address)
