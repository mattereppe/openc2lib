# This module implements the Data Types listed in Sec. 3.4.2 [OpenC2 Language specification]
#
import ipaddress
import datetime 
import dataclasses
import openc2.basetypes

# The usage of the ipaddress module is compliant to what required in the
# language specification for IPv4 addresses, especially the following points:
# a) The IPv4 address should be available both in string and binary form
# b) The network representation is an array according to RFC 4632 Sec. 3.1
#    (host/prefix, host/mask, host/hostmask, etc.)
class IPv4Addr:
	"OpenC2 IPv4 Address"
	__ipv4_addr = ipaddress.IPv4Address("0.0.0.0")
	
	def __init__(self, ipaddr=None):
		if ipaddr == None:
			self.__ipv4_addr = ipaddress.IPv4Address("0.0.0.0")
		else:
			self.__ipv4_addr = ipaddress.IPv4Address(ipaddr)

	def __str__(self):
		return self.__ipv4_addr.exploded

	def __repr__(self):
		return self.__ipv4_addr.exploded

class L4Protocol(openc2.basetypes.Enumerated):
	icmp = 1
	tcp = 6
	udp = 17
	sctp = 132

# According to OpenC2 specification, this is the time in milliseconds from the epoch
# timedate functions works with float timestamps expressed in seconds from the epoch
class DateTime:
	def __init__(self, timestamp=None):
		self.update(timestamp)

	def __str__(self):
		return str(self.time)

	def __int__(self):
		return self.time

	def update(self, timestamp=None):
		if timestamp == None:
			# datetime.timestamp() returns a float in seconds
			self.time = int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
		else:
			self.time = timestamp

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
class IPv4Connection(openc2.basetypes.Record):
	"OpenC2 IPv4 Connection"
	src_addr: IPv4Net = None
	src_port: int = None
	dst_addr: IPv4Net = None
	dst_port: int = None
	protocol: L4Protocol = None

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

