from openc2lib.types.targets import IPv4Connection, IPv6Connection
from openc2lib import ArrayOf

def generate_bpf_filter(ipv4_connections: ArrayOf(IPv4Connection), ipv6_connections: ArrayOf(IPv6Connection)):  # type: ignore
    connection_filters = []

    def build_conn_filter(conn, is_ipv6=False):
        port_parts = []
        ip_proto = 'ip6' if is_ipv6 else 'ip'
        ports = ""

        # Address filtering
        addr_parts = []
        if conn.src_addr is not None:
            addr_parts.append(f"src net {conn.src_addr}")
        if conn.dst_addr is not None:
            addr_parts.append(f"dst net {conn.dst_addr}")

        # Decide how to prefix IP part
        if addr_parts:
            ip_prefix = f"{ip_proto} " + ' and '.join(addr_parts)
        else:
            ip_prefix = f"{ip_proto}"

        # Ports
        if conn.dst_port is not None:
            port_parts.append(f"dst port {conn.dst_port}")
        if conn.src_port is not None:
            port_parts.append(f"src port {conn.src_port}")

        # Protocol
        proto = conn.protocol.name.lower() if conn.protocol else None
        if proto:
            ports = f"{proto} " + ' and '.join(port_parts) if port_parts else proto
        elif port_parts:
            ports = ' and '.join(port_parts)

        # Combine parts
        full_parts = [ip_prefix]
        if ports:
            full_parts.append(ports)

        return f"({' and '.join(full_parts)})"

    for conn in ipv4_connections:
        connection_filters.append(build_conn_filter(conn, is_ipv6=False))

    for conn in ipv6_connections:
        connection_filters.append(build_conn_filter(conn, is_ipv6=True))

    return ' or '.join(connection_filters)
