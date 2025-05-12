from openc2lib.types.base import Record, ArrayOf, Array
from openc2lib.types.targets.ipv4_net import IPv4Net
from openc2lib.types.targets.ipv6_net import IPv6Net
from openc2lib.types.targets import MACAddr  
from openc2lib.profiles.nfm.data.iface_type import IfaceType 

# str, int, str are used directly

class Interface(Record):
    """
    Interface

    Describes a network interface including addresses, identifiers, and status.
    """

    name: str
    """ Internal mnemonical name of the interface """

    description: str = None
    """ Human-readable description of the interface """

    if_id: int = None
    """ Internal interface index """

    ipv4_net: ArrayOf(IPv4Net) = None  # type: ignore
    """ List of assigned IPv4 addresses (with prefix) """

    ipv6_net: ArrayOf(IPv6Net) = None  # type: ignore
    """ List of assigned IPv6 addresses (with prefix) """

    mac_addr: MACAddr = None # type: ignore
    """ MAC address of the interface """

    iface_type: IfaceType = None
    """ Layer 2 interface type """

    active: str = None
    """ Link status (True = up, False = down) """

    def __init__(
        self,
        name: str,
        description: str = None,
        if_id: int = None,
        ipv4_net: ArrayOf = None,  # type: ignore
        ipv6_net: ArrayOf = None,  # type: ignore
        mac_addr: MACAddr = None, # type: ignore
        iface_type: IfaceType = None,
        active: str = None
    ):
        if name is None or if_id and if_id <0:
            raise ValueError("Interface must be provided")
        elif isinstance(name, Interface):
            self._init_from_interface(name)
        else:
            self._init_from_params(name, description, if_id, ipv4_net, ipv6_net, mac_addr, iface_type, active)
        self.validate_fields()

    def _init_from_interface(self, interface):
        self.name = interface.name
        self.description = interface.description
        self.if_id = interface.if_id
        self.ipv4_net = interface.ipv4_net
        self.ipv6_net = interface.ipv6_net
        self.mac_addr = interface.mac_addr
        self.iface_type = interface.iface_type
        self.active = interface.active

    def _init_from_params(
        self, name, description, if_id, ipv4_net, ipv6_net, mac_addr, iface_type, active
    ):
        self.name = name
        self.description = description
        self.if_id = if_id
        self.ipv4_net = ipv4_net
        self.ipv6_net = ipv6_net
        self.mac_addr = mac_addr
        self.iface_type = iface_type
        self.active = active

    def __repr__(self):
        return (
            f"Interface(name={self.name}, description={self.description}, if_id={self.if_id}, "
            f"ipv4_net={self.ipv4_net}, ipv6_net={self.ipv6_net}, mac_addr={self.mac_addr}, "
            f"iface_type={self.iface_type}, active={self.active})"
        )

    def __str__(self):
        return self.__repr__()

    def validate_fields(self):
        if not any([
            self.name, self.description, self.if_id,
            self.ipv4_net, self.ipv6_net,
            self.mac_addr, self.iface_type, self.active is not None
        ]):
            raise ValueError("At least one field must be set in Interface (Map{1..*})")

        if self.name is not None and not isinstance(self.name, str):
            raise TypeError(f"'name' must be str, got {type(self.name)}")
        if self.description is not None and not isinstance(self.description, str):
            raise TypeError(f"'description' must be str, got {type(self.description)}")
        if self.if_id is not None and not isinstance(self.if_id, int):
            raise TypeError(f"'if_id' must be int, got {type(self.if_id)}")
        if self.ipv4_net is not None and not isinstance(self.ipv4_net, Array):
            raise TypeError(f"'ipv4_net' must be ArrayOf(IPv4Addr), got {type(self.ipv4_net)}")
        if self.ipv6_net is not None and not isinstance(self.ipv6_net, Array):
            raise TypeError(f"'ipv6_net' must be ArrayOf(IPv6Addr), got {type(self.ipv6_net)}")
        if self.mac_addr is not None and not isinstance(self.mac_addr, MACAddr):
            raise TypeError(f"'mac_addr' must be MACAddr, got {type(self.mac_addr)}")
        if self.iface_type is not None and not isinstance(self.iface_type, IfaceType):
            raise TypeError(f"'iface_type' must be IfaceType, got {type(self.iface_type)}")
        if self.active is not None and not isinstance(self.active, str):
            raise TypeError(f"'active' must be str, got {type(self.active)}")
