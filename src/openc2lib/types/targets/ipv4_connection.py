import dataclasses

import openc2lib.types.base

from openc2lib.types.targets.ipv4_net import IPv4Net
from openc2lib.core.target import target

@dataclasses.dataclass
@target('ipv4_connection')
class IPv4Connection(openc2lib.types.base.Record):
	"""OpenC2 IPv4 Connection
		
		IPv4 Connection including IPv4 addressed, protocol, and port numbers, as defined in Sec. 3.4.1.10.
	"""
	src_addr: IPv4Net = None
	""" Source address """
	src_port: int = None
	""" Source port """
	dst_addr: IPv4Net = None
	""" Destination address """
	dst_port: int = None
	""" Destination port """
	protocol: openc2lib.types.data.L4Protocol = None
	""" L4 protocol """

	def __repr__(self):
		return (f"IPv4Connection(src='{self.src_addr}', sport={self.src_port}, "
	             f"dst='{self.dst_addr}', dport={self.dst_port}, protocol='{self.protocol}')")
	
	def __str__(self):
		return f"IPv4Connection(" \
	            f"src={self.src_addr}, " \
	            f"dst={self.dst_addr}, " \
	            f"protocol={self.protocol}, " \
	            f"src_port={self.src_port}, " \
	            f"st_port={self.dst_port})"

