""" OpenC2 structures

	Definition of the base types (structures) in the OpenC2 DataModels (Sec. 3.1.1)
	Each OpenC2 object must derive from these classes, which
	affects serialization operations

"""


from otupy.types.base.binary import Binary
from otupy.types.base.binary_x import Binaryx
from otupy.types.base.record import Record
from otupy.types.base.choice import Choice
from otupy.types.base.enumerated import Enumerated
from otupy.types.base.enumerated_id import EnumeratedID
from otupy.types.base.array import Array
from otupy.types.base.array_of import ArrayOf
from otupy.types.base.map import Map
from otupy.types.base.map_of import MapOf




