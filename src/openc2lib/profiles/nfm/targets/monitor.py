import openc2lib as oc2
from openc2lib.profiles.nfm.profile import Profile  # Assuming this exists
from openc2lib.types.base import ArrayOf, Array
from openc2lib.types.targets import IPv4Connection, IPv6Connection
from openc2lib.profiles.nfm.data.interface import Interface  # Assuming the path exists
from openc2lib.profiles.nfm.data.ie import IE  # Assuming the path exists

# Target for FlowMonitor Configuration
@oc2.target(name='monitor', nsid=Profile.nsid)
class FlowMonitor(oc2.types.base.Record):
    """
    FlowMonitor

    Represents a monitoring system capable of handling flow data.
    """

    interfaces: ArrayOf(Interface) = None  # type: ignore
    """ Interfaces capable of running monitoring agents """

    information_elements: ArrayOf(IE) = None  # type: ignore
    """ NetFlow/IPFIX Information Elements """

    filter_v4: ArrayOf(IPv4Connection) = None  # type: ignore
    """ List of IPv4 addresses assigned to the interface (including prefix) """

    filter_v6: ArrayOf(IPv6Connection) = None  # type: ignore
    """ List of IPv6 addresses assigned to the interface (including prefix) """

    def __init__(self, interfaces: ArrayOf = None, information_elements: ArrayOf = None,
                 filter_v4: ArrayOf = None, filter_v6: ArrayOf = None):  # type: ignore
        if isinstance(interfaces, FlowMonitor):
            self._init_from_flowmonitor(interfaces)
        else:
            self._init_from_params(interfaces, information_elements, filter_v4, filter_v6)
        self.validate_fields()

    def _init_from_flowmonitor(self, flowmonitor):
        self.interfaces = flowmonitor.interfaces
        self.information_elements = flowmonitor.information_elements
        self.filter_v4 = flowmonitor.filter_v4
        self.filter_v6 = flowmonitor.filter_v6

    def _init_from_params(self, interfaces, information_elements, filter_v4, filter_v6):
        self.interfaces = interfaces
        self.information_elements = information_elements
        self.filter_v4 = filter_v4
        self.filter_v6 = filter_v6

    def __repr__(self):
        return f"FlowMonitor(interfaces={self.interfaces}, information_elements={self.information_elements}, " \
               f"filter_v4={self.filter_v4}, filter_v6={self.filter_v6})"

    def __str__(self):
        return self.__repr__()

    def validate_fields(self):
        if not any([self.interfaces, self.information_elements, self.filter_v4, self.filter_v6]):
            raise ValueError("At least one field must be set in FlowMonitor (Record{0..*})")

        if self.interfaces is not None and not isinstance(self.interfaces, Array):
            raise TypeError(f"'interfaces' must be ArrayOf(Interface), got {type(self.interfaces)}")
        if self.information_elements is not None and not isinstance(self.information_elements, Array):
            raise TypeError(f"'information_elements' must be ArrayOf(IE), got {type(self.information_elements)}")
        if self.filter_v4 is not None and not isinstance(self.filter_v4, Array):
            raise TypeError(f"'filter_v4' must be ArrayOf(IPv4Addr), got {type(self.filter_v4)}")
        if self.filter_v6 is not None and not isinstance(self.filter_v6, Array):
            raise TypeError(f"'filter_v6' must be ArrayOf(IPv6Addr), got {type(self.filter_v6)}")
    def get(self, key, default=None):
        """ Mimics dictionary get method """
        return getattr(self, key, default)