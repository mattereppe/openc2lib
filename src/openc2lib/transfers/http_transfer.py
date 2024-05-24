""" HTTP Transfer Protocol

	This module defines implementation of the `Transfer` interface for the 
  	HTTP/HTTPs protocols. This implementation is mostly provided for 
	research and development purposes, but it is not suitable for production
	environments.

	The implementation follows the Specification for Transfer of OpenC2 Messages via HTTPS
	Version 1.1, which is indicated as the "Specification" in the following.
"""
import dataclasses
import requests
import logging
import copy

from flask import Flask, request, make_response

import openc2lib as oc2


logger = logging.getLogger('openc2lib')
""" The logging facility in openc2lib """

class Headers(oc2.Map):
	""" HTTP Message Headers (see Sec. 3.3.2 of the Specification) 
		
		Note: the Specification defines `to` as "String [0..*]", but it should be an `ArrayOf(str)`. Using
		a plain Python list does not work with the current openc2lib implementation.
	"""
	fieldtypes = {'request_id': str, 'created': oc2.DateTime, 'from': str, 'to': oc2.ArrayOf(str)}
	extend = None
	regext = {}


OpenC2Contents = oc2.Register()
""" List allowed OpenC2-Content (see Sec. 3.3.2 of the Specification) """
OpenC2Contents.add('request', oc2.Command, 1)
OpenC2Contents.add('response', oc2.Response, 2)
# Event is not currently defined in the Language Specification
# and there is not indication how to manage it.
# OpenC2Contents.add('notification', oc2.Event, 3)

class OpenC2Content(oc2.Choice):
	register = OpenC2Contents

Bodies = oc2.Register()
""" List allowed objects in Body (see Sec. 3.3.2 of the Specification) """
Bodies.add('openc2',OpenC2Content, 1)

class Body(oc2.Choice):
	""" HTTP Message Body (see Sec. 3.3.2 of the Specification) """
	register = Bodies

@dataclasses.dataclass
class Message(oc2.Record):
	""" HTTP Message representation

		This class implements the HTTP-specific representation of the 
		OpenC2 Message metadata. The OpenC2 Message metadata are described in 
		Table 3.1 of the Language Specification as message elements, but they are not
		framed in a concrete structure. The HTTP Specification defines such structure 
		in Sec. 3.3.2, and this class is its implementation.

		The methods of this class are meant to translate back and for the openc2lib
		`Message` class.
	"""
	headers: Headers = None
	""" Contains the `Message` metadata """
	body: Body = None # This is indeed not optional, but the default argument is set to preserve ordering
	""" Contains the `Content` """
	signature: str = None
	""" Not used (the Specification does not define its usage """

	def set(self, msg: oc2.Message):
		""" Create HTTP `Message` from openc2lib `Message` 
			
			:param msg: An openc2lib `Message`.
			:return: An HTTP `Message`
		"""
		self.headers = {}
		self.headers['request_id'] = msg.request_id
		self.headers['created'] = msg.created
		self.headers['from'] = msg.from_
		self.headers['to'] = msg.to

		self.body = Body(OpenC2Content(msg.content))

		
	def get(self):
		""" Create an openc2lib `Message` from HTTP `Message` 
			
			:param msg: An openc2lib `Message`.
			:return: An HTTP `Message`
		"""
		msg = oc2.Message(self.body.getObj().getObj())
		msg.request_id = self.headers['request_id'] if 'request_id' in self.headers.keys() else None
		msg.created = self.headers['created'] if 'created' in self.headers.keys() else None
		msg.from_ = self.headers['from'] if 'from' in self.headers.keys() else None
		msg.to = self.headers['to'] if 'to' in self.headers.keys() else None
		msg.msg_type = msg.content.getType()

		return msg





