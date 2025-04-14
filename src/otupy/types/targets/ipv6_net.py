import ipaddress

from otupy.core.target import target

@target('ipv6_net')
class IPv6Net:
	"""OpenC2 IPv6 Address Range
		
		IPv6 Address Range as defined in Sec. 3.4.1.9.

		The Standard is not clear on this part. The 
		IPv6Net Target is defined as "Array /ipv6-net"
		(where ipv6-net --lowercase!-- is never defined!)
		However, the json serialization requirements explicitely
		define:
		Array /ipv6-net: JSON string containing the text representation 
		 						of an IPv6 address range as specified in 
		 						[RFC4291], Section 2.3.
		According to this definition, I assume a single network address
		should be managed. Extension to an array of IP network addresses
		is rather straightforward by using a list for ipv6_net attribute.
		Note that I have to keep both the string representation of the
		network address as well as the IPv6Network object to easily 
		manage the code and to automate the creation of the dictionary.
		
	"""
	
	def __init__(self, ipv6_net=None, prefix=None):
		""" Initialize IPv6 Address Range

			Initialize `IPv6Net with IPv6 address and prefix.
			If no IPv6 address is given, initialize to null address.
			If no prefix is given, assume /128 (IPv6 address only).
			:param ipv6_net: IPv6 Network Address.
			:param prefix: IPv6 Network Adress Prefix.
		"""
		if ipv6_net is None:
		    net = ipaddress.IPv6Network("::/0")
		elif prefix is None:
		    net = ipaddress.IPv6Network(ipv6_net)
		else:
		    tmp = ipv6_net + "/" + str(prefix)
		    net = ipaddress.IPv6Network(tmp)

		self.__ipv6_net = net.exploded
	
	def addr(self):
		""" Returns address part only (no prefix) """
		return ipaddress.IPv6Network(self.__ipv6_net).network_address.exploded
	
	def prefix(self):
		""" Returns prefix only """
		return ipaddress.IPv6Network(self.__ipv6_net).prefixlen
	
	def __str__(self):
#return ipaddress.IPv6Network(self.__ipv6_net).exploded
	    return ipaddress.IPv6Network(self.__ipv6_net).compressed
	
	def __repr__(self):
#return ipaddress.IPv6Network(self.__ipv6_net).exploded
	    return ipaddress.IPv6Network(self.__ipv6_net).compressed

