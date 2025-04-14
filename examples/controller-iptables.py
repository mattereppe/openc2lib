#!../.oc2-env/bin/python3
# Example to use the OpenC2 library
#

import logging
import sys

import otupy as oc2

from otupy.encoders.json import JSONEncoder
from otupy.transfers.http import HTTPTransfer

import otupy.profiles.slpf as slpf

# logging.basicConfig(filename='openc2.log',level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger('openc2producer')


def main():
    logger.info("Creating Producer")
    p = oc2.Producer("producer.example.net",
                     JSONEncoder(),
                     HTTPTransfer("172.17.0.11",
                                  8080))
    # p = oc2.Producer("producer.example.net",
    #                  JSONEncoder(),
    #                  HTTPTransfer("127.0.0.1",
    #                               5000))


    pf = slpf.Specifiers({'hostname': 'firewall', 'named_group': 'firewalls', 'asset_id': 'iptables'})

    arg = slpf.Args({'response_requested': oc2.ResponseType.complete})
    #	arg = slpf.Args({'response_requested': oc2.ResponseType.none})

    # cmd = oc2.Command(oc2.Actions.query, oc2.Features([oc2.Feature.versions, oc2.Feature.profiles, oc2.Feature.pairs]), arg, actuator=pf)
    # cmd = oc2.Command(oc2.Actions.query, oc2.Features([oc2.Feature.pairs]), arg, actuator=pf)
    # cmd = oc2.Command(oc2.Actions.allow, oc2.IPv4Net('130.0.16.0/20'), arg, actuator=pf)
    # cmd = oc2.Command(oc2.Actions.deny, oc2.IPv4Net('130.0.0.1'), arg, actuator=pf)
    # cmd = oc2.Command(oc2.Actions.delete, slpf.RuleID(1), arg, actuator=pf)
    cmd = oc2.Command(oc2.Actions.update, oc2.File({'path':'http://192.168.197.128:8080','name':'iptables-rules.v4'}), arg, actuator=pf)

    logger.info("Sending command: %s", cmd)
    resp = p.sendcmd(cmd)
    logger.info("Got response: %s", resp)


if __name__ == '__main__':
    main()
