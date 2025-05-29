import otupy.types.base
from otupy.profiles.ctxd.data.name import Name
from otupy.profiles.ctxd.data.consumer import Consumer
from otupy.profiles.ctxd.data.peer_role import PeerRole

class Peer(otupy.types.base.Record):
	"""Peer
    Service connected on the other side of the link
	"""
	
	service_name: Name = None
	""" Id of the service """
	role: PeerRole = None
	""" Role of this Peer in the link """
	consumer: Consumer = None
	""" Consumer connected on the other side of the link """


	def __init__(self, service_name:Name = None, role:PeerRole = None, consumer:Consumer = None):
		if(isinstance(service_name, Peer)):
			self.service_name = service_name.service_name if service_name.service_name is not None else None
			self.role = service_name.role if service_name.role is not None else None
			self.consumer = service_name.consumer if service_name.consumer is not None else None	
		else:
			self.service_name = service_name if service_name is not None else None
			self.role = role if role is not None else None
			self.consumer = consumer if consumer is not None else None
		self.validate_fields()

	def __repr__(self):
		return (f"Peer(service_name={self.service_name}, role={self.role},"
	             f"consumer={self.consumer})")
	
	def __str__(self):
		return f"Peer(" \
	            f"service_name={self.service_name}, " \
				f"role={self.role}, " \
	            f"consumer={self.consumer})"

	def validate_fields(self):
		if self.service_name is not None and not isinstance(self.service_name, Name):
			raise TypeError(f"Expected 'service_name' to be of type {Name}, but got {type(self.service_name)}")
		if self.role is not None and not isinstance(self.role, PeerRole):
			raise TypeError(f"Expected 'role' to be of type {PeerRole}, but got {type(self.role)}")		
		if self.consumer is not None and not isinstance(self.consumer, Consumer):
			raise TypeError(f"Expected 'consumer' to be of type {Consumer}, but got {type(self.consumer)}")