![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAzMCAzMCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLW1pdGVybGltaXQ9IjEwIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik00IDdoMjJNNCAxNWgyMk00IDIzaDIyIiAvPjwvc3ZnPg==)

<div>

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0iYmkgYmktYm94LWFycm93LWluLWxlZnQiIHZpZXdib3g9IjAgMCAxNiAxNiI+CiAgPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMTAgMy41YS41LjUgMCAwIDAtLjUtLjVoLThhLjUuNSAwIDAgMC0uNS41djlhLjUuNSAwIDAgMCAuNS41aDhhLjUuNSAwIDAgMCAuNS0uNXYtMmEuNS41IDAgMCAxIDEgMHYyQTEuNSAxLjUgMCAwIDEgOS41IDE0aC04QTEuNSAxLjUgMCAwIDEgMCAxMi41di05QTEuNSAxLjUgMCAwIDEgMS41IDJoOEExLjUgMS41IDAgMCAxIDExIDMuNXYyYS41LjUgMCAwIDEtMSAwdi0yeiIgLz4KICA8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00LjE0NiA4LjM1NGEuNS41IDAgMCAxIDAtLjcwOGwzLTNhLjUuNSAwIDEgMSAuNzA4LjcwOEw1LjcwNyA3LjVIMTQuNWEuNS41IDAgMCAxIDAgMUg1LjcwN2wyLjE0NyAyLjE0NmEuNS41IDAgMCAxLS43MDguNzA4bC0zLTN6IiAvPgo8L3N2Zz4=){.bi
.bi-box-arrow-in-left}  openc2lib.types](../types.html){.pdoc-button
.module-list-button}

## API Documentation

