import otupy.types.base
from otupy.profiles.ctxd.data.peer import Peer
from otupy.profiles.ctxd.data.link_type import LinkType
from otupy.profiles.ctxd.data.openc2_endpoint import OpenC2Endpoint
from otupy.profiles.ctxd.data.name import Name
from otupy.types.base.array import Array
from otupy.types.base.array_of import ArrayOf
from otupy.core.version import Version


class Link(otupy.types.base.Record):
	"""Link
    Link associated with the service
	"""

	name: Name = None
	""" Id of the link """
	description: str = None
	""" Generic description of the relationship"""
	versions: ArrayOf(Version) = None # type: ignore
	""" Subset of service features used in this relationship (where applicable). E.g.: the version of an API, or of a Network protocol."""
	link_type: LinkType = None
	""" Type of the link"""
	peers: ArrayOf(Peer) = None # type: ignore
	""" Services connected on the link """
	security_functions: ArrayOf(OpenC2Endpoint) = None # type: ignore
	""" security functions applied on the link """

	def __init__(self, name:Name = None, description:str = None, versions:ArrayOf(Version) = None, link_type:LinkType = None, # type: ignore
			   peers:ArrayOf(Peer) = None, security_functions:ArrayOf(OpenC2Endpoint) = None): # type: ignore
		if isinstance(name, Link):
			self._init_from_link(name)
		else:
			self._init_from_params(name, description, versions, link_type, peers, security_functions)
		self.validate_fields()

	def _init_from_link(self, link):
		self.name = link.name if link.name is not None else None
		self.description = link.description if link.description is not None else None
		self.versions = link.versions if link.versions is not None else None
		self.link_type = link.link_type if link.link_type is not None else None
		self.peers = link.peers if link.peers is not None else None
		self.security_functions = link.security_functions if link.security_functions is not None else None

	def _init_from_params(self, name = None, description = None, versions = None, link_type = None, peers = None, security_functions = None):
		self.name = name if name is not None else None
		self.description = description if description is not None else None
		self.versions = versions if versions is not None else None
		self.link_type = link_type if link_type is not None else None
		self.peers = peers if peers is not None else None
		self.security_functions = security_functions if security_functions is not None else None

	def __repr__(self):
		return (f"Link(name={self.name}, "
                 f"description={self.description}, versions={self.versions}, link_type={self.link_type}, peers={self.peers}, "
	             f"security_functions={self.security_functions})")
	
	def __str__(self):
		return f"Link(" \
	            f"name={self.name}, " \
	            f"description={self.description}, " \
				f"versions={self.versions}, " \
				f"link_type={self.link_type}, " \
				f"peers={self.peers}, " \
	            f"security_functions={self.security_functions})"

	def validate_fields(self):
		if self.name is not None and not isinstance(self.name, Name):
			raise TypeError(f"Expected 'name' to be of type {Name}, but got {type(self.name)}")
		if self.description is not None and not isinstance(self.description, str):
			raise TypeError(f"Expected 'description' to be of type {str}, but got {type(self.description)}")
		if self.versions is not None and not isinstance(self.versions, Array):
			raise TypeError(f"Expected 'versions' to be of type {Array}, but got {type(self.versions)}")
		if self.link_type is not None and not isinstance(self.link_type, LinkType):
			raise TypeError(f"Expected 'link_type' to be of type {LinkType}, but got {type(self.link_type)}")
		if self.peers is not None and not isinstance(self.peers, Array):
			raise TypeError(f"Expected 'peers' to be of type {Array}, but got {type(self.peers)}")
		if self.security_functions is not None and not isinstance(self.security_functions, Array):
			raise TypeError(f"Expected 'security_functions' to be of type {Array}, but got {type(self.security_functions)}")
