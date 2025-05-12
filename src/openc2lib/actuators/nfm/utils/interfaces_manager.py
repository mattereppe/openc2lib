import psutil, os
from pyroute2 import IPRoute
from openc2lib.profiles.nfm.data.interface import Interface
from openc2lib.types.targets.ipv4_net import IPv4Net
from openc2lib.types.targets.ipv6_net import IPv6Net
from openc2lib.types.targets import MACAddr
from openc2lib.profiles.nfm.data.iface_type import IfaceType
from openc2lib import ArrayOf
from dotenv import load_dotenv
load_dotenv()

allowed_interfaces_str = os.getenv("ALLOWED_INTERFACES", "")
ALLOWED_INTERFACES = [iface.strip() for iface in allowed_interfaces_str.split(",") if iface.strip()]

def get_iface_status(iface_name: str):
    """Get the status of a specified network interface."""
    stats = psutil.net_if_stats().get(iface_name)
    if stats:
        state = "UP" if stats.isup else "DOWN"
        return state
    else:
        return "Unknown"

def get_iface_type(link_info):

    # Kind to IfaceType map
    KIND_TO_IFACE_TYPE = {
        'ether': IfaceType.ether,
        'bridge': IfaceType.bridge,
        'xfrm': IfaceType.ipsec,
        'ipsec': IfaceType.ipsec,
        'l2tp': IfaceType.i2tp,
        'pptp': IfaceType.pptp,
        'ppp': IfaceType.ppp,
        'pppoe': IfaceType.pppoe,
        'pppoa': IfaceType.pppoa,
        'ovn': IfaceType.ovn,
        'tun': IfaceType.ipsec,
        'tap': IfaceType.ipsec,
    }
    kind = None
    for attr in link_info.get('attrs', []):
        if attr[0] == 'IFLA_LINKINFO':
            kind_attrs = dict(attr[1].get('attrs', []))
            kind = kind_attrs.get('IFLA_INFO_KIND')
            break
    return KIND_TO_IFACE_TYPE.get(kind, IfaceType.ether)

def extract_interfaces() -> ArrayOf(Interface):  # type: ignore
    interfaces = []
    ip = IPRoute()
    for link in ip.get_links():
        attrs = dict(link['attrs'])
        name = attrs.get('IFLA_IFNAME')
        if not name:
            continue
        # Only include interfaces from the allowed list
        if name not in ALLOWED_INTERFACES:
            continue
        flags = link.get('flags', 0)
        iface_type = get_iface_type(link)
        mac = attrs.get('IFLA_ADDRESS')
        index = link['index']
        active = get_iface_status(name)

        ipv4_addrs = ArrayOf(IPv4Net)()
        ipv6_addrs = ArrayOf(IPv6Net)()
        for addr in ip.get_addr(index=index):
            family = addr['family']
            prefixlen = addr['prefixlen']
            ip_addr = addr.get_attr('IFA_ADDRESS')
            if family == 2:  # IPv4
                net = IPv4Net("127.0.0.1", 8)
                ipv4_addrs.append(IPv4Net(ip_addr, prefixlen))
            elif family == 10:  # IPv6
                ipv6_addrs.append(IPv6Net(ip_addr,prefixlen))

        iface = Interface(
            name=name,
            description=f"Interface {name}",
            if_id=int(name.replace('eth', '')) if name.startswith('eth') else None,
            ipv4_net=ipv4_addrs if ipv4_addrs else None,
            ipv6_net=ipv6_addrs if ipv6_addrs else None,
            mac_addr=MACAddr(mac) if mac else None,
            iface_type=iface_type,
            active=active
        )

        interfaces.append(iface)

    return ArrayOf(Interface)(interfaces)