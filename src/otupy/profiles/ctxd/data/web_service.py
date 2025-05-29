import otupy.types.base
from otupy.profiles.ctxd.data.server import Server

class WebService(otupy.types.base.Record):
	
	"""WebService
    it is the description of the service - WebService
	"""
	description: str = None
	""" Generic description of the web service """
	server: Server = None
	""" Hostname or IP address of the server """
	port: int = None
	""" The port used to connect to the web service"""
	endpoint: str = None
	""" The endpoint used to connect to the web service"""
	owner: str = None
	""" Owner of the web service"""

	def __init__(self, description = None, server = None, port = None, endpoint = None, owner = None):
		self.description = description if description is not None else None
		self.server = server if server is not None else None
		self.port = port if port is not None else None
		self.endpoint = endpoint if endpoint is not None else None
		self.owner = owner if owner is not None else None

	def __repr__(self):
		return (f"WebService(description={self.description}, server={self.server}, "
	             f"port={self.port}, endpoint={self.owner},owner={self.owner})")
	
	def __str__(self):
		return f"Webservice(" \
	            f"description={self.description}, " \
	            f"server={self.server}, " \
	            f"port={self.port}, " \
				f"endpoint={self.endpoint}, " \
	            f"owner={self.owner})"

	def validate_fields(self):
		if self.description is not None and not isinstance(self.description, str):
			raise TypeError(f"Expected 'description' to be of type str, but got {type(self.description)}")
		if self.server is not None and not isinstance(self.server, Server):
			raise TypeError(f"Expected 'server' to be of type Server, but got {type(self.server)}")
		if self.port is not None and not isinstance(self.port, int):
			raise TypeError(f"Expected 'port' to be of type int, but got {type(self.port)}")
		if self.endpoint is not None and not isinstance(self.endpoint, str):
			raise TypeError(f"Expected 'endpoint' to be of type {str}, but got {type(self.endpoint)}")
		if self.owner is not None and not isinstance(self.owner, str):
			raise TypeError(f"Expected 'owner' to be of type {str}, but got {type(self.owner)}")