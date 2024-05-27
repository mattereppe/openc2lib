![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAzMCAzMCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLW1pdGVybGltaXQ9IjEwIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik00IDdoMjJNNCAxNWgyMk00IDIzaDIyIiAvPjwvc3ZnPg==)

<div>

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0iYmkgYmktYm94LWFycm93LWluLWxlZnQiIHZpZXdib3g9IjAgMCAxNiAxNiI+CiAgPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMTAgMy41YS41LjUgMCAwIDAtLjUtLjVoLThhLjUuNSAwIDAgMC0uNS41djlhLjUuNSAwIDAgMCAuNS41aDhhLjUuNSAwIDAgMCAuNS0uNXYtMmEuNS41IDAgMCAxIDEgMHYyQTEuNSAxLjUgMCAwIDEgOS41IDE0aC04QTEuNSAxLjUgMCAwIDEgMCAxMi41di05QTEuNSAxLjUgMCAwIDEgMS41IDJoOEExLjUgMS41IDAgMCAxIDExIDMuNXYyYS41LjUgMCAwIDEtMSAwdi0yeiIgLz4KICA8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00LjE0NiA4LjM1NGEuNS41IDAgMCAxIDAtLjcwOGwzLTNhLjUuNSAwIDEgMSAuNzA4LjcwOEw1LjcwNyA3LjVIMTQuNWEuNS41IDAgMCAxIDAgMUg1LjcwN2wyLjE0NyAyLjE0NmEuNS41IDAgMCAxLS43MDguNzA4bC0zLTN6IiAvPgo8L3N2Zz4=){.bi
.bi-box-arrow-in-left}  openc2lib.core](../core.html){.pdoc-button
.module-list-button}

## API Documentation

