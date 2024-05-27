""" OpenC2 target types

	Definition of the target types in the OpenC2 (Sec. 3.4.1).
	The naming strictly follows the definition of the Language Specification
	as close as possible. The relevant exception is represented by hyphens
	that are always dropped.
"""

import dataclasses
import ipaddress

import openc2lib.types.basetypes
import openc2lib.types.datatypes

from openc2lib.core.target import Targets


class IPv4Net:
	"""OpenC2 IPv4 Address Range
		
		IPv4 Address Range as defined in Sec. 3.4.1.9.

		The Standard is not clear on this part. The 
		IPv4Net Target is defined as "Array /ipv4-net"
		(where ipv4-net --lowercase!-- is never defined!)
		However, the json serialization requirements explicitely
		define:
		Array /ipv4-net: JSON string containing the text representation 
		 						of an IPv4 address range as specified in 
		 						[RFC4632], Section 3.1.
		According to this definition, I assume a single network address
		should be managed. Extension to an array of IP network addresses
		is rather straightforward by using a list for ipv4_net attribute.
		Note that I have to keep both the string representation of the
		network address as well as the IPv4Network object to easily 
		manage the code and to automate the creation of the dictionary.
		
	"""
#ipv4_net: str
	
	def __init__(self, ipv4_net=None, prefix=None):
		""" Initialize IPv4 Address Range

			Initialize `IPv4Net with IPv4 address and prefix.
			If no IPv4 address is given, initialize to null address.
			If no prefix is given, assume /32 (iPv4 address only).
			:param ipv4_net: IPv4 Network Address.
			:param prefix: IPv4 Network Adress Prefix.
		"""
		if ipv4_net is None:
		    net = ipaddress.IPv4Network("0.0.0.0/0")
		elif prefix is None:
		    net = ipaddress.IPv4Network(ipv4_net)
		else:
		    tmp = ipv4_net + "/" + str(prefix)
		    net = ipaddress.IPv4Network(tmp)

		self.ipv4_net = net.exploded
	
	def addr(self):
		""" Returns address part only (no prefix) """
		return ipaddress.IPv4Network(self.ipv4_net).network_address.exploded
	
	def prefix(self):
		""" Returns prefix only """
		return ipaddress.IPv4Network(self.ipv4_net).prefixlen
	
	def __str__(self):
	    return ipaddress.IPv4Network(self.ipv4_net).exploded
	
	def __repr__(self):
	    return ipaddress.IPv4Network(self.ipv4_net).exploded


@dataclasses.dataclass
class IPv4Connection(openc2lib.types.basetypes.Record):
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
	protocol: openc2lib.types.datatypes.L4Protocol = None
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

class Features(openc2lib.types.basetypes.ArrayOf(openc2lib.types.datatypes.Feature)):
	""" OpenC2 Features

		Implements the Features target (Section 3.4.1.5).
		Just defines an `ArrayOf` `Feature`.
	"""
# TODO: implmement control on the max number of elements
	pass



# Register the list of available Targets
Targets.add('features', Features, 9)
Targets.add('ipv4_net', IPv4Net, 13)
Targets.add('ipv4_connection', IPv4Connection, 15)