-   [IPv4Addr](#IPv4Addr){.class}
    -   [IPv4Addr](#IPv4Addr.__init__){.function}
-   [L4Protocol](#L4Protocol){.class}
    -   [icmp](#L4Protocol.icmp){.variable}
    -   [tcp](#L4Protocol.tcp){.variable}
    -   [udp](#L4Protocol.udp){.variable}
    -   [sctp](#L4Protocol.sctp){.variable}
-   [DateTime](#DateTime){.class}
    -   [DateTime](#DateTime.__init__){.function}
    -   [update](#DateTime.update){.function}
    -   [httpdate](#DateTime.httpdate){.function}
-   [Duration](#Duration){.class}
    -   [Duration](#Duration.__init__){.function}
-   [Version](#Version){.class}
    -   [Version](#Version.__init__){.function}
    -   [major](#Version.major){.variable}
    -   [minor](#Version.minor){.variable}
    -   [fromstr](#Version.fromstr){.function}
    -   [fromdict](#Version.fromdict){.function}
-   [Feature](#Feature){.class}
    -   [versions](#Feature.versions){.variable}
    -   [profiles](#Feature.profiles){.variable}
    -   [pairs](#Feature.pairs){.variable}
    -   [rate_limit](#Feature.rate_limit){.variable}
-   [Nsid](#Nsid){.class}
    -   [Nsid](#Nsid.__init__){.function}
    -   [fromdict](#Nsid.fromdict){.function}
-   [ResponseType](#ResponseType){.class}
    -   [none](#ResponseType.none){.variable}
    -   [ack](#ResponseType.ack){.variable}
    -   [status](#ResponseType.status){.variable}
    -   [complete](#ResponseType.complete){.variable}
-   [TargetEnum](#TargetEnum){.class}
    -   [features](#TargetEnum.features){.variable}
    -   [ipv4_net](#TargetEnum.ipv4_net){.variable}
    -   [ipv4_connection](#TargetEnum.ipv4_connection){.variable}
    -   [slpf:rule_number](#TargetEnum.slpf:rule_number){.variable}
-   [ActionTargets](#ActionTargets){.class}
-   [ActionArguments](#ActionArguments){.class}

[built with [pdoc]{.visually-hidden}![pdoc
logo](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20role%3D%22img%22%20aria-label%3D%22pdoc%20logo%22%20width%3D%22300%22%20height%3D%22150%22%20viewBox%3D%22-1%200%2060%2030%22%3E%3Ctitle%3Epdoc%3C/title%3E%3Cpath%20d%3D%22M29.621%2021.293c-.011-.273-.214-.475-.511-.481a.5.5%200%200%200-.489.503l-.044%201.393c-.097.551-.695%201.215-1.566%201.704-.577.428-1.306.486-2.193.182-1.426-.617-2.467-1.654-3.304-2.487l-.173-.172a3.43%203.43%200%200%200-.365-.306.49.49%200%200%200-.286-.196c-1.718-1.06-4.931-1.47-7.353.191l-.219.15c-1.707%201.187-3.413%202.131-4.328%201.03-.02-.027-.49-.685-.141-1.763.233-.721.546-2.408.772-4.076.042-.09.067-.187.046-.288.166-1.347.277-2.625.241-3.351%201.378-1.008%202.271-2.586%202.271-4.362%200-.976-.272-1.935-.788-2.774-.057-.094-.122-.18-.184-.268.033-.167.052-.339.052-.516%200-1.477-1.202-2.679-2.679-2.679-.791%200-1.496.352-1.987.9a6.3%206.3%200%200%200-1.001.029c-.492-.564-1.207-.929-2.012-.929-1.477%200-2.679%201.202-2.679%202.679A2.65%202.65%200%200%200%20.97%206.554c-.383.747-.595%201.572-.595%202.41%200%202.311%201.507%204.29%203.635%205.107-.037.699-.147%202.27-.423%203.294l-.137.461c-.622%202.042-2.515%208.257%201.727%2010.643%201.614.908%203.06%201.248%204.317%201.248%202.665%200%204.492-1.524%205.322-2.401%201.476-1.559%202.886-1.854%206.491.82%201.877%201.393%203.514%201.753%204.861%201.068%202.223-1.713%202.811-3.867%203.399-6.374.077-.846.056-1.469.054-1.537zm-4.835%204.313c-.054.305-.156.586-.242.629-.034-.007-.131-.022-.307-.157-.145-.111-.314-.478-.456-.908.221.121.432.25.675.355.115.039.219.051.33.081zm-2.251-1.238c-.05.33-.158.648-.252.694-.022.001-.125-.018-.307-.157-.217-.166-.488-.906-.639-1.573.358.344.754.693%201.198%201.036zm-3.887-2.337c-.006-.116-.018-.231-.041-.342.635.145%201.189.368%201.599.625.097.231.166.481.174.642-.03.049-.055.101-.067.158-.046.013-.128.026-.298.004-.278-.037-.901-.57-1.367-1.087zm-1.127-.497c.116.306.176.625.12.71-.019.014-.117.045-.345.016-.206-.027-.604-.332-.986-.695.41-.051.816-.056%201.211-.031zm-4.535%201.535c.209.22.379.47.358.598-.006.041-.088.138-.351.234-.144.055-.539-.063-.979-.259a11.66%2011.66%200%200%200%20.972-.573zm.983-.664c.359-.237.738-.418%201.126-.554.25.237.479.548.457.694-.006.042-.087.138-.351.235-.174.064-.694-.105-1.232-.375zm-3.381%201.794c-.022.145-.061.29-.149.401-.133.166-.358.248-.69.251h-.002c-.133%200-.306-.26-.45-.621.417.091.854.07%201.291-.031zm-2.066-8.077a4.78%204.78%200%200%201-.775-.584c.172-.115.505-.254.88-.378l-.105.962zm-.331%202.302a10.32%2010.32%200%200%201-.828-.502c.202-.143.576-.328.984-.49l-.156.992zm-.45%202.157l-.701-.403c.214-.115.536-.249.891-.376a11.57%2011.57%200%200%201-.19.779zm-.181%201.716c.064.398.194.702.298.893-.194-.051-.435-.162-.736-.398.061-.119.224-.3.438-.495zM8.87%204.141c0%20.152-.123.276-.276.276s-.275-.124-.275-.276.123-.276.276-.276.275.124.275.276zm-.735-.389a1.15%201.15%200%200%200-.314.783%201.16%201.16%200%200%200%201.162%201.162c.457%200%20.842-.27%201.032-.653.026.117.042.238.042.362a1.68%201.68%200%200%201-1.679%201.679%201.68%201.68%200%200%201-1.679-1.679c0-.843.626-1.535%201.436-1.654zM5.059%205.406A1.68%201.68%200%200%201%203.38%207.085a1.68%201.68%200%200%201-1.679-1.679c0-.037.009-.072.011-.109.21.3.541.508.935.508a1.16%201.16%200%200%200%201.162-1.162%201.14%201.14%200%200%200-.474-.912c.015%200%20.03-.005.045-.005.926.001%201.679.754%201.679%201.68zM3.198%204.141c0%20.152-.123.276-.276.276s-.275-.124-.275-.276.123-.276.276-.276.275.124.275.276zM1.375%208.964c0-.52.103-1.035.288-1.52.466.394%201.06.64%201.717.64%201.144%200%202.116-.725%202.499-1.738.383%201.012%201.355%201.738%202.499%201.738.867%200%201.631-.421%202.121-1.062.307.605.478%201.267.478%201.942%200%202.486-2.153%204.51-4.801%204.51s-4.801-2.023-4.801-4.51zm24.342%2019.349c-.985.498-2.267.168-3.813-.979-3.073-2.281-5.453-3.199-7.813-.705-1.315%201.391-4.163%203.365-8.423.97-3.174-1.786-2.239-6.266-1.261-9.479l.146-.492c.276-1.02.395-2.457.444-3.268a6.11%206.11%200%200%200%201.18.115%206.01%206.01%200%200%200%202.536-.562l-.006.175c-.802.215-1.848.612-2.021%201.25-.079.295.021.601.274.837.219.203.415.364.598.501-.667.304-1.243.698-1.311%201.179-.02.144-.022.507.393.787.213.144.395.26.564.365-1.285.521-1.361.96-1.381%201.126-.018.142-.011.496.427.746l.854.489c-.473.389-.971.914-.999%201.429-.018.278.095.532.316.713.675.556%201.231.721%201.653.721.059%200%20.104-.014.158-.02.207.707.641%201.64%201.513%201.64h.013c.8-.008%201.236-.345%201.462-.626.173-.216.268-.457.325-.692.424.195.93.374%201.372.374.151%200%20.294-.021.423-.068.732-.27.944-.704.993-1.021.009-.061.003-.119.002-.179.266.086.538.147.789.147.15%200%20.294-.021.423-.069.542-.2.797-.489.914-.754.237.147.478.258.704.288.106.014.205.021.296.021.356%200%20.595-.101.767-.229.438.435%201.094.992%201.656%201.067.106.014.205.021.296.021a1.56%201.56%200%200%200%20.323-.035c.17.575.453%201.289.866%201.605.358.273.665.362.914.362a.99.99%200%200%200%20.421-.093%201.03%201.03%200%200%200%20.245-.164c.168.428.39.846.68%201.068.358.273.665.362.913.362a.99.99%200%200%200%20.421-.093c.317-.148.512-.448.639-.762.251.157.495.257.726.257.127%200%20.25-.024.37-.071.427-.17.706-.617.841-1.314.022-.015.047-.022.068-.038.067-.051.133-.104.196-.159-.443%201.486-1.107%202.761-2.086%203.257zM8.66%209.925a.5.5%200%201%200-1%200c0%20.653-.818%201.205-1.787%201.205s-1.787-.552-1.787-1.205a.5.5%200%201%200-1%200c0%201.216%201.25%202.205%202.787%202.205s2.787-.989%202.787-2.205zm4.4%2015.965l-.208.097c-2.661%201.258-4.708%201.436-6.086.527-1.542-1.017-1.88-3.19-1.844-4.198a.4.4%200%200%200-.385-.414c-.242-.029-.406.164-.414.385-.046%201.249.367%203.686%202.202%204.896.708.467%201.547.7%202.51.7%201.248%200%202.706-.392%204.362-1.174l.185-.086a.4.4%200%200%200%20.205-.527c-.089-.204-.326-.291-.527-.206zM9.547%202.292c.093.077.205.114.317.114a.5.5%200%200%200%20.318-.886L8.817.397a.5.5%200%200%200-.703.068.5.5%200%200%200%20.069.703l1.364%201.124zm-7.661-.065c.086%200%20.173-.022.253-.068l1.523-.893a.5.5%200%200%200-.506-.863l-1.523.892a.5.5%200%200%200-.179.685c.094.158.261.247.432.247z%22%20transform%3D%22matrix%28-1%200%200%201%2058%200%29%22%20fill%3D%22%233bb300%22/%3E%3Cpath%20d%3D%22M.3%2021.86V10.18q0-.46.02-.68.04-.22.18-.5.28-.54%201.34-.54%201.06%200%201.42.28.38.26.44.78.76-1.04%202.38-1.04%201.64%200%203.1%201.54%201.46%201.54%201.46%203.58%200%202.04-1.46%203.58-1.44%201.54-3.08%201.54-1.64%200-2.38-.92v4.04q0%20.46-.04.68-.02.22-.18.5-.14.3-.5.42-.36.12-.98.12-.62%200-1-.12-.36-.12-.52-.4-.14-.28-.18-.5-.02-.22-.02-.68zm3.96-9.42q-.46.54-.46%201.18%200%20.64.46%201.18.48.52%201.2.52.74%200%201.24-.52.52-.52.52-1.18%200-.66-.48-1.18-.48-.54-1.26-.54-.76%200-1.22.54zm14.741-8.36q.16-.3.54-.42.38-.12%201-.12.64%200%201.02.12.38.12.52.42.16.3.18.54.04.22.04.68v11.94q0%20.46-.04.7-.02.22-.18.5-.3.54-1.7.54-1.38%200-1.54-.98-.84.96-2.34.96-1.8%200-3.28-1.56-1.48-1.58-1.48-3.66%200-2.1%201.48-3.68%201.5-1.58%203.28-1.58%201.48%200%202.3%201v-4.2q0-.46.02-.68.04-.24.18-.52zm-3.24%2010.86q.52.54%201.26.54.74%200%201.22-.54.5-.54.5-1.18%200-.66-.48-1.22-.46-.56-1.26-.56-.8%200-1.28.56-.48.54-.48%201.2%200%20.66.52%201.2zm7.833-1.2q0-2.4%201.68-3.96%201.68-1.56%203.84-1.56%202.16%200%203.82%201.56%201.66%201.54%201.66%203.94%200%201.66-.86%202.96-.86%201.28-2.1%201.9-1.22.6-2.54.6-1.32%200-2.56-.64-1.24-.66-2.1-1.92-.84-1.28-.84-2.88zm4.18%201.44q.64.48%201.3.48.66%200%201.32-.5.66-.5.66-1.48%200-.98-.62-1.46-.62-.48-1.34-.48-.72%200-1.34.5-.62.5-.62%201.48%200%20.96.64%201.46zm11.412-1.44q0%20.84.56%201.32.56.46%201.18.46.64%200%201.18-.36.56-.38.9-.38.6%200%201.46%201.06.46.58.46%201.04%200%20.76-1.1%201.42-1.14.8-2.8.8-1.86%200-3.58-1.34-.82-.64-1.34-1.7-.52-1.08-.52-2.36%200-1.3.52-2.34.52-1.06%201.34-1.7%201.66-1.32%203.54-1.32.76%200%201.48.22.72.2%201.06.4l.32.2q.36.24.56.38.52.4.52.92%200%20.5-.42%201.14-.72%201.1-1.38%201.1-.38%200-1.08-.44-.36-.34-1.04-.34-.66%200-1.24.48-.58.48-.58%201.34z%22%20fill%3D%22green%22/%3E%3C/svg%3E)](https://pdoc.dev "pdoc: Python API documentation generator"){.attribution
target="_blank"}

</div>

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.pdoc role="main"}
::::: {.section .module-info}
# [openc2lib](./../../openc2lib.html).[types](./../types.html).datatypes {#openc2lib.types.datatypes .modulename}

::: docstring
OpenC2 data types

Definition of the data types in the OpenC2 DataModels (Sec. 3.4.2). The
naming strictly follows the definition of the Language Specification as
close as possible. The relevant exception is represented by hyphens that
are always dropped.
:::

View Source

::: {.pdoc-code .codehilite}
      1""" OpenC2 data types
      2
      3  Definition of the data types in the OpenC2 DataModels (Sec. 3.4.2).
      4  The naming strictly follows the definition of the Language Specification
      5  as close as possible. The relevant exception is represented by hyphens
      6  that are always dropped.
      7"""
      8
      9import ipaddress
     10import aenum
     11import datetime 
     12import dataclasses
     13
     14from openc2lib.types.basetypes import MapOf, Enumerated, ArrayOf
     15from openc2lib.core.actions import Actions
     16
     17
     18""" IPv4 Address
     19
     20    This class implements an IPv4 Address as described in Sec. 3.4.2.8.
     21
     22The usage of the ipaddress module is compliant to what required in the
     23language specification for IPv4 addresses, especially the following points:
     24a) The IPv4 address should be available both in string and binary form
     25b) The network representation is an array according to RFC 4632 Sec. 3.1
     26   (host/prefix, host/mask, host/hostmask, etc.)
     27"""
     28class IPv4Addr:
     29 """OpenC2 IPv4 Address"
     30
     31        This class implements an IPv4 Address as described in Sec. 3.4.2.8.
     32
     33        The usage of the ipaddress module is compliant to what required in the
     34        language specification for IPv4 addresses, especially the following points:
     35        a) The IPv4 address should be available both in string and binary form
     36        b) The network representation is an array according to RFC 4632 Sec. 3.1
     37           (host/prefix, host/mask, host/hostmask, etc.)
     38
     39"""
     40 __ipv4_addr = ipaddress.IPv4Address("0.0.0.0")
     41 """ Internal representation of the IPv4 address"""
     42 
     43 def __init__(self, ipaddr=None):
     44     """ Initialize IPv4 Address 
     45
     46            An IPv4 address is built from a string that uses the common dotted notation.
     47            If no IPv4 address is provided, the null address is used ("0.0.0.0").
     48
     49            :param ipaddr: Quad-dotted representation of the IPv4 address.
     50        """
     51     if ipaddr == None:
     52         self.__ipv4_addr = ipaddress.IPv4Address("0.0.0.0")
     53     else:
     54         self.__ipv4_addr = ipaddress.IPv4Address(ipaddr)
     55
     56 def __str__(self):
     57     return self.__ipv4_addr.exploded
     58
     59 def __repr__(self):
     60     return self.__ipv4_addr.exploded
     61
     62class L4Protocol(Enumerated):
     63 """ OpenC2 L4 Protocol
     64
     65        This is an enumeration for all known transport protocols. The numeric identifier
     66        is set to the protocol number defined for IP.
     67    """
     68 icmp = 1
     69 tcp = 6
     70 udp = 17
     71 sctp = 132
     72
     73class DateTime:
     74 """ OpenC2 Date-Time
     75
     76        This is used to represents dates and times according to Sec. 3.4.2.2.
     77         According to OpenC2 specification, this is the time in milliseconds from the epoch.
     78        Be careful that the `timedate` functions work with float timestamps expressed 
     79        in seconds from the epoch, hence conversion is needed.
     80    """
     81 def __init__(self, timestamp=None):
     82     """ Initialize Date-Time
     83            
     84            The instance is initialized with the provided timestamp, or to the current time if no 
     85            argument is given. The timestamp is expressed in milliseconds
     86                from the epoch, according to the Language Specification.
     87            :param timestamp: The timestamp to initialize the instance.
     88        """
     89     self.update(timestamp)
     90
     91 def __str__(self):
     92     return str(self.time)
     93
     94 def __int__(self):
     95     return self.time
     96
     97 def update(self, timestamp=None):
     98     """ Change Date-Time
     99
    100          Change the timestamp beard by the instance. The timestamp is expressed in milliseconds
    101          from the epoch. If no `timestamp` is given, sets to the current time.
    102          :param timestamp: The timestamp to initialize the instance.
    103      """
    104       if timestamp == None:
    105           # datetime.timestamp() returns a float in seconds
    106           self.time = int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
    107       else:
    108           self.time = timestamp
    109
    110   # RFC 7231       
    111   def httpdate(self, timestamp=None):
    112       """ Format  to HTTP headers
    113
    114          Formats the timestamp according to the requirements of HTTP headers (RFC 7231).
    115          Use either the `timestamp`, if provided,  or the current time.
    116          :param timestamp: The timestamp to format, expressed in milliseconds from the epoch.
    117          :return RFC 7231 representation of the `timestamp`.
    118      """
    119           
    120       if timestamp is None:
    121           timestamp = self.time
    122
    123       return datetime.datetime.fromtimestamp(timestamp/1000).strftime('%a, %d %b %Y %H:%M:%S %Z')
    124
    125class Duration(int):
    126   """ OpenC2 Duration
    127
    128       A time (positive number) expressed in milliseconds (Sec. 3.4.2.3).
    129  """ 
    130   def __init__(self, dur):
    131       """ Initialization
    132
    133          Initialize to `dur` if greater or equal to zero, raise an exception if negative.
    134      """
    135       if int(dur) < 0:
    136           raise ValueError("Duration must be a positive number")
    137       self=int(dur)
    138
    139class Version(str):
    140   """ OpenC2 Version
    141
    142      Version of the OpenC2 protocol (Sec. 3.4.2.16). Currently a *<major>.<minor>* format is used.
    143  """
    144   def __new__(cls, major, minor):
    145       """ Create `Version` instance
    146
    147          Create a Version instance from major and minor numbers, expressed as numbers.
    148          :param major: Major number of OpenC2 version.
    149          :param minor: Minor number of OpenC2 version.
    150          :return: `Version` instance.
    151      """
    152       vers = str(major) + '.' + str(minor)
    153       instance = super().__new__(cls, vers)
    154       return instance
    155
    156   def __init__(self, major, minor):
    157       """ Initialize `Version` instance
    158
    159          Initialize with major and minor numbers.
    160          :param major: Major number of OpenC2 version.
    161          :param minor: Minor number of OpenC2 version.
    162          :return: `Version` instance.
    163      """
    164       self.major = major
    165       self.minor = minor
    166
    167   @staticmethod
    168   def fromstr(v):
    169       """ Create `Version` instance
    170
    171          Create `Version` instance from string (in the *<major>.<minor>* notation.
    172          :param v: Text string with the Version.
    173          :return: `Version` instance.
    174      """
    175       vers = v.split('.',2)
    176       return Version(vers[0], vers[1])
    177   
    178   @classmethod
    179   def fromdict(cls, vers, e=None):
    180       """ Create `Version` instance
    181
    182          Create `Version` instance from string (in the *<major>.<minor>* notation.
    183          This method is provided to deserialize an OpenC2 message according to the openc2lib approach.
    184          This method should only be used internally the openc2lib.
    185          :param vers: Text string with the Version.
    186          :param e: `Encoder` instance to be used (only included to be compliance with the function footprint.
    187          :return: `Version` instance.
    188      """
    189       return Version.fromstr(vers)
    190
    191class Feature(Enumerated):
    192   """ OpenC2 Feature
    193
    194      An enumeration for the fields that can be included in the `Results` (see Sec. 3.4.2.4).
    195  """
    196   versions   = 1
    197   profiles   = 2
    198   pairs      = 3
    199   rate_limit = 4
    200
    201
    202       
    203class Nsid(str):
    204   """ OpenC2 Namespace Identifier
    205
    206      Namespace identifiers are described in Sec. 3.1.4. This class implements the required
    207          controls on the string length.
    208  """
    209   def __init__(self, nsid):
    210       """ Initialize `Nsid`
    211
    212          :param nsid: Text string (must be more than 1 and less than 16 characters.
    213      """
    214       if len(nsid) > 16 or len(nsid) < 1:
    215           raise ValueError("Nsid must be between 1 and 16 characters")
    216       self = nsid
    217
    218   @classmethod
    219   def fromdict(cls, name, e):
    220       """ Create `Nsid` instance
    221
    222          Create `Nsid` instance from string.
    223          This method is provided to deserialize an OpenC2 message according to the openc2lib approach.
    224          This method should only be used internally the openc2lib.
    225          :param name: Text string with the namespace identifier..
    226          :param e: `Encoder` instance to be used (only included to be compliance with the function footprint.
    227          :return: `Version` instance.
    228      """
    229       return Nsid(name)
    230   
    231class ResponseType(Enumerated):
    232   """ OpenC2 Response-Type
    233
    234      Enumerates the Response-Types according to Sec. 3.4.2.15.   
    235  """   
    236   none=0
    237   ack=1
    238   status=2
    239   complete=3
    240
    241class TargetEnum(Enumerated):
    242   """ OpenC2 Targets names
    243  
    244      The Language Specification defines a *Targets* subtypes only used in Sec. 3.4.2.1.
    245      The openc2lib uses this class to keep a record of all registered Target names, while
    246      the *Targets* type is never defined (it is build in an unnamed way to create the 
    247      `ActionTargets`.
    248
    249      This class is only expected to be used internally by the openc2lib.
    250  """
    251   def __repr__(self):
    252       return self.name
    253
    254class ActionTargets(MapOf(Actions, ArrayOf(TargetEnum))):
    255   """ OpenC2 Action-Targets
    256
    257      Map of each action supported by an actuator to the list of targets applicable to 
    258      that action (Sec. 3.4.2.1).
    259      They must be defined by each Profile.
    260  """
    261   pass
    262
    263class ActionArguments(MapOf(Actions, ArrayOf(str))):
    264   """ OpenC2 Action-Arguments mapping
    265
    266      Map of each action supported by an actuator to the list of arguments applicable to
    267      that action. 
    268      This is not defined in the Language Specification, but used e.g., by the SLPF Profile.
    269  """
    270   pass
:::
:::::

:::::::::: {#IPv4Addr .section}
::: {.attr .class}
[class]{.def} [IPv4Addr]{.name}: View Source
:::

[](#IPv4Addr){.headerlink}

::: {.pdoc-code .codehilite}
    29class IPv4Addr:
    30    """OpenC2 IPv4 Address"
    31
    32       This class implements an IPv4 Address as described in Sec. 3.4.2.8.
    33
    34       The usage of the ipaddress module is compliant to what required in the
    35       language specification for IPv4 addresses, especially the following points:
    36       a) The IPv4 address should be available both in string and binary form
    37       b) The network representation is an array according to RFC 4632 Sec. 3.1
    38          (host/prefix, host/mask, host/hostmask, etc.)
    39
    40"""
    41    __ipv4_addr = ipaddress.IPv4Address("0.0.0.0")
    42    """ Internal representation of the IPv4 address"""
    43    
    44    def __init__(self, ipaddr=None):
    45        """ Initialize IPv4 Address 
    46
    47           An IPv4 address is built from a string that uses the common dotted notation.
    48           If no IPv4 address is provided, the null address is used ("0.0.0.0").
    49
    50           :param ipaddr: Quad-dotted representation of the IPv4 address.
    51       """
    52        if ipaddr == None:
    53            self.__ipv4_addr = ipaddress.IPv4Address("0.0.0.0")
    54        else:
    55            self.__ipv4_addr = ipaddress.IPv4Address(ipaddr)
    56
    57    def __str__(self):
    58        return self.__ipv4_addr.exploded
    59
    60    def __repr__(self):
    61        return self.__ipv4_addr.exploded
:::

::: docstring
OpenC2 IPv4 Address\"

This class implements an IPv4 Address as described in Sec. 3.4.2.8.

The usage of the ipaddress module is compliant to what required in the
language specification for IPv4 addresses, especially the following
points: a) The IPv4 address should be available both in string and
binary form b) The network representation is an array according to RFC
4632 Sec. 3.1 (host/prefix, host/mask, host/hostmask, etc.)
:::

:::::: {#IPv4Addr.__init__ .classattr}
::: {.attr .function}
[IPv4Addr]{.name}[([[ipaddr]{.n}[=]{.o}[None]{.kc}]{.param})]{.signature
.pdoc-code .condensed} View Source
:::

[](#IPv4Addr.__init__){.headerlink}

::: {.pdoc-code .codehilite}
    44 def __init__(self, ipaddr=None):
    45      """ Initialize IPv4 Address 
    46
    47         An IPv4 address is built from a string that uses the common dotted notation.
    48         If no IPv4 address is provided, the null address is used ("0.0.0.0").
    49
    50         :param ipaddr: Quad-dotted representation of the IPv4 address.
    51     """
    52      if ipaddr == None:
    53          self.__ipv4_addr = ipaddress.IPv4Address("0.0.0.0")
    54      else:
    55          self.__ipv4_addr = ipaddress.IPv4Address(ipaddr)
:::

::: docstring
Initialize IPv4 Address

An IPv4 address is built from a string that uses the common dotted
notation. If no IPv4 address is provided, the null address is used
(\"0.0.0.0\").

###### Parameters

-   **ipaddr**: Quad-dotted representation of the IPv4 address.
:::
::::::
::::::::::

::::::::::::::: {#L4Protocol .section}
::: {.attr .class}
[class]{.def}
[L4Protocol]{.name}([[openc2lib.types.basetypes.Enumerated](basetypes.html#Enumerated)]{.base}):
View Source
:::

[](#L4Protocol){.headerlink}

::: {.pdoc-code .codehilite}
    63class L4Protocol(Enumerated):
    64    """ OpenC2 L4 Protocol
    65
    66       This is an enumeration for all known transport protocols. The numeric identifier
    67       is set to the protocol number defined for IP.
    68   """
    69    icmp = 1
    70    tcp = 6
    71    udp = 17
    72    sctp = 132
:::

::: docstring
OpenC2 L4 Protocol

This is an enumeration for all known transport protocols. The numeric
identifier is set to the protocol number defined for IP.
:::

:::: {#L4Protocol.icmp .classattr}
::: {.attr .variable}
[icmp]{.name} = [\<[L4Protocol.icmp](#L4Protocol.icmp):
1\>]{.default_value}
:::

[](#L4Protocol.icmp){.headerlink}
::::

:::: {#L4Protocol.tcp .classattr}
::: {.attr .variable}
[tcp]{.name} = [\<[L4Protocol.tcp](#L4Protocol.tcp):
6\>]{.default_value}
:::

[](#L4Protocol.tcp){.headerlink}
::::

:::: {#L4Protocol.udp .classattr}
::: {.attr .variable}
[udp]{.name} = [\<[L4Protocol.udp](#L4Protocol.udp):
17\>]{.default_value}
:::

[](#L4Protocol.udp){.headerlink}
::::

:::: {#L4Protocol.sctp .classattr}
::: {.attr .variable}
[sctp]{.name} = [\<[L4Protocol.sctp](#L4Protocol.sctp):
132\>]{.default_value}
:::

[](#L4Protocol.sctp){.headerlink}
::::

::: inherited
##### Inherited Members

[openc2lib.types.basetypes.Enumerated](basetypes.html#Enumerated)
:   [todict](basetypes.html#Enumerated.todict)
:   [fromdict](basetypes.html#Enumerated.fromdict)

aenum.\_enum.Enum
:   name
:   value
:   values
:::
:::::::::::::::

:::::::::::::::::: {#DateTime .section}
::: {.attr .class}
[class]{.def} [DateTime]{.name}: View Source
:::

[](#DateTime){.headerlink}

::: {.pdoc-code .codehilite}
     74class DateTime:
     75   """ OpenC2 Date-Time
     76
     77      This is used to represents dates and times according to Sec. 3.4.2.2.
     78       According to OpenC2 specification, this is the time in milliseconds from the epoch.
     79      Be careful that the `timedate` functions work with float timestamps expressed 
     80      in seconds from the epoch, hence conversion is needed.
     81  """
     82   def __init__(self, timestamp=None):
     83       """ Initialize Date-Time
     84          
     85          The instance is initialized with the provided timestamp, or to the current time if no 
     86          argument is given. The timestamp is expressed in milliseconds
     87              from the epoch, according to the Language Specification.
     88          :param timestamp: The timestamp to initialize the instance.
     89      """
     90       self.update(timestamp)
     91
     92   def __str__(self):
     93       return str(self.time)
     94
     95   def __int__(self):
     96       return self.time
     97
     98   def update(self, timestamp=None):
     99       """ Change Date-Time
    100
    101            Change the timestamp beard by the instance. The timestamp is expressed in milliseconds
    102            from the epoch. If no `timestamp` is given, sets to the current time.
    103            :param timestamp: The timestamp to initialize the instance.
    104        """
    105     if timestamp == None:
    106         # datetime.timestamp() returns a float in seconds
    107         self.time = int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
    108     else:
    109         self.time = timestamp
    110
    111 # RFC 7231       
    112 def httpdate(self, timestamp=None):
    113     """ Format  to HTTP headers
    114
    115            Formats the timestamp according to the requirements of HTTP headers (RFC 7231).
    116            Use either the `timestamp`, if provided,  or the current time.
    117            :param timestamp: The timestamp to format, expressed in milliseconds from the epoch.
    118            :return RFC 7231 representation of the `timestamp`.
    119        """
    120         
    121     if timestamp is None:
    122         timestamp = self.time
    123
    124     return datetime.datetime.fromtimestamp(timestamp/1000).strftime('%a, %d %b %Y %H:%M:%S %Z')
:::

::: docstring
OpenC2 Date-Time

This is used to represents dates and times according to Sec. 3.4.2.2.
According to OpenC2 specification, this is the time in milliseconds from
the epoch. Be careful that the `timedate` functions work with float
timestamps expressed in seconds from the epoch, hence conversion is
needed.
:::

:::::: {#DateTime.__init__ .classattr}
::: {.attr .function}
[DateTime]{.name}[([[timestamp]{.n}[=]{.o}[None]{.kc}]{.param})]{.signature
.pdoc-code .condensed} View Source
:::

[](#DateTime.__init__){.headerlink}

::: {.pdoc-code .codehilite}
    82 def __init__(self, timestamp=None):
    83      """ Initialize Date-Time
    84         
    85         The instance is initialized with the provided timestamp, or to the current time if no 
    86         argument is given. The timestamp is expressed in milliseconds
    87             from the epoch, according to the Language Specification.
    88         :param timestamp: The timestamp to initialize the instance.
    89     """
    90      self.update(timestamp)
:::

::: docstring
Initialize Date-Time

The instance is initialized with the provided timestamp, or to the
current time if no argument is given. The timestamp is expressed in
milliseconds from the epoch, according to the Language Specification.

###### Parameters {#parameters}

-   **timestamp**: The timestamp to initialize the instance.
:::
::::::

:::::: {#DateTime.update .classattr}
::: {.attr .function}
[def]{.def} [update]{.name}[([[self]{.bp},
]{.param}[[timestamp]{.n}[=]{.o}[None]{.kc}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
:::

[](#DateTime.update){.headerlink}

::: {.pdoc-code .codehilite}
     98    def update(self, timestamp=None):
     99     """ Change Date-Time
    100
    101          Change the timestamp beard by the instance. The timestamp is expressed in milliseconds
    102          from the epoch. If no `timestamp` is given, sets to the current time.
    103          :param timestamp: The timestamp to initialize the instance.
    104      """
    105       if timestamp == None:
    106           # datetime.timestamp() returns a float in seconds
    107           self.time = int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
    108       else:
    109           self.time = timestamp
:::

::: docstring
Change Date-Time

Change the timestamp beard by the instance. The timestamp is expressed
in milliseconds from the epoch. If no `timestamp` is given, sets to the
current time.

###### Parameters {#parameters}

-   **timestamp**: The timestamp to initialize the instance.
:::
::::::

:::::: {#DateTime.httpdate .classattr}
::: {.attr .function}
[def]{.def} [httpdate]{.name}[([[self]{.bp},
]{.param}[[timestamp]{.n}[=]{.o}[None]{.kc}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
:::

[](#DateTime.httpdate){.headerlink}

::: {.pdoc-code .codehilite}
    112  def httpdate(self, timestamp=None):
    113       """ Format  to HTTP headers
    114
    115          Formats the timestamp according to the requirements of HTTP headers (RFC 7231).
    116          Use either the `timestamp`, if provided,  or the current time.
    117          :param timestamp: The timestamp to format, expressed in milliseconds from the epoch.
    118          :return RFC 7231 representation of the `timestamp`.
    119      """
    120           
    121       if timestamp is None:
    122           timestamp = self.time
    123
    124       return datetime.datetime.fromtimestamp(timestamp/1000).strftime('%a, %d %b %Y %H:%M:%S %Z')
:::

::: docstring
Format to HTTP headers

Formats the timestamp according to the requirements of HTTP headers (RFC
7231). Use either the `timestamp`, if provided, or the current time.

###### Parameters {#parameters}

-   **timestamp**: The timestamp to format, expressed in milliseconds
    from the epoch. :return RFC 7231 representation of the `timestamp`.
:::
::::::
::::::::::::::::::

::::::::::: {#Duration .section}
::: {.attr .class}
[class]{.def} [Duration]{.name}([builtins.int]{.base}): View Source
:::

[](#Duration){.headerlink}

::: {.pdoc-code .codehilite}
    126class Duration(int):
    127 """ OpenC2 Duration
    128
    129         A time (positive number) expressed in milliseconds (Sec. 3.4.2.3).
    130    """ 
    131 def __init__(self, dur):
    132     """ Initialization
    133
    134            Initialize to `dur` if greater or equal to zero, raise an exception if negative.
    135        """
    136     if int(dur) < 0:
    137         raise ValueError("Duration must be a positive number")
    138     self=int(dur)
:::

::: docstring
OpenC2 Duration

A time (positive number) expressed in milliseconds (Sec. 3.4.2.3).
:::

:::::: {#Duration.__init__ .classattr}
::: {.attr .function}
[Duration]{.name}[([[dur]{.n}]{.param})]{.signature .pdoc-code
.condensed} View Source
:::

[](#Duration.__init__){.headerlink}

::: {.pdoc-code .codehilite}
    131  def __init__(self, dur):
    132       """ Initialization
    133
    134          Initialize to `dur` if greater or equal to zero, raise an exception if negative.
    135      """
    136       if int(dur) < 0:
    137           raise ValueError("Duration must be a positive number")
    138       self=int(dur)
:::

::: docstring
Initialization

Initialize to `dur` if greater or equal to zero, raise an exception if
negative.
:::
::::::

::: inherited
##### Inherited Members

builtins.int
:   conjugate
:   bit_length
:   bit_count
:   to_bytes
:   from_bytes
:   as_integer_ratio
:   real
:   imag
:   numerator
:   denominator
:::
:::::::::::

::::::::::::::::::::::::: {#Version .section}
::: {.attr .class}
[class]{.def} [Version]{.name}([builtins.str]{.base}): View Source
:::

[](#Version){.headerlink}

::: {.pdoc-code .codehilite}
    140class Version(str):
    141   """ OpenC2 Version
    142
    143      Version of the OpenC2 protocol (Sec. 3.4.2.16). Currently a *<major>.<minor>* format is used.
    144  """
    145   def __new__(cls, major, minor):
    146       """ Create `Version` instance
    147
    148          Create a Version instance from major and minor numbers, expressed as numbers.
    149          :param major: Major number of OpenC2 version.
    150          :param minor: Minor number of OpenC2 version.
    151          :return: `Version` instance.
    152      """
    153       vers = str(major) + '.' + str(minor)
    154       instance = super().__new__(cls, vers)
    155       return instance
    156
    157   def __init__(self, major, minor):
    158       """ Initialize `Version` instance
    159
    160          Initialize with major and minor numbers.
    161          :param major: Major number of OpenC2 version.
    162          :param minor: Minor number of OpenC2 version.
    163          :return: `Version` instance.
    164      """
    165       self.major = major
    166       self.minor = minor
    167
    168   @staticmethod
    169   def fromstr(v):
    170       """ Create `Version` instance
    171
    172          Create `Version` instance from string (in the *<major>.<minor>* notation.
    173          :param v: Text string with the Version.
    174          :return: `Version` instance.
    175      """
    176       vers = v.split('.',2)
    177       return Version(vers[0], vers[1])
    178   
    179   @classmethod
    180   def fromdict(cls, vers, e=None):
    181       """ Create `Version` instance
    182
    183          Create `Version` instance from string (in the *<major>.<minor>* notation.
    184          This method is provided to deserialize an OpenC2 message according to the openc2lib approach.
    185          This method should only be used internally the openc2lib.
    186          :param vers: Text string with the Version.
    187          :param e: `Encoder` instance to be used (only included to be compliance with the function footprint.
    188          :return: `Version` instance.
    189      """
    190       return Version.fromstr(vers)
:::

::: docstring
OpenC2 Version

Version of the OpenC2 protocol (Sec. 3.4.2.16). Currently a *.* format
is used.
:::

:::::: {#Version.__init__ .classattr}
::: {.attr .function}
[Version]{.name}[([[major]{.n},
]{.param}[[minor]{.n}]{.param})]{.signature .pdoc-code .condensed} View
Source
:::

[](#Version.__init__){.headerlink}

::: {.pdoc-code .codehilite}
    157    def __init__(self, major, minor):
    158     """ Initialize `Version` instance
    159
    160            Initialize with major and minor numbers.
    161            :param major: Major number of OpenC2 version.
    162            :param minor: Minor number of OpenC2 version.
    163            :return: `Version` instance.
    164        """
    165     self.major = major
    166     self.minor = minor
:::

::: docstring
Initialize [`Version`](#Version) instance

Initialize with major and minor numbers.

###### Parameters {#parameters}

-   **major**: Major number of OpenC2 version.
-   **minor**: Minor number of OpenC2 version.

###### Returns

> [`Version`](#Version) instance.
:::
::::::

:::: {#Version.major .classattr}
::: {.attr .variable}
[major]{.name}
:::

[](#Version.major){.headerlink}
::::

:::: {#Version.minor .classattr}
::: {.attr .variable}
[minor]{.name}
:::

[](#Version.minor){.headerlink}
::::

::::::: {#Version.fromstr .classattr}
:::: {.attr .function}
::: decorator
\@staticmethod
:::

[def]{.def}
[fromstr]{.name}[([[v]{.n}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
::::

[](#Version.fromstr){.headerlink}

::: {.pdoc-code .codehilite}
    168  @staticmethod
    169   def fromstr(v):
    170       """ Create `Version` instance
    171
    172          Create `Version` instance from string (in the *<major>.<minor>* notation.
    173          :param v: Text string with the Version.
    174          :return: `Version` instance.
    175      """
    176       vers = v.split('.',2)
    177       return Version(vers[0], vers[1])
:::

::: docstring
Create [`Version`](#Version) instance

Create [`Version`](#Version) instance from string (in the *.* notation.

###### Parameters {#parameters}

-   **v**: Text string with the Version.

###### Returns {#returns}

> [`Version`](#Version) instance.
:::
:::::::

::::::: {#Version.fromdict .classattr}
:::: {.attr .function}
::: decorator
\@classmethod
:::

[def]{.def} [fromdict]{.name}[([[cls]{.bp}, ]{.param}[[vers]{.n},
]{.param}[[e]{.n}[=]{.o}[None]{.kc}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
::::

[](#Version.fromdict){.headerlink}

::: {.pdoc-code .codehilite}
    179    @classmethod
    180 def fromdict(cls, vers, e=None):
    181     """ Create `Version` instance
    182
    183            Create `Version` instance from string (in the *<major>.<minor>* notation.
    184            This method is provided to deserialize an OpenC2 message according to the openc2lib approach.
    185            This method should only be used internally the openc2lib.
    186            :param vers: Text string with the Version.
    187            :param e: `Encoder` instance to be used (only included to be compliance with the function footprint.
    188            :return: `Version` instance.
    189        """
    190     return Version.fromstr(vers)
:::

::: docstring
Create [`Version`](#Version) instance

Create [`Version`](#Version) instance from string (in the *.* notation.
This method is provided to deserialize an OpenC2 message according to
the openc2lib approach. This method should only be used internally the
openc2lib.

###### Parameters {#parameters}

-   **vers**: Text string with the Version.
-   **e**: `Encoder` instance to be used (only included to be compliance
    with the function footprint.

###### Returns {#returns}

> [`Version`](#Version) instance.
:::
:::::::

::: inherited
##### Inherited Members

builtins.str
:   encode
:   replace
:   split
:   rsplit
:   join
:   capitalize
:   casefold
:   title
:   center
:   count
:   expandtabs
:   find
:   partition
:   index
:   ljust
:   lower
:   lstrip
:   rfind
:   rindex
:   rjust
:   rstrip
:   rpartition
:   splitlines
:   strip
:   swapcase
:   translate
:   upper
:   startswith
:   endswith
:   removeprefix
:   removesuffix
:   isascii
:   islower
:   isupper
:   istitle
:   isspace
:   isdecimal
:   isdigit
:   isnumeric
:   isalpha
:   isalnum
:   isidentifier
:   isprintable
:   zfill
:   format
:   format_map
:   maketrans
:::
:::::::::::::::::::::::::

::::::::::::::: {#Feature .section}
::: {.attr .class}
[class]{.def}
[Feature]{.name}([[openc2lib.types.basetypes.Enumerated](basetypes.html#Enumerated)]{.base}):
View Source
:::

[](#Feature){.headerlink}

::: {.pdoc-code .codehilite}
    192class Feature(Enumerated):
    193   """ OpenC2 Feature
    194
    195      An enumeration for the fields that can be included in the `Results` (see Sec. 3.4.2.4).
    196  """
    197   versions   = 1
    198   profiles   = 2
    199   pairs      = 3
    200   rate_limit = 4
:::

::: docstring
OpenC2 Feature

An enumeration for the fields that can be included in the `Results` (see
Sec. 3.4.2.4).
:::

:::: {#Feature.versions .classattr}
::: {.attr .variable}
[versions]{.name} = [\<[Feature.versions](#Feature.versions):
1\>]{.default_value}
:::

[](#Feature.versions){.headerlink}
::::

:::: {#Feature.profiles .classattr}
::: {.attr .variable}
[profiles]{.name} = [\<[Feature.profiles](#Feature.profiles):
2\>]{.default_value}
:::

[](#Feature.profiles){.headerlink}
::::

:::: {#Feature.pairs .classattr}
::: {.attr .variable}
[pairs]{.name} = [\<[Feature.pairs](#Feature.pairs):
3\>]{.default_value}
:::

[](#Feature.pairs){.headerlink}
::::

:::: {#Feature.rate_limit .classattr}
::: {.attr .variable}
[rate_limit]{.name} = [\<[Feature.rate_limit](#Feature.rate_limit):
4\>]{.default_value}
:::

[](#Feature.rate_limit){.headerlink}
::::

::: inherited
##### Inherited Members

[openc2lib.types.basetypes.Enumerated](basetypes.html#Enumerated)
:   [todict](basetypes.html#Enumerated.todict)
:   [fromdict](basetypes.html#Enumerated.fromdict)

aenum.\_enum.Enum
:   name
:   value
:   values
:::
:::::::::::::::

:::::::::::::::: {#Nsid .section}
::: {.attr .class}
[class]{.def} [Nsid]{.name}([builtins.str]{.base}): View Source
:::

[](#Nsid){.headerlink}

::: {.pdoc-code .codehilite}
    204class Nsid(str):
    205 """ OpenC2 Namespace Identifier
    206
    207        Namespace identifiers are described in Sec. 3.1.4. This class implements the required
    208            controls on the string length.
    209    """
    210 def __init__(self, nsid):
    211     """ Initialize `Nsid`
    212
    213            :param nsid: Text string (must be more than 1 and less than 16 characters.
    214        """
    215     if len(nsid) > 16 or len(nsid) < 1:
    216         raise ValueError("Nsid must be between 1 and 16 characters")
    217     self = nsid
    218
    219 @classmethod
    220 def fromdict(cls, name, e):
    221     """ Create `Nsid` instance
    222
    223            Create `Nsid` instance from string.
    224            This method is provided to deserialize an OpenC2 message according to the openc2lib approach.
    225            This method should only be used internally the openc2lib.
    226            :param name: Text string with the namespace identifier..
    227            :param e: `Encoder` instance to be used (only included to be compliance with the function footprint.
    228            :return: `Version` instance.
    229        """
    230     return Nsid(name)
:::

::: docstring
OpenC2 Namespace Identifier

Namespace identifiers are described in Sec. 3.1.4. This class implements
the required controls on the string length.
:::

:::::: {#Nsid.__init__ .classattr}
::: {.attr .function}
[Nsid]{.name}[([[nsid]{.n}]{.param})]{.signature .pdoc-code .condensed}
View Source
:::

[](#Nsid.__init__){.headerlink}

::: {.pdoc-code .codehilite}
    210  def __init__(self, nsid):
    211       """ Initialize `Nsid`
    212
    213          :param nsid: Text string (must be more than 1 and less than 16 characters.
    214      """
    215       if len(nsid) > 16 or len(nsid) < 1:
    216           raise ValueError("Nsid must be between 1 and 16 characters")
    217       self = nsid
:::

::: docstring
Initialize [`Nsid`](#Nsid)

###### Parameters {#parameters}

-   **nsid**: Text string (must be more than 1 and less than 16
    characters.
:::
::::::

::::::: {#Nsid.fromdict .classattr}
:::: {.attr .function}
::: decorator
\@classmethod
:::

[def]{.def} [fromdict]{.name}[([[cls]{.bp}, ]{.param}[[name]{.n},
]{.param}[[e]{.n}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
::::

[](#Nsid.fromdict){.headerlink}

::: {.pdoc-code .codehilite}
    219  @classmethod
    220   def fromdict(cls, name, e):
    221       """ Create `Nsid` instance
    222
    223          Create `Nsid` instance from string.
    224          This method is provided to deserialize an OpenC2 message according to the openc2lib approach.
    225          This method should only be used internally the openc2lib.
    226          :param name: Text string with the namespace identifier..
    227          :param e: `Encoder` instance to be used (only included to be compliance with the function footprint.
    228          :return: `Version` instance.
    229      """
    230       return Nsid(name)
:::

::: docstring
Create [`Nsid`](#Nsid) instance

Create [`Nsid`](#Nsid) instance from string. This method is provided to
deserialize an OpenC2 message according to the openc2lib approach. This
method should only be used internally the openc2lib.

###### Parameters {#parameters}

-   **name**: Text string with the namespace identifier..
-   **e**: `Encoder` instance to be used (only included to be compliance
    with the function footprint.

###### Returns {#returns}

> [`Version`](#Version) instance.
:::
:::::::

::: inherited
##### Inherited Members

builtins.str
:   encode
:   replace
:   split
:   rsplit
:   join
:   capitalize
:   casefold
:   title
:   center
:   count
:   expandtabs
:   find
:   partition
:   index
:   ljust
:   lower
:   lstrip
:   rfind
:   rindex
:   rjust
:   rstrip
:   rpartition
:   splitlines
:   strip
:   swapcase
:   translate
:   upper
:   startswith
:   endswith
:   removeprefix
:   removesuffix
:   isascii
:   islower
:   isupper
:   istitle
:   isspace
:   isdecimal
:   isdigit
:   isnumeric
:   isalpha
:   isalnum
:   isidentifier
:   isprintable
:   zfill
:   format
:   format_map
:   maketrans
:::
::::::::::::::::

::::::::::::::: {#ResponseType .section}
::: {.attr .class}
[class]{.def}
[ResponseType]{.name}([[openc2lib.types.basetypes.Enumerated](basetypes.html#Enumerated)]{.base}):
View Source
:::

[](#ResponseType){.headerlink}

::: {.pdoc-code .codehilite}
    232class ResponseType(Enumerated):
    233 """ OpenC2 Response-Type
    234
    235        Enumerates the Response-Types according to Sec. 3.4.2.15.   
    236    """   
    237 none=0
    238 ack=1
    239 status=2
    240 complete=3
:::

::: docstring
OpenC2 Response-Type

Enumerates the Response-Types according to Sec. 3.4.2.15.
:::

:::: {#ResponseType.none .classattr}
::: {.attr .variable}
[none]{.name} = [\<[ResponseType.none](#ResponseType.none):
0\>]{.default_value}
:::

[](#ResponseType.none){.headerlink}
::::

:::: {#ResponseType.ack .classattr}
::: {.attr .variable}
[ack]{.name} = [\<[ResponseType.ack](#ResponseType.ack):
1\>]{.default_value}
:::

[](#ResponseType.ack){.headerlink}
::::

:::: {#ResponseType.status .classattr}
::: {.attr .variable}
[status]{.name} = [\<[ResponseType.status](#ResponseType.status):
2\>]{.default_value}
:::

[](#ResponseType.status){.headerlink}
::::

:::: {#ResponseType.complete .classattr}
::: {.attr .variable}
[complete]{.name} = [\<[ResponseType.complete](#ResponseType.complete):
3\>]{.default_value}
:::

[](#ResponseType.complete){.headerlink}
::::

::: inherited
##### Inherited Members

[openc2lib.types.basetypes.Enumerated](basetypes.html#Enumerated)
:   [todict](basetypes.html#Enumerated.todict)
:   [fromdict](basetypes.html#Enumerated.fromdict)

aenum.\_enum.Enum
:   name
:   value
:   values
:::
:::::::::::::::

::::::::::::::: {#TargetEnum .section}
::: {.attr .class}
[class]{.def}
[TargetEnum]{.name}([[openc2lib.types.basetypes.Enumerated](basetypes.html#Enumerated)]{.base}):
View Source
:::

[](#TargetEnum){.headerlink}

::: {.pdoc-code .codehilite}
    242class TargetEnum(Enumerated):
    243 """ OpenC2 Targets names
    244    
    245        The Language Specification defines a *Targets* subtypes only used in Sec. 3.4.2.1.
    246        The openc2lib uses this class to keep a record of all registered Target names, while
    247        the *Targets* type is never defined (it is build in an unnamed way to create the 
    248        `ActionTargets`.
    249
    250        This class is only expected to be used internally by the openc2lib.
    251    """
    252 def __repr__(self):
    253     return self.name
:::

::: docstring
OpenC2 Targets names

The Language Specification defines a *Targets* subtypes only used in
Sec. 3.4.2.1. The openc2lib uses this class to keep a record of all
registered Target names, while the *Targets* type is never defined (it
is build in an unnamed way to create the
[`ActionTargets`](#ActionTargets).

This class is only expected to be used internally by the openc2lib.
:::

:::: {#TargetEnum.features .classattr}
::: {.attr .variable}
[features]{.name}
:::

[](#TargetEnum.features){.headerlink}
::::

:::: {#TargetEnum.ipv4_net .classattr}
::: {.attr .variable}
[ipv4_net]{.name}
:::

[](#TargetEnum.ipv4_net){.headerlink}
::::

:::: {#TargetEnum.ipv4_connection .classattr}
::: {.attr .variable}
[ipv4_connection]{.name}
:::

[](#TargetEnum.ipv4_connection){.headerlink}
::::

:::: {#TargetEnum.slpf:rule_number .classattr}
::: {.attr .variable}
[slpf:rule_number]{.name}
:::

[](#TargetEnum.slpf:rule_number){.headerlink}
::::

::: inherited
##### Inherited Members

[openc2lib.types.basetypes.Enumerated](basetypes.html#Enumerated)
:   [todict](basetypes.html#Enumerated.todict)
:   [fromdict](basetypes.html#Enumerated.fromdict)

aenum.\_enum.Enum
:   name
:   value
:   values
:::
:::::::::::::::

::::::: {#ActionTargets .section}
::: {.attr .class}
[class]{.def}
[ActionTargets]{.name}([[openc2lib.types.basetypes.MapOf.\_\_new\_\_..MapOf](basetypes.html#MapOf.__new__.%3Clocals%3E.MapOf)]{.base}):
View Source
:::

[](#ActionTargets){.headerlink}

::: {.pdoc-code .codehilite}
    255class ActionTargets(MapOf(Actions, ArrayOf(TargetEnum))):
    256   """ OpenC2 Action-Targets
    257
    258      Map of each action supported by an actuator to the list of targets applicable to 
    259      that action (Sec. 3.4.2.1).
    260      They must be defined by each Profile.
    261  """
    262   pass
:::

::: docstring
OpenC2 Action-Targets

Map of each action supported by an actuator to the list of targets
applicable to that action (Sec. 3.4.2.1). They must be defined by each
Profile.
:::

::: inherited
##### Inherited Members

[openc2lib.types.basetypes.MapOf.\_\_new\_\_..MapOf](basetypes.html#MapOf.__new__.%3Clocals%3E.MapOf)
:   [fieldtypes](basetypes.html#MapOf.__new__.%3Clocals%3E.MapOf.fieldtypes)
:   [fromdict](basetypes.html#MapOf.__new__.%3Clocals%3E.MapOf.fromdict)

[openc2lib.types.basetypes.Map](basetypes.html#Map)
:   [extend](basetypes.html#Map.extend)
:   [regext](basetypes.html#Map.regext)
:   [todict](basetypes.html#Map.todict)

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
:::::::

::::::: {#ActionArguments .section}
::: {.attr .class}
[class]{.def}
[ActionArguments]{.name}([[openc2lib.types.basetypes.MapOf.\_\_new\_\_..MapOf](basetypes.html#MapOf.__new__.%3Clocals%3E.MapOf)]{.base}):
View Source
:::

[](#ActionArguments){.headerlink}

::: {.pdoc-code .codehilite}
    264class ActionArguments(MapOf(Actions, ArrayOf(str))):
    265   """ OpenC2 Action-Arguments mapping
    266
    267      Map of each action supported by an actuator to the list of arguments applicable to
    268      that action. 
    269      This is not defined in the Language Specification, but used e.g., by the SLPF Profile.
    270  """
    271   pass
:::

::: docstring
OpenC2 Action-Arguments mapping

Map of each action supported by an actuator to the list of arguments
applicable to that action. This is not defined in the Language
Specification, but used e.g., by the SLPF Profile.
:::

::: inherited
##### Inherited Members

[openc2lib.types.basetypes.MapOf.\_\_new\_\_..MapOf](basetypes.html#MapOf.__new__.%3Clocals%3E.MapOf)
:   [fieldtypes](basetypes.html#MapOf.__new__.%3Clocals%3E.MapOf.fieldtypes)
:   [fromdict](basetypes.html#MapOf.__new__.%3Clocals%3E.MapOf.fromdict)

[openc2lib.types.basetypes.Map](basetypes.html#Map)
:   [extend](basetypes.html#Map.extend)
:   [regext](basetypes.html#Map.regext)
:   [todict](basetypes.html#Map.todict)

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
:::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
