#
# Definition of the base types in the OpenC2 DataModels.
# Each OpenC2 object must derive from these classes, which
# affects serialization operations
#

import aenum
import inspect


# Maybe this is not necessary. Old stuff
#
#BaseTypes = list()
#
#def register_basetype(cls):
#	if not cls in BaseTypes:
#		BaseTypes.append(cls)
#	return cls
#
#
## Check whether the given object is derived from OpenC2 base types
#def isbasetype(clstype):
#	print(clstype)
#	for cls in clstype.mro():
#		if cls in openc2.basetypes.BaseTypes:
#			return True
#	return False

class Openc2Type():
	pass


#@register_basetype
class Record(Openc2Type):
	def todict(self, e):
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
		# Retrieve class type for each field in the dictionary
		fielddesc = None
		for tpl in inspect.getmembers(clstype):
			if tpl[0] == '__annotations__':
				fielddesc = tpl[1]

		for k,v in dic.items():
			if k not in fielddesc:
				raise Exception("Unknown field '" + k + "' from message")
			dic[k] = e.fromdict(fielddesc[k], v)
		
		# A record should always have more than one field, so the following statement 
		# should not raise exceptions
		return clstype(**dic)



#@register_basetype
class Choice(Openc2Type):
	choice: str = None
	obj = None

	@staticmethod
	def getClass(choice):
		pass

	def todict(self, e):
		# In case of Choice, the specific choice may be the implementation of an additional type,
		# which affects its representation. So, first of all, get the representation of the inner
		# data type
		dic = {}
		dic[self.choice] = e.todict(self.obj)
		return dic

	@classmethod
	def fromdict(cls, dic, e):
		if not len(dic) == 1:
			raise ValueError("Unexpected dict: ", dic)

		for k, v in dic.items():
			# Expected to run one time only!
			objtype = cls.getClass(k)
			return e.fromdict(objtype, v)

#@register_basetype
class Enumerated(Openc2Type, aenum.Enum):

	# Convert enumerations to str
	def todict(self, e):
		return self.name

	@classmethod
	def fromdict(cls, dic, e):
		try:
			return cls[str(dic)]
		except:
			raise TypeError("Unexpected enum value: ", dic)

#@register_basetype
class EnumeratedID(Openc2Type):
	pass

#@register_basetype
class Array(Openc2Type):
	def todict(self):
		for i in self:
			lis.append = e.todict(i)
		return lis

