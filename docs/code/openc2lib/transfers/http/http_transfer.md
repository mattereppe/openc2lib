![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAzMCAzMCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLW1pdGVybGltaXQ9IjEwIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik00IDdoMjJNNCAxNWgyMk00IDIzaDIyIiAvPjwvc3ZnPg==)

<div>

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0iYmkgYmktYm94LWFycm93LWluLWxlZnQiIHZpZXdib3g9IjAgMCAxNiAxNiI+CiAgPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMTAgMy41YS41LjUgMCAwIDAtLjUtLjVoLThhLjUuNSAwIDAgMC0uNS41djlhLjUuNSAwIDAgMCAuNS41aDhhLjUuNSAwIDAgMCAuNS0uNXYtMmEuNS41IDAgMCAxIDEgMHYyQTEuNSAxLjUgMCAwIDEgOS41IDE0aC04QTEuNSAxLjUgMCAwIDEgMCAxMi41di05QTEuNSAxLjUgMCAwIDEgMS41IDJoOEExLjUgMS41IDAgMCAxIDExIDMuNXYyYS41LjUgMCAwIDEtMSAwdi0yeiIgLz4KICA8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00LjE0NiA4LjM1NGEuNS41IDAgMCAxIDAtLjcwOGwzLTNhLjUuNSAwIDEgMSAuNzA4LjcwOEw1LjcwNyA3LjVIMTQuNWEuNS41IDAgMCAxIDAgMUg1LjcwN2wyLjE0NyAyLjE0NmEuNS41IDAgMCAxLS43MDguNzA4bC0zLTN6IiAvPgo8L3N2Zz4=){.bi
.bi-box-arrow-in-left}
 openc2lib.transfers.http](../http.html){.pdoc-button
.module-list-button}

## API Documentation

