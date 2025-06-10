#!../.oc2-env/bin/python3
# Example to use the OpenC2 library
#
import hashlib
import logging
import sys
import time
import openc2lib as oc2
from openc2lib.types.data.uri import  URI
from openc2lib.types.targets.file import File
from openc2lib.profiles.nfm.targets.monitor import FlowMonitor 
from openc2lib.profiles.nfm.data.exporter import Exporter 
from openc2lib.profiles.nfm.data.export_options import ExportOptions 
from openc2lib.profiles.nfm.data.collector import Collector 
from openc2lib.profiles.nfm.data.flow_format import FlowFormat 
from openc2lib.types.base import Record, ArrayOf, Array
from openc2lib.types.data import IPv4Addr, IPv6Addr, Port
from openc2lib.types.targets import MACAddr , IPv4Net
from openc2lib.profiles.nfm.data.iface_type import IfaceType 
from openc2lib.profiles.nfm.data.ie import IE  
from openc2lib.profiles.nfm.data.interface import Interface 
from openc2lib.encoders.json import JSONEncoder
from openc2lib.transfers.http import HTTPTransfer
from openc2lib.types.targets import IPv4Connection, IPv6Connection
from openc2lib.types.data.l4_protocol import L4Protocol

import openc2lib.profiles.nfm as nfm
# logging.basicConfig(filename='openc2.log',level=logging.DEBUG)
'''logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger('openc2producer')'''
logger = logging.getLogger()
# Ask for 4 levels of logging: INFO, WARNING, ERROR, CRITICAL
logger.setLevel(logging.INFO)
# Create stdout handler for logging to the console 
stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(oc2.LogFormatter(datetime=True,name=True))

hdls = [ stdout_handler ]
# Add both handlers to the logger
logger.addHandler(stdout_handler)
# Add file logger
file_handler = logging.FileHandler("controller_nfm_app_probe_y.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(oc2.LogFormatter(datetime=True,name=True, datefmt='%t'))
logger.addHandler(file_handler)


def main():
    logger.info("Creating Producer")
    p = oc2.Producer("producer2.example.net",
                     JSONEncoder(),
                     HTTPTransfer("127.0.0.1",
                                  8080))
    pf = nfm.Specifiers({"asset_id": "probe_y"})

    colls= ArrayOf(Collector)() # type: ignore
    colls.append(
        Collector(
            address=IPv4Net("192.168.1.0"),
            port=Port(5213),
        )
    )
    colls.append(
        Collector(
            address=IPv4Net("192.168.2.0"),
            port=Port(5213),
        )
    )
    arg = nfm.Args({
        #"start_time": oc2.DateTime(time.time() * 1000 + 15000),
        #"stop_time" :  oc2.DateTime(time.time() * 1000 + 20000),
        "exporter" : Exporter(storage=File({'path': '/flows'}), collectors=colls),
        "exporter_options" : ExportOptions(format=FlowFormat.json, sampling=20)
        })
    ifaces= ArrayOf(Interface)() # type: ignore
    ifaces.append(
        Interface( # type: ignore
            name="ens33",
            )
        )
    ies= ArrayOf(IE)() # type: ignore
    ies.append(IE("source ip"))
    ies.append(IE("destination ip"))

    ipv4_connections = [
    #   IPv4Connection(src_addr="192.168.1.1/24", dst_addr="130.251.17.2"),
    #    IPv4Connection(src_addr="192.168.0.104", dst_addr="130.251.17.2", protocol=L4Protocol.tcp),
    #    IPv4Connection(src_addr="192.168.0.104", dst_addr="130.251.17.110", protocol=L4Protocol.tcp, src_port=45),
    #    IPv4Connection(src_addr="192.168.0.104", dst_addr="130.251.17.110", protocol=L4Protocol.tcp, dst_port=443, src_port=54682),
    #    IPv4Connection(src_addr="192.168.0.104", dst_addr="130.251.17.2", protocol=L4Protocol.udp, dst_port=53),
    #    IPv4Connection(dst_addr="130.251.17.2"),
    #    IPv4Connection(protocol=L4Protocol.udp, dst_port=53),
    #    IPv4Connection(src_addr="192.168.0.104", dst_addr="130.251.17.2", protocol=L4Protocol.udp, dst_port=53, src_port=44),
    #    IPv4Connection(src_addr="130.251.17.2", dst_addr="192.168.0.104", protocol=L4Protocol.udp, src_port=53),
    #    IPv4Connection(protocol=L4Protocol.sctp, dst_port=53, src_port=44),
    #    IPv4Connection(src_addr="192.168.0.104", dst_addr="130.251.17.2", protocol=L4Protocol.sctp, dst_port=53, src_port=44),
    #    IPv4Connection(dst_addr="130.251.17.2", protocol=L4Protocol.icmp),   
    ]

    ipv6_connections = [
    #   IPv6Connection(src_addr="2001:db8::1", dst_addr="2001:db8::2", protocol=L4Protocol.udp, dst_port=53),
    #    IPv6Connection(protocol=L4Protocol.sctp, dst_port=53, src_port=44),
    #    IPv6Connection(dst_addr="::130.251.17.110"),
    #    IPv6Connection(src_addr="2001:db8::1", dst_addr="2001:db8::2", protocol=L4Protocol.tcp, src_port=1234, dst_port=443),
    #    IPv6Connection(dst_addr="2001:db8::2", protocol=L4Protocol.icmp),
    ]
    command = nfm.FlowMonitor(interfaces=ifaces,information_elements=ies,filter_v4=ArrayOf(IPv4Connection)(ipv4_connections),filter_v6 = ArrayOf(IPv6Connection)(ipv6_connections))
    #command = nfm.Monitor(FlowMonitor(interfaces=ifaces, information_elements= ies))
    cmd = oc2.Command(oc2.Actions.start, command, arg, actuator=pf)

    logger.info("Sending "
    "command: %s", cmd)
    resp = p.sendcmd(cmd)
    logger.info("Got response: %s", resp)

if __name__ == '__main__':
    main()
