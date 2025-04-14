from otupy.types.base import Enumerated

class Feature(Enumerated):
	""" OpenC2 Feature

		An enumeration for the fields that can be included in the `Results` (see Sec. 3.4.2.4).
	"""
	versions   = 1
	profiles   = 2
	pairs      = 3
	rate_limit = 4

	@classmethod
	def _missing_(cls, value):
		""" Allow retrieving enum by string

			This method extends the basic Enum() method that does not really create an instance,
			but returns a value already initialized. The basic Enum() only works with numbers,
			but I want to make it working with strings as well (which are much more common in 
			otupy usage).

			This method allows you to instantiate a Feature by either calling `Feature(Feature.versions)`
			or `Feature("versions")`.

			You shall not call this function directly.
		"""
		if isinstance(value, str):
			return cls[value]
		else:
		 	return super()._missing_(value)
