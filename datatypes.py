# This module implements the Data Types listed in Sec. 3.4.2 [OpenC2 Language specification]
#
import ipaddress
import enum
import datetime 

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

class L4Protocol(enum.Enum):
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

	def update(self, timestamp=None):
		if timestamp == None:
			# datetime.timestamp() returns a float in seconds
			self.time = int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
		else:
			self.time = timestamp






