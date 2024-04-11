# Example to use the OpenC2 library
#
from openc2lib.producer import Producer
from openc2lib.message import Command, Message
from openc2lib.encoders.json_encoder import JSONEncoder
from openc2lib.transfers.http_transfer import HTTPTransfer

from openc2lib.actions import *
from openc2lib.targets import * # This is here to load the available targets. Find a better solution!
from openc2lib.targettypes import IPv4Net, IPv4Connection
from openc2lib.datatypes import L4Protocol

print("*** Testing command ***")
p = Producer("ge.imati.cnr.ir", JSONEncoder(), HTTPTransfer("acme.com", 8080))
# Sending Command
p.sendcmd(Command(Actions.scan, IPv4Net("130.251.17.0/24")),consumers=["tnt-lab.unige.it"])
resp = p.sendcmd(Command(Actions.query, IPv4Connection(dst_addr = "130.251.17.0/24", dst_port=80, protocol=L4Protocol.sctp)),consumers=["tnt-lab.unige.it", "ge.imati.cnr.it"])

print("*** Testing response ***")

print(resp)

#p.sendcmd(Command(Actions.query,DomainName("cqw")),consumers=["tnt-lab.unige.it"])
#p.sendcmd(Command(Actions.stop,EmailAddress("1486518253@qq.com")),consumers=["tnt-lab.unige.it"])
#p.sendcmd(Command(Actions.restart,IRI("https://www.openc2lib.org")),consumers=["tnt-lab.unige.it"])
#
#file_target = File(name="example.txt", hashes={"md5": "d41d8cd98f00b204e9800998ecf8427e"})
#p.sendcmd(Command(Actions.query, file_target), consumers=["tnt-lab.unige.it"])

