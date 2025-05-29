import dataclasses

import otupy.types.base

from otupy.types.data.port import Port
from otupy.types.data.l4_protocol import L4Protocol
from otupy.types.targets.ipv6_net import IPv6Net
from otupy.core.target import target

#@dataclasses.dataclass
@target('ipv6_connection')
class IPv6Connection(otupy.types.base.Record):
	"""OpenC2 IPv6 Connection
		
		IPv6 Connection including IPv6 addressed, protocol, and port numbers, as defined in Sec. 3.4.1.12.
	"""
	src_addr: IPv6Net = None
	""" Source address """
	src_port: int = None
	""" Source port """
	dst_addr: IPv6Net = None
	""" Destination address """
	dst_port: int = None
	""" Destination port """
	protocol: otupy.types.data.L4Protocol = None
	""" L4 protocol """

	def __init__(self, src_addr = None, src_port = None, dst_addr = None, dst_port = None, protocol = None):
		self.src_addr = IPv6Net(src_addr) if src_addr is not None else None
		self.src_port = Port(src_port) if src_port is not None else None
		self.dst_addr = IPv6Net(dst_addr) if dst_addr is not None else None
		self.dst_port = Port(dst_port) if dst_port is not None else None
		self.protocol = L4Protocol[str(protocol)] if protocol is not None else None

	def __repr__(self):
		return (f"IPv6Connection(src='{self.src_addr}', sport={self.src_port}, "
	             f"dst='{self.dst_addr}', dport={self.dst_port}, protocol='{self.protocol}')")
	
	def __str__(self):
		return f"IPv6Connection(" \
	            f"src={self.src_addr}, " \
	            f"dst={self.dst_addr}, " \
	            f"protocol={self.protocol}, " \
	            f"src_port={self.src_port}, " \
	            f"st_port={self.dst_port})"

