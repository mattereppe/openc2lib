#!/opt/homebrew/bin/python3
# Example to use the OpenC2 library
#
from openc2lib.producer import Producer
from openc2lib.message import Command, Message
from openc2lib.encoders.json_encoder import JSONEncoder
from openc2lib.transfers.http_transfer import HTTPTransfer

from openc2lib.actions import *
from openc2lib.targets import * # This is here to load the available targets. Find a better solution!
from openc2lib.targettypes import IPv4Net, IPv4Connection, Features
from openc2lib.datatypes import L4Protocol, DateTime, Duration
from openc2lib.args import Args
import openc2lib.profiles.slpf as slpf
import logging
import sys

#logging.basicConfig(filename='openc2.log',level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)
#logging.basicConfig(stream=sys.stdout,level=logging.INFO)
logger = logging.getLogger('openc2producer')

def main():
	logger.info("Creating Producer")
	p = Producer("ge.imati.cnr.ir", JSONEncoder(), HTTPTransfer("127.0.0.1", 8080))

	pf = slpf.slpf({'hostname':'abete', 'named_group':'firewalls', 'asset_id':'iptables'})
#pf = slpf.slpf({})
# Alternative initialization
#	pf = slpf.slpf(dict(hostname='abete', named_group='firewalls', asset_id='iptables'))


#arg = slpf.ExtArgs({'start_time': DateTime(), 'duration': 3000,'persistent': True, 'direction': slpf.Direction.ingress})
	arg = slpf.ExtArgs(start_time=DateTime(), duration= 3000,persistent= True, direction= slpf.Direction.ingress)
#	arg = Args({'start_time': DateTime(), 'duration': 3000})

#	cmd = Command(Actions.scan, IPv4Net("130.251.17.0/24"), arg, actuator=pf)
#	cmd = Command(Actions.scan, IPv4Net("130.251.17.0/24"))
	cmd = Command(Actions.query, Features(), actuator=pf)
	logger.info("Sending command: %s", cmd)

	resp = p.sendcmd(cmd,consumers=["tnt-lab.unige.it"])

	logger.info("Got response: %s", resp)






#resp = p.sendcmd(Command(Actions.query, IPv4Connection(dst_addr = "130.251.17.0/24", dst_port=80, protocol=L4Protocol.sctp)),consumers=["tnt-lab.unige.it", "ge.imati.cnr.it"])



#p.sendcmd(Command(Actions.query,DomainName("cqw")),consumers=["tnt-lab.unige.it"])
#p.sendcmd(Command(Actions.stop,EmailAddress("1486518253@qq.com")),consumers=["tnt-lab.unige.it"])
#p.sendcmd(Command(Actions.restart,IRI("https://www.openc2lib.org")),consumers=["tnt-lab.unige.it"])
#
#file_target = File(name="example.txt", hashes={"md5": "d41d8cd98f00b204e9800998ecf8427e"})
#p.sendcmd(Command(Actions.query, file_target), consumers=["tnt-lab.unige.it"])


if __name__ == '__main__':
	main()
