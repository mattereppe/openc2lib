""" Command Arguments

	The definition of the (exendible) arguments of the OpenC2 Command 
	(Sec. 3.3.1.4 of the Language Specification).
"""
import logging

from openc2lib.types.datatypes import DateTime, Duration, ResponseType
from openc2lib.types.basetypes import Map
from openc2lib.core.register import Register
from openc2lib.core.profile import Profiles

logger = logging.getLogger('openc2lib')

ExtendedArguments = Register()
""" List of extensions

	This variable contains all argument extensions registered by Profiles. It is a dictionary which key
	is the profile name, and the value is the `Args` class defined for that Profile.

	Each `Args` definition for a Profile must be registered here to be available for encoding/decoding
	OpenC2 `Message`s.

	Multiple registration of extensions for the same Profile will raise a `ValueError` Exception.

	Usage: see the `Register` interface.	
"""


class Args(Map):
	""" OpenC2 Arguments

		This class defines the base class structure and the common arguments.
		Extensions for specific profiles must be derived from this class by giving the relevant `fieldtypes`, and
		providing the base class and extension type.
	"""
	fieldtypes = dict(start_time= DateTime, stop_time= DateTime, duration= Duration, response_requested= ResponseType)
	""" Allowed arguments

		This is a list of allowed keys and corresponding argument types (classes). The keys and types are set according
		to the Language Specification. This argument defines the syntax for the base Map that builds the
		Args type. There is (currently) no controls on input data; this argument is only used to instantiate
		the Args object from an OpenC2 Message.
	"""
	extend = None
	""" Base class

		This  field must be set to `Args` in all derived classes (i.e., definition of Arguments for specific Profiles).
	"""

	regext = ExtendedArguments
	""" Extension Name Space
	
		This field is for internal use only and must not be modified by any derived class.	
	"""

