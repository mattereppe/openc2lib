from openc2lib.types.base import Choice
from openc2lib.types.data.hostname import  Hostname
from openc2lib.types.data.ipv4_addr import IPv4Addr
from openc2lib.core.register import Register


class Server(Choice):

    #hostname: hostname of the server
	#ipv4_addr: 32 bit IPv4 address as defined in [RFC0791]

	register = Register({'hostname': Hostname, 'ipv4_addr': IPv4Addr})

