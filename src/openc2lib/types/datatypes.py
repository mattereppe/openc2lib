""" OpenC2 data types

	Definition of the data types in the OpenC2 DataModels (Sec. 3.4.2).
	The naming strictly follows the definition of the Language Specification
	as close as possible. The relevant exception is represented by hyphens
	that are always dropped.
"""

import ipaddress
import aenum
import datetime 
import dataclasses

from openc2lib.types.basetypes import MapOf, Enumerated, ArrayOf
from openc2lib.core.actions import Actions


""" IPv4 Address

	This class implements an IPv4 Address as described in Sec. 3.4.2.8.

The usage of the ipaddress module is compliant to what required in the
language specification for IPv4 addresses, especially the following points:
a) The IPv4 address should be available both in string and binary form
b) The network representation is an array according to RFC 4632 Sec. 3.1
   (host/prefix, host/mask, host/hostmask, etc.)
"""
class IPv4Addr:
	"""OpenC2 IPv4 Address"

		This class implements an IPv4 Address as described in Sec. 3.4.2.8.

		The usage of the ipaddress module is compliant to what required in the
		language specification for IPv4 addresses, especially the following points:
		a) The IPv4 address should be available both in string and binary form
		b) The network representation is an array according to RFC 4632 Sec. 3.1
		   (host/prefix, host/mask, host/hostmask, etc.)

"""
	__ipv4_addr = ipaddress.IPv4Address("0.0.0.0")
	""" Internal representation of the IPv4 address"""
	
	def __init__(self, ipaddr=None):
		""" Initialize IPv4 Address 

			An IPv4 address is built from a string that uses the common dotted notation.
			If no IPv4 address is provided, the null address is used ("0.0.0.0").

			:param ipaddr: Quad-dotted representation of the IPv4 address.
		"""
		if ipaddr == None:
			self.__ipv4_addr = ipaddress.IPv4Address("0.0.0.0")
		else:
			self.__ipv4_addr = ipaddress.IPv4Address(ipaddr)

	def __str__(self):
		return self.__ipv4_addr.exploded

	def __repr__(self):
		return self.__ipv4_addr.exploded

class L4Protocol(Enumerated):
	""" OpenC2 L4 Protocol

		This is an enumeration for all known transport protocols. The numeric identifier
		is set to the protocol number defined for IP.
	"""
	icmp = 1
	tcp = 6
	udp = 17
	sctp = 132

class DateTime:
	""" OpenC2 Date-Time

		This is used to represents dates and times according to Sec. 3.4.2.2.
		 According to OpenC2 specification, this is the time in milliseconds from the epoch.
		Be careful that the `timedate` functions work with float timestamps expressed 
		in seconds from the epoch, hence conversion is needed.
	"""
	def __init__(self, timestamp=None):
		""" Initialize Date-Time
			
			The instance is initialized with the provided timestamp, or to the current time if no 
			argument is given. The timestamp is expressed in milliseconds
				from the epoch, according to the Language Specification.
			:param timestamp: The timestamp to initialize the instance.
		"""
		self.update(timestamp)

	def __str__(self):
		return str(self.time)

	def __int__(self):
		return self.time

	def update(self, timestamp=None):
		""" Change Date-Time

			Change the timestamp beard by the instance. The timestamp is expressed in milliseconds
			from the epoch. If no `timestamp` is given, sets to the current time.
			:param timestamp: The timestamp to initialize the instance.
		"""
		if timestamp == None:
			# datetime.timestamp() returns a float in seconds
			self.time = int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
		else:
			self.time = timestamp

	# RFC 7231       
	def httpdate(self, timestamp=None):
		""" Format  to HTTP headers

			Formats the timestamp according to the requirements of HTTP headers (RFC 7231).
			Use either the `timestamp`, if provided,  or the current time.
			:param timestamp: The timestamp to format, expressed in milliseconds from the epoch.
			:return RFC 7231 representation of the `timestamp`.
		"""
			
		if timestamp is None:
			timestamp = self.time

		return datetime.datetime.fromtimestamp(timestamp/1000).strftime('%a, %d %b %Y %H:%M:%S %Z')

