""" OpenC2 target types

	Definition of the target types in the OpenC2 (Sec. 3.4.1).
	The naming strictly follows the definition of the Language Specification
	as close as possible. The relevant exception is represented by hyphens
	that are always dropped.
"""


from openc2lib.core.target import Targets

from openc2lib.types.targets.ipv4_net import IPv4Net
from openc2lib.types.targets.ipv4_connection import IPv4Connection
from openc2lib.types.targets.features import Features



# Register the list of available Targets
Targets.add('features', Features, 9)
Targets.add('ipv4_net', IPv4Net, 13)
Targets.add('ipv4_connection', IPv4Connection, 15)
