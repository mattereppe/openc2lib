import pytest
import parametrize_from_file

import ipaddress
from otupy import IPv6Connection


@parametrize_from_file('parameters/test_ipv6_connection.yml')
def test_good_connections(src, sport, dst, dport, proto):
	assert type(IPv6Connection(src_addr=src, dst_addr=dst, src_port=sport, dst_port=dport, protocol=proto)) == IPv6Connection

@parametrize_from_file('parameters/test_ipv6_connection.yml')
def test_bad_connections(src, sport, dst, dport, proto):
	with pytest.raises(Exception):
		IPv6Connection(src_addr=src, dst_addr=dst, src_port=sport, dst_port=dport, protocol=proto)
