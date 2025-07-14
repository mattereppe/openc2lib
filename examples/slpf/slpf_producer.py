#!../../.oc2-env/bin/python3
# Example to use the OpenC2 library
#
import json
import logging
import os
import time

import openc2lib as oc2

from openc2lib.encoders.json import JSONEncoder
from openc2lib.transfers.http import HTTPTransfer
import openc2lib.profiles.slpf as slpf
from openc2lib.profiles.slpf.data import DropProcess


logger = logging.getLogger()
# Ask for 4 levels of logging: INFO, WARNING, ERROR, CRITICAL
logger.setLevel(logging.INFO)
# Create stdout handler for logging to the console 
stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(oc2.LogFormatter(datetime=True,name=True))
#hdls = [ stdout_handler ]
# Add both handlers to the logger
logger.addHandler(stdout_handler)
# Add file logger
file_handler = logging.FileHandler("controller.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(oc2.LogFormatter(datetime=True,name=True, datefmt='%t'))
logger.addHandler(file_handler)

def main():
    logger.info("Creating Producer")

#    p = oc2.Producer("producer.example.net", JSONEncoder(), HTTPTransfer(parameters['ip'],
#                                                                        parameters['port']))
#    pf = slpf.Specifiers({'hostname': parameters['hostname'],
#                          'named_group': parameters['named_group'],
#                          'asset_id': parameters['asset_id']})
#    pf.fieldtypes['asset_id'] = parameters['asset_id']  # I have to repeat a second time to have no bugs

    p = oc2.Producer("producer.example.net", JSONEncoder(), HTTPTransfer("127.0.0.1", 8080))
#    pf = slpf.Specifiers({'asset_id': 'iptables'})
#    pf = slpf.Specifiers({'asset_id': 'openstack'})
    pf = slpf.Specifiers({'asset_id': 'kubernetes'})

    # Args
#    arg = slpf.Args({})
    # (response_requested)
    arg = oc2.Args({'response_requested': oc2.ResponseType.complete})
#    arg = oc2.Args({'response_requested': oc2.ResponseType.ack})
    # (direction)
#    arg = slpf.Args({'response_requested': oc2.ResponseType.complete, 'direction': slpf.Direction.ingress})
#    arg = slpf.Args({'response_requested': oc2.ResponseType.complete, 'direction': slpf.Direction.egress})
#    arg = slpf.Args({'response_requested': oc2.ResponseType.complete, 'direction': slpf.Direction.both})
    # (insert_rule) (with slpf.RuleID and just int)(response_requested MUST be present)
#    arg = slpf.Args({'insert_rule': slpf.RuleID(3), 'response_requested': oc2.ResponseType.complete})
#    arg = slpf.Args({'insert_rule': 8, 'response_requested': oc2.ResponseType.complete})
    # (drop_process)
#    arg = slpf.Args({'drop_process': DropProcess.reject})
#    arg = slpf.Args({'drop_process': DropProcess.false_ack})
#    arg = slpf.Args({'drop_process': DropProcess.reject, 'direction': slpf.Direction.ingress})
#    arg = slpf.Args({'drop_process': DropProcess.reject, 'direction': slpf.Direction.egress})
#    arg = slpf.Args({'drop_process': DropProcess.reject, 'insert_rule': slpf.RuleID(15)})
#    arg = slpf.Args({'drop_process': DropProcess.reject, 'start_time': oc2.DateTime((time.time() + 10) * 1000)})
    # (persistent) (with bool and int)
#    arg = slpf.Args({'persistent': False})
#    arg = slpf.Args({'persistent': 0})
    # (start_time) (stop_time) (duration) (with oc2.DateTime and just int)
#    arg = slpf.Args({'start_time': oc2.DateTime((time.time() + 10) * 1000)})
#    arg = slpf.Args({'start_time': (time.time() + 20) * 1000})
#    arg = slpf.Args({'stop_time': oc2.DateTime((time.time() + 30) * 1000)})
#    arg = slpf.Args({'duration': oc2.Duration(10000)})
#    arg = slpf.Args({'duration': 10000})
#    arg = slpf.Args({'start_time': oc2.DateTime((time.time() + 30) * 1000), 'stop_time': oc2.DateTime((time.time() + 50) * 1000)})
#    arg = slpf.Args({'start_time': oc2.DateTime((time.time() + 10) * 1000), 'duration': 10000})
#    arg = slpf.Args({'stop_time': oc2.DateTime((time.time() + 15) * 1000), 'duration': 10000})

    # Invalid args
#    arg = slpf.Args({'insert_rule': 1}) # response_requested required
#    arg = slpf.Args({'start_time': (time.time() + 10) * 1000, 'stop_time': (time.time() + 20), 'duration': 10000})


    # Actions
    # (query)
#    cmd = oc2.Command(oc2.Actions.query, oc2.Features([oc2.Feature.versions, oc2.Feature.profiles, oc2.Feature.pairs]), arg, actuator=pf)

#   ----------------------------------------------------------   

    # (allow IPv4Net)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Net("172.19.0.0/24"), arg, actuator=pf)

    # (allow IPv6Net)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv6Net("2001:0db8:85a3::/48"), arg, actuator=pf)

    # (allow IPv4Connection)
    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(src_addr=oc2.IPv4Net("172.19.0.1")), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(dst_addr=oc2.IPv4Net("172.19.0.1")), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(protocol=oc2.L4Protocol.tcp), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(protocol=oc2.L4Protocol.tcp, src_port=oc2.Port(8080)), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(protocol=oc2.L4Protocol.tcp, dst_port=oc2.Port(8080)), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(src_addr=oc2.IPv4Net("172.19.0.1"), protocol=oc2.L4Protocol.tcp), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(dst_addr=oc2.IPv4Net("172.19.0.1"), protocol=oc2.L4Protocol.tcp), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(src_addr=oc2.IPv4Net("172.19.0.1"), protocol=oc2.L4Protocol.icmp), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(dst_addr=oc2.IPv4Net("172.19.0.1"), protocol=oc2.L4Protocol.icmp), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(src_addr=oc2.IPv4Net("172.19.0.1"), src_port=oc2.Port(8080), protocol=oc2.L4Protocol.tcp), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(src_addr=oc2.IPv4Net("172.19.0.1"), src_port=oc2.Port(8080), protocol=oc2.L4Protocol.udp), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(src_addr=oc2.IPv4Net("172.19.0.1"), src_port=oc2.Port(8080), protocol=oc2.L4Protocol.sctp), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(dst_addr=oc2.IPv4Net("172.19.0.1"), dst_port=oc2.Port(8080), protocol=oc2.L4Protocol.tcp), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(src_addr=oc2.IPv4Net("172.19.0.1"), dst_port=oc2.Port(8080), protocol=oc2.L4Protocol.tcp), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(src_addr=oc2.IPv4Net("172.19.0.1"), src_port=oc2.Port(8080), dst_port=oc2.Port(8080), protocol=oc2.L4Protocol.tcp), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(dst_addr=oc2.IPv4Net("172.19.0.1"), src_port=oc2.Port(8080), dst_port=oc2.Port(8080), protocol=oc2.L4Protocol.tcp), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(dst_addr=oc2.IPv4Net("172.19.0.1"), src_port=oc2.Port(8080), protocol=oc2.L4Protocol.tcp), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(src_addr=oc2.IPv4Net("172.19.0.3"), dst_addr=oc2.IPv4Net("172.19.0.4")), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(src_addr=oc2.IPv4Net("172.19.0.3"), dst_addr=oc2.IPv4Net("172.19.0.4"), protocol=oc2.L4Protocol.tcp, src_port=oc2.Port(8080), dst_port=oc2.Port(8080)), arg, actuator=pf)
