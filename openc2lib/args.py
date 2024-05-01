import logging

from openc2lib.datatypes import DateTime, Duration, ResponseType
from openc2lib.basetypes import Map
from openc2lib.profile import Profiles

logger = logging.getLogger('openc2lib')

class ExtArgsDict(dict):
	def add(self, profile: str, extargs):
		if profile in self:
			raise ValueError("ExtArgs already registered")
		self[profile] = extargs
	
ExtendedArguments = ExtArgsDict()

class Args(Map):
	fieldtypes = dict(start_time= DateTime, stop_time= DateTime, duration= Duration, response_requested= ResponseType)
	extend = None
	extns = ExtendedArguments

