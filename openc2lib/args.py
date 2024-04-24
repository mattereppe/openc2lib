import logging

from openc2lib.datatypes import DateTime, Duration, ResponseType
from openc2lib.basetypes import Map
from openc2lib.profile import Profiles

logger = logging.getLogger('openc2lib')

class Args(Map):
	fieldtypes = dict(start_time= DateTime, stop_time= DateTime, duration= Duration, response_requested= ResponseType)

	# This is re-defined here to manage extended Argument namespaces 
	# (see pages 23-24 of the specification)
	def todict(self, e):
		newdic=dict()
		for k,v in self.items():
			if k not in self.fieldtypes:
				raise ValueError('Unknown field: ', k)
			if k in Args.fieldtypes:
				# k is part of the core Arguments types
				newdic[k] = v
			else:
				# k is an extension part of a profile
				newdic[self.nsid]={k:v}
					
		return e.todict(newdic)

	@classmethod
	def __itemfromdict(cls, k, v, e):
		print("Now processing: ", k, v, ' with ', cls)
		if k not in cls.fieldtypes:
			raise TypeError("Unexpected field: ", k)
		return e.fromdict(cls.fieldtypes[k], v)

	@classmethod
	def fromdict(cls, dic, e):
		objdic = {}
		extargs = None
		logger.debug('Building %s from %s in Args', cls, dic)
		for k,v in dic.items():
			if k in ExtendedArguments:
				logger.debug('Using profile %s to decode: %s', k, v)
				extargs = ExtendedArguments[k]
				for l,w in v.items():
					objdic[l] = extargs.__itemfromdict(l, w, e) 
			else:
				objdic[k] = cls.__itemfromdict(k, v, e)

		if extargs is not None:
			cls = extargs

		return cls(objdic)

class ExtArgsDict(dict):
	def add(self, profile: str, extargs):
		if profile in self:
			raise ValueError("ExtArgs already registered")
		self[profile] = extargs
	
ExtendedArguments = ExtArgsDict()

