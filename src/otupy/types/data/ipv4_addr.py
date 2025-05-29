""" IPv4 Address

	This module implements an IPv4 Address as described in Sec. 3.4.2.8.

The usage of the ipaddress module is compliant to what required in the
language specification for IPv4 addresses, especially the following points:
a) The IPv4 address should be available both in string and binary form
b) The network representation is an array according to RFC 4632 Sec. 3.1
   (host/prefix, host/mask, host/hostmask, etc.)
"""

import ipaddress

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

