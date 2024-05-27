![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAzMCAzMCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLW1pdGVybGltaXQ9IjEwIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik00IDdoMjJNNCAxNWgyMk00IDIzaDIyIiAvPjwvc3ZnPg==)

<div>

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0iYmkgYmktYm94LWFycm93LWluLWxlZnQiIHZpZXdib3g9IjAgMCAxNiAxNiI+CiAgPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMTAgMy41YS41LjUgMCAwIDAtLjUtLjVoLThhLjUuNSAwIDAgMC0uNS41djlhLjUuNSAwIDAgMCAuNS41aDhhLjUuNSAwIDAgMCAuNS0uNXYtMmEuNS41IDAgMCAxIDEgMHYyQTEuNSAxLjUgMCAwIDEgOS41IDE0aC04QTEuNSAxLjUgMCAwIDEgMCAxMi41di05QTEuNSAxLjUgMCAwIDEgMS41IDJoOEExLjUgMS41IDAgMCAxIDExIDMuNXYyYS41LjUgMCAwIDEtMSAwdi0yeiIgLz4KICA8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00LjE0NiA4LjM1NGEuNS41IDAgMCAxIDAtLjcwOGwzLTNhLjUuNSAwIDEgMSAuNzA4LjcwOEw1LjcwNyA3LjVIMTQuNWEuNS41IDAgMCAxIDAgMUg1LjcwN2wyLjE0NyAyLjE0NmEuNS41IDAgMCAxLS43MDguNzA4bC0zLTN6IiAvPgo8L3N2Zz4=){.bi
.bi-box-arrow-in-left}  openc2lib.types](../types.html){.pdoc-button
.module-list-button}

## API Documentation

