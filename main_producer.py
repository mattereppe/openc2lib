# Example to use the OpenC2 library
#
from openc2.producer import Producer
from openc2.message import Command, Message
from openc2.encoders.json_encoder import JSONEncoder
from openc2.transfers.http_transfer import HTTPTransfer

from openc2.actions import *
from openc2.targets import *
p = Producer("ge.imati.cnr.ir", JSONEncoder(), HTTPTransfer("acme.com", 8080))
p.sendcmd(Command(Actions.scan, IPv4Net("130.251.17.0/24")),consumers=["tnt-lab.unige.it"])

#cmd = Command(Actions.scan, IPv4Net("130.251.17.0/24"))
#msg = Message(cmd)
#msg.from_="ciccio"
#msg.to=["paperino"]
#e = Encoder.todict(msg)