#	not valid:
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(src_port=oc2.Port(8080)), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(dst_port=oc2.Port(8080)), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Connection(src_port=oc2.Port(8080), protocol=oc2.L4Protocol.icmp), arg, actuator=pf)

    # (allow IPv6Connection)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv6Connection(src_addr=oc2.IPv6Net("2001:db8:85a3::8a2e:370:7334")), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv6Connection(dst_addr=oc2.IPv6Net("2001:db8:85a3::8a2e:370:7334")), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv6Connection(src_addr=oc2.IPv6Net("2001:db8:85a3::8a2e:370:7334"), protocol=oc2.L4Protocol.tcp), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv6Connection(dst_addr=oc2.IPv6Net("2001:db8:85a3::8a2e:370:7334"), protocol=oc2.L4Protocol.tcp), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv6Connection(src_addr=oc2.IPv6Net("2001:db8:85a3::8a2e:370:7334"), dst_port=oc2.Port(8080), protocol=oc2.L4Protocol.tcp), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv6Connection(dst_addr=oc2.IPv6Net("2001:db8:85a3::8a2e:370:7334"), src_port=oc2.Port(8080), protocol=oc2.L4Protocol.tcp), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv6Connection(src_addr=oc2.IPv6Net("2001:db8:85a3::8a2e:370:7334"), dst_addr=oc2.IPv6Net("2001:db8:85a3::8a2e:370:7334")), arg, actuator=pf)
#	not valid:
#    cmd = oc2.Command(oc2.Actions.allow, oc2.IPv6Connection(src_addr=oc2.IPv6Net("2001:db8:85a3::8a2e:370:7334"), dst_port=oc2.Port(8080)), arg, actuator=pf)
#	cmd = oc2.Command(oc2.Actions.allow, oc2.IPv6Connection(dst_addr=oc2.IPv6Net("2001:db8:85a3::8a2e:370:7334"), src_port=oc2.Port(8080)), arg, actuator=pf)

#   ----------------------------------------------------------  

    # (deny IPv4Net)
#    cmd = oc2.Command(oc2.Actions.deny, oc2.IPv4Net("172.19.0.0/24"), arg, actuator=pf)
    # deny IPv6Net
