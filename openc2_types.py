import ipaddress
from enum import Enum
from datetime import datetime, timezone

# define OPENC2_VERSION "version=1.0"
# define ..

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

class L4Protocol(Enum):
	icmp = 1
	tcp = 6
	udp = 17
	sctp = 132

class IPv4Connection:
	def __init__(self, src=None, sport=None, dst=None, dport=None, protocol=L4Protocol.tcp):
		__src_addr = IPv4Net(src)
		__src_port = int(sport)
		__dst_addr = IPv4Net(dst)
		__dst_port = int(dpost)
		__protocol = protocol



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
			self.time = int(datetime.now(timezone.utc).timestamp()*1000)
		else:
			self.time = timestamp






#
#class Command:
#	__action: Action()
#	__target: Target()
#	__args: Args()
#	__actuator: Actuator()
#	
#	def to_json():
#		return "{" + __action.to_json() + ", " +  __target.to_json() + ...
#				
#
#	def execute()
#		...
#		__action.run()
#
#
#
#
#	a = Scan()
#
#	Command(a, 
#
#
#
#class ICMP(L4Protocol):
#	pass
#
#class TCP(L4Protocol):
#	pass
#
#class Message():
#	__content: 
#	__content_type: 
#
#	to_json():
#		json = "{ headers: { 
#			"request_id": "...
#			"body: "
#			"{ "
#
#	def type():
#		return "openc2"
#
#	def version():
#		return OPENC2_VERSION
#
#class Request(Message):
#	def __init__(self, command, target, args=None, ...
#
#	def to_json()
#		(call the base class to_json to have the common headers)
#		+ "body part"
#
#class Response(Message):
#
#
