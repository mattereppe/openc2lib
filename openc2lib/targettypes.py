#
#
# This modules contains all target types defined in the
# Language Specification
#
#

import dataclasses
import ipaddress
import openc2lib.basetypes
import openc2lib.datatypes



# The Standard is not clear on this part. The 
# IPv4Net Target is defined as "Array /ipv4-net"
# (where ipv4-net --lowercase!-- is never defined!)
# However, the json serialization requirements explicitely
# define:
# Array /ipv4-net: JSON string containing the text representation 
#							of an IPv4 address range as specified in 
#							[RFC4632], Section 3.1.
# According to this definition, I assume a single network address
# should be managed. Extension to an array of IP network addresses
# is rather straightforward by using a list for ipv4_net attribute.
# Note that I have to keep both the string representation of the
# network address as well as the IPv4Network object to easily 
# manage the code and to automate the creation of the dictionary.
class IPv4Net:
	"OpenC2 IPv4 Network"
	ipv4_net: str
	
	def __init__(self, ipv4_net=None, prefix=None):
		if ipv4_net is None:
		    net = ipaddress.IPv4Network("0.0.0.0/0")
		elif prefix is None:
		    net = ipaddress.IPv4Network(ipv4_net)
		else:
		    tmp = ipv4_net + "/" + str(prefix)
		    net = ipaddress.IPv4Network(tmp)

		self.ipv4_net = net.exploded
	
	def addr(self):
	    return ipaddress.IPv4Network(self.ipv4_net).network_address.exploded
	
	def prefix(self):
	    return ipaddress.IPv4Network(self.ipv4_net).prefixlen
	
	def __str__(self):
	    return ipaddress.IPv4Network(self.ipv4_net).exploded
	
	def __repr__(self):
	    return ipaddress.IPv4Network(self.ipv4_net).exploded


@dataclasses.dataclass
class IPv4Connection(openc2lib.basetypes.Record):
	"OpenC2 IPv4 Connection"
	src_addr: IPv4Net = None
	src_port: int = None
	dst_addr: IPv4Net = None
	dst_port: int = None
	protocol: openc2lib.datatypes.L4Protocol = None

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