-   [MessageType](#MessageType){.class}
    -   [command](#MessageType.command){.variable}
    -   [response](#MessageType.response){.variable}
-   [Content](#Content){.class}
    -   [msg_type](#Content.msg_type){.variable}
    -   [getType](#Content.getType){.function}
-   [Message](#Message){.class}
    -   [Message](#Message.__init__){.function}
    -   [content](#Message.content){.variable}
    -   [content_type](#Message.content_type){.variable}
    -   [msg_type](#Message.msg_type){.variable}
    -   [status](#Message.status){.variable}
    -   [request_id](#Message.request_id){.variable}
    -   [created](#Message.created){.variable}
    -   [from\_](#Message.from_){.variable}
    -   [to](#Message.to){.variable}
    -   [version](#Message.version){.variable}
    -   [encoding](#Message.encoding){.variable}
    -   [todict](#Message.todict){.function}
-   [Command](#Command){.class}
    -   [Command](#Command.__init__){.function}
    -   [action](#Command.action){.variable}
    -   [target](#Command.target){.variable}
    -   [args](#Command.args){.variable}
    -   [actuator](#Command.actuator){.variable}
    -   [command_id](#Command.command_id){.variable}
    -   [msg_type](#Command.msg_type){.variable}
-   [Response](#Response){.class}
    -   [fieldtypes](#Response.fieldtypes){.variable}
    -   [msg_type](#Response.msg_type){.variable}

[built with [pdoc]{.visually-hidden}![pdoc
logo](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20role%3D%22img%22%20aria-label%3D%22pdoc%20logo%22%20width%3D%22300%22%20height%3D%22150%22%20viewBox%3D%22-1%200%2060%2030%22%3E%3Ctitle%3Epdoc%3C/title%3E%3Cpath%20d%3D%22M29.621%2021.293c-.011-.273-.214-.475-.511-.481a.5.5%200%200%200-.489.503l-.044%201.393c-.097.551-.695%201.215-1.566%201.704-.577.428-1.306.486-2.193.182-1.426-.617-2.467-1.654-3.304-2.487l-.173-.172a3.43%203.43%200%200%200-.365-.306.49.49%200%200%200-.286-.196c-1.718-1.06-4.931-1.47-7.353.191l-.219.15c-1.707%201.187-3.413%202.131-4.328%201.03-.02-.027-.49-.685-.141-1.763.233-.721.546-2.408.772-4.076.042-.09.067-.187.046-.288.166-1.347.277-2.625.241-3.351%201.378-1.008%202.271-2.586%202.271-4.362%200-.976-.272-1.935-.788-2.774-.057-.094-.122-.18-.184-.268.033-.167.052-.339.052-.516%200-1.477-1.202-2.679-2.679-2.679-.791%200-1.496.352-1.987.9a6.3%206.3%200%200%200-1.001.029c-.492-.564-1.207-.929-2.012-.929-1.477%200-2.679%201.202-2.679%202.679A2.65%202.65%200%200%200%20.97%206.554c-.383.747-.595%201.572-.595%202.41%200%202.311%201.507%204.29%203.635%205.107-.037.699-.147%202.27-.423%203.294l-.137.461c-.622%202.042-2.515%208.257%201.727%2010.643%201.614.908%203.06%201.248%204.317%201.248%202.665%200%204.492-1.524%205.322-2.401%201.476-1.559%202.886-1.854%206.491.82%201.877%201.393%203.514%201.753%204.861%201.068%202.223-1.713%202.811-3.867%203.399-6.374.077-.846.056-1.469.054-1.537zm-4.835%204.313c-.054.305-.156.586-.242.629-.034-.007-.131-.022-.307-.157-.145-.111-.314-.478-.456-.908.221.121.432.25.675.355.115.039.219.051.33.081zm-2.251-1.238c-.05.33-.158.648-.252.694-.022.001-.125-.018-.307-.157-.217-.166-.488-.906-.639-1.573.358.344.754.693%201.198%201.036zm-3.887-2.337c-.006-.116-.018-.231-.041-.342.635.145%201.189.368%201.599.625.097.231.166.481.174.642-.03.049-.055.101-.067.158-.046.013-.128.026-.298.004-.278-.037-.901-.57-1.367-1.087zm-1.127-.497c.116.306.176.625.12.71-.019.014-.117.045-.345.016-.206-.027-.604-.332-.986-.695.41-.051.816-.056%201.211-.031zm-4.535%201.535c.209.22.379.47.358.598-.006.041-.088.138-.351.234-.144.055-.539-.063-.979-.259a11.66%2011.66%200%200%200%20.972-.573zm.983-.664c.359-.237.738-.418%201.126-.554.25.237.479.548.457.694-.006.042-.087.138-.351.235-.174.064-.694-.105-1.232-.375zm-3.381%201.794c-.022.145-.061.29-.149.401-.133.166-.358.248-.69.251h-.002c-.133%200-.306-.26-.45-.621.417.091.854.07%201.291-.031zm-2.066-8.077a4.78%204.78%200%200%201-.775-.584c.172-.115.505-.254.88-.378l-.105.962zm-.331%202.302a10.32%2010.32%200%200%201-.828-.502c.202-.143.576-.328.984-.49l-.156.992zm-.45%202.157l-.701-.403c.214-.115.536-.249.891-.376a11.57%2011.57%200%200%201-.19.779zm-.181%201.716c.064.398.194.702.298.893-.194-.051-.435-.162-.736-.398.061-.119.224-.3.438-.495zM8.87%204.141c0%20.152-.123.276-.276.276s-.275-.124-.275-.276.123-.276.276-.276.275.124.275.276zm-.735-.389a1.15%201.15%200%200%200-.314.783%201.16%201.16%200%200%200%201.162%201.162c.457%200%20.842-.27%201.032-.653.026.117.042.238.042.362a1.68%201.68%200%200%201-1.679%201.679%201.68%201.68%200%200%201-1.679-1.679c0-.843.626-1.535%201.436-1.654zM5.059%205.406A1.68%201.68%200%200%201%203.38%207.085a1.68%201.68%200%200%201-1.679-1.679c0-.037.009-.072.011-.109.21.3.541.508.935.508a1.16%201.16%200%200%200%201.162-1.162%201.14%201.14%200%200%200-.474-.912c.015%200%20.03-.005.045-.005.926.001%201.679.754%201.679%201.68zM3.198%204.141c0%20.152-.123.276-.276.276s-.275-.124-.275-.276.123-.276.276-.276.275.124.275.276zM1.375%208.964c0-.52.103-1.035.288-1.52.466.394%201.06.64%201.717.64%201.144%200%202.116-.725%202.499-1.738.383%201.012%201.355%201.738%202.499%201.738.867%200%201.631-.421%202.121-1.062.307.605.478%201.267.478%201.942%200%202.486-2.153%204.51-4.801%204.51s-4.801-2.023-4.801-4.51zm24.342%2019.349c-.985.498-2.267.168-3.813-.979-3.073-2.281-5.453-3.199-7.813-.705-1.315%201.391-4.163%203.365-8.423.97-3.174-1.786-2.239-6.266-1.261-9.479l.146-.492c.276-1.02.395-2.457.444-3.268a6.11%206.11%200%200%200%201.18.115%206.01%206.01%200%200%200%202.536-.562l-.006.175c-.802.215-1.848.612-2.021%201.25-.079.295.021.601.274.837.219.203.415.364.598.501-.667.304-1.243.698-1.311%201.179-.02.144-.022.507.393.787.213.144.395.26.564.365-1.285.521-1.361.96-1.381%201.126-.018.142-.011.496.427.746l.854.489c-.473.389-.971.914-.999%201.429-.018.278.095.532.316.713.675.556%201.231.721%201.653.721.059%200%20.104-.014.158-.02.207.707.641%201.64%201.513%201.64h.013c.8-.008%201.236-.345%201.462-.626.173-.216.268-.457.325-.692.424.195.93.374%201.372.374.151%200%20.294-.021.423-.068.732-.27.944-.704.993-1.021.009-.061.003-.119.002-.179.266.086.538.147.789.147.15%200%20.294-.021.423-.069.542-.2.797-.489.914-.754.237.147.478.258.704.288.106.014.205.021.296.021.356%200%20.595-.101.767-.229.438.435%201.094.992%201.656%201.067.106.014.205.021.296.021a1.56%201.56%200%200%200%20.323-.035c.17.575.453%201.289.866%201.605.358.273.665.362.914.362a.99.99%200%200%200%20.421-.093%201.03%201.03%200%200%200%20.245-.164c.168.428.39.846.68%201.068.358.273.665.362.913.362a.99.99%200%200%200%20.421-.093c.317-.148.512-.448.639-.762.251.157.495.257.726.257.127%200%20.25-.024.37-.071.427-.17.706-.617.841-1.314.022-.015.047-.022.068-.038.067-.051.133-.104.196-.159-.443%201.486-1.107%202.761-2.086%203.257zM8.66%209.925a.5.5%200%201%200-1%200c0%20.653-.818%201.205-1.787%201.205s-1.787-.552-1.787-1.205a.5.5%200%201%200-1%200c0%201.216%201.25%202.205%202.787%202.205s2.787-.989%202.787-2.205zm4.4%2015.965l-.208.097c-2.661%201.258-4.708%201.436-6.086.527-1.542-1.017-1.88-3.19-1.844-4.198a.4.4%200%200%200-.385-.414c-.242-.029-.406.164-.414.385-.046%201.249.367%203.686%202.202%204.896.708.467%201.547.7%202.51.7%201.248%200%202.706-.392%204.362-1.174l.185-.086a.4.4%200%200%200%20.205-.527c-.089-.204-.326-.291-.527-.206zM9.547%202.292c.093.077.205.114.317.114a.5.5%200%200%200%20.318-.886L8.817.397a.5.5%200%200%200-.703.068.5.5%200%200%200%20.069.703l1.364%201.124zm-7.661-.065c.086%200%20.173-.022.253-.068l1.523-.893a.5.5%200%200%200-.506-.863l-1.523.892a.5.5%200%200%200-.179.685c.094.158.261.247.432.247z%22%20transform%3D%22matrix%28-1%200%200%201%2058%200%29%22%20fill%3D%22%233bb300%22/%3E%3Cpath%20d%3D%22M.3%2021.86V10.18q0-.46.02-.68.04-.22.18-.5.28-.54%201.34-.54%201.06%200%201.42.28.38.26.44.78.76-1.04%202.38-1.04%201.64%200%203.1%201.54%201.46%201.54%201.46%203.58%200%202.04-1.46%203.58-1.44%201.54-3.08%201.54-1.64%200-2.38-.92v4.04q0%20.46-.04.68-.02.22-.18.5-.14.3-.5.42-.36.12-.98.12-.62%200-1-.12-.36-.12-.52-.4-.14-.28-.18-.5-.02-.22-.02-.68zm3.96-9.42q-.46.54-.46%201.18%200%20.64.46%201.18.48.52%201.2.52.74%200%201.24-.52.52-.52.52-1.18%200-.66-.48-1.18-.48-.54-1.26-.54-.76%200-1.22.54zm14.741-8.36q.16-.3.54-.42.38-.12%201-.12.64%200%201.02.12.38.12.52.42.16.3.18.54.04.22.04.68v11.94q0%20.46-.04.7-.02.22-.18.5-.3.54-1.7.54-1.38%200-1.54-.98-.84.96-2.34.96-1.8%200-3.28-1.56-1.48-1.58-1.48-3.66%200-2.1%201.48-3.68%201.5-1.58%203.28-1.58%201.48%200%202.3%201v-4.2q0-.46.02-.68.04-.24.18-.52zm-3.24%2010.86q.52.54%201.26.54.74%200%201.22-.54.5-.54.5-1.18%200-.66-.48-1.22-.46-.56-1.26-.56-.8%200-1.28.56-.48.54-.48%201.2%200%20.66.52%201.2zm7.833-1.2q0-2.4%201.68-3.96%201.68-1.56%203.84-1.56%202.16%200%203.82%201.56%201.66%201.54%201.66%203.94%200%201.66-.86%202.96-.86%201.28-2.1%201.9-1.22.6-2.54.6-1.32%200-2.56-.64-1.24-.66-2.1-1.92-.84-1.28-.84-2.88zm4.18%201.44q.64.48%201.3.48.66%200%201.32-.5.66-.5.66-1.48%200-.98-.62-1.46-.62-.48-1.34-.48-.72%200-1.34.5-.62.5-.62%201.48%200%20.96.64%201.46zm11.412-1.44q0%20.84.56%201.32.56.46%201.18.46.64%200%201.18-.36.56-.38.9-.38.6%200%201.46%201.06.46.58.46%201.04%200%20.76-1.1%201.42-1.14.8-2.8.8-1.86%200-3.58-1.34-.82-.64-1.34-1.7-.52-1.08-.52-2.36%200-1.3.52-2.34.52-1.06%201.34-1.7%201.66-1.32%203.54-1.32.76%200%201.48.22.72.2%201.06.4l.32.2q.36.24.56.38.52.4.52.92%200%20.5-.42%201.14-.72%201.1-1.38%201.1-.38%200-1.08-.44-.36-.34-1.04-.34-.66%200-1.24.48-.58.48-.58%201.34z%22%20fill%3D%22green%22/%3E%3C/svg%3E)](https://pdoc.dev "pdoc: Python API documentation generator"){.attribution
target="_blank"}

</div>

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.pdoc role="main"}
::::: {.section .module-info}
# [openc2lib](./../../openc2lib.html).[core](./../core.html).message {#openc2lib.core.message .modulename}

::: docstring
OpenC2 Message structures

This module defines the OpenC2 Message structure and its content type,
as defined in Sec. 3.2 of the Language Specification.

The definition include: [`Message`](#Message), [`Content`](#Content),
[`Command`](#Command), and [`Response`](#Response).
:::

View Source

::: {.pdoc-code .codehilite}
      1"""OpenC2 Message structures
      2
      3This module defines the OpenC2 Message structure and its content type, as defined
      4in Sec. 3.2 of the Language Specification.
      5
      6The definition include: `Message`, `Content`, `Command`, and `Response`.
      7"""
      8
      9
     10import enum
     11import dataclasses
     12import uuid
     13
     14from openc2lib.types.datatypes import DateTime, Version
     15from openc2lib.types.basetypes import Record, Map
     16
     17from openc2lib.core.actions import Actions 
     18from openc2lib.core.target import Target
     19from openc2lib.core.response import StatusCode, Results
     20from openc2lib.core.args import Args
     21
     22from openc2lib.core.actuator import Actuator
     23
     24_OPENC2_CONTENT_TYPE = "openc2"
     25_OPENC2_VERSION = Version(1,0)
     26
     27class MessageType(enum.Enum):
     28 """OpenC2 Message Type
     29    
     30    Message type can be either `command` or `response`.
     31    """
     32 command = 1
     33 response = 2
     34
     35
     36class Content:
     37 """ Content of the OpenC2 Message
     38
     39        A content is the base class to derive either a `Command` or a `Response`. 
     40    """
     41 msg_type: MessageType = None
     42 "The type of Content (`MessageType`)"
     43
     44 def getType(self):
     45     """ Returns the Content type """
     46     return self.msg_type
     47
     48@dataclasses.dataclass
     49class Message:
     50 """OpenC2 Message
     51    
     52    The Message class embeds all Message fields that are defined in Table 3.1 of the
     53    Language Specification. It is just an internal structure that is not automatically
     54    serialized, since the use of the fields depends on the specific transport protocol.
     55    """
     56 content: Content
     57 """ Message body as specified by `content_type` and `msg_type`. """
     58 content_type: str = _OPENC2_CONTENT_TYPE
     59 """ Media Type that identifies the format of the content, including major version."""
     60 msg_type: MessageType = None
     61 """The type of OpenC2 Message."""
     62 status: int = None
     63 """Populated with a numeric status code in Responses."""
     64 request_id: str = None
     65 """A unique identifier created by the Producer and copied by Consumer into all Responses."""
     66 created: int = None
     67 """Creation date/time of the content."""
     68 from_: str = None
     69 """Authenticated identifier of the creator of or authority for execution of a message. 
     70
     71    This field is named `from` in the Specification.
     72    """
     73 to: [] = None
     74 """ Authenticated identifier(s) of the authorized recipient(s) of a message."""
     75 version: Version = _OPENC2_VERSION
     76 """OpenC2 version used to encode the `Message`.
     77
     78    This is is an additional field not envisioned by the Language Specification.
     79    """
     80 encoding: object = None
     81 """Encoding format used to serialize the `Message`.
     82
     83    This is is an additional field not envisioned by the Language Specification.
     84    """
     85 
     86 def __post_init__(self ):
     87     self.request_id = str(uuid.uuid4()) 
     88     self.created = int(DateTime())
     89     try:
     90         self.msg_type = self.content.msg_type
     91     except AttributeError:
     92         pass
     93
     94#todo
     95 def todict(self):
     96     """ Serialization to dictionary."""
     97#dict = {"headers
     98     dic = self.__dict__
     99     return dic
    100
    101
    102# Init and other standard methods are automatically created
    103@dataclasses.dataclass
    104class Command(Content, Record):
    105   """OpenC2 Command
    106
    107  This class defines the structure of the OpenC2 Command. The name, meaning, and restrictions for
    108  the fields are described in Sec. 3.3.1 of the Specification.
    109
    110  The `target` object is implicitely initialized by passing any valid `Target`.
    111  """
    112   action: Actions
    113   target: Target
    114   args: Args = None
    115   actuator: Actuator = None
    116   command_id: str = None
    117   msg_type = MessageType.command
    118
    119   # Mind that the __post_init__ hides Exceptions!!!! 
    120   # If something fails in its code, it returns with no errors but does 
    121   # not complete the code
    122   def __post_init__(self):
    123       if not isinstance(self.target, Target):
    124           self.target = Target(self.target)
    125       if not isinstance(self.actuator, Actuator) and self.actuator is not None:
    126           self.actuator = Actuator(self.actuator)
    127
    128
    129class Response(Content, Map):
    130   """OpenC2 Response
    131
    132      This class defines the structure of the OpenC2 Response. According to the definition
    133          in Sec. 3.3.2 of the Language Specification, the `Response` contains a list of
    134        <key, value> pair. This allows for extensions by the Profiles.
    135
    136          Extensions to `Response` must extend `fieldtypes` according to the allowed field
    137          names and types. `fieldtypes` is used to parse incoming OpenC2 messages and to build
    138         and initialize   the
    139          correct Python objects for each \<key, value\> pair.      
    140  """
    141       
    142   fieldtypes = dict(status= StatusCode, status_text= str, results= Results)
    143   """The list of allowed \<key,value\> pair expected in a `Response`"""
    144   msg_type = MessageType.response
:::
:::::

::::::::::: {#MessageType .section}
::: {.attr .class}
[class]{.def} [MessageType]{.name}([enum.Enum]{.base}): View Source
:::

[](#MessageType){.headerlink}

::: {.pdoc-code .codehilite}
    28class MessageType(enum.Enum):
    29  """OpenC2 Message Type
    30 
    31 Message type can be either `command` or `response`.
    32 """
    33  command = 1
    34  response = 2
:::

::: docstring
OpenC2 Message Type

Message type can be either [`command`](#MessageType.command) or
[`response`](#MessageType.response).
:::

:::: {#MessageType.command .classattr}
::: {.attr .variable}
[command]{.name} = [\<[MessageType.command](#MessageType.command):
1\>]{.default_value}
:::

[](#MessageType.command){.headerlink}
::::

:::: {#MessageType.response .classattr}
::: {.attr .variable}
[response]{.name} = [\<[MessageType.response](#MessageType.response):
2\>]{.default_value}
:::

[](#MessageType.response){.headerlink}
::::

::: inherited
##### Inherited Members

enum.Enum
:   name
:   value
:::
:::::::::::

::::::::::::: {#Content .section}
::: {.attr .class}
[class]{.def} [Content]{.name}: View Source
:::

[](#Content){.headerlink}

::: {.pdoc-code .codehilite}
    37class Content:
    38  """ Content of the OpenC2 Message
    39
    40     A content is the base class to derive either a `Command` or a `Response`. 
    41 """
    42  msg_type: MessageType = None
    43  "The type of Content (`MessageType`)"
    44
    45  def getType(self):
    46      """ Returns the Content type """
    47      return self.msg_type
:::

::: docstring
Content of the OpenC2 Message

A content is the base class to derive either a [`Command`](#Command) or
a [`Response`](#Response).
:::

::::: {#Content.msg_type .classattr}
::: {.attr .variable}
[msg_type]{.name}[: [MessageType](#MessageType)]{.annotation} =
[None]{.default_value}
:::

[](#Content.msg_type){.headerlink}

::: docstring
The type of Content ([`MessageType`](#MessageType))
:::
:::::

:::::: {#Content.getType .classattr}
::: {.attr .function}
[def]{.def}
[getType]{.name}[([[self]{.bp}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
:::

[](#Content.getType){.headerlink}

::: {.pdoc-code .codehilite}
    45 def getType(self):
    46      """ Returns the Content type """
    47      return self.msg_type
:::

::: docstring
Returns the Content type
:::
::::::
:::::::::::::

::::::::::::::::::::::::::::::::::::::::::: {#Message .section}
:::: {.attr .class}
::: decorator
\@dataclasses.dataclass
:::

[class]{.def} [Message]{.name}: View Source
::::

[](#Message){.headerlink}

::: {.pdoc-code .codehilite}
     49@dataclasses.dataclass
     50class Message:
     51 """OpenC2 Message
     52    
     53    The Message class embeds all Message fields that are defined in Table 3.1 of the
     54    Language Specification. It is just an internal structure that is not automatically
     55    serialized, since the use of the fields depends on the specific transport protocol.
     56    """
     57 content: Content
     58 """ Message body as specified by `content_type` and `msg_type`. """
     59 content_type: str = _OPENC2_CONTENT_TYPE
     60 """ Media Type that identifies the format of the content, including major version."""
     61 msg_type: MessageType = None
     62 """The type of OpenC2 Message."""
     63 status: int = None
     64 """Populated with a numeric status code in Responses."""
     65 request_id: str = None
     66 """A unique identifier created by the Producer and copied by Consumer into all Responses."""
     67 created: int = None
     68 """Creation date/time of the content."""
     69 from_: str = None
     70 """Authenticated identifier of the creator of or authority for execution of a message. 
     71
     72    This field is named `from` in the Specification.
     73    """
     74 to: [] = None
     75 """ Authenticated identifier(s) of the authorized recipient(s) of a message."""
     76 version: Version = _OPENC2_VERSION
     77 """OpenC2 version used to encode the `Message`.
     78
     79    This is is an additional field not envisioned by the Language Specification.
     80    """
     81 encoding: object = None
     82 """Encoding format used to serialize the `Message`.
     83
     84    This is is an additional field not envisioned by the Language Specification.
     85    """
     86 
     87 def __post_init__(self ):
     88     self.request_id = str(uuid.uuid4()) 
     89     self.created = int(DateTime())
     90     try:
     91         self.msg_type = self.content.msg_type
     92     except AttributeError:
     93         pass
     94
     95#todo
     96 def todict(self):
     97     """ Serialization to dictionary."""
     98#dict = {"headers
     99     dic = self.__dict__
    100       return dic
:::

::: docstring
OpenC2 Message

The Message class embeds all Message fields that are defined in Table
3.1 of the Language Specification. It is just an internal structure that
is not automatically serialized, since the use of the fields depends on
the specific transport protocol.
:::

:::: {#Message.__init__ .classattr}
::: {.attr .function}
[Message]{.name}[([ [content]{.n}[:]{.p}
[[Content](#Content)]{.n},]{.param}[ [content_type]{.n}[:]{.p}
[str]{.nb} [=]{.o} [\'openc2\']{.s1},]{.param}[ [msg_type]{.n}[:]{.p}
[[MessageType](#MessageType)]{.n} [=]{.o} [None]{.kc},]{.param}[
[status]{.n}[:]{.p} [int]{.nb} [=]{.o} [None]{.kc},]{.param}[
[request_id]{.n}[:]{.p} [str]{.nb} [=]{.o} [None]{.kc},]{.param}[
[created]{.n}[:]{.p} [int]{.nb} [=]{.o} [None]{.kc},]{.param}[
[from\_]{.n}[:]{.p} [str]{.nb} [=]{.o} [None]{.kc},]{.param}[
[to]{.n}[:]{.p} [\[\]]{.p} [=]{.o} [None]{.kc},]{.param}[
[version]{.n}[:]{.p}
[[openc2lib.types.datatypes.Version](../types/datatypes.html#Version)]{.n}
[=]{.o} [\'1.0\']{.s1},]{.param}[ [encoding]{.n}[:]{.p} [object]{.nb}
[=]{.o} [None]{.kc}]{.param})]{.signature .pdoc-code .multiline}
:::

[](#Message.__init__){.headerlink}
::::

::::: {#Message.content .classattr}
::: {.attr .variable}
[content]{.name}[: [Content](#Content)]{.annotation}
:::

[](#Message.content){.headerlink}

::: docstring
Message body as specified by [`content_type`](#Message.content_type) and
[`msg_type`](#Message.msg_type).
:::
:::::

::::: {#Message.content_type .classattr}
::: {.attr .variable}
[content_type]{.name}[: str]{.annotation} = [\'openc2\']{.default_value}
:::

[](#Message.content_type){.headerlink}

::: docstring
Media Type that identifies the format of the content, including major
version.
:::
:::::

::::: {#Message.msg_type .classattr}
::: {.attr .variable}
[msg_type]{.name}[: [MessageType](#MessageType)]{.annotation} =
[None]{.default_value}
:::

[](#Message.msg_type){.headerlink}

::: docstring
The type of OpenC2 Message.
:::
:::::

::::: {#Message.status .classattr}
::: {.attr .variable}
[status]{.name}[: int]{.annotation} = [None]{.default_value}
:::

[](#Message.status){.headerlink}

::: docstring
Populated with a numeric status code in Responses.
:::
:::::

::::: {#Message.request_id .classattr}
::: {.attr .variable}
[request_id]{.name}[: str]{.annotation} = [None]{.default_value}
:::

[](#Message.request_id){.headerlink}

::: docstring
A unique identifier created by the Producer and copied by Consumer into
all Responses.
:::
:::::

::::: {#Message.created .classattr}
::: {.attr .variable}
[created]{.name}[: int]{.annotation} = [None]{.default_value}
:::

[](#Message.created){.headerlink}

::: docstring
Creation date/time of the content.
:::
:::::

::::: {#Message.from_ .classattr}
::: {.attr .variable}
[from\_]{.name}[: str]{.annotation} = [None]{.default_value}
:::

[](#Message.from_){.headerlink}

::: docstring
Authenticated identifier of the creator of or authority for execution of
a message.

This field is named `from` in the Specification.
:::
:::::

::::: {#Message.to .classattr}
::: {.attr .variable}
[to]{.name}[: \[\]]{.annotation} = [None]{.default_value}
:::

[](#Message.to){.headerlink}

::: docstring
Authenticated identifier(s) of the authorized recipient(s) of a message.
:::
:::::

::::: {#Message.version .classattr}
::: {.attr .variable}
[version]{.name}[:
[openc2lib.types.datatypes.Version](../types/datatypes.html#Version)]{.annotation}
= [\'1.0\']{.default_value}
:::

[](#Message.version){.headerlink}

::: docstring
OpenC2 version used to encode the [`Message`](#Message).

This is is an additional field not envisioned by the Language
Specification.
:::
:::::

::::: {#Message.encoding .classattr}
::: {.attr .variable}
[encoding]{.name}[: object]{.annotation} = [None]{.default_value}
:::

[](#Message.encoding){.headerlink}

::: docstring
Encoding format used to serialize the [`Message`](#Message).

This is is an additional field not envisioned by the Language
Specification.
:::
:::::

:::::: {#Message.todict .classattr}
::: {.attr .function}
[def]{.def}
[todict]{.name}[([[self]{.bp}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
:::

[](#Message.todict){.headerlink}

::: {.pdoc-code .codehilite}
     96  def todict(self):
     97       """ Serialization to dictionary."""
     98#dict = {"headers
     99       dic = self.__dict__
    100     return dic
:::

::: docstring
Serialization to dictionary.
:::
::::::
:::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::: {#Command .section}
:::: {.attr .class}
::: decorator
\@dataclasses.dataclass
:::

[class]{.def} [Command]{.name}([[Content](#Content)]{.base},
[[openc2lib.types.basetypes.Record](../types/basetypes.html#Record)]{.base}):
View Source
::::

[](#Command){.headerlink}

::: {.pdoc-code .codehilite}
    104@dataclasses.dataclass
    105class Command(Content, Record):
    106   """OpenC2 Command
    107
    108  This class defines the structure of the OpenC2 Command. The name, meaning, and restrictions for
    109  the fields are described in Sec. 3.3.1 of the Specification.
    110
    111  The `target` object is implicitely initialized by passing any valid `Target`.
    112  """
    113   action: Actions
    114   target: Target
    115   args: Args = None
    116   actuator: Actuator = None
    117   command_id: str = None
    118   msg_type = MessageType.command
    119
    120   # Mind that the __post_init__ hides Exceptions!!!! 
    121   # If something fails in its code, it returns with no errors but does 
    122   # not complete the code
    123   def __post_init__(self):
    124       if not isinstance(self.target, Target):
    125           self.target = Target(self.target)
    126       if not isinstance(self.actuator, Actuator) and self.actuator is not None:
    127           self.actuator = Actuator(self.actuator)
:::

::: docstring
OpenC2 Command

This class defines the structure of the OpenC2 Command. The name,
meaning, and restrictions for the fields are described in Sec. 3.3.1 of
the Specification.

The [`target`](#Command.target) object is implicitely initialized by
passing any valid `Target`.
:::

:::: {#Command.__init__ .classattr}
::: {.attr .function}
[Command]{.name}[([ [action]{.n}[:]{.p}
[[openc2lib.core.actions.Actions](actions.html#Actions)]{.n},]{.param}[
[target]{.n}[:]{.p}
[[openc2lib.core.target.Target](target.html#Target)]{.n},]{.param}[
[args]{.n}[:]{.p} [[openc2lib.core.args.Args](args.html#Args)]{.n}
[=]{.o} [None]{.kc},]{.param}[ [actuator]{.n}[:]{.p}
[[openc2lib.core.actuator.Actuator](actuator.html#Actuator)]{.n} [=]{.o}
[None]{.kc},]{.param}[ [command_id]{.n}[:]{.p} [str]{.nb} [=]{.o}
[None]{.kc}]{.param})]{.signature .pdoc-code .multiline}
:::

[](#Command.__init__){.headerlink}
::::

:::: {#Command.action .classattr}
::: {.attr .variable}
[action]{.name}[:
[openc2lib.core.actions.Actions](actions.html#Actions)]{.annotation}
:::

[](#Command.action){.headerlink}
::::

:::: {#Command.target .classattr}
::: {.attr .variable}
[target]{.name}[:
[openc2lib.core.target.Target](target.html#Target)]{.annotation}
:::

[](#Command.target){.headerlink}
::::

:::: {#Command.args .classattr}
::: {.attr .variable}
[args]{.name}[: [openc2lib.core.args.Args](args.html#Args)]{.annotation}
= [None]{.default_value}
:::

[](#Command.args){.headerlink}
::::

:::: {#Command.actuator .classattr}
::: {.attr .variable}
[actuator]{.name}[:
[openc2lib.core.actuator.Actuator](actuator.html#Actuator)]{.annotation}
= [None]{.default_value}
:::

[](#Command.actuator){.headerlink}
::::

:::: {#Command.command_id .classattr}
::: {.attr .variable}
[command_id]{.name}[: str]{.annotation} = [None]{.default_value}
:::

[](#Command.command_id){.headerlink}
::::

::::: {#Command.msg_type .classattr}
::: {.attr .variable}
[msg_type]{.name} = [\<[MessageType.command](#MessageType.command):
1\>]{.default_value}
:::

[](#Command.msg_type){.headerlink}

::: docstring
The type of Content ([`MessageType`](#MessageType))
:::
:::::

::: inherited
##### Inherited Members

[Content](#Content)
:   [getType](#Content.getType)

[openc2lib.types.basetypes.Record](../types/basetypes.html#Record)
:   [todict](../types/basetypes.html#Record.todict)
:   [fromdict](../types/basetypes.html#Record.fromdict)
:::
:::::::::::::::::::::::

::::::::::::: {#Response .section}
::: {.attr .class}
[class]{.def} [Response]{.name}([[Content](#Content)]{.base},
[[openc2lib.types.basetypes.Map](../types/basetypes.html#Map)]{.base}):
View Source
:::

[](#Response){.headerlink}

::: {.pdoc-code .codehilite}
    130class Response(Content, Map):
    131 """OpenC2 Response
    132
    133        This class defines the structure of the OpenC2 Response. According to the definition
    134            in Sec. 3.3.2 of the Language Specification, the `Response` contains a list of
    135          <key, value> pair. This allows for extensions by the Profiles.
    136
    137            Extensions to `Response` must extend `fieldtypes` according to the allowed field
    138            names and types. `fieldtypes` is used to parse incoming OpenC2 messages and to build
    139           and initialize   the
    140            correct Python objects for each \<key, value\> pair.      
    141    """
    142     
    143 fieldtypes = dict(status= StatusCode, status_text= str, results= Results)
    144 """The list of allowed \<key,value\> pair expected in a `Response`"""
    145 msg_type = MessageType.response
:::

::: docstring
OpenC2 Response

This class defines the structure of the OpenC2 Response. According to
the definition in Sec. 3.3.2 of the Language Specification, the
[`Response`](#Response) contains a list of pair. This allows for
extensions by the Profiles.

        Extensions to `Response` must extend `fieldtypes` according to the allowed field
        names and types. `fieldtypes` is used to parse incoming OpenC2 messages and to build

and initialize the correct Python objects for each \<key, value\> pair.
:::

::::: {#Response.fieldtypes .classattr}
::: {.attr .variable}
[fieldtypes]{.name} =

[{\'status\': \<aenum \'StatusCode\'\>, \'status_text\': \<class
\'str\'\>, \'results\': \<class
\'[openc2lib.core.response.Results](response.html#Results)\'\>}]{.default_value}
:::

[](#Response.fieldtypes){.headerlink}

::: docstring
The list of allowed \<key,value\> pair expected in a
[`Response`](#Response)
:::
:::::

::::: {#Response.msg_type .classattr}
::: {.attr .variable}
[msg_type]{.name} = [\<[MessageType.response](#MessageType.response):
2\>]{.default_value}
:::

[](#Response.msg_type){.headerlink}

::: docstring
The type of Content ([`MessageType`](#MessageType))
:::
:::::

::: inherited
##### Inherited Members

[Content](#Content)
:   [getType](#Content.getType)

[openc2lib.types.basetypes.Map](../types/basetypes.html#Map)
:   [extend](../types/basetypes.html#Map.extend)
:   [regext](../types/basetypes.html#Map.regext)
:   [todict](../types/basetypes.html#Map.todict)
:   [fromdict](../types/basetypes.html#Map.fromdict)

builtins.dict
:   get
:   setdefault
:   pop
:   popitem
:   keys
:   items
:   values
:   update
:   fromkeys
:   clear
:   copy
:::
:::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
