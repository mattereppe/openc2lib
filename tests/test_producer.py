#!../.venv/bin/python3
# Example to use the OpenC2 library
#

import logging
import sys
#sys.path.insert(0,'/Users/matteo/Progetti/OpenC2/openc2/src')

import otupy as oc2

from otupy.encoders.json_encoder import JSONEncoder
from otupy.transfers.http_transfer import HTTPTransfer

import otupy.profiles.slpf as slpf


#logging.basicConfig(filename='openc2.log',level=logging.DEBUG)
#logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout,level=logging.INFO)
logger = logging.getLogger('openc2producer')

def main():
	logger.info("Creating Producer")
	p = oc2.Producer("ge.imati.cnr.ir", JSONEncoder(), HTTPTransfer("127.0.0.1", 8080))

	pf = slpf.slpf({'hostname':'abete', 'named_group':'firewalls', 'asset_id':'iptables'})
#pf = slpf.slpf({})
# Alternative initialization
#	pf = slpf.slpf(dict(hostname='abete', named_group='firewalls', asset_id='iptables'))


	arg = slpf.Args({'start_time': oc2.DateTime(), 'duration': 3000,'persistent': True, 'direction': slpf.Direction.ingress})
#arg = slpf.ExtArgs(start_time=oc2.DateTime(), response_requested=oc2.ResponseType.complete, duration= 3000,persistent= True, direction= slpf.Direction.ingress)
#	arg = Args({'start_time': DateTime(), 'duration': 3000})

	cmd = oc2.Command(oc2.Actions.query, oc2.IPv4Net("130.251.17.0/24"), arg, actuator=pf)
#	cmd = Command(Actions.scan, IPv4Net("130.251.17.0/24"))
#	cmd = oc2.Command(oc2.Actions.query, oc2.Features(), actuator=pf)
	logger.info("Sending command: %s", cmd)

	resp = p.sendcmd(cmd,consumers=["tnt-lab.unige.it"])

	logger.info("Got response: %s", resp)






#resp = p.sendcmd(Command(Actions.query, IPv4Connection(dst_addr = "130.251.17.0/24", dst_port=80, protocol=L4Protocol.sctp)),consumers=["tnt-lab.unige.it", "ge.imati.cnr.it"])



#p.sendcmd(Command(Actions.query,DomainName("cqw")),consumers=["tnt-lab.unige.it"])
#p.sendcmd(Command(Actions.stop,EmailAddress("1486518253@qq.com")),consumers=["tnt-lab.unige.it"])
#p.sendcmd(Command(Actions.restart,IRI("https://www.otupy.org")),consumers=["tnt-lab.unige.it"])
#
#file_target = File(name="example.txt", hashes={"md5": "d41d8cd98f00b204e9800998ecf8427e"})
#p.sendcmd(Command(Actions.query, file_target), consumers=["tnt-lab.unige.it"])


if __name__ == '__main__':
	main()
