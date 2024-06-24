""" IPv6 Address

	This module implements an IPv6 Address as described in Sec. 3.4.2.9.

The usage of the ipaddress module is compliant to what required in the
language specification for IPv6 addresses, especially the following points:
a) The IPv6 address should be available both in string and binary form
b) The network representation is an array according to RFC 4291 Sec. 2.3
   (host/prefix, host/mask, host/hostmask, etc.)
"""

import ipaddress

class IPv6Addr:
	"""OpenC2 IPv6 Address"

		This class implements an IPv6 Address as described in Sec. 3.4.2.9.

		The usage of the ipaddress module is compliant to what required in the
		language specification for IPv6 addresses, especially the following points:
		a) The IPv6 address should be available both in string and binary form
		b) The network representation is an array according to RFC 4291 Sec. 2.3
		   (host/prefix, host/mask, host/hostmask, etc.)

"""
	__ipv6_addr = ipaddress.IPv6Address("::")
	""" Internal representation of the IPv6 address"""
	
	def __init__(self, ipaddr=None):
		""" Initialize IPv6 Address 

			An IPv6 address is built from a string that uses the common dotted notation.
			If no IPv6 address is provided, the null address is used ("::").

			:param ipaddr: Quad-dotted representation of the IPv6 address.
		"""
		if ipaddr == None:
			self.__ipv6_addr = ipaddress.IPv6Address("::")
		else:
			self.__ipv6_addr = ipaddress.IPv6Address(ipaddr)

	def __str__(self):
		return self.__ipv6_addr.exploded

	def __repr__(self):
		return self.__ipv6_addr.exploded