-   [logger](#logger){.variable}
-   [HTTPTransfer](#HTTPTransfer){.class}
    -   [HTTPTransfer](#HTTPTransfer.__init__){.function}
    -   [host](#HTTPTransfer.host){.variable}
    -   [port](#HTTPTransfer.port){.variable}
    -   [endpoint](#HTTPTransfer.endpoint){.variable}
    -   [scheme](#HTTPTransfer.scheme){.variable}
    -   [url](#HTTPTransfer.url){.variable}
    -   [ssl_context](#HTTPTransfer.ssl_context){.variable}
    -   [send](#HTTPTransfer.send){.function}
    -   [receive](#HTTPTransfer.receive){.function}
-   [HTTPSTransfer](#HTTPSTransfer){.class}
    -   [HTTPSTransfer](#HTTPSTransfer.__init__){.function}
    -   [ssl_context](#HTTPSTransfer.ssl_context){.variable}

[built with [pdoc]{.visually-hidden}![pdoc
logo](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20role%3D%22img%22%20aria-label%3D%22pdoc%20logo%22%20width%3D%22300%22%20height%3D%22150%22%20viewBox%3D%22-1%200%2060%2030%22%3E%3Ctitle%3Epdoc%3C/title%3E%3Cpath%20d%3D%22M29.621%2021.293c-.011-.273-.214-.475-.511-.481a.5.5%200%200%200-.489.503l-.044%201.393c-.097.551-.695%201.215-1.566%201.704-.577.428-1.306.486-2.193.182-1.426-.617-2.467-1.654-3.304-2.487l-.173-.172a3.43%203.43%200%200%200-.365-.306.49.49%200%200%200-.286-.196c-1.718-1.06-4.931-1.47-7.353.191l-.219.15c-1.707%201.187-3.413%202.131-4.328%201.03-.02-.027-.49-.685-.141-1.763.233-.721.546-2.408.772-4.076.042-.09.067-.187.046-.288.166-1.347.277-2.625.241-3.351%201.378-1.008%202.271-2.586%202.271-4.362%200-.976-.272-1.935-.788-2.774-.057-.094-.122-.18-.184-.268.033-.167.052-.339.052-.516%200-1.477-1.202-2.679-2.679-2.679-.791%200-1.496.352-1.987.9a6.3%206.3%200%200%200-1.001.029c-.492-.564-1.207-.929-2.012-.929-1.477%200-2.679%201.202-2.679%202.679A2.65%202.65%200%200%200%20.97%206.554c-.383.747-.595%201.572-.595%202.41%200%202.311%201.507%204.29%203.635%205.107-.037.699-.147%202.27-.423%203.294l-.137.461c-.622%202.042-2.515%208.257%201.727%2010.643%201.614.908%203.06%201.248%204.317%201.248%202.665%200%204.492-1.524%205.322-2.401%201.476-1.559%202.886-1.854%206.491.82%201.877%201.393%203.514%201.753%204.861%201.068%202.223-1.713%202.811-3.867%203.399-6.374.077-.846.056-1.469.054-1.537zm-4.835%204.313c-.054.305-.156.586-.242.629-.034-.007-.131-.022-.307-.157-.145-.111-.314-.478-.456-.908.221.121.432.25.675.355.115.039.219.051.33.081zm-2.251-1.238c-.05.33-.158.648-.252.694-.022.001-.125-.018-.307-.157-.217-.166-.488-.906-.639-1.573.358.344.754.693%201.198%201.036zm-3.887-2.337c-.006-.116-.018-.231-.041-.342.635.145%201.189.368%201.599.625.097.231.166.481.174.642-.03.049-.055.101-.067.158-.046.013-.128.026-.298.004-.278-.037-.901-.57-1.367-1.087zm-1.127-.497c.116.306.176.625.12.71-.019.014-.117.045-.345.016-.206-.027-.604-.332-.986-.695.41-.051.816-.056%201.211-.031zm-4.535%201.535c.209.22.379.47.358.598-.006.041-.088.138-.351.234-.144.055-.539-.063-.979-.259a11.66%2011.66%200%200%200%20.972-.573zm.983-.664c.359-.237.738-.418%201.126-.554.25.237.479.548.457.694-.006.042-.087.138-.351.235-.174.064-.694-.105-1.232-.375zm-3.381%201.794c-.022.145-.061.29-.149.401-.133.166-.358.248-.69.251h-.002c-.133%200-.306-.26-.45-.621.417.091.854.07%201.291-.031zm-2.066-8.077a4.78%204.78%200%200%201-.775-.584c.172-.115.505-.254.88-.378l-.105.962zm-.331%202.302a10.32%2010.32%200%200%201-.828-.502c.202-.143.576-.328.984-.49l-.156.992zm-.45%202.157l-.701-.403c.214-.115.536-.249.891-.376a11.57%2011.57%200%200%201-.19.779zm-.181%201.716c.064.398.194.702.298.893-.194-.051-.435-.162-.736-.398.061-.119.224-.3.438-.495zM8.87%204.141c0%20.152-.123.276-.276.276s-.275-.124-.275-.276.123-.276.276-.276.275.124.275.276zm-.735-.389a1.15%201.15%200%200%200-.314.783%201.16%201.16%200%200%200%201.162%201.162c.457%200%20.842-.27%201.032-.653.026.117.042.238.042.362a1.68%201.68%200%200%201-1.679%201.679%201.68%201.68%200%200%201-1.679-1.679c0-.843.626-1.535%201.436-1.654zM5.059%205.406A1.68%201.68%200%200%201%203.38%207.085a1.68%201.68%200%200%201-1.679-1.679c0-.037.009-.072.011-.109.21.3.541.508.935.508a1.16%201.16%200%200%200%201.162-1.162%201.14%201.14%200%200%200-.474-.912c.015%200%20.03-.005.045-.005.926.001%201.679.754%201.679%201.68zM3.198%204.141c0%20.152-.123.276-.276.276s-.275-.124-.275-.276.123-.276.276-.276.275.124.275.276zM1.375%208.964c0-.52.103-1.035.288-1.52.466.394%201.06.64%201.717.64%201.144%200%202.116-.725%202.499-1.738.383%201.012%201.355%201.738%202.499%201.738.867%200%201.631-.421%202.121-1.062.307.605.478%201.267.478%201.942%200%202.486-2.153%204.51-4.801%204.51s-4.801-2.023-4.801-4.51zm24.342%2019.349c-.985.498-2.267.168-3.813-.979-3.073-2.281-5.453-3.199-7.813-.705-1.315%201.391-4.163%203.365-8.423.97-3.174-1.786-2.239-6.266-1.261-9.479l.146-.492c.276-1.02.395-2.457.444-3.268a6.11%206.11%200%200%200%201.18.115%206.01%206.01%200%200%200%202.536-.562l-.006.175c-.802.215-1.848.612-2.021%201.25-.079.295.021.601.274.837.219.203.415.364.598.501-.667.304-1.243.698-1.311%201.179-.02.144-.022.507.393.787.213.144.395.26.564.365-1.285.521-1.361.96-1.381%201.126-.018.142-.011.496.427.746l.854.489c-.473.389-.971.914-.999%201.429-.018.278.095.532.316.713.675.556%201.231.721%201.653.721.059%200%20.104-.014.158-.02.207.707.641%201.64%201.513%201.64h.013c.8-.008%201.236-.345%201.462-.626.173-.216.268-.457.325-.692.424.195.93.374%201.372.374.151%200%20.294-.021.423-.068.732-.27.944-.704.993-1.021.009-.061.003-.119.002-.179.266.086.538.147.789.147.15%200%20.294-.021.423-.069.542-.2.797-.489.914-.754.237.147.478.258.704.288.106.014.205.021.296.021.356%200%20.595-.101.767-.229.438.435%201.094.992%201.656%201.067.106.014.205.021.296.021a1.56%201.56%200%200%200%20.323-.035c.17.575.453%201.289.866%201.605.358.273.665.362.914.362a.99.99%200%200%200%20.421-.093%201.03%201.03%200%200%200%20.245-.164c.168.428.39.846.68%201.068.358.273.665.362.913.362a.99.99%200%200%200%20.421-.093c.317-.148.512-.448.639-.762.251.157.495.257.726.257.127%200%20.25-.024.37-.071.427-.17.706-.617.841-1.314.022-.015.047-.022.068-.038.067-.051.133-.104.196-.159-.443%201.486-1.107%202.761-2.086%203.257zM8.66%209.925a.5.5%200%201%200-1%200c0%20.653-.818%201.205-1.787%201.205s-1.787-.552-1.787-1.205a.5.5%200%201%200-1%200c0%201.216%201.25%202.205%202.787%202.205s2.787-.989%202.787-2.205zm4.4%2015.965l-.208.097c-2.661%201.258-4.708%201.436-6.086.527-1.542-1.017-1.88-3.19-1.844-4.198a.4.4%200%200%200-.385-.414c-.242-.029-.406.164-.414.385-.046%201.249.367%203.686%202.202%204.896.708.467%201.547.7%202.51.7%201.248%200%202.706-.392%204.362-1.174l.185-.086a.4.4%200%200%200%20.205-.527c-.089-.204-.326-.291-.527-.206zM9.547%202.292c.093.077.205.114.317.114a.5.5%200%200%200%20.318-.886L8.817.397a.5.5%200%200%200-.703.068.5.5%200%200%200%20.069.703l1.364%201.124zm-7.661-.065c.086%200%20.173-.022.253-.068l1.523-.893a.5.5%200%200%200-.506-.863l-1.523.892a.5.5%200%200%200-.179.685c.094.158.261.247.432.247z%22%20transform%3D%22matrix%28-1%200%200%201%2058%200%29%22%20fill%3D%22%233bb300%22/%3E%3Cpath%20d%3D%22M.3%2021.86V10.18q0-.46.02-.68.04-.22.18-.5.28-.54%201.34-.54%201.06%200%201.42.28.38.26.44.78.76-1.04%202.38-1.04%201.64%200%203.1%201.54%201.46%201.54%201.46%203.58%200%202.04-1.46%203.58-1.44%201.54-3.08%201.54-1.64%200-2.38-.92v4.04q0%20.46-.04.68-.02.22-.18.5-.14.3-.5.42-.36.12-.98.12-.62%200-1-.12-.36-.12-.52-.4-.14-.28-.18-.5-.02-.22-.02-.68zm3.96-9.42q-.46.54-.46%201.18%200%20.64.46%201.18.48.52%201.2.52.74%200%201.24-.52.52-.52.52-1.18%200-.66-.48-1.18-.48-.54-1.26-.54-.76%200-1.22.54zm14.741-8.36q.16-.3.54-.42.38-.12%201-.12.64%200%201.02.12.38.12.52.42.16.3.18.54.04.22.04.68v11.94q0%20.46-.04.7-.02.22-.18.5-.3.54-1.7.54-1.38%200-1.54-.98-.84.96-2.34.96-1.8%200-3.28-1.56-1.48-1.58-1.48-3.66%200-2.1%201.48-3.68%201.5-1.58%203.28-1.58%201.48%200%202.3%201v-4.2q0-.46.02-.68.04-.24.18-.52zm-3.24%2010.86q.52.54%201.26.54.74%200%201.22-.54.5-.54.5-1.18%200-.66-.48-1.22-.46-.56-1.26-.56-.8%200-1.28.56-.48.54-.48%201.2%200%20.66.52%201.2zm7.833-1.2q0-2.4%201.68-3.96%201.68-1.56%203.84-1.56%202.16%200%203.82%201.56%201.66%201.54%201.66%203.94%200%201.66-.86%202.96-.86%201.28-2.1%201.9-1.22.6-2.54.6-1.32%200-2.56-.64-1.24-.66-2.1-1.92-.84-1.28-.84-2.88zm4.18%201.44q.64.48%201.3.48.66%200%201.32-.5.66-.5.66-1.48%200-.98-.62-1.46-.62-.48-1.34-.48-.72%200-1.34.5-.62.5-.62%201.48%200%20.96.64%201.46zm11.412-1.44q0%20.84.56%201.32.56.46%201.18.46.64%200%201.18-.36.56-.38.9-.38.6%200%201.46%201.06.46.58.46%201.04%200%20.76-1.1%201.42-1.14.8-2.8.8-1.86%200-3.58-1.34-.82-.64-1.34-1.7-.52-1.08-.52-2.36%200-1.3.52-2.34.52-1.06%201.34-1.7%201.66-1.32%203.54-1.32.76%200%201.48.22.72.2%201.06.4l.32.2q.36.24.56.38.52.4.52.92%200%20.5-.42%201.14-.72%201.1-1.38%201.1-.38%200-1.08-.44-.36-.34-1.04-.34-.66%200-1.24.48-.58.48-.58%201.34z%22%20fill%3D%22green%22/%3E%3C/svg%3E)](https://pdoc.dev "pdoc: Python API documentation generator"){.attribution
target="_blank"}

</div>

:::::::::::::::::::::::::::::::::::::::::::::::: {.pdoc role="main"}
::::: {.section .module-info}
# [openc2lib](./../../../openc2lib.html).[transfers](./../../transfers.html).[http](./../http.html).http_transfer {#openc2lib.transfers.http.http_transfer .modulename}

::: docstring
HTTP Transfer Protocol

This module defines implementation of the `Transfer` interface for the
HTTP/HTTPs protocols. This implementation is mostly provided for
research and development purposes, but it is not suitable for production
environments.

The implementation follows the Specification for Transfer of OpenC2
Messages via HTTPS Version 1.1, which is indicated as the
\"Specification\" in the following.
:::

View Source

::: {.pdoc-code .codehilite}
      1""" HTTP Transfer Protocol
      2
      3  This module defines implementation of the `Transfer` interface for the 
      4      HTTP/HTTPs protocols. This implementation is mostly provided for 
      5  research and development purposes, but it is not suitable for production
      6  environments.
      7
      8  The implementation follows the Specification for Transfer of OpenC2 Messages via HTTPS
      9  Version 1.1, which is indicated as the "Specification" in the following.
     10"""
     11import dataclasses
     12import requests
     13import logging
     14import copy
     15
     16from flask import Flask, request, make_response
     17
     18import openc2lib as oc2
     19from openc2lib.transfers.http.message import Message
     20
     21
     22logger = logging.getLogger('openc2lib')
     23""" The logging facility in openc2lib """
     24
     25class HTTPTransfer(oc2.Transfer):
     26 """ HTTP Transfer Protocol
     27
     28        This class provides an implementation of the Specification. It builds on Flask and so it is not
     29        suitable for production environments.
     30
     31        Use `HTTPTransfer` to build OpenC2 communication stacks in `Producer` and `Consumer`.
     32    """
     33 def __init__(self, host, port = 80, endpoint = '/.well-known/openc2', usessl=False):
     34     """ Builds the `HTTPTransfer` instance
     35
     36            The `host` and `port` parameters are used either for selecting the remote server (`Producer`) or
     37            for local binding (`Consumer`). This implementation only supports TCP as transport protocol.
     38            :param host: Hostname or IP address of the OpenC2 server.
     39            :param port: Transport port of the OpenC2 server.
     40            :param endpoint: The remote endpoint to contact the OpenC2 server (`Producer` only).
     41            :param usessl: Enable (`True`) or disable (`False`) SSL. Internal use only. Do not set this argument,
     42                use the `HTTPSTransfer` instead.
     43        """
     44     self.host = host
     45     self.port = port
     46     self.endpoint = endpoint
     47     self.scheme = 'https' if usessl else 'http'
     48     self.url = f"{self.scheme}://{host}:{port}{endpoint}"
     49     self.ssl_context = None
     50
     51 def _tohttp(self, msg, encoder):
     52     """ Convert openc2lib `Message` to HTTP `Message` """
     53     m = Message()
     54     m.set(msg)
     55
     56     # Encode the data
     57     if encoder is not None:
     58         data = encoder.encode(m)
     59     else:
     60         data = oc2.Encoder().encode(m)
     61
     62     return data
     63
     64 def _fromhttp(self, hdr, data):
     65     """ Convert HTTP `Message` to openc2lib `Message` """
     66
     67     # TODO: Check the HTTP headers for version/encoding
     68     content_type =hdr['Content-type']
     69
     70     if not content_type.removeprefix('application/').startswith(oc2.Message.content_type):
     71         raise ValueError("Unsupported content type")
     72
     73     enctype = content_type.removeprefix('application/'+oc2.Message.content_type+'+').split(';')[0]
     74     try:
     75         encoder = oc2.Encoders[enctype].value
     76     except KeyError:
     77         raise ValueError("Unsupported encoding scheme: " + enctype)
     78
     79     # HTTP processing to extract the headers
     80     # and the transport body
     81     msg = encoder.decode(data, Message).get()
     82     msg.content_type = hdr['Content-type'].removeprefix('application/').split('+')[0]
     83     msg.version = oc2.Version.fromstr(hdr['Content-type'].split(';')[1].removeprefix("version="))
     84     msg.encoding = encoder
     85
     86     
     87     try:
     88         msg.status = msg.content['status']
     89     except:
     90         msg.status = None
     91
     92
     93     return msg, encoder
     94
     95
     96 # This function is used to send an HTTP request
     97 def send(self, msg, encoder):
     98     """ Sends OpenC2 message
     99
    100          This method implements the required `Transfer` interface to send message to an OpenC2 server.
    101          :param msg: The message to send (openc2lib `Message`).
    102          :param encoder: The encoder to use for encoding the `msg`.
    103          :return: An OpenC2  response (`Response`).
    104      """
    105       # Convert the message to the specific HTTP representation
    106       openc2data = self._tohttp(msg, encoder)
    107
    108       # Building the requested headers for the Request
    109       content_type = f"application/{msg.content_type}+{encoder.getName()};version={msg.version}"
    110       date = msg.created if msg.created else int(oc2.DateTime())
    111       openc2headers={'Content-Type': content_type, 'Accept': content_type, 'Date': oc2.DateTime(date).httpdate()}
    112
    113       logger.info("Sending to %s", self.url)
    114       logger.info(" -> body: %s", openc2data)
    115
    116       # Send the OpenC2 message and get the response
    117       if self.scheme == 'https':
    118           logger.warning("Certificate validation disabled!")
    119       response = requests.post(self.url, data=openc2data, headers=openc2headers, verify=False)
    120       logger.info("HTTP got response: %s", response)
    121   
    122       # TODO: How to manage HTTP response code? Can we safely assume they always match the Openc2 response?
    123       try:
    124           if response.text != "":
    125               msg = self._fromhttp(response.headers, response.text)
    126           else:
    127               msg = None
    128       except ValueError as e:
    129           msg = oc2.Message(oc2.Content())
    130           msg.status = response.status_code
    131           logger.error("Unable to parse data: >%s<", response.text)
    132           logger.error(str(e))
    133
    134       return msg
    135
    136   # This function is used to prepare the headers and content in a response
    137   def _respond(self, msg, encoder):
    138       """ Responds to received OpenC2 message """
    139
    140       headers = {}
    141       if msg is not None:
    142           if encoder is not None:
    143               content_type = f"application/{msg.content_type}+{encoder.getName()};version={msg.version}"
    144           else: 
    145               content_type = f"text/plain"
    146           headers['Content-Type']= content_type
    147           date = msg.created if msg.created else int(oc2.DateTime())
    148           data = self._tohttp(msg, encoder)
    149       else:
    150           content_type = None
    151           data = None
    152           date = int(oc2.DateTime())
    153
    154       # Date is currently autmatically inserted by Flask (probably 
    155       # after I used 'make_response')
    156       #headers['Date'] = oc2.DateTime(date).httpdate()
    157
    158       return headers, data
    159
    160   def _recv(self, headers, data):
    161       """ Retrieve HTTP messages
    162          
    163          Internal function to convert Flask data into openc2lib `Message` structure and `Encoder`.
    164          The `encoder` is derived from the HTTP header, to provide the ability to manage multiple
    165          clients that use different encoding formats.
    166          :param headers: HTTP headers.
    167          :param data: HTTP body.
    168          :return: An openc2lib `Message` (first) and an `Encoder` instance (second).
    169      """
    170
    171       logger.debug("Received body: %s", data)
    172       msg, encoder = self._fromhttp(headers, data)
    173       logger.info("Received command: %s", msg)
    174           
    175       return msg, encoder
    176   
    177   def receive(self, callback, encoder):
    178       """ Listen for incoming messages
    179
    180          This method implements the `Transfer` interface to listen for and receive OpenC2 messages.
    181          The internal implementation uses `Flask` as HTTP server. The method invokes the `callback`
    182          for each received message, which must be provided by a `Producer` to properly dispatch 
    183          `Command`s to the relevant server(s). It also takes an `Encoder` that is used to create
    184          responses to `Command`s encoded with unknown encoders.
    185          :param callback: The function that is invoked to process OpenC2 messages.
    186          :param encoder: Default `Encoder` instance to respond to unknown or wrong messages.
    187          :return :None
    188      """
    189       app = Flask(__name__)
    190       app.config['OPENC2']=self
    191       app.config['CALLBACK']=callback
    192       app.config['ENCODER']=encoder
    193
    194       @app.route(self.endpoint, methods=['POST'])
    195       def _consumer():
    196           """ Serving endpoint for `Flask` """
    197           server = app.config['OPENC2']
    198           callback = app.config['CALLBACK']
    199           encoder=app.config['ENCODER']
    200           
    201           try:
    202               cmd, encoder = server._recv(request.headers, request.data.decode('UTF-8') )
    203               # TODO: Add the code to answer according to 'response_requested'
    204           except ValueError as e:
    205               # TODO: Find better formatting (what should be returned if the request is not understood?)
    206               content = oc2.Response(status=oc2.StatusCode.BADREQUEST, status_text=str(e))
    207               resp = oc2.Message(content)
    208               resp.content_type = oc2.Message.content_type
    209               resp.version = oc2.Message.version
    210               resp.encoder = encoder
    211               resp.status=oc2.StatusCode.BADREQUEST
    212           else:
    213               logger.info("Received command: %s", cmd)
    214               resp = callback(cmd)
    215
    216           
    217           logger.debug("Got response: %s", resp)
    218           
    219           # TODO: Set HTTP headers as appropriate
    220           hdrs, data = server._respond(resp, encoder)
    221           logger.info("Sending response: %s", data)
    222           httpresp = make_response(data if data is not None else "") 
    223           httpresp.headers = hdrs
    224
    225           if data is None:
    226               resp_code = 200
    227           else:
    228               resp_code = resp.status.value
    229
    230           return httpresp, resp_code
    231
    232       app.run(debug=True, host=self.host, port=self.port, ssl_context=self.ssl_context)
    233
    234
    235class HTTPSTransfer(HTTPTransfer):
    236   """ HTTP Transfer Protocol with SSL
    237
    238      This class provides an implementation of the Specification. It builds on Flask and so it is not
    239      suitable for production environments.
    240
    241      Use `HTTPSTransfer` to build OpenC2 communication stacks in `Producer` and `Consumer`.
    242      Usage and methods of `HTTPSTransfer` are semanthically the same as for `HTTPTransfer`.
    243  """
    244   def __init__(self, host, port = 443, endpoint = '/.well-known/openc2'):
    245       """ Builds the `HTTPSTransfer` instance
    246
    247          The `host` and `port` parameters are used either for selecting the remote server (`Producer`) or
    248          for local binding (`Consumer`). This implementation only supports TCP as transport protocol.
    249          :param host: Hostname or IP address of the OpenC2 server.
    250          :param port: Transport port of the OpenC2 server.
    251          :param endpoint: The remote endpoint to contact the OpenC2 server (`Producer` only).
    252      """
    253       HTTPTransfer.__init__(self, host, port, endpoint, usessl=True)
    254       self.ssl_context = "adhoc"
:::
:::::

::::: {#logger .section}
::: {.attr .variable}
[logger]{.name} = [\<Logger openc2lib (WARNING)\>]{.default_value}
:::

[](#logger){.headerlink}

::: docstring
The logging facility in openc2lib
:::
:::::

:::::::::::::::::::::::::::::: {#HTTPTransfer .section}
::: {.attr .class}
[class]{.def}
[HTTPTransfer]{.name}([[openc2lib.core.transfer.Transfer](../../core/transfer.html#Transfer)]{.base}):
View Source
:::

[](#HTTPTransfer){.headerlink}

::: {.pdoc-code .codehilite}
     26class HTTPTransfer(oc2.Transfer):
     27   """ HTTP Transfer Protocol
     28
     29      This class provides an implementation of the Specification. It builds on Flask and so it is not
     30      suitable for production environments.
     31
     32      Use `HTTPTransfer` to build OpenC2 communication stacks in `Producer` and `Consumer`.
     33  """
     34   def __init__(self, host, port = 80, endpoint = '/.well-known/openc2', usessl=False):
     35       """ Builds the `HTTPTransfer` instance
     36
     37          The `host` and `port` parameters are used either for selecting the remote server (`Producer`) or
     38          for local binding (`Consumer`). This implementation only supports TCP as transport protocol.
     39          :param host: Hostname or IP address of the OpenC2 server.
     40          :param port: Transport port of the OpenC2 server.
     41          :param endpoint: The remote endpoint to contact the OpenC2 server (`Producer` only).
     42          :param usessl: Enable (`True`) or disable (`False`) SSL. Internal use only. Do not set this argument,
     43              use the `HTTPSTransfer` instead.
     44      """
     45       self.host = host
     46       self.port = port
     47       self.endpoint = endpoint
     48       self.scheme = 'https' if usessl else 'http'
     49       self.url = f"{self.scheme}://{host}:{port}{endpoint}"
     50       self.ssl_context = None
     51
     52   def _tohttp(self, msg, encoder):
     53       """ Convert openc2lib `Message` to HTTP `Message` """
     54       m = Message()
     55       m.set(msg)
     56
     57       # Encode the data
     58       if encoder is not None:
     59           data = encoder.encode(m)
     60       else:
     61           data = oc2.Encoder().encode(m)
     62
     63       return data
     64
     65   def _fromhttp(self, hdr, data):
     66       """ Convert HTTP `Message` to openc2lib `Message` """
     67
     68       # TODO: Check the HTTP headers for version/encoding
     69       content_type =hdr['Content-type']
     70
     71       if not content_type.removeprefix('application/').startswith(oc2.Message.content_type):
     72           raise ValueError("Unsupported content type")
     73
     74       enctype = content_type.removeprefix('application/'+oc2.Message.content_type+'+').split(';')[0]
     75       try:
     76           encoder = oc2.Encoders[enctype].value
     77       except KeyError:
     78           raise ValueError("Unsupported encoding scheme: " + enctype)
     79
     80       # HTTP processing to extract the headers
     81       # and the transport body
     82       msg = encoder.decode(data, Message).get()
     83       msg.content_type = hdr['Content-type'].removeprefix('application/').split('+')[0]
     84       msg.version = oc2.Version.fromstr(hdr['Content-type'].split(';')[1].removeprefix("version="))
     85       msg.encoding = encoder
     86
     87       
     88       try:
     89           msg.status = msg.content['status']
     90       except:
     91           msg.status = None
     92
     93
     94       return msg, encoder
     95
     96
     97   # This function is used to send an HTTP request
     98   def send(self, msg, encoder):
     99       """ Sends OpenC2 message
    100
    101            This method implements the required `Transfer` interface to send message to an OpenC2 server.
    102            :param msg: The message to send (openc2lib `Message`).
    103            :param encoder: The encoder to use for encoding the `msg`.
    104            :return: An OpenC2  response (`Response`).
    105        """
    106     # Convert the message to the specific HTTP representation
    107     openc2data = self._tohttp(msg, encoder)
    108
    109     # Building the requested headers for the Request
    110     content_type = f"application/{msg.content_type}+{encoder.getName()};version={msg.version}"
    111     date = msg.created if msg.created else int(oc2.DateTime())
    112     openc2headers={'Content-Type': content_type, 'Accept': content_type, 'Date': oc2.DateTime(date).httpdate()}
    113
    114     logger.info("Sending to %s", self.url)
    115     logger.info(" -> body: %s", openc2data)
    116
    117     # Send the OpenC2 message and get the response
    118     if self.scheme == 'https':
    119         logger.warning("Certificate validation disabled!")
    120     response = requests.post(self.url, data=openc2data, headers=openc2headers, verify=False)
    121     logger.info("HTTP got response: %s", response)
    122 
    123     # TODO: How to manage HTTP response code? Can we safely assume they always match the Openc2 response?
    124     try:
    125         if response.text != "":
    126             msg = self._fromhttp(response.headers, response.text)
    127         else:
    128             msg = None
    129     except ValueError as e:
    130         msg = oc2.Message(oc2.Content())
    131         msg.status = response.status_code
    132         logger.error("Unable to parse data: >%s<", response.text)
    133         logger.error(str(e))
    134
    135     return msg
    136
    137 # This function is used to prepare the headers and content in a response
    138 def _respond(self, msg, encoder):
    139     """ Responds to received OpenC2 message """
    140
    141     headers = {}
    142     if msg is not None:
    143         if encoder is not None:
    144             content_type = f"application/{msg.content_type}+{encoder.getName()};version={msg.version}"
    145         else: 
    146             content_type = f"text/plain"
    147         headers['Content-Type']= content_type
    148         date = msg.created if msg.created else int(oc2.DateTime())
    149         data = self._tohttp(msg, encoder)
    150     else:
    151         content_type = None
    152         data = None
    153         date = int(oc2.DateTime())
    154
    155     # Date is currently autmatically inserted by Flask (probably 
    156     # after I used 'make_response')
    157     #headers['Date'] = oc2.DateTime(date).httpdate()
    158
    159     return headers, data
    160
    161 def _recv(self, headers, data):
    162     """ Retrieve HTTP messages
    163            
    164            Internal function to convert Flask data into openc2lib `Message` structure and `Encoder`.
    165            The `encoder` is derived from the HTTP header, to provide the ability to manage multiple
    166            clients that use different encoding formats.
    167            :param headers: HTTP headers.
    168            :param data: HTTP body.
    169            :return: An openc2lib `Message` (first) and an `Encoder` instance (second).
    170        """
    171
    172     logger.debug("Received body: %s", data)
    173     msg, encoder = self._fromhttp(headers, data)
    174     logger.info("Received command: %s", msg)
    175             
    176     return msg, encoder
    177 
    178 def receive(self, callback, encoder):
    179     """ Listen for incoming messages
    180
    181            This method implements the `Transfer` interface to listen for and receive OpenC2 messages.
    182            The internal implementation uses `Flask` as HTTP server. The method invokes the `callback`
    183            for each received message, which must be provided by a `Producer` to properly dispatch 
    184            `Command`s to the relevant server(s). It also takes an `Encoder` that is used to create
    185            responses to `Command`s encoded with unknown encoders.
    186            :param callback: The function that is invoked to process OpenC2 messages.
    187            :param encoder: Default `Encoder` instance to respond to unknown or wrong messages.
    188            :return :None
    189        """
    190     app = Flask(__name__)
    191     app.config['OPENC2']=self
    192     app.config['CALLBACK']=callback
    193     app.config['ENCODER']=encoder
    194
    195     @app.route(self.endpoint, methods=['POST'])
    196     def _consumer():
    197         """ Serving endpoint for `Flask` """
    198         server = app.config['OPENC2']
    199         callback = app.config['CALLBACK']
    200         encoder=app.config['ENCODER']
    201         
    202         try:
    203             cmd, encoder = server._recv(request.headers, request.data.decode('UTF-8') )
    204             # TODO: Add the code to answer according to 'response_requested'
    205         except ValueError as e:
    206             # TODO: Find better formatting (what should be returned if the request is not understood?)
    207             content = oc2.Response(status=oc2.StatusCode.BADREQUEST, status_text=str(e))
    208             resp = oc2.Message(content)
    209             resp.content_type = oc2.Message.content_type
    210             resp.version = oc2.Message.version
    211             resp.encoder = encoder
    212             resp.status=oc2.StatusCode.BADREQUEST
    213         else:
    214             logger.info("Received command: %s", cmd)
    215             resp = callback(cmd)
    216
    217         
    218         logger.debug("Got response: %s", resp)
    219         
    220         # TODO: Set HTTP headers as appropriate
    221         hdrs, data = server._respond(resp, encoder)
    222         logger.info("Sending response: %s", data)
    223         httpresp = make_response(data if data is not None else "") 
    224         httpresp.headers = hdrs
    225
    226         if data is None:
    227             resp_code = 200
    228         else:
    229             resp_code = resp.status.value
    230
    231         return httpresp, resp_code
    232
    233     app.run(debug=True, host=self.host, port=self.port, ssl_context=self.ssl_context)
:::

::: docstring
HTTP Transfer Protocol

This class provides an implementation of the Specification. It builds on
Flask and so it is not suitable for production environments.

Use [`HTTPTransfer`](#HTTPTransfer) to build OpenC2 communication stacks
in `Producer` and `Consumer`.
:::

:::::: {#HTTPTransfer.__init__ .classattr}
::: {.attr .function}
[HTTPTransfer]{.name}[([[host]{.n},
]{.param}[[port]{.n}[=]{.o}[80]{.mi},
]{.param}[[endpoint]{.n}[=]{.o}[\'/.well-known/openc2\']{.s1},
]{.param}[[usessl]{.n}[=]{.o}[False]{.kc}]{.param})]{.signature
.pdoc-code .condensed} View Source
:::

[](#HTTPTransfer.__init__){.headerlink}

::: {.pdoc-code .codehilite}
    34 def __init__(self, host, port = 80, endpoint = '/.well-known/openc2', usessl=False):
    35      """ Builds the `HTTPTransfer` instance
    36
    37         The `host` and `port` parameters are used either for selecting the remote server (`Producer`) or
    38         for local binding (`Consumer`). This implementation only supports TCP as transport protocol.
    39         :param host: Hostname or IP address of the OpenC2 server.
    40         :param port: Transport port of the OpenC2 server.
    41         :param endpoint: The remote endpoint to contact the OpenC2 server (`Producer` only).
    42         :param usessl: Enable (`True`) or disable (`False`) SSL. Internal use only. Do not set this argument,
    43             use the `HTTPSTransfer` instead.
    44     """
    45      self.host = host
    46      self.port = port
    47      self.endpoint = endpoint
    48      self.scheme = 'https' if usessl else 'http'
    49      self.url = f"{self.scheme}://{host}:{port}{endpoint}"
    50      self.ssl_context = None
:::

::: docstring
Builds the [`HTTPTransfer`](#HTTPTransfer) instance

The [`host`](#HTTPTransfer.host) and [`port`](#HTTPTransfer.port)
parameters are used either for selecting the remote server (`Producer`)
or for local binding (`Consumer`). This implementation only supports TCP
as transport protocol.

###### Parameters

-   **host**: Hostname or IP address of the OpenC2 server.
-   **port**: Transport port of the OpenC2 server.
-   **endpoint**: The remote endpoint to contact the OpenC2 server
    (`Producer` only).
-   **usessl**: Enable (`True`) or disable (`False`) SSL. Internal use
    only. Do not set this argument, use the
    [`HTTPSTransfer`](#HTTPSTransfer) instead.
:::
::::::

:::: {#HTTPTransfer.host .classattr}
::: {.attr .variable}
[host]{.name}
:::

[](#HTTPTransfer.host){.headerlink}
::::

:::: {#HTTPTransfer.port .classattr}
::: {.attr .variable}
[port]{.name}
:::

[](#HTTPTransfer.port){.headerlink}
::::

:::: {#HTTPTransfer.endpoint .classattr}
::: {.attr .variable}
[endpoint]{.name}
:::

[](#HTTPTransfer.endpoint){.headerlink}
::::

:::: {#HTTPTransfer.scheme .classattr}
::: {.attr .variable}
[scheme]{.name}
:::

[](#HTTPTransfer.scheme){.headerlink}
::::

:::: {#HTTPTransfer.url .classattr}
::: {.attr .variable}
[url]{.name}
:::

[](#HTTPTransfer.url){.headerlink}
::::

:::: {#HTTPTransfer.ssl_context .classattr}
::: {.attr .variable}
[ssl_context]{.name}
:::

[](#HTTPTransfer.ssl_context){.headerlink}
::::

:::::: {#HTTPTransfer.send .classattr}
::: {.attr .function}
[def]{.def} [send]{.name}[([[self]{.bp}, ]{.param}[[msg]{.n},
]{.param}[[encoder]{.n}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
:::

[](#HTTPTransfer.send){.headerlink}

::: {.pdoc-code .codehilite}
     98    def send(self, msg, encoder):
     99     """ Sends OpenC2 message
    100
    101          This method implements the required `Transfer` interface to send message to an OpenC2 server.
    102          :param msg: The message to send (openc2lib `Message`).
    103          :param encoder: The encoder to use for encoding the `msg`.
    104          :return: An OpenC2  response (`Response`).
    105      """
    106       # Convert the message to the specific HTTP representation
    107       openc2data = self._tohttp(msg, encoder)
    108
    109       # Building the requested headers for the Request
    110       content_type = f"application/{msg.content_type}+{encoder.getName()};version={msg.version}"
    111       date = msg.created if msg.created else int(oc2.DateTime())
    112       openc2headers={'Content-Type': content_type, 'Accept': content_type, 'Date': oc2.DateTime(date).httpdate()}
    113
    114       logger.info("Sending to %s", self.url)
    115       logger.info(" -> body: %s", openc2data)
    116
    117       # Send the OpenC2 message and get the response
    118       if self.scheme == 'https':
    119           logger.warning("Certificate validation disabled!")
    120       response = requests.post(self.url, data=openc2data, headers=openc2headers, verify=False)
    121       logger.info("HTTP got response: %s", response)
    122   
    123       # TODO: How to manage HTTP response code? Can we safely assume they always match the Openc2 response?
    124       try:
    125           if response.text != "":
    126               msg = self._fromhttp(response.headers, response.text)
    127           else:
    128               msg = None
    129       except ValueError as e:
    130           msg = oc2.Message(oc2.Content())
    131           msg.status = response.status_code
    132           logger.error("Unable to parse data: >%s<", response.text)
    133           logger.error(str(e))
    134
    135       return msg
:::

::: docstring
Sends OpenC2 message

This method implements the required `Transfer` interface to send message
to an OpenC2 server.

###### Parameters {#parameters}

-   **msg**: The message to send (openc2lib `Message`).
-   **encoder**: The encoder to use for encoding the `msg`.

###### Returns

> An OpenC2 response (`Response`).
:::
::::::

:::::: {#HTTPTransfer.receive .classattr}
::: {.attr .function}
[def]{.def} [receive]{.name}[([[self]{.bp}, ]{.param}[[callback]{.n},
]{.param}[[encoder]{.n}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
:::

[](#HTTPTransfer.receive){.headerlink}

::: {.pdoc-code .codehilite}
    178    def receive(self, callback, encoder):
    179     """ Listen for incoming messages
    180
    181            This method implements the `Transfer` interface to listen for and receive OpenC2 messages.
    182            The internal implementation uses `Flask` as HTTP server. The method invokes the `callback`
    183            for each received message, which must be provided by a `Producer` to properly dispatch 
    184            `Command`s to the relevant server(s). It also takes an `Encoder` that is used to create
    185            responses to `Command`s encoded with unknown encoders.
    186            :param callback: The function that is invoked to process OpenC2 messages.
    187            :param encoder: Default `Encoder` instance to respond to unknown or wrong messages.
    188            :return :None
    189        """
    190     app = Flask(__name__)
    191     app.config['OPENC2']=self
    192     app.config['CALLBACK']=callback
    193     app.config['ENCODER']=encoder
    194
    195     @app.route(self.endpoint, methods=['POST'])
    196     def _consumer():
    197         """ Serving endpoint for `Flask` """
    198         server = app.config['OPENC2']
    199         callback = app.config['CALLBACK']
    200         encoder=app.config['ENCODER']
    201         
    202         try:
    203             cmd, encoder = server._recv(request.headers, request.data.decode('UTF-8') )
    204             # TODO: Add the code to answer according to 'response_requested'
    205         except ValueError as e:
    206             # TODO: Find better formatting (what should be returned if the request is not understood?)
    207             content = oc2.Response(status=oc2.StatusCode.BADREQUEST, status_text=str(e))
    208             resp = oc2.Message(content)
    209             resp.content_type = oc2.Message.content_type
    210             resp.version = oc2.Message.version
    211             resp.encoder = encoder
    212             resp.status=oc2.StatusCode.BADREQUEST
    213         else:
    214             logger.info("Received command: %s", cmd)
    215             resp = callback(cmd)
    216
    217         
    218         logger.debug("Got response: %s", resp)
    219         
    220         # TODO: Set HTTP headers as appropriate
    221         hdrs, data = server._respond(resp, encoder)
    222         logger.info("Sending response: %s", data)
    223         httpresp = make_response(data if data is not None else "") 
    224         httpresp.headers = hdrs
    225
    226         if data is None:
    227             resp_code = 200
    228         else:
    229             resp_code = resp.status.value
    230
    231         return httpresp, resp_code
    232
    233     app.run(debug=True, host=self.host, port=self.port, ssl_context=self.ssl_context)
:::

::: docstring
Listen for incoming messages

This method implements the `Transfer` interface to listen for and
receive OpenC2 messages. The internal implementation uses `Flask` as
HTTP server. The method invokes the `callback` for each received
message, which must be provided by a `Producer` to properly dispatch
`Command`s to the relevant server(s). It also takes an `Encoder` that is
used to create responses to `Command`s encoded with unknown encoders.

###### Parameters {#parameters}

-   **callback**: The function that is invoked to process OpenC2
    messages.
-   **encoder**: Default `Encoder` instance to respond to unknown or
    wrong messages. :return :None
:::
::::::
::::::::::::::::::::::::::::::

::::::::::::: {#HTTPSTransfer .section}
::: {.attr .class}
[class]{.def}
[HTTPSTransfer]{.name}([[HTTPTransfer](#HTTPTransfer)]{.base}): View
Source
:::

[](#HTTPSTransfer){.headerlink}

::: {.pdoc-code .codehilite}
    236class HTTPSTransfer(HTTPTransfer):
    237   """ HTTP Transfer Protocol with SSL
    238
    239      This class provides an implementation of the Specification. It builds on Flask and so it is not
    240      suitable for production environments.
    241
    242      Use `HTTPSTransfer` to build OpenC2 communication stacks in `Producer` and `Consumer`.
    243      Usage and methods of `HTTPSTransfer` are semanthically the same as for `HTTPTransfer`.
    244  """
    245   def __init__(self, host, port = 443, endpoint = '/.well-known/openc2'):
    246       """ Builds the `HTTPSTransfer` instance
    247
    248          The `host` and `port` parameters are used either for selecting the remote server (`Producer`) or
    249          for local binding (`Consumer`). This implementation only supports TCP as transport protocol.
    250          :param host: Hostname or IP address of the OpenC2 server.
    251          :param port: Transport port of the OpenC2 server.
    252          :param endpoint: The remote endpoint to contact the OpenC2 server (`Producer` only).
    253      """
    254       HTTPTransfer.__init__(self, host, port, endpoint, usessl=True)
    255       self.ssl_context = "adhoc"
:::

::: docstring
HTTP Transfer Protocol with SSL

This class provides an implementation of the Specification. It builds on
Flask and so it is not suitable for production environments.

Use [`HTTPSTransfer`](#HTTPSTransfer) to build OpenC2 communication
stacks in `Producer` and `Consumer`. Usage and methods of
[`HTTPSTransfer`](#HTTPSTransfer) are semanthically the same as for
[`HTTPTransfer`](#HTTPTransfer).
:::

:::::: {#HTTPSTransfer.__init__ .classattr}
::: {.attr .function}
[HTTPSTransfer]{.name}[([[host]{.n},
]{.param}[[port]{.n}[=]{.o}[443]{.mi},
]{.param}[[endpoint]{.n}[=]{.o}[\'/.well-known/openc2\']{.s1}]{.param})]{.signature
.pdoc-code .condensed} View Source
:::

[](#HTTPSTransfer.__init__){.headerlink}

::: {.pdoc-code .codehilite}
    245    def __init__(self, host, port = 443, endpoint = '/.well-known/openc2'):
    246     """ Builds the `HTTPSTransfer` instance
    247
    248            The `host` and `port` parameters are used either for selecting the remote server (`Producer`) or
    249            for local binding (`Consumer`). This implementation only supports TCP as transport protocol.
    250            :param host: Hostname or IP address of the OpenC2 server.
    251            :param port: Transport port of the OpenC2 server.
    252            :param endpoint: The remote endpoint to contact the OpenC2 server (`Producer` only).
    253        """
    254     HTTPTransfer.__init__(self, host, port, endpoint, usessl=True)
    255     self.ssl_context = "adhoc"
:::

::: docstring
Builds the [`HTTPSTransfer`](#HTTPSTransfer) instance

The [`host`](#HTTPSTransfer.host) and [`port`](#HTTPSTransfer.port)
parameters are used either for selecting the remote server (`Producer`)
or for local binding (`Consumer`). This implementation only supports TCP
as transport protocol.

###### Parameters {#parameters}

-   **host**: Hostname or IP address of the OpenC2 server.
-   **port**: Transport port of the OpenC2 server.
-   **endpoint**: The remote endpoint to contact the OpenC2 server
    (`Producer` only).
:::
::::::

:::: {#HTTPSTransfer.ssl_context .classattr}
::: {.attr .variable}
[ssl_context]{.name}
:::

[](#HTTPSTransfer.ssl_context){.headerlink}
::::

::: inherited
##### Inherited Members

[HTTPTransfer](#HTTPTransfer)
:   [host](#HTTPTransfer.host)
:   [port](#HTTPTransfer.port)
:   [endpoint](#HTTPTransfer.endpoint)
:   [scheme](#HTTPTransfer.scheme)
:   [url](#HTTPTransfer.url)
:   [send](#HTTPTransfer.send)
:   [receive](#HTTPTransfer.receive)
:::
:::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::
