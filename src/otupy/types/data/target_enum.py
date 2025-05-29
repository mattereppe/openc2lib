from otupy.types.base import Enumerated

class TargetEnum(Enumerated):
	""" OpenC2 Targets names
	
		The Language Specification defines a *Targets* subtypes only used in Sec. 3.4.2.1.
		The otupy uses this class to keep a record of all registered Target names, while
		the *Targets* type is never defined (it is build in an unnamed way to create the 
		`ActionTargets`.

		This class is only expected to be used internally by the otupy.
	"""
	def __repr__(self):
		return self.name

