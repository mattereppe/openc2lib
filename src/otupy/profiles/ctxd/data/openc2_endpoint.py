import otupy.types.base
from otupy.profiles.ctxd.data.consumer import Consumer
from otupy.types.data.nsid import Nsid


class OpenC2Endpoint(otupy.types.base.Record):
	"""OpenC2-Endpoint
    Actuator Profile
	"""

	actuator: Nsid = None
	""" It specifies the Actuator Profile """
	consumer: Consumer = None
	""" It specifies the Consumer that implements the security functions"""


	def __init__(self, actuator:Nsid = None, consumer:Consumer = None):
		if(isinstance(actuator, OpenC2Endpoint)):
			self.actuator = actuator.actuator
			self.consumer = actuator.consumer
		else:
			self.actuator = actuator if actuator is not None else None
			self.consumer = consumer if consumer is not None else None
		self.validate_fields()


	def __repr__(self):
		return (f"OpenC2Endpoint(actuator={self.actuator}, "
	             f"consumer={self.consumer})")
	
	def __str__(self):
		return f"OpenC2Endpoint(" \
	            f"actuator={self.actuator}, " \
	            f"consumer={self.consumer})"

	def validate_fields(self):
		if self.actuator is not None and not isinstance(self.actuator, Nsid):
			raise TypeError(f"Expected 'actuator' to be of type {Nsid}, but got {type(self.actuator)}")
		if self.consumer is not None and not isinstance(self.consumer, Consumer):
			raise TypeError(f"Expected 'consumer' to be of type {Consumer}, but got {type(self.consumer)}")		