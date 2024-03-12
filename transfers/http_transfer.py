from openc2.transfer import Transfer
from openc2.message import MessageType, Message, Command, Response
from openc2.basetypes import Openc2Type
import dataclasses

# This can be taken as an example that defines an additional Openc2Type
# for parsing a custom data structure (HTTP Message, in this case)
#@register_basetype
@dataclasses.dataclass
class Payload(Openc2Type):
	headers: dict = None
	body: dict = None
	signature: str = None

	def getContent(self):
		try:
			for k,v in self.body['openc2'].items():
				return v
		except:
		  	return None

	def getContentType(self):
		try:
			for k,v in self.body['openc2'].items():
				return k
		except:
		  return None

	@staticmethod
	def getMessageType(content_type):
		match content_type:
			case 'request':
				return MessageType.command
			case 'response':
				return MessageType.response
			case _: # Should only be 'notification' (HTTP transfer specification)
				raise TypeException("Unhandled Openc2 message type: ", content_type)
	
	@staticmethod
	def getContentClass(content_type):
		match content_type:
			case 'request':
				return Command
			case 'response':
				return Response
			case _: # Should only be 'notification' (HTTP transfer specification)
				raise TypeException("Unhandled Openc2 message type: ", content_type)

	def todict(self, e):
		dic = vars(self)
		# Remove void fields
		for k in list(dic.keys()):
			if dic[k] is None:
				del dic[k]
		e.todict(dic)
		
		return dic

	
	@classmethod
	def fromdict(cls, dic, e):
		payload = Payload()
		try:
			payload.headers = dic['headers']
		except KeyError:
			payload. headers = None
		try:
			payload.body = dic['body']

		except KeyError:
			payload.body = None
		try:
			payload.signature = dic['signature']
		except KeyError:
			payload.signature: None

		# TODO: check if this is expected to run once or more times (more commands in a single message?)
		for k,v in payload.body['openc2'].items():
			content_type = k
			content = v

		payload.body['openc2'][payload.getContentType()] = e.decode(Payload.getContentClass(content_type), payload.getContent())

		return payload



class HTTPTransfer(Transfer):
	# TODO: Define initializer for HTTP (base URL, endpoint, etc.)
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.payload = Payload()

	def send(self, msg, encoder):
		# HTTP processing to prepare the headers
		# and the transport body
		self.payload.headers = {}
		self.payload.headers['request_id'] = msg.request_id
		self.payload.headers['created'] = msg.created
		self.payload.headers['from'] = msg.from_
		self.payload.headers['to'] = msg.to

		self.payload.body = {}
		self.payload.body['openc2'] = {}
		match msg.msg_type:
			case MessageType.command:
				content = 'request'
			case MessageType.response:
				content = 'response'
			# Missing "event" type (not found in language specification)
		self.payload.body['openc2'][content] = msg.content

		enc = encoder.encode(self.payload)

		# TODO: Remove me!
		print(enc)

		# TODO: Add the code to set the HTTP headers
		# Note: the content-type MUST be built from the following information
		# msg.content-type (usually: application/openc2)
		# msg.verstion (usually: "version=1.0")
		# encoder.getName(): (usually "json")
		# The result could be something like:
		# msg.content-type + '+' + encoder.getName() + ';' + msg.version()


		# TODO: Add code to transfer the message with HTTP


	def recv(self, encoder):
	# TODO: Add the code for actually receiving the message with HTTP
	# Replace the following debug code!!!!
		body = '{"headers": {"request_id": "", "created": 1709914239523, "from": "ge.imati.cnr.ir", "to": ["tnt-lab.unige.it"]}, "body": {"openc2": {"request": {"action": "scan", "target": {"ipv4_net": "130.251.17.0/24"}}}}}'
#		body = 

		payload = encoder.decode(body, Payload)

		# HTTP processing to extract the headers
		# and the transport body
		print(payload.getContent())
		msg = Message(payload.getContent())
		msg.request_id = payload.headers['request_id'] 
		msg.created = payload.headers['created'] 
		msg.from_ = payload.headers['from'] 
		msg.to = payload.headers['to'] 
		msg.msg_type = Payload.getMessageType(payload.getContentType())
  			
		return msg
	


class HTTPSTransfer(HTTPTransfer):
	def __init__(self, host, port):
		self.host = host
		self.port = port

	def send(self, msg, encoder):
		pass


