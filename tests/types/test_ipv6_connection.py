import pytest
import parametrize_from_file

import ipaddress
from openc2lib import IPv6Connection


@parametrize_from_file
def test_good_connections(src, sport, dst, dport, proto):
	assert type(IPv6Connection(src_addr=src, dst_addr=dst, src_port=sport, dst_port=dport, protocol=proto)) == IPv6Connection

@parametrize_from_file
def test_bad_connections(src, sport, dst, dport, proto):
	with pytest.raises(Exception):
		IPv6Connection(src_addr=src, dst_addr=dst, src_port=sport, dst_port=dport, protocol=proto)
