import openc2lib.types.base
from openc2lib.profiles.ctxd.data.server import Server
from openc2lib.types.data.l4_protocol import L4Protocol
from openc2lib.profiles.ctxd.data.transfer import Transfer
from openc2lib.profiles.ctxd.data.encoding import Encoding

class Consumer(openc2lib.types.base.Record):
	"""Consumer
    consumer connected on the other side of the link
	"""
	server: Server = None
	""" Hostname or IP address of the server """
	port: int = None
	""" port used to connect to the actuator """
	protocol: L4Protocol = None
	""" protocol used to connect to the actuator """
	endpoint: str = None
	""" path to the endpoint (.../.well-known/openc2) """
	transfer: Transfer = None
	""" transfer protocol used to connect to the actuator """
	encoding: Encoding = None
	""" encoding format used to connect to the actuator """	

	def __init__(self, server:Server = None, port:int = None, protocol:L4Protocol = None, endpoint:str = None, transfer:Transfer = None, encoding:Encoding = None):
		self.server = server if server is not None else None
		self.port = port if port is not None else None
		self.protocol = protocol if protocol is not None else None
		self.endpoint = endpoint if endpoint is not None else None
		self.transfer = transfer if transfer is not None else None
		self.encoding = encoding if encoding is not None else None
		self.validate_fields()

	def __repr__(self):
		return (f"Consumer(server={self.server}, port={self.port}, protocol='{self.protocol}'"
	             f"endpoint={self.endpoint}, transfer={self.transfer}, encoding='{self.encoding}')")
	
	def __str__(self):
		return f"Consumer(" \
	            f"server={self.server}, " \
	            f"port={self.port}, " \
	            f"protocol={self.protocol}, " \
	            f"endpoint={self.endpoint}, " \
				f"transfe={self.transfer}, " \
	            f"encoding={self.encoding})"

	def validate_fields(self):
		if self.server is not None and not isinstance(self.server, Server):
			raise TypeError(f"Expected 'server' to be of type {Server}, but got {type(self.server)}")
		if self.port is not None and not isinstance(self.port, int):
			raise TypeError(f"Expected 'port' to be of type {int}, but got {type(self.port)}")		
		if self.protocol is not None and not isinstance(self.protocol, L4Protocol):
			raise TypeError(f"Expected 'protocol' to be of type {L4Protocol}, but got {type(self.protocol)}")
		if self.endpoint is not None and not isinstance(self.endpoint, str):
			raise TypeError(f"Expected 'endpoint' to be of type {str}, but got {type(self.endpoint)}")
		if self.transfer is not None and not isinstance(self.transfer, Transfer):
			raise TypeError(f"Expected 'transfer' to be of type {Transfer}, but got {type(self.transfer)}")
		if self.encoding is not None and not isinstance(self.encoding, Encoding):
			raise TypeError(f"Expected 'encoding' to be of type {Encoding}, but got {type(self.encoding)}")