class HTTPTransfer(oc2.Transfer):
	def __init__(self, host, port = 80, endpoint = '/.well-known/openc2', usessl=False):
		self.host = host
		self.port = port
		self.endpoint = endpoint
		self.scheme = 'https' if usessl else 'http'
		self.url = f"{self.scheme}://{host}:{port}{endpoint}"
		self.ssl_context = None

	def tohttp(self, msg, encoder):
		m = Message()
		m.set(msg)

		# Encode the data
		if encoder is not None:
			data = encoder.encode(m)
		else:
			data = oc2.Encoder().encode(m)

		return data

	def fromhttp(self, hdr, data):

		# TODO: Check the HTTP headers for version/encoding
		content_type =hdr['Content-type']

		if not content_type.removeprefix('application/').startswith(oc2.Message.content_type):
			raise ValueError("Unsupported content type")

		enctype = content_type.removeprefix('application/'+oc2.Message.content_type+'+').split(';')[0]
		try:
			encoder = oc2.Encoders[enctype].value
		except KeyError:
			raise ValueError("Unsupported encoding scheme: " + enctype)

		# HTTP processing to extract the headers
		# and the transport body
		msg = encoder.decode(data, Message).get()
		msg.content_type = hdr['Content-type'].removeprefix('application/').split('+')[0]
		msg.version = oc2.Version.fromstr(hdr['Content-type'].split(';')[1].removeprefix("version="))
		msg.encoding = encoder

		
		try:
			msg.status = msg.content['status']
		except:
			msg.status = None


		return msg, encoder


	# This function is used to send an HTTP request
	def send(self, msg, encoder):
		# Convert the message to the specific HTTP representation
		openc2data = self.tohttp(msg, encoder)

		# Building the requested headers for the Request
		content_type = f"application/{msg.content_type}+{encoder.getName()};version={msg.version}"
		date = msg.created if msg.created else int(oc2.DateTime())
		openc2headers={'Content-Type': content_type, 'Accept': content_type, 'Date': oc2.DateTime(date).httpdate()}

		logger.info("Sending to %s", self.url)
		logger.info(" -> body: %s", openc2data)

		# Send the OpenC2 message and get the response
		if self.scheme == 'https':
			logger.warning("Certificate validation disabled!")
		response = requests.post(self.url, data=openc2data, headers=openc2headers, verify=False)
		logger.info("HTTP got response: %s", response)
	
		# TODO: How to manage HTTP response code? Can we safely assume they always match the Openc2 response?
		try:
			if response.text != "":
				msg = self.fromhttp(response.headers, response.text)
			else:
				msg = None
		except ValueError as e:
			msg = oc2.Message(oc2.Content())
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
			date = msg.created if msg.created else int(oc2.DateTime())
			data = self.tohttp(msg, encoder)
		else:
			content_type = None
			data = None
			date = int(oc2.DateTime())

		# Date is currently autmatically inserted by Flask (probably 
		# after I used 'make_response')
		#headers['Date'] = oc2.DateTime(date).httpdate()

		return headers, data

	def recv(self, headers, data):

		logger.debug("Received body: %s", data)
		msg, encoder = self.fromhttp(headers, data)
		logger.info("Received command: %s", msg)
  			
		return msg, encoder
	
	def receive(self, callback, encoder):
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
				content = oc2.Response(status=oc2.StatusCode.BADREQUEST, status_text=str(e))
				resp = oc2.Message(content)
				resp.content_type = oc2.Message.content_type
				resp.version = oc2.Message.version
				resp.encoder = encoder
				resp.status=oc2.StatusCode.BADREQUEST
			else:
				logger.info("Received command: %s", cmd)
				resp = callback(cmd)

			
			logger.debug("Got response: %s", resp)
			
			# TODO: Set HTTP headers as appropriate
			hdrs, data = server.respond(resp, encoder)
			logger.info("Sending response: %s", data)
			httpresp = make_response(data if data is not None else "") 
			httpresp.headers = hdrs

			if data is None:
				resp_code = 200
			else:
				resp_code = resp.status.value

			return httpresp, resp_code

		app.run(debug=True, host=self.host, port=self.port, ssl_context=self.ssl_context)


class HTTPSTransfer(HTTPTransfer):
	def __init__(self, host, port = 443, endpoint = '/.well-known/openc2'):
		HTTPTransfer.__init__(self, host, port, endpoint, usessl=True)
		self.ssl_context = "adhoc"