-   [IPv4Net](#IPv4Net){.class}
    -   [IPv4Net](#IPv4Net.__init__){.function}
    -   [ipv4_net](#IPv4Net.ipv4_net){.variable}
    -   [addr](#IPv4Net.addr){.function}
    -   [prefix](#IPv4Net.prefix){.function}
-   [IPv4Connection](#IPv4Connection){.class}
    -   [IPv4Connection](#IPv4Connection.__init__){.function}
    -   [src_addr](#IPv4Connection.src_addr){.variable}
    -   [src_port](#IPv4Connection.src_port){.variable}
    -   [dst_addr](#IPv4Connection.dst_addr){.variable}
    -   [dst_port](#IPv4Connection.dst_port){.variable}
    -   [protocol](#IPv4Connection.protocol){.variable}
-   [Features](#Features){.class}

[built with [pdoc]{.visually-hidden}![pdoc
logo](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20role%3D%22img%22%20aria-label%3D%22pdoc%20logo%22%20width%3D%22300%22%20height%3D%22150%22%20viewBox%3D%22-1%200%2060%2030%22%3E%3Ctitle%3Epdoc%3C/title%3E%3Cpath%20d%3D%22M29.621%2021.293c-.011-.273-.214-.475-.511-.481a.5.5%200%200%200-.489.503l-.044%201.393c-.097.551-.695%201.215-1.566%201.704-.577.428-1.306.486-2.193.182-1.426-.617-2.467-1.654-3.304-2.487l-.173-.172a3.43%203.43%200%200%200-.365-.306.49.49%200%200%200-.286-.196c-1.718-1.06-4.931-1.47-7.353.191l-.219.15c-1.707%201.187-3.413%202.131-4.328%201.03-.02-.027-.49-.685-.141-1.763.233-.721.546-2.408.772-4.076.042-.09.067-.187.046-.288.166-1.347.277-2.625.241-3.351%201.378-1.008%202.271-2.586%202.271-4.362%200-.976-.272-1.935-.788-2.774-.057-.094-.122-.18-.184-.268.033-.167.052-.339.052-.516%200-1.477-1.202-2.679-2.679-2.679-.791%200-1.496.352-1.987.9a6.3%206.3%200%200%200-1.001.029c-.492-.564-1.207-.929-2.012-.929-1.477%200-2.679%201.202-2.679%202.679A2.65%202.65%200%200%200%20.97%206.554c-.383.747-.595%201.572-.595%202.41%200%202.311%201.507%204.29%203.635%205.107-.037.699-.147%202.27-.423%203.294l-.137.461c-.622%202.042-2.515%208.257%201.727%2010.643%201.614.908%203.06%201.248%204.317%201.248%202.665%200%204.492-1.524%205.322-2.401%201.476-1.559%202.886-1.854%206.491.82%201.877%201.393%203.514%201.753%204.861%201.068%202.223-1.713%202.811-3.867%203.399-6.374.077-.846.056-1.469.054-1.537zm-4.835%204.313c-.054.305-.156.586-.242.629-.034-.007-.131-.022-.307-.157-.145-.111-.314-.478-.456-.908.221.121.432.25.675.355.115.039.219.051.33.081zm-2.251-1.238c-.05.33-.158.648-.252.694-.022.001-.125-.018-.307-.157-.217-.166-.488-.906-.639-1.573.358.344.754.693%201.198%201.036zm-3.887-2.337c-.006-.116-.018-.231-.041-.342.635.145%201.189.368%201.599.625.097.231.166.481.174.642-.03.049-.055.101-.067.158-.046.013-.128.026-.298.004-.278-.037-.901-.57-1.367-1.087zm-1.127-.497c.116.306.176.625.12.71-.019.014-.117.045-.345.016-.206-.027-.604-.332-.986-.695.41-.051.816-.056%201.211-.031zm-4.535%201.535c.209.22.379.47.358.598-.006.041-.088.138-.351.234-.144.055-.539-.063-.979-.259a11.66%2011.66%200%200%200%20.972-.573zm.983-.664c.359-.237.738-.418%201.126-.554.25.237.479.548.457.694-.006.042-.087.138-.351.235-.174.064-.694-.105-1.232-.375zm-3.381%201.794c-.022.145-.061.29-.149.401-.133.166-.358.248-.69.251h-.002c-.133%200-.306-.26-.45-.621.417.091.854.07%201.291-.031zm-2.066-8.077a4.78%204.78%200%200%201-.775-.584c.172-.115.505-.254.88-.378l-.105.962zm-.331%202.302a10.32%2010.32%200%200%201-.828-.502c.202-.143.576-.328.984-.49l-.156.992zm-.45%202.157l-.701-.403c.214-.115.536-.249.891-.376a11.57%2011.57%200%200%201-.19.779zm-.181%201.716c.064.398.194.702.298.893-.194-.051-.435-.162-.736-.398.061-.119.224-.3.438-.495zM8.87%204.141c0%20.152-.123.276-.276.276s-.275-.124-.275-.276.123-.276.276-.276.275.124.275.276zm-.735-.389a1.15%201.15%200%200%200-.314.783%201.16%201.16%200%200%200%201.162%201.162c.457%200%20.842-.27%201.032-.653.026.117.042.238.042.362a1.68%201.68%200%200%201-1.679%201.679%201.68%201.68%200%200%201-1.679-1.679c0-.843.626-1.535%201.436-1.654zM5.059%205.406A1.68%201.68%200%200%201%203.38%207.085a1.68%201.68%200%200%201-1.679-1.679c0-.037.009-.072.011-.109.21.3.541.508.935.508a1.16%201.16%200%200%200%201.162-1.162%201.14%201.14%200%200%200-.474-.912c.015%200%20.03-.005.045-.005.926.001%201.679.754%201.679%201.68zM3.198%204.141c0%20.152-.123.276-.276.276s-.275-.124-.275-.276.123-.276.276-.276.275.124.275.276zM1.375%208.964c0-.52.103-1.035.288-1.52.466.394%201.06.64%201.717.64%201.144%200%202.116-.725%202.499-1.738.383%201.012%201.355%201.738%202.499%201.738.867%200%201.631-.421%202.121-1.062.307.605.478%201.267.478%201.942%200%202.486-2.153%204.51-4.801%204.51s-4.801-2.023-4.801-4.51zm24.342%2019.349c-.985.498-2.267.168-3.813-.979-3.073-2.281-5.453-3.199-7.813-.705-1.315%201.391-4.163%203.365-8.423.97-3.174-1.786-2.239-6.266-1.261-9.479l.146-.492c.276-1.02.395-2.457.444-3.268a6.11%206.11%200%200%200%201.18.115%206.01%206.01%200%200%200%202.536-.562l-.006.175c-.802.215-1.848.612-2.021%201.25-.079.295.021.601.274.837.219.203.415.364.598.501-.667.304-1.243.698-1.311%201.179-.02.144-.022.507.393.787.213.144.395.26.564.365-1.285.521-1.361.96-1.381%201.126-.018.142-.011.496.427.746l.854.489c-.473.389-.971.914-.999%201.429-.018.278.095.532.316.713.675.556%201.231.721%201.653.721.059%200%20.104-.014.158-.02.207.707.641%201.64%201.513%201.64h.013c.8-.008%201.236-.345%201.462-.626.173-.216.268-.457.325-.692.424.195.93.374%201.372.374.151%200%20.294-.021.423-.068.732-.27.944-.704.993-1.021.009-.061.003-.119.002-.179.266.086.538.147.789.147.15%200%20.294-.021.423-.069.542-.2.797-.489.914-.754.237.147.478.258.704.288.106.014.205.021.296.021.356%200%20.595-.101.767-.229.438.435%201.094.992%201.656%201.067.106.014.205.021.296.021a1.56%201.56%200%200%200%20.323-.035c.17.575.453%201.289.866%201.605.358.273.665.362.914.362a.99.99%200%200%200%20.421-.093%201.03%201.03%200%200%200%20.245-.164c.168.428.39.846.68%201.068.358.273.665.362.913.362a.99.99%200%200%200%20.421-.093c.317-.148.512-.448.639-.762.251.157.495.257.726.257.127%200%20.25-.024.37-.071.427-.17.706-.617.841-1.314.022-.015.047-.022.068-.038.067-.051.133-.104.196-.159-.443%201.486-1.107%202.761-2.086%203.257zM8.66%209.925a.5.5%200%201%200-1%200c0%20.653-.818%201.205-1.787%201.205s-1.787-.552-1.787-1.205a.5.5%200%201%200-1%200c0%201.216%201.25%202.205%202.787%202.205s2.787-.989%202.787-2.205zm4.4%2015.965l-.208.097c-2.661%201.258-4.708%201.436-6.086.527-1.542-1.017-1.88-3.19-1.844-4.198a.4.4%200%200%200-.385-.414c-.242-.029-.406.164-.414.385-.046%201.249.367%203.686%202.202%204.896.708.467%201.547.7%202.51.7%201.248%200%202.706-.392%204.362-1.174l.185-.086a.4.4%200%200%200%20.205-.527c-.089-.204-.326-.291-.527-.206zM9.547%202.292c.093.077.205.114.317.114a.5.5%200%200%200%20.318-.886L8.817.397a.5.5%200%200%200-.703.068.5.5%200%200%200%20.069.703l1.364%201.124zm-7.661-.065c.086%200%20.173-.022.253-.068l1.523-.893a.5.5%200%200%200-.506-.863l-1.523.892a.5.5%200%200%200-.179.685c.094.158.261.247.432.247z%22%20transform%3D%22matrix%28-1%200%200%201%2058%200%29%22%20fill%3D%22%233bb300%22/%3E%3Cpath%20d%3D%22M.3%2021.86V10.18q0-.46.02-.68.04-.22.18-.5.28-.54%201.34-.54%201.06%200%201.42.28.38.26.44.78.76-1.04%202.38-1.04%201.64%200%203.1%201.54%201.46%201.54%201.46%203.58%200%202.04-1.46%203.58-1.44%201.54-3.08%201.54-1.64%200-2.38-.92v4.04q0%20.46-.04.68-.02.22-.18.5-.14.3-.5.42-.36.12-.98.12-.62%200-1-.12-.36-.12-.52-.4-.14-.28-.18-.5-.02-.22-.02-.68zm3.96-9.42q-.46.54-.46%201.18%200%20.64.46%201.18.48.52%201.2.52.74%200%201.24-.52.52-.52.52-1.18%200-.66-.48-1.18-.48-.54-1.26-.54-.76%200-1.22.54zm14.741-8.36q.16-.3.54-.42.38-.12%201-.12.64%200%201.02.12.38.12.52.42.16.3.18.54.04.22.04.68v11.94q0%20.46-.04.7-.02.22-.18.5-.3.54-1.7.54-1.38%200-1.54-.98-.84.96-2.34.96-1.8%200-3.28-1.56-1.48-1.58-1.48-3.66%200-2.1%201.48-3.68%201.5-1.58%203.28-1.58%201.48%200%202.3%201v-4.2q0-.46.02-.68.04-.24.18-.52zm-3.24%2010.86q.52.54%201.26.54.74%200%201.22-.54.5-.54.5-1.18%200-.66-.48-1.22-.46-.56-1.26-.56-.8%200-1.28.56-.48.54-.48%201.2%200%20.66.52%201.2zm7.833-1.2q0-2.4%201.68-3.96%201.68-1.56%203.84-1.56%202.16%200%203.82%201.56%201.66%201.54%201.66%203.94%200%201.66-.86%202.96-.86%201.28-2.1%201.9-1.22.6-2.54.6-1.32%200-2.56-.64-1.24-.66-2.1-1.92-.84-1.28-.84-2.88zm4.18%201.44q.64.48%201.3.48.66%200%201.32-.5.66-.5.66-1.48%200-.98-.62-1.46-.62-.48-1.34-.48-.72%200-1.34.5-.62.5-.62%201.48%200%20.96.64%201.46zm11.412-1.44q0%20.84.56%201.32.56.46%201.18.46.64%200%201.18-.36.56-.38.9-.38.6%200%201.46%201.06.46.58.46%201.04%200%20.76-1.1%201.42-1.14.8-2.8.8-1.86%200-3.58-1.34-.82-.64-1.34-1.7-.52-1.08-.52-2.36%200-1.3.52-2.34.52-1.06%201.34-1.7%201.66-1.32%203.54-1.32.76%200%201.48.22.72.2%201.06.4l.32.2q.36.24.56.38.52.4.52.92%200%20.5-.42%201.14-.72%201.1-1.38%201.1-.38%200-1.08-.44-.36-.34-1.04-.34-.66%200-1.24.48-.58.48-.58%201.34z%22%20fill%3D%22green%22/%3E%3C/svg%3E)](https://pdoc.dev "pdoc: Python API documentation generator"){.attribution
target="_blank"}

</div>

:::::::::::::::::::::::::::::::::::::::::::::::::::: {.pdoc role="main"}
::::: {.section .module-info}
# [openc2lib](./../../openc2lib.html).[types](./../types.html).targettypes {#openc2lib.types.targettypes .modulename}

::: docstring
OpenC2 target types

Definition of the target types in the OpenC2 (Sec. 3.4.1). The naming
strictly follows the definition of the Language Specification as close
as possible. The relevant exception is represented by hyphens that are
always dropped.
:::

View Source

::: {.pdoc-code .codehilite}
      1""" OpenC2 target types
      2
      3  Definition of the target types in the OpenC2 (Sec. 3.4.1).
      4  The naming strictly follows the definition of the Language Specification
      5  as close as possible. The relevant exception is represented by hyphens
      6  that are always dropped.
      7"""
      8
      9import dataclasses
     10import ipaddress
     11
     12import openc2lib.types.basetypes
     13import openc2lib.types.datatypes
     14
     15from openc2lib.core.target import Targets
     16
     17
     18class IPv4Net:
     19 """OpenC2 IPv4 Address Range
     20        
     21        IPv4 Address Range as defined in Sec. 3.4.1.9.
     22
     23        The Standard is not clear on this part. The 
     24        IPv4Net Target is defined as "Array /ipv4-net"
     25        (where ipv4-net --lowercase!-- is never defined!)
     26        However, the json serialization requirements explicitely
     27        define:
     28        Array /ipv4-net: JSON string containing the text representation 
     29                                of an IPv4 address range as specified in 
     30                                [RFC4632], Section 3.1.
     31        According to this definition, I assume a single network address
     32        should be managed. Extension to an array of IP network addresses
     33        is rather straightforward by using a list for ipv4_net attribute.
     34        Note that I have to keep both the string representation of the
     35        network address as well as the IPv4Network object to easily 
     36        manage the code and to automate the creation of the dictionary.
     37        
     38    """
     39#ipv4_net: str
     40 
     41 def __init__(self, ipv4_net=None, prefix=None):
     42     """ Initialize IPv4 Address Range
     43
     44            Initialize `IPv4Net with IPv4 address and prefix.
     45            If no IPv4 address is given, initialize to null address.
     46            If no prefix is given, assume /32 (iPv4 address only).
     47            :param ipv4_net: IPv4 Network Address.
     48            :param prefix: IPv4 Network Adress Prefix.
     49        """
     50     if ipv4_net is None:
     51         net = ipaddress.IPv4Network("0.0.0.0/0")
     52     elif prefix is None:
     53         net = ipaddress.IPv4Network(ipv4_net)
     54     else:
     55         tmp = ipv4_net + "/" + str(prefix)
     56         net = ipaddress.IPv4Network(tmp)
     57
     58     self.ipv4_net = net.exploded
     59 
     60 def addr(self):
     61     """ Returns address part only (no prefix) """
     62     return ipaddress.IPv4Network(self.ipv4_net).network_address.exploded
     63 
     64 def prefix(self):
     65     """ Returns prefix only """
     66     return ipaddress.IPv4Network(self.ipv4_net).prefixlen
     67 
     68 def __str__(self):
     69     return ipaddress.IPv4Network(self.ipv4_net).exploded
     70 
     71 def __repr__(self):
     72     return ipaddress.IPv4Network(self.ipv4_net).exploded
     73
     74
     75@dataclasses.dataclass
     76class IPv4Connection(openc2lib.types.basetypes.Record):
     77 """OpenC2 IPv4 Connection
     78        
     79        IPv4 Connection including IPv4 addressed, protocol, and port numbers, as defined in Sec. 3.4.1.10.
     80    """
     81 src_addr: IPv4Net = None
     82 """ Source address """
     83 src_port: int = None
     84 """ Source port """
     85 dst_addr: IPv4Net = None
     86 """ Destination address """
     87 dst_port: int = None
     88 """ Destination port """
     89 protocol: openc2lib.types.datatypes.L4Protocol = None
     90 """ L4 protocol """
     91
     92 def __repr__(self):
     93     return (f"IPv4Connection(src='{self.src_addr}', sport={self.src_port}, "
     94              f"dst='{self.dst_addr}', dport={self.dst_port}, protocol='{self.protocol}')")
     95 
     96 def __str__(self):
     97     return f"IPv4Connection(" \
     98             f"src={self.src_addr}, " \
     99             f"dst={self.dst_addr}, " \
    100               f"protocol={self.protocol}, " \
    101               f"src_port={self.src_port}, " \
    102               f"st_port={self.dst_port})"
    103
    104class Features(openc2lib.types.basetypes.ArrayOf(openc2lib.types.datatypes.Feature)):
    105   """ OpenC2 Features
    106
    107      Implements the Features target (Section 3.4.1.5).
    108      Just defines an `ArrayOf` `Feature`.
    109  """
    110# TODO: implmement control on the max number of elements
    111   pass
    112
    113
    114
    115# Register the list of available Targets
    116Targets.add('features', Features, 9)
    117Targets.add('ipv4_net', IPv4Net, 13)
    118Targets.add('ipv4_connection', IPv4Connection, 15)
:::
:::::

:::::::::::::::::::: {#IPv4Net .section}
::: {.attr .class}
[class]{.def} [IPv4Net]{.name}: View Source
:::

[](#IPv4Net){.headerlink}

::: {.pdoc-code .codehilite}
    19class IPv4Net:
    20  """OpenC2 IPv4 Address Range
    21     
    22     IPv4 Address Range as defined in Sec. 3.4.1.9.
    23
    24     The Standard is not clear on this part. The 
    25     IPv4Net Target is defined as "Array /ipv4-net"
    26     (where ipv4-net --lowercase!-- is never defined!)
    27     However, the json serialization requirements explicitely
    28     define:
    29     Array /ipv4-net: JSON string containing the text representation 
    30                             of an IPv4 address range as specified in 
    31                             [RFC4632], Section 3.1.
    32     According to this definition, I assume a single network address
    33     should be managed. Extension to an array of IP network addresses
    34     is rather straightforward by using a list for ipv4_net attribute.
    35     Note that I have to keep both the string representation of the
    36     network address as well as the IPv4Network object to easily 
    37     manage the code and to automate the creation of the dictionary.
    38     
    39 """
    40#ipv4_net: str
    41  
    42  def __init__(self, ipv4_net=None, prefix=None):
    43      """ Initialize IPv4 Address Range
    44
    45         Initialize `IPv4Net with IPv4 address and prefix.
    46         If no IPv4 address is given, initialize to null address.
    47         If no prefix is given, assume /32 (iPv4 address only).
    48         :param ipv4_net: IPv4 Network Address.
    49         :param prefix: IPv4 Network Adress Prefix.
    50     """
    51      if ipv4_net is None:
    52          net = ipaddress.IPv4Network("0.0.0.0/0")
    53      elif prefix is None:
    54          net = ipaddress.IPv4Network(ipv4_net)
    55      else:
    56          tmp = ipv4_net + "/" + str(prefix)
    57          net = ipaddress.IPv4Network(tmp)
    58
    59      self.ipv4_net = net.exploded
    60  
    61  def addr(self):
    62      """ Returns address part only (no prefix) """
    63      return ipaddress.IPv4Network(self.ipv4_net).network_address.exploded
    64  
    65  def prefix(self):
    66      """ Returns prefix only """
    67      return ipaddress.IPv4Network(self.ipv4_net).prefixlen
    68  
    69  def __str__(self):
    70      return ipaddress.IPv4Network(self.ipv4_net).exploded
    71  
    72  def __repr__(self):
    73      return ipaddress.IPv4Network(self.ipv4_net).exploded
:::

::: docstring
OpenC2 IPv4 Address Range

IPv4 Address Range as defined in Sec. 3.4.1.9.

The Standard is not clear on this part. The IPv4Net Target is defined as
\"Array /ipv4-net\" (where ipv4-net \--lowercase!\-- is never defined!)
However, the json serialization requirements explicitely define: Array
/ipv4-net: JSON string containing the text representation of an IPv4
address range as specified in \[RFC4632\], Section 3.1. According to
this definition, I assume a single network address should be managed.
Extension to an array of IP network addresses is rather straightforward
by using a list for ipv4_net attribute. Note that I have to keep both
the string representation of the network address as well as the
IPv4Network object to easily manage the code and to automate the
creation of the dictionary.
:::

:::::: {#IPv4Net.__init__ .classattr}
::: {.attr .function}
[IPv4Net]{.name}[([[ipv4_net]{.n}[=]{.o}[None]{.kc},
]{.param}[[prefix]{.n}[=]{.o}[None]{.kc}]{.param})]{.signature
.pdoc-code .condensed} View Source
:::

[](#IPv4Net.__init__){.headerlink}

::: {.pdoc-code .codehilite}
    42   def __init__(self, ipv4_net=None, prefix=None):
    43        """ Initialize IPv4 Address Range
    44
    45           Initialize `IPv4Net with IPv4 address and prefix.
    46           If no IPv4 address is given, initialize to null address.
    47           If no prefix is given, assume /32 (iPv4 address only).
    48           :param ipv4_net: IPv4 Network Address.
    49           :param prefix: IPv4 Network Adress Prefix.
    50       """
    51        if ipv4_net is None:
    52            net = ipaddress.IPv4Network("0.0.0.0/0")
    53        elif prefix is None:
    54            net = ipaddress.IPv4Network(ipv4_net)
    55        else:
    56            tmp = ipv4_net + "/" + str(prefix)
    57            net = ipaddress.IPv4Network(tmp)
    58
    59        self.ipv4_net = net.exploded
:::

::: docstring
Initialize IPv4 Address Range

Initialize \`IPv4Net with IPv4 address and prefix. If no IPv4 address is
given, initialize to null address. If no prefix is given, assume /32
(iPv4 address only).

###### Parameters

-   **ipv4_net**: IPv4 Network Address.
-   **prefix**: IPv4 Network Adress Prefix.
:::
::::::

:::: {#IPv4Net.ipv4_net .classattr}
::: {.attr .variable}
[ipv4_net]{.name}
:::

[](#IPv4Net.ipv4_net){.headerlink}
::::

:::::: {#IPv4Net.addr .classattr}
::: {.attr .function}
[def]{.def}
[addr]{.name}[([[self]{.bp}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
:::

[](#IPv4Net.addr){.headerlink}

::: {.pdoc-code .codehilite}
    61   def addr(self):
    62        """ Returns address part only (no prefix) """
    63        return ipaddress.IPv4Network(self.ipv4_net).network_address.exploded
:::

::: docstring
Returns address part only (no prefix)
:::
::::::

:::::: {#IPv4Net.prefix .classattr}
::: {.attr .function}
[def]{.def}
[prefix]{.name}[([[self]{.bp}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
:::

[](#IPv4Net.prefix){.headerlink}

::: {.pdoc-code .codehilite}
    65   def prefix(self):
    66        """ Returns prefix only """
    67        return ipaddress.IPv4Network(self.ipv4_net).prefixlen
:::

::: docstring
Returns prefix only
:::
::::::
::::::::::::::::::::

::::::::::::::::::::::::: {#IPv4Connection .section}
:::: {.attr .class}
::: decorator
\@dataclasses.dataclass
:::

[class]{.def}
[IPv4Connection]{.name}([[openc2lib.types.basetypes.Record](basetypes.html#Record)]{.base}):
View Source
::::

[](#IPv4Connection){.headerlink}

::: {.pdoc-code .codehilite}
     76@dataclasses.dataclass
     77class IPv4Connection(openc2lib.types.basetypes.Record):
     78   """OpenC2 IPv4 Connection
     79      
     80      IPv4 Connection including IPv4 addressed, protocol, and port numbers, as defined in Sec. 3.4.1.10.
     81  """
     82   src_addr: IPv4Net = None
     83   """ Source address """
     84   src_port: int = None
     85   """ Source port """
     86   dst_addr: IPv4Net = None
     87   """ Destination address """
     88   dst_port: int = None
     89   """ Destination port """
     90   protocol: openc2lib.types.datatypes.L4Protocol = None
     91   """ L4 protocol """
     92
     93   def __repr__(self):
     94       return (f"IPv4Connection(src='{self.src_addr}', sport={self.src_port}, "
     95                f"dst='{self.dst_addr}', dport={self.dst_port}, protocol='{self.protocol}')")
     96   
     97   def __str__(self):
     98       return f"IPv4Connection(" \
     99               f"src={self.src_addr}, " \
    100             f"dst={self.dst_addr}, " \
    101             f"protocol={self.protocol}, " \
    102             f"src_port={self.src_port}, " \
    103             f"st_port={self.dst_port})"
:::

::: docstring
OpenC2 IPv4 Connection

IPv4 Connection including IPv4 addressed, protocol, and port numbers, as
defined in Sec. 3.4.1.10.
:::

:::: {#IPv4Connection.__init__ .classattr}
::: {.attr .function}
[IPv4Connection]{.name}[([ [src_addr]{.n}[:]{.p}
[[IPv4Net](#IPv4Net)]{.n} [=]{.o} [None]{.kc},]{.param}[
[src_port]{.n}[:]{.p} [int]{.nb} [=]{.o} [None]{.kc},]{.param}[
[dst_addr]{.n}[:]{.p} [[IPv4Net](#IPv4Net)]{.n} [=]{.o}
[None]{.kc},]{.param}[ [dst_port]{.n}[:]{.p} [int]{.nb} [=]{.o}
[None]{.kc},]{.param}[ [protocol]{.n}[:]{.p}
[[openc2lib.types.datatypes.L4Protocol](datatypes.html#L4Protocol)]{.n}
[=]{.o} [None]{.kc}]{.param})]{.signature .pdoc-code .multiline}
:::

[](#IPv4Connection.__init__){.headerlink}
::::

::::: {#IPv4Connection.src_addr .classattr}
::: {.attr .variable}
[src_addr]{.name}[: [IPv4Net](#IPv4Net)]{.annotation} =
[None]{.default_value}
:::

[](#IPv4Connection.src_addr){.headerlink}

::: docstring
Source address
:::
:::::

::::: {#IPv4Connection.src_port .classattr}
::: {.attr .variable}
[src_port]{.name}[: int]{.annotation} = [None]{.default_value}
:::

[](#IPv4Connection.src_port){.headerlink}

::: docstring
Source port
:::
:::::

::::: {#IPv4Connection.dst_addr .classattr}
::: {.attr .variable}
[dst_addr]{.name}[: [IPv4Net](#IPv4Net)]{.annotation} =
[None]{.default_value}
:::

[](#IPv4Connection.dst_addr){.headerlink}

::: docstring
Destination address
:::
:::::

::::: {#IPv4Connection.dst_port .classattr}
::: {.attr .variable}
[dst_port]{.name}[: int]{.annotation} = [None]{.default_value}
:::

[](#IPv4Connection.dst_port){.headerlink}

::: docstring
Destination port
:::
:::::

::::: {#IPv4Connection.protocol .classattr}
::: {.attr .variable}
[protocol]{.name}[:
[openc2lib.types.datatypes.L4Protocol](datatypes.html#L4Protocol)]{.annotation}
= [None]{.default_value}
:::

[](#IPv4Connection.protocol){.headerlink}

::: docstring
L4 protocol
:::
:::::

::: inherited
##### Inherited Members

[openc2lib.types.basetypes.Record](basetypes.html#Record)
:   [todict](basetypes.html#Record.todict)
:   [fromdict](basetypes.html#Record.fromdict)
:::
:::::::::::::::::::::::::

::::::: {#Features .section}
::: {.attr .class}
[class]{.def}
[Features]{.name}([[openc2lib.types.basetypes.ArrayOf.\_\_new\_\_..ArrayOf](basetypes.html#ArrayOf.__new__.%3Clocals%3E.ArrayOf)]{.base}):
View Source
:::

[](#Features){.headerlink}

::: {.pdoc-code .codehilite}
    105class Features(openc2lib.types.basetypes.ArrayOf(openc2lib.types.datatypes.Feature)):
    106 """ OpenC2 Features
    107
    108        Implements the Features target (Section 3.4.1.5).
    109        Just defines an `ArrayOf` `Feature`.
    110    """
    111# TODO: implmement control on the max number of elements
    112 pass
:::

::: docstring
OpenC2 Features

Implements the Features target (Section 3.4.1.5). Just defines an
`ArrayOf` `Feature`.
:::

::: inherited
##### Inherited Members

builtins.list
:   list
:   clear
:   copy
:   append
:   insert
:   extend
:   pop
:   remove
:   index
:   count
:   reverse
:   sort

[openc2lib.types.basetypes.ArrayOf.\_\_new\_\_..ArrayOf](basetypes.html#ArrayOf.__new__.%3Clocals%3E.ArrayOf)
:   [fieldtype](basetypes.html#ArrayOf.__new__.%3Clocals%3E.ArrayOf.fieldtype)
:   [fromdict](basetypes.html#ArrayOf.__new__.%3Clocals%3E.ArrayOf.fromdict)

[openc2lib.types.basetypes.Array](basetypes.html#Array)
:   [fieldtypes](basetypes.html#Array.fieldtypes)
:   [todict](basetypes.html#Array.todict)
:::
:::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::
