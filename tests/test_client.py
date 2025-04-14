import pytest
from unittest.mock import patch
from otupy import *
from otupy.transfers.http import HTTPTransfer
from otupy.encoders.json import  JSONEncoder
import otupy.profiles.slpf as slpf

@pytest.fixture
def create_new_command():

    pf = slpf.slpf({'hostname': 'firewall', 'named_group': 'firewalls', 'asset_id': 'iptables'})

    arg = slpf.Args({'response_requested': ResponseType.complete})
    #	arg = slpf.Args({'response_requested': ResponseType.none})

    cmd = []
    cmd.append(Command(Actions.query, Features([Feature.versions, Feature.profiles, Feature.pairs]), arg, actuator=pf))
    cmd.append(Command(Actions.query, Features([Feature.pairs]), arg, actuator=pf))
    cmd.append( Command(Actions.allow, IPv4Net('130.0.16.0/20'), arg, actuator=pf))
    cmd.append(Command(Actions.deny, IPv4Net('130.0.0.1'), arg, actuator=pf))


    return cmd


def test_create_openc2_command(create_new_command):
    assert isinstance(create_new_command,list)

#def test_actuator(create_new_command)
#	actuator = IptablesActuator(...)
#	resp = actuator.run(create_new_command)
#
#	assert ... 


def test_result(create_new_command):
    producer = Producer("OpenC2_Producer",
                        JSONEncoder(),
                        HTTPTransfer("172.17.0.11",
                                     8080,
                                     endpoint="/.well-known/openc2"))
    resp = []
    for cmd in create_new_command:
        resp.append(producer.sendcmd(cmd))
    print(type(resp))

#print("Response: ", 
    for r in resp:
        assert isinstance(r,Message)
        assert isinstance(r.content, Response)
        assert r.content['status'] == StatusCode.OK
        assert 'rule_number' in r.content['results']
        assert r.content['results']['rule_number'] >= 0 

#    expected_resp = {
#            "headers": {
#                "request_id": str,
#                "created": int,
#                "from": str,
#                "to": [
#                    str
#                ]
#            },
#            "body": {
#                "openc2": {
#                    "request": {
#                        "action": "",
#                        "target": "",
#                        "args": ""
#                    }
#                }
#            }
#        }

#    assert actual_resp == expected_resp











# @pytest.mark.parametrize("action,target,args", [
#     ("allow", {"ipv4_net": {"network_address": "150.0.0.1", "netmask": "255.255.255.0"}}, {}),
#     ("deny", {"ipv4_net": {"network_address": "150.0.0.2", "netmask": "255.255.255.0"}}, {}),
#     ("update", {"slpf:rule_number": 1}, {"iptables_target": "ACCEPT"}),
#     ("delete", {"slpf:rule_number": 2}, {}),
#     ("query", {"features": {"versions","pairs","profiles","rate_limit"}}, {}),
# ])
# def test_send(action, target, args):
#     with patch.object(HTTPTransfer, 'send', return_value=None) as mock_send:
#         command, _, _ = create_openc2_command(action, target, args)
#
#         producer = Producer("test_producer", JSONEncoder(), HTTPTransfer("192.168.197.128", 5000, endpoint="/.well-known/openc2"))
#         producer.sendcmd(command, consumers="OpenC2_Consumer")
#
#         mock_send.assert_called_once()
#         call_args = mock_send.call_args[0]
#         assert isinstance(call_args[0], Message)
#         assert isinstance(call_args[1], JSONEncoder)
#         assert call_args[0].content == command
