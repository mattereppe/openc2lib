""" Encoder base functions and interface

	This module provides base encoding functions to translate openc2lib objects into an intermediary
	representation.
"""

import copy
import aenum
import enum
import logging

logger = logging.getLogger(__name__)
""" Logging features

	Most of logging from this modules are conceived for debugging only.
"""

_UNCODED = (bool, str, int, float)
""" Basic types that do not need further encoding """
_NOTSTRING = (bool, int, float)
""" Types that must not be converted to strings """

class EncoderError(Exception):
	pass

class Encoders(aenum.Enum):
	""" List of available Encoders
	
		This list can be used in `Transfer` protocols to select the correct class to decode an incoming OpenC2 Message
		based on its metadata. The list is created as enumeration, which associate the name of the encoding
		formats to the class that implements it.
	"""
	pass

def register_encoder(cls):
	""" Register an `Encoder`

		This function is used to register a new `Encoder`. It can be used as a decorator to the class that 
		defines the new `Encoder`.
		:param cls: The class definition that must be registered. The class internally holds its name.
		:return: The same class passed as argument (used to create a decoratetor).
	"""
	aenum.extend_enum(Encoders, cls.getName(), cls)
	return cls

@register_encoder
class Encoder:
	""" Base `Encoder`

		The Base `Encoder` provides a common interface that must be implemented by all implementations of
		Encoding mechanisms. Each new `Encoder` should be derived from this class.

		The Base Encoder translates openc2lib data types and structures
		into dictionaries. This function can be used by derived class to have an intermediary representation
		which strictly follows the OpenC2 formatting rules. The intermediary representation must then be
		translated into the specific syntax used by the derived `Encoder` (e.g., json, xml, yaml).

		Currently, this class is only designed to encode into text formats.
	"""
	encoder_type = 'dictionary'

	@classmethod
	def getName(cls):
		""" Encoder name

			This method MUST be implemented to return the name of the encoding format. The name should be
			highly representative, possible using official terminology (e.g.: json, xml).

			:return: The class name.
		"""
		return cls.encoder_type

	@staticmethod
	def encode(obj):
		""" Encode an OpenC2 object

			This method encodes an openc2lib object (namely, a data structure derived from `BaseType`). 
			It MUST be implemented by each derived class. It could be applied to any openc2lib object,
			but the most common use is for `Message`, `Command`, or `Response`.

			:param obj: An OpenC2 object derived from a `BaseType`. 
			:return: A string that contains the encoded object.
		"""
		return str(Encoder.todict(obj))

	@staticmethod
	def decode(msgtype, msg):
		""" Decode into OpenC2 object

			This method decodes a text representation into an openc2lib object. The method throws an `Exception`
			in case of unknown elements. 

			This method requires to specify the openc2lib class that implements the OpenC2 object described
			by the text. This will commonly be either `Message`, `Command`, or `Response`. 

			:param msgtype: The class of an openc2lib object.
			:param msg: Text-based representation of the OpenC2 object.
			:return: An instance of an openc2lib object.
		"""
		return Encoder.fromdict(msgtype, msg)

	@staticmethod
	def __objtodict(obj):
		if isinstance(obj, list):
			return Encoder.__iteratelist(obj)

		if isinstance(obj, dict):
			return  Encoder.__iteratedic(obj)

		if isinstance(obj, _NOTSTRING):
			return obj

		# Default: return a string representation of the object
		return str(obj)


	# This method 
	def __objfromdict(clstype, dic):
		if isinstance(dic, dict):
			return clstype(**dic)
		if isinstance(dic, list):
			lis = []
			for i in dic:
				lis.append[Encoder.fromdict(clstype, i)]
			return lis
		if isinstance(dic, _UNCODED):
			return clstype(dic)
		raise ValueError("Unmanaged obj value: ", dic)

	# Convert complex types to string by interatively invoking the todict function
	@staticmethod
	def __iteratedic(dic):
		newdic = {}
		for k,v in dic.items():
			if v is not None:
				newdic[Encoder.todict(k)] = Encoder.todict(v)
		return newdic

	@staticmethod
	def __iteratelist(lis):
		objlist = []
		for i in lis:
			objlist.append( Encoder.todict(i) )
		return objlist	

	@staticmethod
	def todict(obj):
		""" Convert object to dictionary

			This is an internal method to convert an openc2lib object into a dictionary. The dictionary is
		  	structured according to OpenC2 syntax.

			This method should only be invoked by derived classes to get the intermediary representation
			of openc2lib objects. It will likely be used in the implementation of the `decode` method.	
			:param obj: The openc2lib object to convert into a dictionary.
			:return: A dictionary compliant with the OpenC2 syntax rules.
		"""
		try:
			return obj.todict(Encoder)
		except AttributeError:
			return Encoder.__objtodict(obj)
			

	@staticmethod
	def fromdict(clstype, dic):
		""" Create an object from dictionary

			This is an internal method to create an openc2lib object from a dictionary. The dictionary
			must be compliant with the OpenC2 syntax rules. Derived classes are expected to create this
			intermediate representation and use this method in the `encode` method. It is necessary to 
			provide the class definition of the openc2lib object to be instantiated.

			:param clstype: The class definition that must be used to instantiate the object.
			:param dic: The dictionary with the OpenC2 description.
			:return: An instance of `clstype` initialized with the data in the `dic`.
		"""
		logger.debug("Decondig: %s with %s", dic, clstype)
		try:
			logging.debug("Trying: %s", clstype.fromdict)
			return clstype.fromdict(dic, Encoder)
		except AttributeError:
			logger.debug("Falling back: Encoder.objfromdict for %s", clstype)
			return Encoder.__objfromdict(clstype, dic)
		except Exception as e:
			logger.warning("Unable to decode: %s. Returning EncoderError due to: %s", str(dic), type(e).__name__)
			raise EncoderError("Invalid message")
		

