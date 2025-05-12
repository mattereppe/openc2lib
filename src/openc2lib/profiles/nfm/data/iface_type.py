from openc2lib.types.base import Enumerated

class IfaceType(Enumerated):
    """Interface type

    type of the interface
    """

    ether = 1
    bridge = 2
    ipsec = 3
    i2tp = 4
    pptp = 5
    ppp = 6
    pppoe = 7
    pppoa = 8
    ovn = 9