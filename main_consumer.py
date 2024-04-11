from openc2lib.consumer import Consumer
from openc2lib.encoders.json_encoder import JSONEncoder
from openc2lib.encoder import Encoder
from openc2lib.transfers.http_transfer import HTTPTransfer
from openc2lib.transfer	import Transfer
from openc2lib.message import Response
from openc2lib.datatypes import *
import openc2lib.response


	
c = Consumer("testconsumer", JSONEncoder(), HTTPTransfer("acme.com", 8080))

msg = c.recv()

print(msg)
print(msg.content)

#print(type(msg.content.target))

print("Creating response")

at = ActionTargets()
at[Actions.scan] = [TargetEnum.ipv4_net]
at[Actions.query] = [TargetEnum.ipv4_net, TargetEnum.ipv4_connection]
pf = openc2lib.basetypes.ArrayOf(Nsid)()
pf.append(Nsid('slpf'))
res = openc2lib.response.Results(versions=Version(1,0), profiles=pf, pairs=at,rate_limit=3)
r = Response(openc2lib.response.StatusCode.OK, openc2lib.response.StatusCodeDescription[openc2lib.response.StatusCode.OK], res)

print(r)

c.reply(r)

