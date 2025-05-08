import ipaddress

import openc2lib.types.data
from openc2lib.core.target import target

@target('ipv4_net')
class IPv4Net:
    """OpenC2 IPv4 Address Range
        
        IPv4 Address Range as defined in Sec. 3.4.1.9.

        The Standard is not clear on this part. The 
        IPv4Net Target is defined as "Array /ipv4-net"
        (where ipv4-net --lowercase!-- is never defined!)
        However, the json serialization requirements explicitely
        define:
        Array /ipv4-net: JSON string containing the text representation 
                                 of an IPv4 address range as specified in 
                                 [RFC4632], Section 3.1.
        According to this definition, I assume a single network address
        should be managed. Extension to an array of IP network addresses
        is rather straightforward by using a list for ipv4_net attribute.
        Note that I have to keep both the string representation of the
        network address as well as the IPv4Network object to easily 
        manage the code and to automate the creation of the dictionary.
        
    """
#ipv4_net: str
    
    def __init__(self, ipv4_net=None, prefix=None):
        """ Initialize IPv4 Address Range

            Initialize `IPv4Net with IPv4 address and prefix.
            If no IPv4 address is given, initialize to null address.
            If no prefix is given, assume /32 (iPv4 address only).
            :param ipv4_net: IPv4 Network Address.
            :param prefix: IPv4 Network Adress Prefix.
        """
        if ipv4_net is None:
            net = ipaddress.IPv4Network("0.0.0.0/0")
        elif prefix is None:
            net = ipaddress.IPv4Network(ipv4_net)
        else:
            tmp = ipv4_net + "/" + str(prefix)
            net = ipaddress.IPv4Network(tmp)

        self.__ipv4_net = net.exploded
    
    def addr(self):
        """ Returns address part only (no prefix) """
        return ipaddress.IPv4Network(self.__ipv4_net).network_address.exploded
    
    def prefix(self):
        """ Returns prefix only """
        return ipaddress.IPv4Network(self.__ipv4_net).prefixlen
    
    def __str__(self):
        return ipaddress.IPv4Network(self.__ipv4_net).exploded
    
    def __repr__(self):
        return ipaddress.IPv4Network(self.__ipv4_net).exploded

