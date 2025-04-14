from otupy.types.base import Enumerated

class LinkType(Enumerated):
    """Link-Type

    type of the link
    """

    api = 1
    hosting = 2
    packet_flow = 3
    control = 4
    protect = 5