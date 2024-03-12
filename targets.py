# This module lists the available targets for the base language specification
#

# This should be improved to import all types with a simpler instruction
# (not importing everything)
from openc2.datatypes import IPv4Net, IPv4Connection

# Keep the order given in the Language Specification!
# TODO: add missing items from language specification
Targets = {
	"ipv4_net": IPv4Net,
	"ipv4_connection": IPv4Connection
}

