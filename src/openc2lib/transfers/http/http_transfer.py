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
from openc2lib.transfers.http.message import Message


logger = logging.getLogger('openc2lib')
""" The logging facility in openc2lib """

class HTTPTransfer(oc2.Transfer):
	""" HTTP Transfer Protocol

		This class provides an implementation of the Specification. It builds on Flask and so it is not
		suitable for production environments.

		Use `HTTPTransfer` to build OpenC2 communication stacks in `Producer` and `Consumer`.
	"""
	def __init__(self, host, port = 80, endpoint = '/.well-known/openc2', usessl=False):
		""" Builds the `HTTPTransfer` instance

			The `host` and `port` parameters are used either for selecting the remote server (`Producer`) or
			for local binding (`Consumer`). This implementation only supports TCP as transport protocol.
			:param host: Hostname or IP address of the OpenC2 server.
			:param port: Transport port of the OpenC2 server.
			:param endpoint: The remote endpoint to contact the OpenC2 server (`Producer` only).
			:param usessl: Enable (`True`) or disable (`False`) SSL. Internal use only. Do not set this argument,
				use the `HTTPSTransfer` instead.
		"""
		self.host = host
		self.port = port
		self.endpoint = endpoint
		self.scheme = 'https' if usessl else 'http'
		self.url = f"{self.scheme}://{host}:{port}{endpoint}"
		self.ssl_context = None

	def _tohttp(self, msg, encoder):
		""" Convert openc2lib `Message` to HTTP `Message` """
		m = Message()
		m.set(msg)

		# Encode the data
		if encoder is not None:
			data = encoder.encode(m)
		else:
			data = oc2.Encoder().encode(m)

		return data

	def _fromhttp(self, hdr, data):
		""" Convert HTTP `Message` to openc2lib `Message` """

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
		""" Sends OpenC2 message

			This method implements the required `Transfer` interface to send message to an OpenC2 server.
			:param msg: The message to send (openc2lib `Message`).
			:param encoder: The encoder to use for encoding the `msg`.
			:return: An OpenC2  response (`Response`).
		"""
		# Convert the message to the specific HTTP representation
		openc2data = self._tohttp(msg, encoder)

		# Building the requested headers for the Request
		content_type = f"application/{msg.content_type}+{encoder.getName()};version={msg.version}"
		date = msg.created if msg.created else int(oc2.DateTime())
		openc2headers={'Content-Type': content_type, 'Accept': content_type, 'Date': oc2.DateTime(date).httpdate()}

		logger.info("Sending to %s", self.url)
		logger.info("HTTP Content:\n%s", openc2data)

		# Send the OpenC2 message and get the response
		if self.scheme == 'https':
			logger.warning("Certificate validation disabled!")
		response = requests.post(self.url, data=openc2data, headers=openc2headers, verify=False)
		logger.info("HTTP got response: %s", response)
	
		# TODO: How to manage HTTP response code? Can we safely assume they always match the Openc2 response?
		try:
			if response.text != "":
				msg = self._fromhttp(response.headers, response.text)
			else:
				msg = None
		except ValueError as e:
			msg = oc2.Message(oc2.Content())
			msg.status = response.status_code
			logger.error("Unable to parse data: >%s<", response.text)
			logger.error(str(e))

		return msg

	# This function is used to prepare the headers and content in a response
	def _respond(self, msg, encoder):
		""" Responds to received OpenC2 message """

		headers = {}
		if msg is not None:
			if encoder is not None:
				content_type = f"application/{msg.content_type}+{encoder.getName()};version={msg.version}"
			else:	
				content_type = f"text/plain"
			headers['Content-Type']= content_type
			date = msg.created if msg.created else int(oc2.DateTime())
			data = self._tohttp(msg, encoder)
		else:
			content_type = None
			data = None
			date = int(oc2.DateTime())

		# Date is currently autmatically inserted by Flask (probably 
		# after I used 'make_response')
		#headers['Date'] = oc2.DateTime(date).httpdate()

		return headers, data

	def _recv(self, headers, data):
		""" Retrieve HTTP messages
			
			Internal function to convert Flask data into openc2lib `Message` structure and `Encoder`.
			The `encoder` is derived from the HTTP header, to provide the ability to manage multiple
			clients that use different encoding formats.
			:param headers: HTTP headers.
			:param data: HTTP body.
			:return: An openc2lib `Message` (first) and an `Encoder` instance (second).
		"""

		logger.debug("Received body: %s", data)
		msg, encoder = self._fromhttp(headers, data)
		logger.info("Received command: %s", msg)
  			
		return msg, encoder
	
	def receive(self, callback, encoder):
		""" Listen for incoming messages

			This method implements the `Transfer` interface to listen for and receive OpenC2 messages.
			The internal implementation uses `Flask` as HTTP server. The method invokes the `callback`
			for each received message, which must be provided by a `Producer` to properly dispatch 
			`Command`s to the relevant server(s). It also takes an `Encoder` that is used to create
			responses to `Command`s encoded with unknown encoders.
			:param callback: The function that is invoked to process OpenC2 messages.
			:param encoder: Default `Encoder` instance to respond to unknown or wrong messages.
			:return :None
		"""
		app = Flask(__name__)
		app.config['OPENC2']=self
		app.config['CALLBACK']=callback
		app.config['ENCODER']=encoder

		@app.route(self.endpoint, methods=['POST'])
		def _consumer():
			""" Serving endpoint for `Flask` """
			server = app.config['OPENC2']
			callback = app.config['CALLBACK']
			encoder=app.config['ENCODER']
			
			try:
				cmd, encoder = server._recv(request.headers, request.data.decode('UTF-8') )
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
			hdrs, data = server._respond(resp, encoder)
			logger.info("Sending response:\n%s", data)
			httpresp = make_response(data if data is not None else "") 
			httpresp.headers = hdrs

			if data is None:
				resp_code = 200
			else:
				resp_code = resp.status.value

			return httpresp, resp_code

		app.run(debug=True, host=self.host, port=self.port, ssl_context=self.ssl_context)


class HTTPSTransfer(HTTPTransfer):
	""" HTTP Transfer Protocol with SSL

		This class provides an implementation of the Specification. It builds on Flask and so it is not
		suitable for production environments.

		Use `HTTPSTransfer` to build OpenC2 communication stacks in `Producer` and `Consumer`.
		Usage and methods of `HTTPSTransfer` are semanthically the same as for `HTTPTransfer`.
	"""
	def __init__(self, host, port = 443, endpoint = '/.well-known/openc2'):
		""" Builds the `HTTPSTransfer` instance

			The `host` and `port` parameters are used either for selecting the remote server (`Producer`) or
			for local binding (`Consumer`). This implementation only supports TCP as transport protocol.
			:param host: Hostname or IP address of the OpenC2 server.
			:param port: Transport port of the OpenC2 server.
			:param endpoint: The remote endpoint to contact the OpenC2 server (`Producer` only).
		"""
		HTTPTransfer.__init__(self, host, port, endpoint, usessl=True)
		self.ssl_context = "adhoc"


