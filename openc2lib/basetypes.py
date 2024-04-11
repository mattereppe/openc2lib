#
# Definition of the base types in the OpenC2 DataModels.
# Each OpenC2 object must derive from these classes, which
# affects serialization operations
#

import aenum
import inspect


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
	
# This class should check the names are integers.
# The enum syntax only allows to define <str = int> pairs,
# so to use this class it is necessary to define mnemonic label
# TODO: Test this code
class EnumeratedID(Enumerated):

	def todict(self, e):
		return int(self.value)

	@classmethod
	def fromdict(cls, dic, e):
		try:
			return cls[int(dic)]
		except:
			raise TypeError("Unexpected enum value: ", dic)

#@register_basetype
class Array(Openc2Type, list):
	fieldtypes = None

	def todict(self, e):
		lis = []
		for i in self:
			lis.append = e.todict(i)
		return lis

# TODO: fromdict???
# Currently not implemented because there are no examples of usage of this
# type (only Array/net, which is not clear)
	def fromdict(cls, dic, e):
		raise Exception("Function not implemented")

# One might like to check the type of the elements before inserting them.
# However, this is not the Python-way. Python use the duck typing approach:
# https://en.wikipedia.org/wiki/Duck_typing
# We ask for the type of objects just to keep this information according to
# the OpenC2 data model.
class ArrayOf:

	def __new__(self, fldtype):
		class ArrayOf(Array):
			fieldtype = fldtype

			@classmethod
			def fromdict(cls, lis, e):
				objlis = cls()
				print("ArrayOf: ", lis)
				print("Instantiating: ", cls.fieldtype)
				for k in lis:
					objlis.append(e.fromdict(cls.fieldtype, k))
		
				return objlis
			
			# This is the code if I would like to do type checking
			# when inserting data
#			def append(self, item):
#				if isinstance(item, self.fieldtype):
#					super().append(item)
#				else:
#					raise ValueError(self.fieldtype,' allowed only')
#			
#			def insert(self, index, item):
#				if isinstance(item, self.fieldtype):
#					super().insert(index, item)
#				else:
#					raise ValueError(self.fieldtype,' allowed only')
#			
#			def __add__(self, item):
#				if isinstance(item, self.fieldtype):
#					super().__add__(item)
#				else:
#					raise ValueError(self.fieldtype,' allowed only')
#			
#			def __iadd__(self, item):
#				if isinstance(item, self.fieldtype):
#					super().__iadd__(item)
#				else:
#					raise ValueError(self.fieldtype,' allowed only')

		return ArrayOf


class Map(Openc2Type, dict):
	fieldtypes: dict = None

	def todict(self, e):
		return e.todict(dict(self))

	@classmethod
	def fromdict(cls, dic, e):
		objdic = {}
		print("dicitems: ", dic.items())
		for k,v in dic.items():
			print("k: ",k)
			print("fieldtypes: ", cls.fieldtypes)
			if k not in cls.fieldtypes:
				raise TypeError("Unexpected field: ", k)
			objdic[k] = e.fromdict(cls.fieldtypes[k], v)
			print("objdic[k]", objdic)

#return cls(objdic)
		return objdic

class MapOf:

	def __new__(self,ktype, vtype):
		class MapOf(Map):
			fieldtypes = {ktype: vtype}

			@classmethod
			def fromdict(cls, dic, e):
				objdic = {}
				print("MapOf dicitems: ", dic.items())
				for k,v in dic.items():
					print("k: ",k)
					print("fieldtypes: ", cls.fieldtypes)
					kclass = list(cls.fieldtypes)[0]
					objk = e.fromdict(kclass, k)
					
					print("MapOf k type: ", type(objk))
					print("MapOf v type: ", type(cls.fieldtypes[kclass]))
					objdic[objk] = e.fromdict(cls.fieldtypes[kclass], v)
					print("objdic[k]", objdic)
				return objdic

		return MapOf