#    cmd = oc2.Command(oc2.Actions.deny, oc2.IPv6Net("2001:0db8:85a3::/64"), arg, actuator=pf)

    # (deny IPv4Connection)
#    cmd = oc2.Command(oc2.Actions.deny, oc2.IPv4Connection(src_addr=oc2.IPv4Net("172.19.0.1")), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.deny, oc2.IPv4Connection(dst_addr=oc2.IPv4Net("172.19.0.1")), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.deny, oc2.IPv4Connection(src_addr=oc2.IPv4Net("172.19.0.3"), dst_addr=oc2.IPv4Net("172.19.0.4")), arg, actuator=pf)


    # (deny IPv6Connection)
#    cmd = oc2.Command(oc2.Actions.deny, oc2.IPv6Connection(src_addr=oc2.IPv6Net("2001:db8:85a3::8a2e:370:7334")), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.deny, oc2.IPv6Connection(dst_addr=oc2.IPv6Net("2001:db8:85a3::8a2e:370:7334")), arg, actuator=pf)

#   ----------------------------------------------------------  

    # (Delete)

    cmd = oc2.Command(oc2.Actions.delete, slpf.RuleID(1), arg, actuator=pf)

#   ----------------------------------------------------------

    # (Update)
    # (iptables)
#    cmd = oc2.Command(oc2.Actions.update, oc2.File(name="new_iptables_rules.v4"), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.update, oc2.File(name="new_iptables_rules.v6"), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.update, oc2.File(name="new_iptables_rules.v6", path="/home/kali/Scrivania/openc2lib/examples/slpf", hashes=oc2.Hashes(hashes={'md5': oc2.Binaryx(bytes.fromhex('3e4d11990c706c9ccc787951026ccf82'))})), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.update, oc2.File(name="new_iptables_rules.v6", path="/home/kali/Scrivania/openc2lib/examples/slpf", hashes=oc2.Hashes(hashes={'sha1': oc2.Binaryx(bytes.fromhex('504cd4900a2791dd07e0fef60623d2086e6e3705'))})), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.update, oc2.File(name="new_iptables_rules.v6", path="/home/kali/Scrivania/openc2lib/examples/slpf", hashes=oc2.Hashes(hashes={'sha256': oc2.Binaryx(bytes.fromhex('5e2ba905ca03620586f71eeb4bb5008548219ac4da49f130e5200cd3db3bc593'))})), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.update, oc2.File(name="new_iptables_rules.v6", path="/home/kali/Scrivania/openc2lib/examples/slpf", hashes=oc2.Hashes(hashes={'md5': oc2.Binaryx(bytes.fromhex('3e4d11990c706c9ccc787951026ccf82')), 'sha1': oc2.Binaryx(bytes.fromhex('504cd4900a2791dd07e0fef60623d2086e6e3705')), 'sha256': oc2.Binaryx(bytes.fromhex('5e2ba905ca03620586f71eeb4bb5008548219ac4da49f130e5200cd3db3bc593'))})), arg, actuator=pf)
#   not valid:
#    cmd = oc2.Command(oc2.Actions.update, oc2.File(name="server.log"), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.update, oc2.File(name="non_existing_file.txt"), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.update, oc2.File(path="/home/kali/Scrivania/openc2lib/examples/slpf"), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.update, oc2.File(name="new_iptables_rules.v6", path="/home/kali/Scrivania/openc2lib/examples/slpf", hashes=oc2.Hashes(hashes={'md5': oc2.Binaryx(bytes.fromhex('3e4d11990c706c9ccc787951026ccf80'))})), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.update, oc2.File(name="new_iptables_rules.v6", path="/home/kali/Scrivania/openc2lib/examples/slpf", hashes=oc2.Hashes(hashes={'sha1': oc2.Binaryx(bytes.fromhex('504cd4900a2791dd07e0fef60623d2086e6e3700'))})), arg, actuator=pf)
#    cmd = oc2.Command(oc2.Actions.update, oc2.File(name="new_iptables_rules.v6", path="/home/kali/Scrivania/openc2lib/examples/slpf", hashes=oc2.Hashes(hashes={'sha256': oc2.Binaryx(bytes.fromhex('5e2ba905ca03620586f71eeb4bb5008548219ac4da49f130e5200cd3db3bc590'))})), arg, actuator=pf)
    
    # (kubernetes)
#    cmd = oc2.Command(oc2.Actions.update, oc2.File(name="kubernetes_network_policy.yaml", path="/home/kali/Scrivania/openc2lib/examples/slpf"), arg, actuator=pf)


    logger.info("Sending command: %s", cmd)
    response = p.sendcmd(cmd)
    logger.info("Got response: %s", response)
    

if __name__ == '__main__':
    main()
	
#    configuration_file = os.path.dirname(os.path.abspath(__file__))+"/configuration.json"
#    with open(configuration_file, 'r') as file:
#        configuration_parameters = json.load(file)

#    for element in configuration_parameters['slpf_actuators']:
#        if (element["type"] == "iptables"):      
#            main(element)
#        elif (element["type"] == "openstack"):      
#            main(element)
