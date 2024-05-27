![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAzMCAzMCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLW1pdGVybGltaXQ9IjEwIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik00IDdoMjJNNCAxNWgyMk00IDIzaDIyIiAvPjwvc3ZnPg==)

<div>

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0iYmkgYmktYm94LWFycm93LWluLWxlZnQiIHZpZXdib3g9IjAgMCAxNiAxNiI+CiAgPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMTAgMy41YS41LjUgMCAwIDAtLjUtLjVoLThhLjUuNSAwIDAgMC0uNS41djlhLjUuNSAwIDAgMCAuNS41aDhhLjUuNSAwIDAgMCAuNS0uNXYtMmEuNS41IDAgMCAxIDEgMHYyQTEuNSAxLjUgMCAwIDEgOS41IDE0aC04QTEuNSAxLjUgMCAwIDEgMCAxMi41di05QTEuNSAxLjUgMCAwIDEgMS41IDJoOEExLjUgMS41IDAgMCAxIDExIDMuNXYyYS41LjUgMCAwIDEtMSAwdi0yeiIgLz4KICA8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00LjE0NiA4LjM1NGEuNS41IDAgMCAxIDAtLjcwOGwzLTNhLjUuNSAwIDEgMSAuNzA4LjcwOEw1LjcwNyA3LjVIMTQuNWEuNS41IDAgMCAxIDAgMUg1LjcwN2wyLjE0NyAyLjE0NmEuNS41IDAgMCAxLS43MDguNzA4bC0zLTN6IiAvPgo8L3N2Zz4=){.bi
.bi-box-arrow-in-left}  openc2lib.core](../core.html){.pdoc-button
.module-list-button}

## API Documentation

