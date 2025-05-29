""" Command Arguments

	The definition of the (exendible) arguments of the OpenC2 Command 
	(Sec. 3.3.1.4 of the Language Specification).
"""

from otupy.types.data import DateTime, Duration, ResponseType
from otupy.types.base import Map
from otupy.core.register import Register
from otupy.core.extensions import extensible

@extensible
class Args(Map):
	""" OpenC2 Arguments

		This class defines the base class structure and the common arguments.

		Extensions for specific profiles must be declared with the `@extension` decorator, and the namespace identifier
		must be given as parameter.
		
		Extensions must define the additional fields envisioned by the Profile specification in the `fieldtypes` 
		dictionary.
	"""
	fieldtypes = dict(start_time= DateTime, stop_time= DateTime, duration= Duration, response_requested= ResponseType)
	""" Allowed arguments

		This is a list of allowed keys and corresponding argument types (classes). The keys and types are set according
		to the Language Specification. This argument defines the syntax for the base Map that builds the
		Args type. There is (currently) no controls on input data; this argument is only used to instantiate
		the Args object from an OpenC2 Message.
	"""

