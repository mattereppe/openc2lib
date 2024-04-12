import dataclasses
import requests
import logging
from flask import Flask, request
from openc2lib.transfer import Transfer
from openc2lib.message import MessageType, Message, Command, Response
from openc2lib.basetypes import Openc2Type
# TODO: remove this when the encoder is instantiated based on message content
from openc2lib.encoders.json_encoder import JSONEncoder

logger = logging.getLogger('openc2')

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
		return e.todict(dic)

	
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
	def __init__(self, host, port = 80, endpoint = '/.well-known/openc2'):
		self.host = host
		self.port = port
		self.endpoint = endpoint
		self.url = f"http://{host}:{port}{endpoint}"
		self.payload = Payload()

	def tohttp(self, msg, encoder):
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

		# Encode the data
		data = encoder.encode(self.payload)

		# Building the Content-Type header
		content_type = f"{msg.content_type}+{encoder.getName()};{msg.version}"
		headers={'Content-Type': content_type}

		return headers, data

	def fromhttp(self, data, encoder):
		payload = encoder.decode(data, Payload)

		# HTTP processing to extract the headers
		# and the transport body
		msg = Message(payload.getContent())
		msg.request_id = payload.headers['request_id'] 
		msg.created = payload.headers['created'] 
		msg.from_ = payload.headers['from'] 
		msg.to = payload.headers['to'] 
		msg.msg_type = Payload.getMessageType(payload.getContentType())
		try:
			msg.status = msg.content['status']
		except:
			msg.status = None


		return msg


	# This function is used to send an HTTP request
	def send(self, msg, encoder):
		# HTTP processing to prepare the headers
		# and the transport body
		openc2headers, openc2data = self.tohttp(msg, encoder)

		logger.info("Sending to %s", self.url)

		# Send the OpenC2 message and get the response
		response = requests.post(self.url, data=openc2data, headers=openc2headers)
		logger.debug("HTTP got response: %s", response)
	
		# TODO: How to manage HTTP response code? Can we safely assume they always match the Openc2 response?
		print("+++++++ Now encoding")
		msg = self.fromhttp(response.text, encoder)
		print("+++++++ msg: ", msg.content['status'])

		return msg

	# This function is used to prepare the headers and content in a response
	def respond(self, msg, encoder):
		return self.tohttp(msg, encoder)

	def recv(self, headers, data):

		enctype = headers.get('Content-type')
		# TODO: Check the HTTP headers for version/encoding
		encoder = JSONEncoder()

		logger.debug("Received body: %s", data)
		msg = self.fromhttp(data, encoder)
		logger.info("Received command: %s", msg)
  			
		return msg, encoder
	
	def run(self, callback, encoder=None):
		app = Flask(__name__)
		app.config['OPENC2']=self
		app.config['CALLBACK']=callback
		app.config['ENCODER']=encoder

		@app.route(self.endpoint, methods=['POST'])
		def consumer():
			server = app.config['OPENC2']
			callback = app.config['CALLBACK']
			encoders=app.config['ENCODER']

			
			cmd, encoder = server.recv(request.headers, request.data.decode('UTF-8') )
			logger.info("Received command: %s", cmd)
			resp = callback(cmd)
			logger.debug("Got response: %s", resp)
			
			# TODO: Set HTTP headers as appropriate
			hdrs, data = server.respond(resp, encoder)
			logger.debug("Sending response: %s", data)

			return data

		app.run(debug=True)


class HTTPSTransfer(HTTPTransfer):
	def __init__(self, host, port):
		self.host = host
		self.port = port

	def send(self, msg, encoder):
		pass


