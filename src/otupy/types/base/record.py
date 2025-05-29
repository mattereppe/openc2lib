import inspect
import logging

from otupy.types.base.openc2_type import Openc2Type

logger = logging.getLogger(__name__)

class Record(Openc2Type):
	""" OpenC2 Record

		Implements OpenC2 Record: 
			>An ordered map from a list of keys with positions to values with 
			positionally-defined semantics. Each key has a position and name, 
			and is mapped to a type.

		It expect keys to be public class attributes. All internal attributes 
		must be kept private by prefixing it with an '_'.

	"""
	def todict(self, e):
		""" Converts to dictionary 
		
			It is used to convert this object to an intermediary representation during 
			serialization. It takes an `Encoder` argument that is used to recursively
			serialize inner data and structures (the `Encoder` provides standard methods
			for converting base types to dictionaries).. 

			:param e: The `Encoder` that is being used.
			:return: A dictionary compliants to the Language Specification's serialization
			rules.
		"""
		objdic = vars(self)

		dic = {}
		for k,v in objdic.items():
			# Fix keywords corresponding to variable names that clash with Python keywords
			if isinstance(k, str) and k.endswith('_'):
				k = k.rstrip('_')
			# Remove empty and private elements; do not include non-string keys
			if not v is None and not k.startswith('_') and isinstance(k, str):
				dic[k] = v	

		return e.todict(dic)

	@classmethod
	def fromdict(clstype, dic, e):
		""" Builds instance from dictionary 

			It is used during deserialization to create an otupy instance from the text message.
			It takes an `Encoder` instance that is used to recursively build instances of the inner
			objects (the `Encoder` provides standard methods to create instances of base objects like
			strings, integers, boolean).

			:param dic: The intermediary dictionary representation from which the object is built.
			:param e: The `Encoder that is being used.
			:return: An instance of this class initialized from the dictionary values.
		"""
		objdic = {}
		# Retrieve class type for each field in the dictionary
		fielddesc = None
		logger.debug("Decondig: %s with %s", dic, clstype)
		for tpl in inspect.getmembers(clstype):
			if tpl[0] == '__annotations__':
				fielddesc = tpl[1]

		
		if not isinstance(dic, dict):
			raise EncoderError("Invalid data type for Record")
		for k,v in dic.items():
			if k not in fielddesc:
				raise Exception("Unknown field '" + k + "' from message")
			objdic[k] = e.fromdict(fielddesc[k], v)

		# A record should always have more than one field, so the following statement 
		# should not raise exceptions
		try:
			logger.debug("Building %s with %s", clstype, objdic)
			return clstype(**objdic)
		except Exception as e:
			logger.warning("Unable to decode: %s. Returning EncoderError due to: %s", str(dic), type(e).__name__)
			raise EncoderError("Unable to parse message")

