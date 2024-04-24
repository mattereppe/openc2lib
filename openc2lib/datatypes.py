# This module implements the Data Types listed in Sec. 3.4.2 [OpenC2 Language specification]
#
import ipaddress
import aenum
import datetime 
import dataclasses
import openc2lib.basetypes
from openc2lib.actions import Actions

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

class L4Protocol(openc2lib.basetypes.Enumerated):
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

# A time (positive number) expressed in milliseconds
class Duration(int):
	def __init__(self, dur):
		if int(dur) < 0:
			raise ValueError("Duration must be a positive number")
		self=int(dur)

class Version(str):
	def __new__(cls, major, minor):
		vers = str(major) + '.' + str(minor)
		instance = super().__new__(cls, vers)
		return instance

	def __init__(self, major, minor):
		self.major = major
		self.minor = minor

	@staticmethod
	def fromstr(v):
		vers = v.split('.',2)
		return Version(vers[0], vers[1])
	
	@classmethod
	def fromdict(cls, vers, e=None):
		return Version.fromstr(vers)

		
class Nsid(str):
	def __init__(self, nsid):
		if len(nsid) > 16 or len(nsid) < 1:
			raise ValueError("Nsid must be between 1 and 16 characters")
		self = nsid

	@classmethod
	def fromdict(cls, name, e):
		return Nsid(name)
	
class ResponseType(openc2lib.basetypes.Enumerated):
	none=0
	ack=1
	status=2
	complete=3

class TargetEnum(openc2lib.basetypes.Enumerated):
	def __repr__(self):
		return self.name

class ActionTargets(openc2lib.basetypes.MapOf(Actions, openc2lib.basetypes.ArrayOf(TargetEnum))):
	pass

