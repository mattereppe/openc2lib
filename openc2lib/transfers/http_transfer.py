import dataclasses
import requests
import logging
import copy

from flask import Flask, request, make_response

from openc2lib import Transfer, MessageType, Message, Command, Response, Content, Encoders, StatusCode, Version, Encoder, DateTime

# TODO: remove this when the encoder is instantiated based on message content
from openc2lib.encoders.json_encoder import JSONEncoder

logger = logging.getLogger('openc2lib')

# This can be taken as an example that defines an additional Openc2Type
# for parsing a custom data structure (HTTP Message, in this case)
#@register_basetype
@dataclasses.dataclass
class Payload:
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
			# deepcopy is necessary to avoid unpleasant issues when the decode functions
			# is called multiple times (an issues that may occur while debugging)
			payload.body = copy.deepcopy(dic['body'])
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
		if encoder is not None:
			data = encoder.encode(self.payload)
		else:
			data = Encoder().encode(self.payload)


		return data

	def fromhttp(self, hdr, data):

		# TODO: Check the HTTP headers for version/encoding
		content_type =hdr['Content-type']

		if not content_type.removeprefix('application/').startswith(Message.content_type):
			raise ValueError("Unsupported content type")

		enctype = content_type.removeprefix('application/'+Message.content_type+'+').split(';')[0]
		try:
			encoder = Encoders[enctype].value
		except KeyError:
			raise ValueError("Unsupported encoding scheme: " + enctype)

		payload = encoder.decode(data, Payload)

		# HTTP processing to extract the headers
		# and the transport body
		msg = Message(payload.getContent())
		msg.request_id = payload.headers['request_id'] if 'request_id' in payload.headers.keys() else None
		msg.created = payload.headers['created'] if 'created' in payload.headers.keys() else None
		msg.from_ = payload.headers['from'] if 'from' in payload.headers.keys() else None
		msg.to = payload.headers['to'] if 'to' in payload.headers.keys() else None
		msg.msg_type = Payload.getMessageType(payload.getContentType())
		msg.content_type = hdr['Content-type'].removeprefix('application/').split('+')[0]
		msg.version = Version.fromstr(hdr['Content-type'].split(';')[1].removeprefix("version="))
		msg.encoding = encoder
		
		try:
			msg.status = msg.content['status']
		except:
			msg.status = None


		return msg, encoder


	# This function is used to send an HTTP request
	def send(self, msg, encoder):
		# HTTP processing to prepare the headers
		# and the transport body
		openc2data = self.tohttp(msg, encoder)

		# Building the requested headers for the Request
		content_type = f"application/{msg.content_type}+{encoder.getName()};version={msg.version}"
		date = msg.created if msg.created else int(DateTime())
		openc2headers={'Content-Type': content_type, 'Accept': content_type, 'Date': DateTime(date).httpdate()}

		logger.info("Sending to %s", self.url)
		logger.debug(" -> body: %s", openc2data)

		# Send the OpenC2 message and get the response
		response = requests.post(self.url, data=openc2data, headers=openc2headers)
		logger.debug("HTTP got response: %s", response)
		print("data: ", response.text)
	
		# TODO: How to manage HTTP response code? Can we safely assume they always match the Openc2 response?
		try:
			if response.text != "":
				msg = self.fromhttp(response.headers, response.text)
			else:
				msg = None
		except ValueError as e:
			msg = Message(Content())
			msg.status = response.status_code
			logger.error("Unable to parse data: >%s<", response.text)
			logger.error(str(e))

		return msg

	# This function is used to prepare the headers and content in a response
	def respond(self, msg, encoder):

		headers = {}
		if msg is not None:
			if encoder is not None:
				content_type = f"application/{msg.content_type}+{encoder.getName()};version={msg.version}"
			else:	
				content_type = f"text/plain"
			headers['Content-Type']= content_type
			date = msg.created if msg.created else int(DateTime())
			data = self.tohttp(msg, encoder)
		else:
			content_type = None
			data = None
			date = int(DateTime())

		# Date is currently autmatically inserted by Flask (probably 
		# after I used 'make_response')
		#headers['Date'] = DateTime(date).httpdate()

		return headers, data

	def recv(self, headers, data):

		logger.debug("Received body: %s", data)
		msg, encoder = self.fromhttp(headers, data)
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
			encoder=app.config['ENCODER']
			
			try:
				cmd, encoder = server.recv(request.headers, request.data.decode('UTF-8') )
				# TODO: Add the code to answer according to 'response_requested'
			except ValueError as e:
				# TODO: Find better formatting (what should be returned if the request is not understood?)
				content = Response(status=StatusCode.BADREQUEST, status_text=str(e))
				resp = Message(content)
				resp.content_type = Message.content_type
				resp.version = Message.version
				resp.encoder = encoder
				resp.status=StatusCode.BADREQUEST
			else:
				logger.info("Received command: %s", cmd)
				resp = callback(cmd)

			
			logger.debug("Got response: %s", resp)
			
			# TODO: Set HTTP headers as appropriate
			hdrs, data = server.respond(resp, encoder)
			logger.debug("Sending response: %s", data)
			httpresp = make_response(data if data is not None else "") 
			httpresp.headers = hdrs

			if data is None:
				resp_code = 200
			else:
				resp_code = resp.status.value

			return httpresp, resp_code

		app.run(debug=True, host=self.host, port=self.port)


class HTTPSTransfer(HTTPTransfer):
	def __init__(self, host, port):
		self.host = host
		self.port = port

	def send(self, msg, encoder):
		pass


