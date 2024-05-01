import copy
import aenum
import enum
import logging

logger = logging.getLogger('openc2lib')

UNCODED = (bool, str, int, float)

class Encoders(aenum.Enum):
	pass

def register_encoder(cls):
	aenum.extend_enum(Encoders, cls.getName(), cls)
	return cls

@register_encoder
class Encoder:
	encoder_type = 'dictionary'

	@classmethod
	def getName(cls):
		return cls.encoder_type

	@staticmethod
	def encode(obj):
		return Encoder.todict(obj)

	@staticmethod
	def decode(msgtype, msg):
		return Encoder.fromdict(msgtype, msg)

	@staticmethod
	def objtodict(obj):
		if isinstance(obj, list):
			return Encoder.__iteratelist(obj)

		if isinstance(obj, dict):
			return  Encoder.__iteratedic(obj)

		# Default: return a string representation of the object
		return str(obj)


	# This method 
	def objfromdict(clstype, dic):
		if isinstance(dic, dict):
			return clstype(**dic)
		if isinstance(dic, list):
			lis = []
			for i in dic:
				lis.append[Encoder.fromdict(clstype, i)]
			return lis
		if isinstance(dic, UNCODED):
			return clstype(dic)
		raise ValueError("Unmanaged obj value: ", dic)

	# Convert complex types to string by interatively invoking the todict function
	@staticmethod
	def __iteratedic(dic):
		newdic = {}
		for k,v in dic.items():
			if v is not None:
				newdic[Encoder.todict(k)] = Encoder.todict(v)
#			if not isinstance(v, UNCODED):
#				dic[k] = Encoder.todict(v)
		return newdic

	@staticmethod
	def __iteratelist(lis):
		objlist = []
		for i in lis:
#			if isinstance(i, UNCODED):
#				objlist.append(i)
#			else:
#				print("append: ", i)
#				objlist.append( Encoder.todict(i) )
			objlist.append( Encoder.todict(i) )
		return objlist	

	@staticmethod
	def hasmethod(obj, method):
		return callable(hasattr(obj, method, None))


	# The main entry point to convert an OpenC2 object to
	# a dictionary
	@staticmethod
	def todict(obj):
		try:
			return obj.todict(Encoder)
		except AttributeError:
			return Encoder.objtodict(obj)
			

	# The entry point to translate a dictionary to an object
	# dic is the dictionary with values
	# clstype is the classtype to use for the conversion
	@staticmethod
	def fromdict(clstype, dic):
		logger.debug("Decondig: %s with %s", dic, clstype)
		try:
			logging.debug("Trying: %s", clstype.fromdict)
			return clstype.fromdict(dic, Encoder)
		except AttributeError:
			logger.debug("Falling back: Encoder.objfromdict for %s", clstype)
			return Encoder.objfromdict(clstype, dic)
		

