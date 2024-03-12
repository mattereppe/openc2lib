# This module implements the Target types defined in Sec. 3.4.1 [OpenC2 Languate specification]
#
import aenum
import abc
import ipaddress
from openc2.datatypes import IPv4Addr,L4Protocol

class Targets(aenum.Enum):
	pass

def register_target(cls):
	aenum.extend_enum(Targets, cls.getName(), cls)
	return cls

class Target(abc.ABC):
	id = 0
	name = 'target'

	# This is not really necessary
	@classmethod
	def getId(self):
		return self.id
	
	# This is not really necessary
	@classmethod
	def getName(self):
		return self.name

	def __str__(self):
		return Targets(self.__class__).name

#	def __new__(cls, name=None):
#		if( name is None ):
#			return super().__new__(cls)
#		else:
#			return Targets[name].value()	

@register_target
class IPv4Net(Target):
	"OpenC2 IPv4 Network"
	id = 15
	name = "ipv4_net"
	
	def __init__(self, ipaddr=None, prefix=None):
	    if ipaddr is None:
	        self.__ipv4_net = ipaddress.IPv4Network("0.0.0.0/0")
	    elif prefix is None:
	        self.__ipv4_net = ipaddress.IPv4Network(ipaddr)
	    else:
	        ipv4_net = ipaddr + "/" + str(prefix)
	        self.__ipv4_net = ipaddress.IPv4Network(ipv4_net)
	
	def addr(self):
	    return self.__ipv4_net.network_address.exploded
	
	def prefix(self):
	    return self.__ipv4_net.prefixlen
	
	def __str__(self):
	    return self.__ipv4_net.exploded
	
	def __repr__(self):
	    return self.__ipv4_net.exploded

@register_target
class IPv4Connection(Target):
	"OpenC2 IPv4 Connection"
	id = 13
	name = 'ipv4_connection'

	def __init__(self, src=None, src_port=None, dst=None, dst_port=None, protocol=L4Protocol.tcp):
		self.__src_addr = IPv4Net(src) 
		self.__src_port = int(src_port)
		self.__dst_addr = IPv4Net(dst) 
		self.__dst_port = int(dst_port)
		self.__protocol = L4protocol(protocol)
	
	def __repr__(self):
		return (f"IPv4Connection(src='{self.__src_addr}', sport={self.__src_port}, "
	             f"dst='{self.__dst_addr}', dport={self.__dst_port}, protocol='{self.__protocol}')")
	
	def __str__(self):
		return f"IPv4Connection(" \
	            f"src={self.__src_addr}, " \
	            f"dst={self.__dst_addr}, " \
	            f"protocol={self.__protocol}, " \
	            f"src_port={self.__src_port}, " \
	            f"st_port={self.__dst_port})"