-   [logger](#logger){.variable}
-   [Consumer](#Consumer){.class}
    -   [Consumer](#Consumer.__init__){.function}
    -   [consumer](#Consumer.consumer){.variable}
    -   [encoder](#Consumer.encoder){.variable}
    -   [transfer](#Consumer.transfer){.variable}
    -   [actuators](#Consumer.actuators){.variable}
    -   [run](#Consumer.run){.function}
    -   [dispatch](#Consumer.dispatch){.function}

[built with [pdoc]{.visually-hidden}![pdoc
logo](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20role%3D%22img%22%20aria-label%3D%22pdoc%20logo%22%20width%3D%22300%22%20height%3D%22150%22%20viewBox%3D%22-1%200%2060%2030%22%3E%3Ctitle%3Epdoc%3C/title%3E%3Cpath%20d%3D%22M29.621%2021.293c-.011-.273-.214-.475-.511-.481a.5.5%200%200%200-.489.503l-.044%201.393c-.097.551-.695%201.215-1.566%201.704-.577.428-1.306.486-2.193.182-1.426-.617-2.467-1.654-3.304-2.487l-.173-.172a3.43%203.43%200%200%200-.365-.306.49.49%200%200%200-.286-.196c-1.718-1.06-4.931-1.47-7.353.191l-.219.15c-1.707%201.187-3.413%202.131-4.328%201.03-.02-.027-.49-.685-.141-1.763.233-.721.546-2.408.772-4.076.042-.09.067-.187.046-.288.166-1.347.277-2.625.241-3.351%201.378-1.008%202.271-2.586%202.271-4.362%200-.976-.272-1.935-.788-2.774-.057-.094-.122-.18-.184-.268.033-.167.052-.339.052-.516%200-1.477-1.202-2.679-2.679-2.679-.791%200-1.496.352-1.987.9a6.3%206.3%200%200%200-1.001.029c-.492-.564-1.207-.929-2.012-.929-1.477%200-2.679%201.202-2.679%202.679A2.65%202.65%200%200%200%20.97%206.554c-.383.747-.595%201.572-.595%202.41%200%202.311%201.507%204.29%203.635%205.107-.037.699-.147%202.27-.423%203.294l-.137.461c-.622%202.042-2.515%208.257%201.727%2010.643%201.614.908%203.06%201.248%204.317%201.248%202.665%200%204.492-1.524%205.322-2.401%201.476-1.559%202.886-1.854%206.491.82%201.877%201.393%203.514%201.753%204.861%201.068%202.223-1.713%202.811-3.867%203.399-6.374.077-.846.056-1.469.054-1.537zm-4.835%204.313c-.054.305-.156.586-.242.629-.034-.007-.131-.022-.307-.157-.145-.111-.314-.478-.456-.908.221.121.432.25.675.355.115.039.219.051.33.081zm-2.251-1.238c-.05.33-.158.648-.252.694-.022.001-.125-.018-.307-.157-.217-.166-.488-.906-.639-1.573.358.344.754.693%201.198%201.036zm-3.887-2.337c-.006-.116-.018-.231-.041-.342.635.145%201.189.368%201.599.625.097.231.166.481.174.642-.03.049-.055.101-.067.158-.046.013-.128.026-.298.004-.278-.037-.901-.57-1.367-1.087zm-1.127-.497c.116.306.176.625.12.71-.019.014-.117.045-.345.016-.206-.027-.604-.332-.986-.695.41-.051.816-.056%201.211-.031zm-4.535%201.535c.209.22.379.47.358.598-.006.041-.088.138-.351.234-.144.055-.539-.063-.979-.259a11.66%2011.66%200%200%200%20.972-.573zm.983-.664c.359-.237.738-.418%201.126-.554.25.237.479.548.457.694-.006.042-.087.138-.351.235-.174.064-.694-.105-1.232-.375zm-3.381%201.794c-.022.145-.061.29-.149.401-.133.166-.358.248-.69.251h-.002c-.133%200-.306-.26-.45-.621.417.091.854.07%201.291-.031zm-2.066-8.077a4.78%204.78%200%200%201-.775-.584c.172-.115.505-.254.88-.378l-.105.962zm-.331%202.302a10.32%2010.32%200%200%201-.828-.502c.202-.143.576-.328.984-.49l-.156.992zm-.45%202.157l-.701-.403c.214-.115.536-.249.891-.376a11.57%2011.57%200%200%201-.19.779zm-.181%201.716c.064.398.194.702.298.893-.194-.051-.435-.162-.736-.398.061-.119.224-.3.438-.495zM8.87%204.141c0%20.152-.123.276-.276.276s-.275-.124-.275-.276.123-.276.276-.276.275.124.275.276zm-.735-.389a1.15%201.15%200%200%200-.314.783%201.16%201.16%200%200%200%201.162%201.162c.457%200%20.842-.27%201.032-.653.026.117.042.238.042.362a1.68%201.68%200%200%201-1.679%201.679%201.68%201.68%200%200%201-1.679-1.679c0-.843.626-1.535%201.436-1.654zM5.059%205.406A1.68%201.68%200%200%201%203.38%207.085a1.68%201.68%200%200%201-1.679-1.679c0-.037.009-.072.011-.109.21.3.541.508.935.508a1.16%201.16%200%200%200%201.162-1.162%201.14%201.14%200%200%200-.474-.912c.015%200%20.03-.005.045-.005.926.001%201.679.754%201.679%201.68zM3.198%204.141c0%20.152-.123.276-.276.276s-.275-.124-.275-.276.123-.276.276-.276.275.124.275.276zM1.375%208.964c0-.52.103-1.035.288-1.52.466.394%201.06.64%201.717.64%201.144%200%202.116-.725%202.499-1.738.383%201.012%201.355%201.738%202.499%201.738.867%200%201.631-.421%202.121-1.062.307.605.478%201.267.478%201.942%200%202.486-2.153%204.51-4.801%204.51s-4.801-2.023-4.801-4.51zm24.342%2019.349c-.985.498-2.267.168-3.813-.979-3.073-2.281-5.453-3.199-7.813-.705-1.315%201.391-4.163%203.365-8.423.97-3.174-1.786-2.239-6.266-1.261-9.479l.146-.492c.276-1.02.395-2.457.444-3.268a6.11%206.11%200%200%200%201.18.115%206.01%206.01%200%200%200%202.536-.562l-.006.175c-.802.215-1.848.612-2.021%201.25-.079.295.021.601.274.837.219.203.415.364.598.501-.667.304-1.243.698-1.311%201.179-.02.144-.022.507.393.787.213.144.395.26.564.365-1.285.521-1.361.96-1.381%201.126-.018.142-.011.496.427.746l.854.489c-.473.389-.971.914-.999%201.429-.018.278.095.532.316.713.675.556%201.231.721%201.653.721.059%200%20.104-.014.158-.02.207.707.641%201.64%201.513%201.64h.013c.8-.008%201.236-.345%201.462-.626.173-.216.268-.457.325-.692.424.195.93.374%201.372.374.151%200%20.294-.021.423-.068.732-.27.944-.704.993-1.021.009-.061.003-.119.002-.179.266.086.538.147.789.147.15%200%20.294-.021.423-.069.542-.2.797-.489.914-.754.237.147.478.258.704.288.106.014.205.021.296.021.356%200%20.595-.101.767-.229.438.435%201.094.992%201.656%201.067.106.014.205.021.296.021a1.56%201.56%200%200%200%20.323-.035c.17.575.453%201.289.866%201.605.358.273.665.362.914.362a.99.99%200%200%200%20.421-.093%201.03%201.03%200%200%200%20.245-.164c.168.428.39.846.68%201.068.358.273.665.362.913.362a.99.99%200%200%200%20.421-.093c.317-.148.512-.448.639-.762.251.157.495.257.726.257.127%200%20.25-.024.37-.071.427-.17.706-.617.841-1.314.022-.015.047-.022.068-.038.067-.051.133-.104.196-.159-.443%201.486-1.107%202.761-2.086%203.257zM8.66%209.925a.5.5%200%201%200-1%200c0%20.653-.818%201.205-1.787%201.205s-1.787-.552-1.787-1.205a.5.5%200%201%200-1%200c0%201.216%201.25%202.205%202.787%202.205s2.787-.989%202.787-2.205zm4.4%2015.965l-.208.097c-2.661%201.258-4.708%201.436-6.086.527-1.542-1.017-1.88-3.19-1.844-4.198a.4.4%200%200%200-.385-.414c-.242-.029-.406.164-.414.385-.046%201.249.367%203.686%202.202%204.896.708.467%201.547.7%202.51.7%201.248%200%202.706-.392%204.362-1.174l.185-.086a.4.4%200%200%200%20.205-.527c-.089-.204-.326-.291-.527-.206zM9.547%202.292c.093.077.205.114.317.114a.5.5%200%200%200%20.318-.886L8.817.397a.5.5%200%200%200-.703.068.5.5%200%200%200%20.069.703l1.364%201.124zm-7.661-.065c.086%200%20.173-.022.253-.068l1.523-.893a.5.5%200%200%200-.506-.863l-1.523.892a.5.5%200%200%200-.179.685c.094.158.261.247.432.247z%22%20transform%3D%22matrix%28-1%200%200%201%2058%200%29%22%20fill%3D%22%233bb300%22/%3E%3Cpath%20d%3D%22M.3%2021.86V10.18q0-.46.02-.68.04-.22.18-.5.28-.54%201.34-.54%201.06%200%201.42.28.38.26.44.78.76-1.04%202.38-1.04%201.64%200%203.1%201.54%201.46%201.54%201.46%203.58%200%202.04-1.46%203.58-1.44%201.54-3.08%201.54-1.64%200-2.38-.92v4.04q0%20.46-.04.68-.02.22-.18.5-.14.3-.5.42-.36.12-.98.12-.62%200-1-.12-.36-.12-.52-.4-.14-.28-.18-.5-.02-.22-.02-.68zm3.96-9.42q-.46.54-.46%201.18%200%20.64.46%201.18.48.52%201.2.52.74%200%201.24-.52.52-.52.52-1.18%200-.66-.48-1.18-.48-.54-1.26-.54-.76%200-1.22.54zm14.741-8.36q.16-.3.54-.42.38-.12%201-.12.64%200%201.02.12.38.12.52.42.16.3.18.54.04.22.04.68v11.94q0%20.46-.04.7-.02.22-.18.5-.3.54-1.7.54-1.38%200-1.54-.98-.84.96-2.34.96-1.8%200-3.28-1.56-1.48-1.58-1.48-3.66%200-2.1%201.48-3.68%201.5-1.58%203.28-1.58%201.48%200%202.3%201v-4.2q0-.46.02-.68.04-.24.18-.52zm-3.24%2010.86q.52.54%201.26.54.74%200%201.22-.54.5-.54.5-1.18%200-.66-.48-1.22-.46-.56-1.26-.56-.8%200-1.28.56-.48.54-.48%201.2%200%20.66.52%201.2zm7.833-1.2q0-2.4%201.68-3.96%201.68-1.56%203.84-1.56%202.16%200%203.82%201.56%201.66%201.54%201.66%203.94%200%201.66-.86%202.96-.86%201.28-2.1%201.9-1.22.6-2.54.6-1.32%200-2.56-.64-1.24-.66-2.1-1.92-.84-1.28-.84-2.88zm4.18%201.44q.64.48%201.3.48.66%200%201.32-.5.66-.5.66-1.48%200-.98-.62-1.46-.62-.48-1.34-.48-.72%200-1.34.5-.62.5-.62%201.48%200%20.96.64%201.46zm11.412-1.44q0%20.84.56%201.32.56.46%201.18.46.64%200%201.18-.36.56-.38.9-.38.6%200%201.46%201.06.46.58.46%201.04%200%20.76-1.1%201.42-1.14.8-2.8.8-1.86%200-3.58-1.34-.82-.64-1.34-1.7-.52-1.08-.52-2.36%200-1.3.52-2.34.52-1.06%201.34-1.7%201.66-1.32%203.54-1.32.76%200%201.48.22.72.2%201.06.4l.32.2q.36.24.56.38.52.4.52.92%200%20.5-.42%201.14-.72%201.1-1.38%201.1-.38%200-1.08-.44-.36-.34-1.04-.34-.66%200-1.24.48-.58.48-.58%201.34z%22%20fill%3D%22green%22/%3E%3C/svg%3E)](https://pdoc.dev "pdoc: Python API documentation generator"){.attribution
target="_blank"}

</div>

:::::::::::::::::::::::::::::::: {.pdoc role="main"}
::::: {.section .module-info}
# [openc2lib](./../../openc2lib.html).[core](./../core.html).consumer {#openc2lib.core.consumer .modulename}

::: docstring
OpenC2 Consumer

The [`Consumer`](#Consumer) implements the expected behaviour of an
OpenC2 Consumer server that dispatches OpenC2 Commands to the Actuators.
:::

View Source

::: {.pdoc-code .codehilite}
      1"""OpenC2 Consumer
      2
      3The `Consumer` implements the expected behaviour of an OpenC2 Consumer server that dispatches OpenC2 Commands
      4to the Actuators.
      5"""
      6
      7import logging
      8
      9from openc2lib.types.datatypes import DateTime, ResponseType
     10
     11from openc2lib.core.encoder import Encoder
     12from openc2lib.core.transfer import Transfer
     13from openc2lib.core.message import Message, Response
     14from openc2lib.core.response import StatusCode, StatusCodeDescription
     15
     16logger = logging.getLogger('openc2')
     17
     18class Consumer:
     19 """OpenC2 Consumer
     20
     21        The `Consumer` is designed to dispatch OpenC2 `Message`s to the relevant `Actuator`. 
     22        The current implementation receives the configuration at initialization time. It is therefore
     23        not conceived to be runned itself as a service, but to be integrated in an external component 
     24        that reads the relevant configuration from file and passes it to the Consumer.
     25
     26        The `Consumer` has two main tasks:
     27        - creating the OpenC2 stack to process Messages (namely the combination of an Encoding format and
     28                a Transfer protocol);
     29        - dispatching incoming `Command`s to the relevant `Actuator`.
     30
     31        Each `Consumer` will only run a single `Transfer` protocol. All registered `Encoder`s can be used,
     32        and a default `Encoder` is explicitely given that will be used when no other selection is available 
     33        (e.g., to answer Messages that the Consumer does not understand).
     34        
     35    """
     36 def __init__(self, consumer: str, actuators: [] =None, encoder: Encoder = None, transfer: Transfer = None):
     37     """ Create a `Consumer`
     38            :param consumer: This is a string that identifies the `Consumer` and is used in `from` 
     39                and `to` fields of the OpenC2 `Message` (see Table 3.1 of the Language Specification.
     40            :param actuators: This must be a list of available `Actuator`s. The list contains the
     41                `Actuator` instances that will be used by the `Consumer`.
     42            :param encoder: This is an instance of the `Encoder` that will be used by default.
     43            :param transfer: This is the `Transfer` protocol that will be used to send/receive `Message`s.
     44        """
     45     self.consumer = consumer
     46     self.encoder = encoder
     47     self.transfer = transfer
     48     self.actuators = actuators
     49
     50     # TODO: Read configuration from file
     51
     52 # TODO: Manage non-blocking implementation of the Transfer.receive() function
     53 def run(self, encoder: Encoder = None, transfer: Transfer = None):
     54     """Runs a `Consumer`
     55
     56            This is the entry point of the `Consumer`. It must be invoked to start operation of the `Consumer`.
     57            This method may be blocking, depending on the implementation of the `receive()` method of the 
     58            used `Transfer`.
     59
     60            The arguments of this method can be used to create multiple OpenC2 stacks (e.g., using 
     61            different `Encoder`s and `Transfer`s). This feature clearly requires the `Transfer` 
     62            implementation to be non-blocking.
     63
     64            :param encoder: A different `Encoder` that might be passed to overwrite what set at initialization time. 
     65            :param transfer: A different `Transfer` that might be passed to overwrite what set at initialization time.
     66            :return: None.
     67        """
     68     if not encoder: encoder = self.encoder
     69     if not transfer: transfer = self.transfer
     70     if not transfer: raise ValueError('Missing transfer object')
     71
     72     transfer.receive(self.dispatch, self.encoder)
     73
     74
     75 def dispatch(self, msg):
     76     """ Dispatches Commands to Actuators
     77
     78            This method scans the actuator profile carried in the `Command` and select one or more
     79            `Actuator`s that will process the `Command`. 
     80            
     81            The current implementation is only meant to be used within the
     82            implementation of `Transfer` protocols as a callback for returning control to the main code.
     83            This approach is motivated by those Transfer protocols that replies to messages on the same 
     84            TCP connection, so to avoid errors with NAT and firewalls 
     85            (if a Command were passed back from the `Transfer.receive()` and processed within the `Consumer.run()`, 
     86             the following `Transfer.send() would use a different TCP connection).
     87            
     88            :param msg: The full openc2lib `Message` that embeds the `Command` to be processed.
     89            :return: A `Message` that embeds the `Response` (from the `Actuator` or elaborated by the `Consumer` in
     90                    case of errors).
     91        """
     92     #TODO: The logic to select the actuator that matches the request
     93     # OC2 Architecture, Sec. 2.1:
     94     # The Profile field, if present, specifies the profile that defines the function 
     95     # to be performed. A Consumer executes the command if it supports the specified 
     96     # profile, otherwise the command is ignored. The Profile field may be omitted and 
     97     # typically will not be included in implementations where the functions of the 
     98     # recipients are unambiguous or when a high- level effects-based command is 
     99     # desired and tactical decisions on how the effect is achieved is left to the 
    100       # recipient. If Profile is omitted and the recipient supports multiple profiles, 
    101       # the command will be executed in the context of each profile that supports the 
    102       # command's combination of action and target.
    103       try:
    104           profile = msg.content.actuator.getName()
    105       except AttributeError:
    106           # For a packet filter-only consumer, the following may apply:
    107           # profile = slpf.nsid
    108           # Default: execute in the context of multiple profiles
    109           profile = None
    110           # TODO: how to mix responses from multiple actuators?
    111           # Workaround: strictly require a profile to be present
    112           response = Response(status=StatusCode.BADREQUEST, status_text='Missing profile')
    113           return self.__respmsg(msg, response)
    114
    115       try:
    116           asset_id = msg.content.actuator.getObj()['asset_id']
    117       except KeyError:
    118           # assed_id = None means the default actuator that implements the required profile
    119           asset_id = None
    120
    121       try:
    122           if profile == None:
    123               # Select all actuators
    124               actuator = list(self.actuators.values())
    125           elif asset_id == None:
    126               # Select all actuators that implement the specific profile
    127               actuator = list(dict(filter(lambda p: p[0][0]==profile, self.actuators.items())).values())
    128           else:
    129               # Only one instance is expected to be present in this case
    130               actuator = [self.actuators[(profile,asset_id)]]
    131       except KeyError:
    132           response = Response(status=StatusCode.NOTFOUND, status_text='No actuator available')
    133           return self.__respmsg(msg, response)
    134
    135       response_content = None
    136       if msg.content.args:
    137           if 'response_requested' in msg.content.args.keys():
    138               match msg.content.args['response_requested']:
    139                   case ResponseType.none:
    140                       response_content = None
    141                   case ResponseType.ack:
    142                       response_content = Response(status=StatusCode.PROCESSING, status_text=StatusCodeDescription[StatusCode.PROCESSING])
    143                       # TODO: Spawn a process to run the process offline
    144                       logger.warn("Command: %s not run! -- Missing code")
    145                   case ResponseType.status:
    146                       response_content = Response(status=StatusCode.PROCESSING, status_text=StatusCodeDescription[StatusCode.PROCESSING])
    147                       # TODO: Spawn a process to run the process offline
    148                       logger.warn("Command: %s not run! -- Missing code")
    149                   case ResponseType.complete:
    150                       response_content = self.__runcmd(msg, actuator)
    151                   case _:
    152                       response_content = Response(status=StatusCode.BADREQUEST, status_text="Invalid response requested")
    153
    154       if not response_content:
    155           # Default: ResponseType == complete. Return an answer after the command is executed.
    156           response_content = self.__runcmd(msg, actuator)
    157                   
    158       logger.debug("Actuator %s returned: %s", actuator, response_content)
    159
    160       # Add the metadata to be returned to the Producer
    161       return self.__respmsg(msg, response_content)
    162
    163   def __runcmd(self, msg, actuator):
    164       # Run the command and collect the response
    165       # TODO: Define how to manage concurrent execution from more than one actuator
    166       try:
    167           # TODO: How to merge multiple responses?
    168           # for a in actuators.items(): 
    169           response_content = actuator[0].run(msg.content) 
    170       except (IndexError,AttributeError):
    171           response_content = Response(status=StatusCode.NOTFOUND, status_text='No actuator available')
    172
    173       return response_content
    174
    175   def __respmsg(self, msg, response):
    176       if response:
    177           respmsg = Message(response)
    178           respmsg.from_=self.consumer
    179           respmsg.to=[msg.from_]
    180           respmsg.content_type=msg.content_type
    181           respmsg.request_id=msg.request_id
    182           respmsg.created=int(DateTime())
    183           respmsg.status=response['status']
    184       else:
    185           respmsg = None
    186       logger.debug("Response to be sent: %s", respmsg)
    187
    188       return respmsg
    189
    190
    191
    192# TODO: Add main to load configuration from file
:::
:::::

:::: {#logger .section}
::: {.attr .variable}
[logger]{.name} = [\<Logger openc2 (WARNING)\>]{.default_value}
:::

[](#logger){.headerlink}
::::

:::::::::::::::::::::::::: {#Consumer .section}
::: {.attr .class}
[class]{.def} [Consumer]{.name}: View Source
:::

[](#Consumer){.headerlink}

::: {.pdoc-code .codehilite}
     19class Consumer:
     20   """OpenC2 Consumer
     21
     22      The `Consumer` is designed to dispatch OpenC2 `Message`s to the relevant `Actuator`. 
     23      The current implementation receives the configuration at initialization time. It is therefore
     24      not conceived to be runned itself as a service, but to be integrated in an external component 
     25      that reads the relevant configuration from file and passes it to the Consumer.
     26
     27      The `Consumer` has two main tasks:
     28      - creating the OpenC2 stack to process Messages (namely the combination of an Encoding format and
     29              a Transfer protocol);
     30      - dispatching incoming `Command`s to the relevant `Actuator`.
     31
     32      Each `Consumer` will only run a single `Transfer` protocol. All registered `Encoder`s can be used,
     33      and a default `Encoder` is explicitely given that will be used when no other selection is available 
     34      (e.g., to answer Messages that the Consumer does not understand).
     35      
     36  """
     37   def __init__(self, consumer: str, actuators: [] =None, encoder: Encoder = None, transfer: Transfer = None):
     38       """ Create a `Consumer`
     39          :param consumer: This is a string that identifies the `Consumer` and is used in `from` 
     40              and `to` fields of the OpenC2 `Message` (see Table 3.1 of the Language Specification.
     41          :param actuators: This must be a list of available `Actuator`s. The list contains the
     42              `Actuator` instances that will be used by the `Consumer`.
     43          :param encoder: This is an instance of the `Encoder` that will be used by default.
     44          :param transfer: This is the `Transfer` protocol that will be used to send/receive `Message`s.
     45      """
     46       self.consumer = consumer
     47       self.encoder = encoder
     48       self.transfer = transfer
     49       self.actuators = actuators
     50
     51       # TODO: Read configuration from file
     52
     53   # TODO: Manage non-blocking implementation of the Transfer.receive() function
     54   def run(self, encoder: Encoder = None, transfer: Transfer = None):
     55       """Runs a `Consumer`
     56
     57          This is the entry point of the `Consumer`. It must be invoked to start operation of the `Consumer`.
     58          This method may be blocking, depending on the implementation of the `receive()` method of the 
     59          used `Transfer`.
     60
     61          The arguments of this method can be used to create multiple OpenC2 stacks (e.g., using 
     62          different `Encoder`s and `Transfer`s). This feature clearly requires the `Transfer` 
     63          implementation to be non-blocking.
     64
     65          :param encoder: A different `Encoder` that might be passed to overwrite what set at initialization time. 
     66          :param transfer: A different `Transfer` that might be passed to overwrite what set at initialization time.
     67          :return: None.
     68      """
     69       if not encoder: encoder = self.encoder
     70       if not transfer: transfer = self.transfer
     71       if not transfer: raise ValueError('Missing transfer object')
     72
     73       transfer.receive(self.dispatch, self.encoder)
     74
     75
     76   def dispatch(self, msg):
     77       """ Dispatches Commands to Actuators
     78
     79          This method scans the actuator profile carried in the `Command` and select one or more
     80          `Actuator`s that will process the `Command`. 
     81          
     82          The current implementation is only meant to be used within the
     83          implementation of `Transfer` protocols as a callback for returning control to the main code.
     84          This approach is motivated by those Transfer protocols that replies to messages on the same 
     85          TCP connection, so to avoid errors with NAT and firewalls 
     86          (if a Command were passed back from the `Transfer.receive()` and processed within the `Consumer.run()`, 
     87           the following `Transfer.send() would use a different TCP connection).
     88          
     89          :param msg: The full openc2lib `Message` that embeds the `Command` to be processed.
     90          :return: A `Message` that embeds the `Response` (from the `Actuator` or elaborated by the `Consumer` in
     91                  case of errors).
     92      """
     93       #TODO: The logic to select the actuator that matches the request
     94       # OC2 Architecture, Sec. 2.1:
     95       # The Profile field, if present, specifies the profile that defines the function 
     96       # to be performed. A Consumer executes the command if it supports the specified 
     97       # profile, otherwise the command is ignored. The Profile field may be omitted and 
     98       # typically will not be included in implementations where the functions of the 
     99       # recipients are unambiguous or when a high- level effects-based command is 
    100     # desired and tactical decisions on how the effect is achieved is left to the 
    101     # recipient. If Profile is omitted and the recipient supports multiple profiles, 
    102     # the command will be executed in the context of each profile that supports the 
    103     # command's combination of action and target.
    104     try:
    105         profile = msg.content.actuator.getName()
    106     except AttributeError:
    107         # For a packet filter-only consumer, the following may apply:
    108         # profile = slpf.nsid
    109         # Default: execute in the context of multiple profiles
    110         profile = None
    111         # TODO: how to mix responses from multiple actuators?
    112         # Workaround: strictly require a profile to be present
    113         response = Response(status=StatusCode.BADREQUEST, status_text='Missing profile')
    114         return self.__respmsg(msg, response)
    115
    116     try:
    117         asset_id = msg.content.actuator.getObj()['asset_id']
    118     except KeyError:
    119         # assed_id = None means the default actuator that implements the required profile
    120         asset_id = None
    121
    122     try:
    123         if profile == None:
    124             # Select all actuators
    125             actuator = list(self.actuators.values())
    126         elif asset_id == None:
    127             # Select all actuators that implement the specific profile
    128             actuator = list(dict(filter(lambda p: p[0][0]==profile, self.actuators.items())).values())
    129         else:
    130             # Only one instance is expected to be present in this case
    131             actuator = [self.actuators[(profile,asset_id)]]
    132     except KeyError:
    133         response = Response(status=StatusCode.NOTFOUND, status_text='No actuator available')
    134         return self.__respmsg(msg, response)
    135
    136     response_content = None
    137     if msg.content.args:
    138         if 'response_requested' in msg.content.args.keys():
    139             match msg.content.args['response_requested']:
    140                 case ResponseType.none:
    141                     response_content = None
    142                 case ResponseType.ack:
    143                     response_content = Response(status=StatusCode.PROCESSING, status_text=StatusCodeDescription[StatusCode.PROCESSING])
    144                     # TODO: Spawn a process to run the process offline
    145                     logger.warn("Command: %s not run! -- Missing code")
    146                 case ResponseType.status:
    147                     response_content = Response(status=StatusCode.PROCESSING, status_text=StatusCodeDescription[StatusCode.PROCESSING])
    148                     # TODO: Spawn a process to run the process offline
    149                     logger.warn("Command: %s not run! -- Missing code")
    150                 case ResponseType.complete:
    151                     response_content = self.__runcmd(msg, actuator)
    152                 case _:
    153                     response_content = Response(status=StatusCode.BADREQUEST, status_text="Invalid response requested")
    154
    155     if not response_content:
    156         # Default: ResponseType == complete. Return an answer after the command is executed.
    157         response_content = self.__runcmd(msg, actuator)
    158                 
    159     logger.debug("Actuator %s returned: %s", actuator, response_content)
    160
    161     # Add the metadata to be returned to the Producer
    162     return self.__respmsg(msg, response_content)
    163
    164 def __runcmd(self, msg, actuator):
    165     # Run the command and collect the response
    166     # TODO: Define how to manage concurrent execution from more than one actuator
    167     try:
    168         # TODO: How to merge multiple responses?
    169         # for a in actuators.items(): 
    170         response_content = actuator[0].run(msg.content) 
    171     except (IndexError,AttributeError):
    172         response_content = Response(status=StatusCode.NOTFOUND, status_text='No actuator available')
    173
    174     return response_content
    175
    176 def __respmsg(self, msg, response):
    177     if response:
    178         respmsg = Message(response)
    179         respmsg.from_=self.consumer
    180         respmsg.to=[msg.from_]
    181         respmsg.content_type=msg.content_type
    182         respmsg.request_id=msg.request_id
    183         respmsg.created=int(DateTime())
    184         respmsg.status=response['status']
    185     else:
    186         respmsg = None
    187     logger.debug("Response to be sent: %s", respmsg)
    188
    189     return respmsg
:::

::: docstring
OpenC2 Consumer

The [`Consumer`](#Consumer) is designed to dispatch OpenC2 `Message`s to
the relevant `Actuator`. The current implementation receives the
configuration at initialization time. It is therefore not conceived to
be runned itself as a service, but to be integrated in an external
component that reads the relevant configuration from file and passes it
to the Consumer.

The [`Consumer`](#Consumer) has two main tasks:

-   creating the OpenC2 stack to process Messages (namely the
    combination of an Encoding format and a Transfer protocol);
-   dispatching incoming `Command`s to the relevant `Actuator`.

Each [`Consumer`](#Consumer) will only run a single `Transfer` protocol.
All registered `Encoder`s can be used, and a default `Encoder` is
explicitely given that will be used when no other selection is available
(e.g., to answer Messages that the Consumer does not understand).
:::

:::::: {#Consumer.__init__ .classattr}
::: {.attr .function}
[Consumer]{.name}[([ [consumer]{.n}[:]{.p} [str]{.nb},]{.param}[
[actuators]{.n}[:]{.p} [\[\]]{.p} [=]{.o} [None]{.kc},]{.param}[
[encoder]{.n}[:]{.p}
[[openc2lib.core.encoder.Encoder](encoder.html#Encoder)]{.n} [=]{.o}
[None]{.kc},]{.param}[ [transfer]{.n}[:]{.p}
[[openc2lib.core.transfer.Transfer](transfer.html#Transfer)]{.n} [=]{.o}
[None]{.kc}]{.param})]{.signature .pdoc-code .multiline} View Source
:::

[](#Consumer.__init__){.headerlink}

::: {.pdoc-code .codehilite}
    37 def __init__(self, consumer: str, actuators: [] =None, encoder: Encoder = None, transfer: Transfer = None):
    38      """ Create a `Consumer`
    39         :param consumer: This is a string that identifies the `Consumer` and is used in `from` 
    40             and `to` fields of the OpenC2 `Message` (see Table 3.1 of the Language Specification.
    41         :param actuators: This must be a list of available `Actuator`s. The list contains the
    42             `Actuator` instances that will be used by the `Consumer`.
    43         :param encoder: This is an instance of the `Encoder` that will be used by default.
    44         :param transfer: This is the `Transfer` protocol that will be used to send/receive `Message`s.
    45     """
    46      self.consumer = consumer
    47      self.encoder = encoder
    48      self.transfer = transfer
    49      self.actuators = actuators
    50
    51      # TODO: Read configuration from file
:::

::: docstring
Create a [`Consumer`](#Consumer)

###### Parameters

-   **consumer**: This is a string that identifies the
    [`Consumer`](#Consumer) and is used in `from` and `to` fields of the
    OpenC2 `Message` (see Table 3.1 of the Language Specification.
-   **actuators**: This must be a list of available `Actuator`s. The
    list contains the `Actuator` instances that will be used by the
    [`Consumer`](#Consumer).
-   **encoder**: This is an instance of the `Encoder` that will be used
    by default.
-   **transfer**: This is the `Transfer` protocol that will be used to
    send/receive `Message`s.
:::
::::::

:::: {#Consumer.consumer .classattr}
::: {.attr .variable}
[consumer]{.name}
:::

[](#Consumer.consumer){.headerlink}
::::

:::: {#Consumer.encoder .classattr}
::: {.attr .variable}
[encoder]{.name}
:::

[](#Consumer.encoder){.headerlink}
::::

:::: {#Consumer.transfer .classattr}
::: {.attr .variable}
[transfer]{.name}
:::

[](#Consumer.transfer){.headerlink}
::::

:::: {#Consumer.actuators .classattr}
::: {.attr .variable}
[actuators]{.name}
:::

[](#Consumer.actuators){.headerlink}
::::

:::::: {#Consumer.run .classattr}
::: {.attr .function}
[def]{.def} [run]{.name}[([ [self]{.bp},]{.param}[ [encoder]{.n}[:]{.p}
[[openc2lib.core.encoder.Encoder](encoder.html#Encoder)]{.n} [=]{.o}
[None]{.kc},]{.param}[ [transfer]{.n}[:]{.p}
[[openc2lib.core.transfer.Transfer](transfer.html#Transfer)]{.n} [=]{.o}
[None]{.kc}]{.param}[):]{.return-annotation}]{.signature .pdoc-code
.multiline} View Source
:::

[](#Consumer.run){.headerlink}

::: {.pdoc-code .codehilite}
    54   def run(self, encoder: Encoder = None, transfer: Transfer = None):
    55        """Runs a `Consumer`
    56
    57           This is the entry point of the `Consumer`. It must be invoked to start operation of the `Consumer`.
    58           This method may be blocking, depending on the implementation of the `receive()` method of the 
    59           used `Transfer`.
    60
    61           The arguments of this method can be used to create multiple OpenC2 stacks (e.g., using 
    62           different `Encoder`s and `Transfer`s). This feature clearly requires the `Transfer` 
    63           implementation to be non-blocking.
    64
    65           :param encoder: A different `Encoder` that might be passed to overwrite what set at initialization time. 
    66           :param transfer: A different `Transfer` that might be passed to overwrite what set at initialization time.
    67           :return: None.
    68       """
    69        if not encoder: encoder = self.encoder
    70        if not transfer: transfer = self.transfer
    71        if not transfer: raise ValueError('Missing transfer object')
    72
    73        transfer.receive(self.dispatch, self.encoder)
:::

::: docstring
Runs a [`Consumer`](#Consumer)

This is the entry point of the [`Consumer`](#Consumer). It must be
invoked to start operation of the [`Consumer`](#Consumer). This method
may be blocking, depending on the implementation of the `receive()`
method of the used `Transfer`.

The arguments of this method can be used to create multiple OpenC2
stacks (e.g., using different `Encoder`s and `Transfer`s). This feature
clearly requires the `Transfer` implementation to be non-blocking.

###### Parameters {#parameters}

-   **encoder**: A different `Encoder` that might be passed to overwrite
    what set at initialization time.
-   **transfer**: A different `Transfer` that might be passed to
    overwrite what set at initialization time.

###### Returns

> None.
:::
::::::

:::::: {#Consumer.dispatch .classattr}
::: {.attr .function}
[def]{.def} [dispatch]{.name}[([[self]{.bp},
]{.param}[[msg]{.n}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
:::

[](#Consumer.dispatch){.headerlink}

::: {.pdoc-code .codehilite}
     76    def dispatch(self, msg):
     77     """ Dispatches Commands to Actuators
     78
     79            This method scans the actuator profile carried in the `Command` and select one or more
     80            `Actuator`s that will process the `Command`. 
     81            
     82            The current implementation is only meant to be used within the
     83            implementation of `Transfer` protocols as a callback for returning control to the main code.
     84            This approach is motivated by those Transfer protocols that replies to messages on the same 
     85            TCP connection, so to avoid errors with NAT and firewalls 
     86            (if a Command were passed back from the `Transfer.receive()` and processed within the `Consumer.run()`, 
     87             the following `Transfer.send() would use a different TCP connection).
     88            
     89            :param msg: The full openc2lib `Message` that embeds the `Command` to be processed.
     90            :return: A `Message` that embeds the `Response` (from the `Actuator` or elaborated by the `Consumer` in
     91                    case of errors).
     92        """
     93     #TODO: The logic to select the actuator that matches the request
     94     # OC2 Architecture, Sec. 2.1:
     95     # The Profile field, if present, specifies the profile that defines the function 
     96     # to be performed. A Consumer executes the command if it supports the specified 
     97     # profile, otherwise the command is ignored. The Profile field may be omitted and 
     98     # typically will not be included in implementations where the functions of the 
     99     # recipients are unambiguous or when a high- level effects-based command is 
    100       # desired and tactical decisions on how the effect is achieved is left to the 
    101       # recipient. If Profile is omitted and the recipient supports multiple profiles, 
    102       # the command will be executed in the context of each profile that supports the 
    103       # command's combination of action and target.
    104       try:
    105           profile = msg.content.actuator.getName()
    106       except AttributeError:
    107           # For a packet filter-only consumer, the following may apply:
    108           # profile = slpf.nsid
    109           # Default: execute in the context of multiple profiles
    110           profile = None
    111           # TODO: how to mix responses from multiple actuators?
    112           # Workaround: strictly require a profile to be present
    113           response = Response(status=StatusCode.BADREQUEST, status_text='Missing profile')
    114           return self.__respmsg(msg, response)
    115
    116       try:
    117           asset_id = msg.content.actuator.getObj()['asset_id']
    118       except KeyError:
    119           # assed_id = None means the default actuator that implements the required profile
    120           asset_id = None
    121
    122       try:
    123           if profile == None:
    124               # Select all actuators
    125               actuator = list(self.actuators.values())
    126           elif asset_id == None:
    127               # Select all actuators that implement the specific profile
    128               actuator = list(dict(filter(lambda p: p[0][0]==profile, self.actuators.items())).values())
    129           else:
    130               # Only one instance is expected to be present in this case
    131               actuator = [self.actuators[(profile,asset_id)]]
    132       except KeyError:
    133           response = Response(status=StatusCode.NOTFOUND, status_text='No actuator available')
    134           return self.__respmsg(msg, response)
    135
    136       response_content = None
    137       if msg.content.args:
    138           if 'response_requested' in msg.content.args.keys():
    139               match msg.content.args['response_requested']:
    140                   case ResponseType.none:
    141                       response_content = None
    142                   case ResponseType.ack:
    143                       response_content = Response(status=StatusCode.PROCESSING, status_text=StatusCodeDescription[StatusCode.PROCESSING])
    144                       # TODO: Spawn a process to run the process offline
    145                       logger.warn("Command: %s not run! -- Missing code")
    146                   case ResponseType.status:
    147                       response_content = Response(status=StatusCode.PROCESSING, status_text=StatusCodeDescription[StatusCode.PROCESSING])
    148                       # TODO: Spawn a process to run the process offline
    149                       logger.warn("Command: %s not run! -- Missing code")
    150                   case ResponseType.complete:
    151                       response_content = self.__runcmd(msg, actuator)
    152                   case _:
    153                       response_content = Response(status=StatusCode.BADREQUEST, status_text="Invalid response requested")
    154
    155       if not response_content:
    156           # Default: ResponseType == complete. Return an answer after the command is executed.
    157           response_content = self.__runcmd(msg, actuator)
    158                   
    159       logger.debug("Actuator %s returned: %s", actuator, response_content)
    160
    161       # Add the metadata to be returned to the Producer
    162       return self.__respmsg(msg, response_content)
:::

::: docstring
Dispatches Commands to Actuators

This method scans the actuator profile carried in the `Command` and
select one or more `Actuator`s that will process the `Command`.

The current implementation is only meant to be used within the
implementation of `Transfer` protocols as a callback for returning
control to the main code. This approach is motivated by those Transfer
protocols that replies to messages on the same TCP connection, so to
avoid errors with NAT and firewalls (if a Command were passed back from
the `Transfer.receive()` and processed within the
[`Consumer.run()`](#Consumer.run), the following \`Transfer.send() would
use a different TCP connection).

###### Parameters {#parameters}

-   **msg**: The full openc2lib `Message` that embeds the `Command` to
    be processed.

###### Returns {#returns}

> A `Message` that embeds the `Response` (from the `Actuator` or
> elaborated by the [`Consumer`](#Consumer) in case of errors).
:::
::::::
::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::
