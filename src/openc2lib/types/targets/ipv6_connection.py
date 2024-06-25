import dataclasses

import openc2lib.types.base

from openc2lib.types.targets.ipv6_net import IPv6Net
from openc2lib.core.target import target

@dataclasses.dataclass
@target('ipv6_connection')
class IPv6Connection(openc2lib.types.base.Record):
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
	protocol: openc2lib.types.data.L4Protocol = None
	""" L4 protocol """

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

