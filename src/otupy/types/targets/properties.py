from otupy.types.base import ArrayOf
from otupy.core.target import target

@target('properties')
class Properties(ArrayOf(str)):
	""" OpenC2 Properties

		Implements the `properties` target (Section 3.4.1.16). 
		Data attribute associated with an Actuator: a list of names that uniquely identify its properties.
	"""
	pass
