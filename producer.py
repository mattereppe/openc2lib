from openc2.message import Command, Message
from openc2.encoder import Encoder
from openc2.transfer import Transfer

class Producer:
	def __init__(self, producer, encoding=None, transfer=None):
		if not isinstance(producer, str):
			raise TypeError('Only strings are allowed for producer identifier')
		self.producer = producer
		self.encoding = encoding
		self.transfer = transfer

	def sendcmd(self, cmd: Command, encoding: Encoder =None, transfer: Transfer =None, consumers: [] =None):
		if not encoding: encoding = self.encoding
		if not transfer: transfer = self.transfer
		if not transfer: raise ValueError('Missing transfer object')
		if not encoding: raise ValueError('Missing encoder object')
		
		msg = Message(cmd)
		msg.from_=self.producer
		msg.to=consumers

		transfer.send(cmd, encoding)


# DEBUG -- remove me
from openc2.actions import *
from openc2.targets import *
p = Producer("ge.imati.cnr.ir", Encoder(), Transfer())
cmd = p.sendcmd(Command(Scan(), IPv4Net("130.251.17.0/24")),consumers=["tnt-lab.unige.it"])