class Duration(int):
	""" OpenC2 Duration

		 A time (positive number) expressed in milliseconds (Sec. 3.4.2.3).
	""" 
	def __init__(self, dur):
		""" Initialization

			Initialize to `dur` if greater or equal to zero, raise an exception if negative.
		"""
		if int(dur) < 0:
			raise ValueError("Duration must be a positive number")
		self=int(dur)

class Version(str):
	""" OpenC2 Version

		Version of the OpenC2 protocol (Sec. 3.4.2.16). Currently a *<major>.<minor>* format is used.
	"""
	def __new__(cls, major, minor):
		""" Create `Version` instance

			Create a Version instance from major and minor numbers, expressed as numbers.
			:param major: Major number of OpenC2 version.
			:param minor: Minor number of OpenC2 version.
			:return: `Version` instance.
		"""
		vers = str(major) + '.' + str(minor)
		instance = super().__new__(cls, vers)
		return instance

	def __init__(self, major, minor):
		""" Initialize `Version` instance

			Initialize with major and minor numbers.
			:param major: Major number of OpenC2 version.
			:param minor: Minor number of OpenC2 version.
			:return: `Version` instance.
		"""
		self.major = major
		self.minor = minor

	@staticmethod
	def fromstr(v):
		""" Create `Version` instance

			Create `Version` instance from string (in the *<major>.<minor>* notation.
			:param v: Text string with the Version.
			:return: `Version` instance.
		"""
		vers = v.split('.',2)
		return Version(vers[0], vers[1])
	
	@classmethod
	def fromdict(cls, vers, e=None):
		""" Create `Version` instance

			Create `Version` instance from string (in the *<major>.<minor>* notation.
			This method is provided to deserialize an OpenC2 message according to the openc2lib approach.
			This method should only be used internally the openc2lib.
			:param vers: Text string with the Version.
			:param e: `Encoder` instance to be used (only included to be compliance with the function footprint.
			:return: `Version` instance.
		"""
		return Version.fromstr(vers)

class Feature(Enumerated):
	""" OpenC2 Feature

		An enumeration for the fields that can be included in the `Results` (see Sec. 3.4.2.4).
	"""
	versions   = 1
	profiles   = 2
	pairs      = 3
	rate_limit = 4


		
class Nsid(str):
	""" OpenC2 Namespace Identifier

		Namespace identifiers are described in Sec. 3.1.4. This class implements the required
			controls on the string length.
	"""
	def __init__(self, nsid):
		""" Initialize `Nsid`

			:param nsid: Text string (must be more than 1 and less than 16 characters.
		"""
		if len(nsid) > 16 or len(nsid) < 1:
			raise ValueError("Nsid must be between 1 and 16 characters")
		self = nsid

	@classmethod
	def fromdict(cls, name, e):
		""" Create `Nsid` instance

			Create `Nsid` instance from string.
			This method is provided to deserialize an OpenC2 message according to the openc2lib approach.
			This method should only be used internally the openc2lib.
			:param name: Text string with the namespace identifier..
			:param e: `Encoder` instance to be used (only included to be compliance with the function footprint.
			:return: `Version` instance.
		"""
		return Nsid(name)
	
class ResponseType(Enumerated):
	""" OpenC2 Response-Type

		Enumerates the Response-Types according to Sec. 3.4.2.15.	
	"""	
	none=0
	ack=1
	status=2
	complete=3

class TargetEnum(Enumerated):
	""" OpenC2 Targets names
	
		The Language Specification defines a *Targets* subtypes only used in Sec. 3.4.2.1.
		The openc2lib uses this class to keep a record of all registered Target names, while
		the *Targets* type is never defined (it is build in an unnamed way to create the 
		`ActionTargets`.

		This class is only expected to be used internally by the openc2lib.
	"""
	def __repr__(self):
		return self.name

class ActionTargets(MapOf(Actions, ArrayOf(TargetEnum))):
	""" OpenC2 Action-Targets

		Map of each action supported by an actuator to the list of targets applicable to 
		that action (Sec. 3.4.2.1).
		They must be defined by each Profile.
	"""
	pass

class ActionArguments(MapOf(Actions, ArrayOf(str))):
	""" OpenC2 Action-Arguments mapping

		Map of each action supported by an actuator to the list of arguments applicable to
		that action. 
		This is not defined in the Language Specification, but used e.g., by the SLPF Profile.
	"""
	pass
