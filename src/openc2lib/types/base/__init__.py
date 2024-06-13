""" OpenC2 structures

	Definition of the base types (structures) in the OpenC2 DataModels (Sec. 3.1.1)
	Each OpenC2 object must derive from these classes, which
	affects serialization operations

"""


from openc2lib.types.base.binary import Binary
from openc2lib.types.base.binary_x import Binaryx
from openc2lib.types.base.record import Record
from openc2lib.types.base.choice import Choice
from openc2lib.types.base.enumerated import Enumerated
from openc2lib.types.base.enumerated_id import EnumeratedID
from openc2lib.types.base.array import Array
from openc2lib.types.base.array_of import ArrayOf
from openc2lib.types.base.map import Map
from openc2lib.types.base.map_of import MapOf




