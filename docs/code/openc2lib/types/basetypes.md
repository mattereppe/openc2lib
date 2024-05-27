![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAzMCAzMCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLW1pdGVybGltaXQ9IjEwIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik00IDdoMjJNNCAxNWgyMk00IDIzaDIyIiAvPjwvc3ZnPg==)

<div>

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0iYmkgYmktYm94LWFycm93LWluLWxlZnQiIHZpZXdib3g9IjAgMCAxNiAxNiI+CiAgPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMTAgMy41YS41LjUgMCAwIDAtLjUtLjVoLThhLjUuNSAwIDAgMC0uNS41djlhLjUuNSAwIDAgMCAuNS41aDhhLjUuNSAwIDAgMCAuNS0uNXYtMmEuNS41IDAgMCAxIDEgMHYyQTEuNSAxLjUgMCAwIDEgOS41IDE0aC04QTEuNSAxLjUgMCAwIDEgMCAxMi41di05QTEuNSAxLjUgMCAwIDEgMS41IDJoOEExLjUgMS41IDAgMCAxIDExIDMuNXYyYS41LjUgMCAwIDEtMSAwdi0yeiIgLz4KICA8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00LjE0NiA4LjM1NGEuNS41IDAgMCAxIDAtLjcwOGwzLTNhLjUuNSAwIDEgMSAuNzA4LjcwOEw1LjcwNyA3LjVIMTQuNWEuNS41IDAgMCAxIDAgMUg1LjcwN2wyLjE0NyAyLjE0NmEuNS41IDAgMCAxLS43MDguNzA4bC0zLTN6IiAvPgo8L3N2Zz4=){.bi
.bi-box-arrow-in-left}  openc2lib.types](../types.html){.pdoc-button
.module-list-button}

## API Documentation

-   [logger](#logger){.variable}
-   [Openc2Type](#Openc2Type){.class}
-   [Record](#Record){.class}
    -   [todict](#Record.todict){.function}
    -   [fromdict](#Record.fromdict){.function}
-   [Choice](#Choice){.class}
    -   [Choice](#Choice.__init__){.function}
    -   [register](#Choice.register){.variable}
    -   [choice](#Choice.choice){.variable}
    -   [obj](#Choice.obj){.variable}
    -   [getObj](#Choice.getObj){.function}
    -   [getName](#Choice.getName){.function}
    -   [getClass](#Choice.getClass){.function}
    -   [todict](#Choice.todict){.function}
    -   [fromdict](#Choice.fromdict){.function}
-   [Enumerated](#Enumerated){.class}
    -   [todict](#Enumerated.todict){.function}
    -   [fromdict](#Enumerated.fromdict){.function}
-   [EnumeratedID](#EnumeratedID){.class}
    -   [todict](#EnumeratedID.todict){.function}
    -   [fromdict](#EnumeratedID.fromdict){.function}
-   [Array](#Array){.class}
    -   [fieldtypes](#Array.fieldtypes){.variable}
    -   [todict](#Array.todict){.function}
    -   [fromdict](#Array.fromdict){.function}
-   [ArrayOf](#ArrayOf){.class}
    -   [ArrayOf](#ArrayOf.__init__){.function}
-   [Map](#Map){.class}
    -   [fieldtypes](#Map.fieldtypes){.variable}
    -   [extend](#Map.extend){.variable}
    -   [regext](#Map.regext){.variable}
    -   [todict](#Map.todict){.function}
    -   [fromdict](#Map.fromdict){.function}
-   [MapOf](#MapOf){.class}
    -   [MapOf](#MapOf.__init__){.function}

[built with [pdoc]{.visually-hidden}![pdoc
logo](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20role%3D%22img%22%20aria-label%3D%22pdoc%20logo%22%20width%3D%22300%22%20height%3D%22150%22%20viewBox%3D%22-1%200%2060%2030%22%3E%3Ctitle%3Epdoc%3C/title%3E%3Cpath%20d%3D%22M29.621%2021.293c-.011-.273-.214-.475-.511-.481a.5.5%200%200%200-.489.503l-.044%201.393c-.097.551-.695%201.215-1.566%201.704-.577.428-1.306.486-2.193.182-1.426-.617-2.467-1.654-3.304-2.487l-.173-.172a3.43%203.43%200%200%200-.365-.306.49.49%200%200%200-.286-.196c-1.718-1.06-4.931-1.47-7.353.191l-.219.15c-1.707%201.187-3.413%202.131-4.328%201.03-.02-.027-.49-.685-.141-1.763.233-.721.546-2.408.772-4.076.042-.09.067-.187.046-.288.166-1.347.277-2.625.241-3.351%201.378-1.008%202.271-2.586%202.271-4.362%200-.976-.272-1.935-.788-2.774-.057-.094-.122-.18-.184-.268.033-.167.052-.339.052-.516%200-1.477-1.202-2.679-2.679-2.679-.791%200-1.496.352-1.987.9a6.3%206.3%200%200%200-1.001.029c-.492-.564-1.207-.929-2.012-.929-1.477%200-2.679%201.202-2.679%202.679A2.65%202.65%200%200%200%20.97%206.554c-.383.747-.595%201.572-.595%202.41%200%202.311%201.507%204.29%203.635%205.107-.037.699-.147%202.27-.423%203.294l-.137.461c-.622%202.042-2.515%208.257%201.727%2010.643%201.614.908%203.06%201.248%204.317%201.248%202.665%200%204.492-1.524%205.322-2.401%201.476-1.559%202.886-1.854%206.491.82%201.877%201.393%203.514%201.753%204.861%201.068%202.223-1.713%202.811-3.867%203.399-6.374.077-.846.056-1.469.054-1.537zm-4.835%204.313c-.054.305-.156.586-.242.629-.034-.007-.131-.022-.307-.157-.145-.111-.314-.478-.456-.908.221.121.432.25.675.355.115.039.219.051.33.081zm-2.251-1.238c-.05.33-.158.648-.252.694-.022.001-.125-.018-.307-.157-.217-.166-.488-.906-.639-1.573.358.344.754.693%201.198%201.036zm-3.887-2.337c-.006-.116-.018-.231-.041-.342.635.145%201.189.368%201.599.625.097.231.166.481.174.642-.03.049-.055.101-.067.158-.046.013-.128.026-.298.004-.278-.037-.901-.57-1.367-1.087zm-1.127-.497c.116.306.176.625.12.71-.019.014-.117.045-.345.016-.206-.027-.604-.332-.986-.695.41-.051.816-.056%201.211-.031zm-4.535%201.535c.209.22.379.47.358.598-.006.041-.088.138-.351.234-.144.055-.539-.063-.979-.259a11.66%2011.66%200%200%200%20.972-.573zm.983-.664c.359-.237.738-.418%201.126-.554.25.237.479.548.457.694-.006.042-.087.138-.351.235-.174.064-.694-.105-1.232-.375zm-3.381%201.794c-.022.145-.061.29-.149.401-.133.166-.358.248-.69.251h-.002c-.133%200-.306-.26-.45-.621.417.091.854.07%201.291-.031zm-2.066-8.077a4.78%204.78%200%200%201-.775-.584c.172-.115.505-.254.88-.378l-.105.962zm-.331%202.302a10.32%2010.32%200%200%201-.828-.502c.202-.143.576-.328.984-.49l-.156.992zm-.45%202.157l-.701-.403c.214-.115.536-.249.891-.376a11.57%2011.57%200%200%201-.19.779zm-.181%201.716c.064.398.194.702.298.893-.194-.051-.435-.162-.736-.398.061-.119.224-.3.438-.495zM8.87%204.141c0%20.152-.123.276-.276.276s-.275-.124-.275-.276.123-.276.276-.276.275.124.275.276zm-.735-.389a1.15%201.15%200%200%200-.314.783%201.16%201.16%200%200%200%201.162%201.162c.457%200%20.842-.27%201.032-.653.026.117.042.238.042.362a1.68%201.68%200%200%201-1.679%201.679%201.68%201.68%200%200%201-1.679-1.679c0-.843.626-1.535%201.436-1.654zM5.059%205.406A1.68%201.68%200%200%201%203.38%207.085a1.68%201.68%200%200%201-1.679-1.679c0-.037.009-.072.011-.109.21.3.541.508.935.508a1.16%201.16%200%200%200%201.162-1.162%201.14%201.14%200%200%200-.474-.912c.015%200%20.03-.005.045-.005.926.001%201.679.754%201.679%201.68zM3.198%204.141c0%20.152-.123.276-.276.276s-.275-.124-.275-.276.123-.276.276-.276.275.124.275.276zM1.375%208.964c0-.52.103-1.035.288-1.52.466.394%201.06.64%201.717.64%201.144%200%202.116-.725%202.499-1.738.383%201.012%201.355%201.738%202.499%201.738.867%200%201.631-.421%202.121-1.062.307.605.478%201.267.478%201.942%200%202.486-2.153%204.51-4.801%204.51s-4.801-2.023-4.801-4.51zm24.342%2019.349c-.985.498-2.267.168-3.813-.979-3.073-2.281-5.453-3.199-7.813-.705-1.315%201.391-4.163%203.365-8.423.97-3.174-1.786-2.239-6.266-1.261-9.479l.146-.492c.276-1.02.395-2.457.444-3.268a6.11%206.11%200%200%200%201.18.115%206.01%206.01%200%200%200%202.536-.562l-.006.175c-.802.215-1.848.612-2.021%201.25-.079.295.021.601.274.837.219.203.415.364.598.501-.667.304-1.243.698-1.311%201.179-.02.144-.022.507.393.787.213.144.395.26.564.365-1.285.521-1.361.96-1.381%201.126-.018.142-.011.496.427.746l.854.489c-.473.389-.971.914-.999%201.429-.018.278.095.532.316.713.675.556%201.231.721%201.653.721.059%200%20.104-.014.158-.02.207.707.641%201.64%201.513%201.64h.013c.8-.008%201.236-.345%201.462-.626.173-.216.268-.457.325-.692.424.195.93.374%201.372.374.151%200%20.294-.021.423-.068.732-.27.944-.704.993-1.021.009-.061.003-.119.002-.179.266.086.538.147.789.147.15%200%20.294-.021.423-.069.542-.2.797-.489.914-.754.237.147.478.258.704.288.106.014.205.021.296.021.356%200%20.595-.101.767-.229.438.435%201.094.992%201.656%201.067.106.014.205.021.296.021a1.56%201.56%200%200%200%20.323-.035c.17.575.453%201.289.866%201.605.358.273.665.362.914.362a.99.99%200%200%200%20.421-.093%201.03%201.03%200%200%200%20.245-.164c.168.428.39.846.68%201.068.358.273.665.362.913.362a.99.99%200%200%200%20.421-.093c.317-.148.512-.448.639-.762.251.157.495.257.726.257.127%200%20.25-.024.37-.071.427-.17.706-.617.841-1.314.022-.015.047-.022.068-.038.067-.051.133-.104.196-.159-.443%201.486-1.107%202.761-2.086%203.257zM8.66%209.925a.5.5%200%201%200-1%200c0%20.653-.818%201.205-1.787%201.205s-1.787-.552-1.787-1.205a.5.5%200%201%200-1%200c0%201.216%201.25%202.205%202.787%202.205s2.787-.989%202.787-2.205zm4.4%2015.965l-.208.097c-2.661%201.258-4.708%201.436-6.086.527-1.542-1.017-1.88-3.19-1.844-4.198a.4.4%200%200%200-.385-.414c-.242-.029-.406.164-.414.385-.046%201.249.367%203.686%202.202%204.896.708.467%201.547.7%202.51.7%201.248%200%202.706-.392%204.362-1.174l.185-.086a.4.4%200%200%200%20.205-.527c-.089-.204-.326-.291-.527-.206zM9.547%202.292c.093.077.205.114.317.114a.5.5%200%200%200%20.318-.886L8.817.397a.5.5%200%200%200-.703.068.5.5%200%200%200%20.069.703l1.364%201.124zm-7.661-.065c.086%200%20.173-.022.253-.068l1.523-.893a.5.5%200%200%200-.506-.863l-1.523.892a.5.5%200%200%200-.179.685c.094.158.261.247.432.247z%22%20transform%3D%22matrix%28-1%200%200%201%2058%200%29%22%20fill%3D%22%233bb300%22/%3E%3Cpath%20d%3D%22M.3%2021.86V10.18q0-.46.02-.68.04-.22.18-.5.28-.54%201.34-.54%201.06%200%201.42.28.38.26.44.78.76-1.04%202.38-1.04%201.64%200%203.1%201.54%201.46%201.54%201.46%203.58%200%202.04-1.46%203.58-1.44%201.54-3.08%201.54-1.64%200-2.38-.92v4.04q0%20.46-.04.68-.02.22-.18.5-.14.3-.5.42-.36.12-.98.12-.62%200-1-.12-.36-.12-.52-.4-.14-.28-.18-.5-.02-.22-.02-.68zm3.96-9.42q-.46.54-.46%201.18%200%20.64.46%201.18.48.52%201.2.52.74%200%201.24-.52.52-.52.52-1.18%200-.66-.48-1.18-.48-.54-1.26-.54-.76%200-1.22.54zm14.741-8.36q.16-.3.54-.42.38-.12%201-.12.64%200%201.02.12.38.12.52.42.16.3.18.54.04.22.04.68v11.94q0%20.46-.04.7-.02.22-.18.5-.3.54-1.7.54-1.38%200-1.54-.98-.84.96-2.34.96-1.8%200-3.28-1.56-1.48-1.58-1.48-3.66%200-2.1%201.48-3.68%201.5-1.58%203.28-1.58%201.48%200%202.3%201v-4.2q0-.46.02-.68.04-.24.18-.52zm-3.24%2010.86q.52.54%201.26.54.74%200%201.22-.54.5-.54.5-1.18%200-.66-.48-1.22-.46-.56-1.26-.56-.8%200-1.28.56-.48.54-.48%201.2%200%20.66.52%201.2zm7.833-1.2q0-2.4%201.68-3.96%201.68-1.56%203.84-1.56%202.16%200%203.82%201.56%201.66%201.54%201.66%203.94%200%201.66-.86%202.96-.86%201.28-2.1%201.9-1.22.6-2.54.6-1.32%200-2.56-.64-1.24-.66-2.1-1.92-.84-1.28-.84-2.88zm4.18%201.44q.64.48%201.3.48.66%200%201.32-.5.66-.5.66-1.48%200-.98-.62-1.46-.62-.48-1.34-.48-.72%200-1.34.5-.62.5-.62%201.48%200%20.96.64%201.46zm11.412-1.44q0%20.84.56%201.32.56.46%201.18.46.64%200%201.18-.36.56-.38.9-.38.6%200%201.46%201.06.46.58.46%201.04%200%20.76-1.1%201.42-1.14.8-2.8.8-1.86%200-3.58-1.34-.82-.64-1.34-1.7-.52-1.08-.52-2.36%200-1.3.52-2.34.52-1.06%201.34-1.7%201.66-1.32%203.54-1.32.76%200%201.48.22.72.2%201.06.4l.32.2q.36.24.56.38.52.4.52.92%200%20.5-.42%201.14-.72%201.1-1.38%201.1-.38%200-1.08-.44-.36-.34-1.04-.34-.66%200-1.24.48-.58.48-.58%201.34z%22%20fill%3D%22green%22/%3E%3C/svg%3E)](https://pdoc.dev "pdoc: Python API documentation generator"){.attribution
target="_blank"}

</div>

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.pdoc role="main"}
::::: {.section .module-info}
# [openc2lib](./../../openc2lib.html).[types](./../types.html).basetypes {#openc2lib.types.basetypes .modulename}

::: docstring
OpenC2 structures

Definition of the base types (structures) in the OpenC2 DataModels (Sec.
3.1.1) Each OpenC2 object must derive from these classes, which affects
serialization operations
:::

View Source

::: {.pdoc-code .codehilite}
      1""" OpenC2 structures
      2
      3  Definition of the base types (structures) in the OpenC2 DataModels (Sec. 3.1.1)
      4  Each OpenC2 object must derive from these classes, which
      5  affects serialization operations
      6
      7"""
      8
      9import aenum
     10import inspect
     11import logging
     12
     13logger = logging.getLogger('openc2lib')
     14""" openc2lib logger """
     15
     16
     17class Openc2Type():
     18 """ OpenC2 Language Element
     19        
     20        This class is currently unused and is only provided to have a common ancestor for all
     21        OpenC2 basic types. It may be used in the future to implement common methods or arguments.
     22    """
     23 pass
     24
     25
     26#@register_basetype
     27class Record(Openc2Type):
     28 """ OpenC2 Record
     29
     30        Implements OpenC2 Record: 
     31            >An ordered map from a list of keys with positions to values with 
     32            positionally-defined semantics. Each key has a position and name, 
     33            and is mapped to a type.
     34
     35        It expect keys to be public class attributes. All internal attributes 
     36        must be kept private by prefixing it with an '_'.
     37
     38    """
     39 def todict(self, e):
     40     """ Converts to dictionary 
     41        
     42            It is used to convert this object to an intermediary representation during 
     43            serialization. It takes an `Encoder` argument that is used to recursively
     44            serialize inner data and structures (the `Encoder` provides standard methods
     45            for converting base types to dictionaries).. 
     46
     47            :param e: The `Encoder` that is being used.
     48            :return: A dictionary compliants to the Language Specification's serialization
     49            rules.
     50        """
     51     objdic = vars(self)
     52
     53     dic = {}
     54     for k,v in objdic.items():
     55         # Fix keywords corresponding to variable names that clash with Python keywords
     56         if isinstance(k, str) and k.endswith('_'):
     57             k = k.rstrip('_')
     58         # Remove empty and private elements; do not include non-string keys
     59         if not v is None and not k.startswith('_') and isinstance(k, str):
     60             dic[k] = v    
     61
     62     return e.todict(dic)
     63
     64 @classmethod
     65 def fromdict(clstype, dic, e):
     66     """ Builds instance from dictionary 
     67
     68            It is used during deserialization to create an openc2lib instance from the text message.
     69            It takes an `Encoder` instance that is used to recursively build instances of the inner
     70            objects (the `Encoder` provides standard methods to create instances of base objects like
     71            strings, integers, boolean).
     72
     73            :param dic: The intermediary dictionary representation from which the object is built.
     74            :param e: The `Encoder that is being used.
     75            :return: An instance of this class initialized from the dictionary values.
     76        """
     77     objdic = {}
     78     # Retrieve class type for each field in the dictionary
     79     fielddesc = None
     80     for tpl in inspect.getmembers(clstype):
     81         if tpl[0] == '__annotations__':
     82             fielddesc = tpl[1]
     83
     84     for k,v in dic.items():
     85         if k not in fielddesc:
     86             raise Exception("Unknown field '" + k + "' from message")
     87         objdic[k] = e.fromdict(fielddesc[k], v)
     88
     89
     90     # A record should always have more than one field, so the following statement 
     91     # should not raise exceptions
     92     return clstype(**objdic)
     93
     94
     95
     96class Choice(Openc2Type):
     97 """ OpenC2 Choice
     98        Implements the OpenC2 Choice:
     99        >One field selected from a set of named fields. The API value has a name and a type.
    100
    101      It expect all allowed values to be provided in a `Register` class, which must be defined
    102      as class attribute `register` in all derived classes (see `Target` and `Actuator` as examples).
    103  """
    104   register = None
    105   """ List of registered name/class options available """
    106
    107   def __init__(self, obj):
    108       """ Initialize the `Choice` object
    109
    110          Objects used as `Choice` must be registered in advance in the `register` dictionary.
    111
    112          :arg obj: An object among those defined in the `register`.
    113      """
    114       self.choice: str = self.register.getName(obj.__class__)
    115       """ Selected name for the `Choice` """
    116       self.obj = obj
    117       """ Class corresponding to the `choice` """
    118
    119   def getObj(self):
    120       """ Returns the objet instance embedded in the `register`."""
    121       return self.obj
    122   
    123   def getName(self):
    124       """Returns the name of the choice
    125
    126          Returns the name of object, which is the selector carried by the `Choice` element. 
    127          This does not include the object itself.
    128      """
    129       return self.choice
    130
    131   @classmethod
    132   def getClass(cls, choice):
    133       """ Get the class corresponding to the current `choice` 
    134          
    135          It may be implemented by any derived class, if a different logic than the `Register` class 
    136          is followed to store the name/class bindings.
    137          :param choice: The name of the alternative that is being looked for.
    138          :return: The class corresponding to the provided `choice`.
    139      """
    140       return cls.register.get(choice)
    141
    142   def __str__(self):
    143       return self.choice
    144
    145   def __repr__(self):
    146       return str(self.obj)
    147
    148   def todict(self, e):
    149       """ Converts to dictionary 
    150      
    151          It is used to convert this object to an intermediary representation during 
    152          serialization. It takes an `Encoder` argument that is used to recursively
    153          serialize inner data and structures (the `Encoder` provides standard methods
    154          for converting base types to dictionaries).. 
    155
    156          :param e: The `Encoder` that is being used.
    157          :return: A dictionary compliants to the Language Specification's serialization
    158          rules.
    159      """
    160       # In case of Choice, the specific choice may be the implementation of an additional type,
    161       # which affects its representation. So, first of all, get the representation of the inner
    162       # data type
    163       dic = {}
    164       dic[self.choice] = e.todict(self.obj)
    165       return dic
    166
    167   @classmethod
    168   def fromdict(cls, dic, e):
    169       """ Builds instance from dictionary 
    170
    171          It is used during deserialization to create an openc2lib instance from the text message.
    172          It takes an `Encoder` instance that is used to recursively build instances of the inner
    173          objects (the `Encoder` provides standard methods to create instances of base objects like
    174          strings, integers, boolean).
    175
    176          :param dic: The intermediary dictionary representation from which the object is built.
    177          :param e: The `Encoder that is being used.
    178          :return: An instance of this class initialized from the dictionary values.
    179      """
    180       if not len(dic) == 1:
    181           raise ValueError("Unexpected dict: ", dic)
    182
    183       for k, v in dic.items():
    184           # Expected to run one time only!
    185           objtype = cls.getClass(k)
    186           return cls(e.fromdict(objtype, v))
    187
    188class Enumerated(Openc2Type, aenum.Enum):
    189   """ OpenC2 Enumerated
    190
    191      Implements OpenC2 Enumerated:
    192      >A set of named integral constants. The API value is a name.
    193
    194      The constants may be anything, including strings, integers, classes.
    195  """
    196
    197   # Convert enumerations to str
    198   def todict(self, e):
    199       """ Converts to dictionary 
    200      
    201          It is used to convert this object to an intermediary representation during 
    202          serialization. It takes an `Encoder` argument that is used to recursively
    203          serialize inner data and structures (the `Encoder` provides standard methods
    204          for converting base types to dictionaries).. 
    205
    206          :param e: The `Encoder` that is being used.
    207          :return: A dictionary compliants to the Language Specification's serialization
    208          rules.
    209      """
    210       return self.name
    211
    212   @classmethod
    213   def fromdict(cls, dic, e):
    214       """ Builds instance from dictionary 
    215
    216          It is used during deserialization to create an openc2lib instance from the text message.
    217          It takes an `Encoder` instance that is used to recursively build instances of the inner
    218          objects (the `Encoder` provides standard methods to create instances of base objects like
    219          strings, integers, boolean).
    220
    221          :param dic: The intermediary dictionary representation from which the object is built.
    222          :param e: The `Encoder that is being used.
    223          :return: An instance of this class initialized from the dictionary values.
    224      """
    225       try:
    226           return cls[str(dic)]
    227       except:
    228           raise TypeError("Unexpected enum value: ", dic)
    229   
    230# This class should check the names are integers.
    231# The enum syntax only allows to define <str = int> pairs,
    232# so to use this class it is necessary to define mnemonic label
    233# TODO: Test this code
    234class EnumeratedID(Enumerated):
    235   """ OpenC2 EnumeratedID
    236
    237      Implements OpenC2 EnumeratedID: 
    238      >A set of unnamed integral constants. The API value is an id.
    239
    240      The current implementation does not check the values to be integer.
    241      However, coversion to/from integer is explicitly done during the
    242      intermediary dictionary serialization, hence throwing an Exception if
    243      the IDs are not integers.
    244  """
    245
    246   def todict(self, e):
    247       """ Converts to dictionary 
    248      
    249          It is used to convert this object to an intermediary representation during 
    250          serialization. It takes an `Encoder` argument that is used to recursively
    251          serialize inner data and structures (the `Encoder` provides standard methods
    252          for converting base types to dictionaries).. 
    253
    254          :param e: The `Encoder` that is being used.
    255          :return: A dictionary compliants to the Language Specification's serialization
    256          rules.
    257      """
    258       return int(self.value)
    259
    260   @classmethod
    261   def fromdict(cls, dic, e):
    262       """ Builds instance from dictionary 
    263
    264          It is used during deserialization to create an openc2lib instance from the text message.
    265          It takes an `Encoder` instance that is used to recursively build instances of the inner
    266          objects (the `Encoder` provides standard methods to create instances of base objects like
    267          strings, integers, boolean).
    268
    269          :param dic: The intermediary dictionary representation from which the object is built.
    270          :param e: The `Encoder that is being used.
    271          :return: An instance of this class initialized from the dictionary values.
    272      """
    273       try:
    274           return cls(int(dic))
    275       except:
    276           raise TypeError("Unexpected enum value: ", dic)
    277
    278class Array(Openc2Type, list):
    279   """ OpenC2 Array
    280
    281      Implements OpenC2 Array:
    282      >An ordered list of unnamed fields with positionally-defined semantics. 
    283      Each field has a position, label, and type.
    284
    285      However, position does not matter in this implementation.
    286
    287      Derived classes must provide a `fieldtypes` dictionary that associate each field name
    288      to its class. This is strictly required in order to instantiate the object at
    289      deserialization time. However, no check is performed when new items are inserted.
    290  """
    291   fieldtypes = None
    292   """ Field types
    293
    294      A `dictionary` which keys are field names and which values are the corresponding classes.
    295      Must be provided by any derived class.
    296  """
    297
    298   def todict(self, e):
    299       """ Converts to dictionary 
    300      
    301          It is used to convert this object to an intermediary representation during 
    302          serialization. It takes an `Encoder` argument that is used to recursively
    303          serialize inner data and structures (the `Encoder` provides standard methods
    304          for converting base types to dictionaries).. 
    305
    306          :param e: The `Encoder` that is being used.
    307          :return: A dictionary compliants to the Language Specification's serialization
    308          rules.
    309      """
    310       lis = []
    311       for i in self:
    312           lis.append = e.todict(i)
    313       return lis
    314
    315   def fromdict(cls, dic, e):
    316       """ !!! WARNING !!!
    317          Currently not implemented because there are no examples of usage of this
    318          type (only Array/net, which is not clear)
    319      """
    320       raise Exception("Function not implemented")
    321
    322class ArrayOf:
    323   """ OpenC2 ArrayOf
    324
    325      Implements OpenC2 ArrayOf(*vtype*):
    326      >An ordered list of fields with the same semantics. 
    327      Each field has a position and type *vtype*.
    328
    329      It extends the `Array` type. However, to make its usage simpler and compliant 
    330      to the description given in the
    331      Language Specification, the implementation is quite different.
    332      Note that in many cases `ArrayOf` is only used to create arrays without the need
    333      to derive an additional data type.
    334  """
    335
    336   def __new__(self, fldtype):
    337       """ `ArrayOf` builder
    338
    339          Creates a unnamed derived class from `Array`, which `fieldtypes` is set to `fldtype`.
    340          :param fldtype: The type of the fields stored in the array (indicated as *vtype* in 
    341                  the Language Specification.
    342          :return: A new unnamed class definition.
    343      """
    344       class ArrayOf(Array):
    345           """ OpenC2 unnamed `ArrayOf`
    346
    347              This class inherits from `Array` and sets its `fieldtypes` to a given type.
    348      
    349              One might like to check the type of the elements before inserting them.
    350              However, this is not the Python-way. Python use the duck typing approach:
    351              https://en.wikipedia.org/wiki/Duck_typing
    352              We ask for the type of objects just to keep this information according to
    353              the OpenC2 data model.
    354
    355              Note: no `todict()` method is provided, since `Array.todict()` is fine here.
    356          """
    357           fieldtype = fldtype
    358           """ The type of values stored in this container """
    359
    360           @classmethod
    361           def fromdict(cls, lis, e):
    362               """ Builds instance from dictionary 
    363      
    364                  It is used during deserialization to create an openc2lib instance from the text message.
    365                  It takes an `Encoder` instance that is used to recursively build instances of the inner
    366                  objects (the `Encoder` provides standard methods to create instances of base objects like
    367                  strings, integers, boolean).
    368      
    369                  :param lis: The intermediary dictionary representation from which the object is built.
    370                  :param e: The `Encoder that is being used.
    371                  :return: An instance of this class initialized from the dictionary values.
    372              """
    373               objlis = cls()
    374               logger.debug('Building %s from %s in ArrayOf', cls, lis)
    375               logger.debug('-> instantiating: %s', cls.fieldtype)
    376               for k in lis:
    377                   objlis.append(e.fromdict(cls.fieldtype, k))
    378       
    379               return objlis
    380           
    381           # This is the code if I would like to do type checking
    382           # when inserting data
    383#         def append(self, item):
    384#             if isinstance(item, self.fieldtype):
    385#                 super().append(item)
    386#             else:
    387#                 raise ValueError(self.fieldtype,' allowed only')
    388#         
    389#         def insert(self, index, item):
    390#             if isinstance(item, self.fieldtype):
    391#                 super().insert(index, item)
    392#             else:
    393#                 raise ValueError(self.fieldtype,' allowed only')
    394#         
    395#         def __add__(self, item):
    396#             if isinstance(item, self.fieldtype):
    397#                 super().__add__(item)
    398#             else:
    399#                 raise ValueError(self.fieldtype,' allowed only')
    400#         
    401#         def __iadd__(self, item):
    402#             if isinstance(item, self.fieldtype):
    403#                 super().__iadd__(item)
    404#             else:
    405#                 raise ValueError(self.fieldtype,' allowed only')
    406
    407       return ArrayOf
    408
    409
    410class Map(Openc2Type, dict):
    411   """ OpenC2 Map
    412
    413      Implements OpenC2 Map:
    414      >An unordered map from a set of specified keys to values with semantics 
    415          bound to each key. Each field has an id, name and type.
    416
    417      However, the id is not considered in this implementation.
    418
    419      The implementation follows a similar logic than `Array`. Each derived class
    420      is expected to provide a `fieldtypes` class attribute that associate field names 
    421      with their class definition. 
    422      
    423      Additionally, according to the Language Specification, `Map`s may be extended by
    424      Profiles. Such extensions must use the `extend` and `regext` class attributes to 
    425      bind to the base element they extend and the `Profile` in which they are defined.
    426  """
    427   fieldtypes: dict = None
    428   """ Field types
    429
    430      A `dictionary` which keys are field names and which values are the corresponding classes.
    431      Must be provided by any derived class.
    432  """
    433   extend = None
    434   """ Base class
    435
    436      Data types defined in the Language Specification shall not set this field. Data types defined in
    437      Profiles that extends a Data Type defined in the Language Specification, must set this field to
    438      the corresponding class of the base Data Type.
    439
    440      Note: Extensions defined in the openc2lib context are recommended to use the same name of the base
    441      Data Type, and to distinguish them through appropriate usage of the namespacing mechanism.
    442  """
    443   regext = {}
    444   """ Registered extensions
    445
    446      Classes that implement a Data Type defined in the Language Specification will use this field to
    447      register extensions defined by external Profiles. Classes that define extensions within Profiles
    448      shall register themselves according to the specific documentation of the base type class, but 
    449      shall not modify this field.
    450  """
    451
    452   def todict(self, e):
    453       """ Converts to dictionary 
    454      
    455          It is used to convert this object to an intermediary representation during 
    456          serialization. It takes an `Encoder` argument that is used to recursively
    457          serialize inner data and structures (the `Encoder` provides standard methods
    458          for converting base types to dictionaries).. 
    459
    460          :param e: The `Encoder` that is being used.
    461          :return: A dictionary compliants to the Language Specification's serialization
    462          rules.
    463      """
    464       newdic=dict()
    465
    466       # This is necessary because self.extend.fieldtypes does
    467       # not exist for non-extended classes
    468       if self.extend is None:
    469           return e.todict(dict(self))
    470           
    471       for k,v in self.items():
    472           if k not in self.fieldtypes:
    473               raise ValueError('Unknown field: ', k)
    474           if k in self.extend.fieldtypes:
    475               newdic[k] = v
    476           else:
    477               if self.nsid not in newdic:
    478                   newdic[self.nsid]={}
    479               newdic[self.nsid][k]=v
    480           
    481       return e.todict(newdic)
    482
    483   @classmethod
    484   def fromdict(cls, dic, e):
    485       """ Builds instance from dictionary 
    486
    487          It is used during deserialization to create an openc2lib instance from the text message.
    488          It takes an `Encoder` instance that is used to recursively build instances of the inner
    489          objects (the `Encoder` provides standard methods to create instances of base objects like
    490          strings, integers, boolean).
    491
    492          :param dic: The intermediary dictionary representation from which the object is built.
    493          :param e: The `Encoder that is being used.
    494          :return: An instance of this class initialized from the dictionary values.
    495      """
    496       objdic = {}
    497       extension = None
    498       logger.debug('Building %s from %s in Map', cls, dic)
    499       for k,v in dic.items():
    500           if k in cls.fieldtypes:
    501               objdic[k] = e.fromdict(cls.fieldtypes[k], v)
    502           elif k in cls.regext:
    503               logger.debug('   Using profile %s to decode: %s', k, v)
    504               extension = cls.regext[k]
    505               for l,w in v.items():
    506                   objdic[l] = e.fromdict(extension.fieldtypes[l], w)
    507           else:
    508               raise TypeError("Unexpected field: ", k)
    509
    510       if extension is not None:
    511           cls = extension
    512
    513       return cls(objdic)
    514
    515class MapOf:
    516   """ OpenC2 MapOf
    517
    518      Implements OpenC2 MapOf(*ktype, vtype*):
    519      >An unordered set of keys to values with the same semantics. 
    520          Each key has key type *ktype* and is mapped to value type *vtype*.
    521
    522      It extends `Map` with the same approach already used for `ArrayOf`.
    523      `MapOf` for specific types are created as anonymous classes by passing
    524      `ktype` and `vtype` as arguments.
    525
    526      Note: `MapOf` implementation currently does not support extensins!.
    527  """
    528
    529   def __new__(self,ktype, vtype):
    530       """ `MapOf` builder
    531
    532          Creates a unnamed derived class from `Map`, which `fieldtypes` is set to a single value
    533          `ktype: vtype`.
    534          :param ktype: The key type of the items stored in the map.
    535          :param vtype: The value type of the items stored in the map.
    536          :return: A new unnamed class definition.
    537      """
    538       class MapOf(Map):
    539           """ OpenC2 unnamed `MapOf`
    540
    541              This class inherits from `Map` and sets its `fieldtypes` to a given type.
    542      
    543              Note: no `todict()` method is provided, since `Map.todict()` is fine here.
    544          """
    545           fieldtypes = {ktype: vtype}
    546           """ The type of values stored in this container """
    547
    548           @classmethod
    549           def fromdict(cls, dic, e):
    550               """ Builds instance from dictionary 
    551      
    552                  It is used during deserialization to create an openc2lib instance from the text message.
    553                  It takes an `Encoder` instance that is used to recursively build instances of the inner
    554                  objects (the `Encoder` provides standard methods to create instances of base objects like
    555                  strings, integers, boolean).
    556      
    557                  :param dic: The intermediary dictionary representation from which the object is built.
    558                  :param e: The `Encoder that is being used.
    559                  :return: An instance of this class initialized from the dictionary values.
    560              """
    561               objdic = {}
    562               logger.debug('Building %s from %s in MapOf', cls, dic)
    563               for k,v in dic.items():
    564                   kclass = list(cls.fieldtypes)[0]
    565                   objk = e.fromdict(kclass, k)
    566                   objdic[objk] = e.fromdict(cls.fieldtypes[kclass], v)
    567               return objdic
    568
    569       return MapOf
:::
:::::

::::: {#logger .section}
::: {.attr .variable}
[logger]{.name} = [\<Logger openc2lib (WARNING)\>]{.default_value}
:::

[](#logger){.headerlink}

::: docstring
openc2lib logger
:::
:::::

:::::: {#Openc2Type .section}
::: {.attr .class}
[class]{.def} [Openc2Type]{.name}: View Source
:::

[](#Openc2Type){.headerlink}

::: {.pdoc-code .codehilite}
    18class Openc2Type():
    19    """ OpenC2 Language Element
    20       
    21       This class is currently unused and is only provided to have a common ancestor for all
    22       OpenC2 basic types. It may be used in the future to implement common methods or arguments.
    23   """
    24    pass
:::

::: docstring
OpenC2 Language Element

This class is currently unused and is only provided to have a common
ancestor for all OpenC2 basic types. It may be used in the future to
implement common methods or arguments.
:::
::::::

::::::::::::::: {#Record .section}
::: {.attr .class}
[class]{.def} [Record]{.name}([[Openc2Type](#Openc2Type)]{.base}): View
Source
:::

[](#Record){.headerlink}

::: {.pdoc-code .codehilite}
    28class Record(Openc2Type):
    29    """ OpenC2 Record
    30
    31       Implements OpenC2 Record: 
    32           >An ordered map from a list of keys with positions to values with 
    33           positionally-defined semantics. Each key has a position and name, 
    34           and is mapped to a type.
    35
    36       It expect keys to be public class attributes. All internal attributes 
    37       must be kept private by prefixing it with an '_'.
    38
    39   """
    40    def todict(self, e):
    41        """ Converts to dictionary 
    42       
    43           It is used to convert this object to an intermediary representation during 
    44           serialization. It takes an `Encoder` argument that is used to recursively
    45           serialize inner data and structures (the `Encoder` provides standard methods
    46           for converting base types to dictionaries).. 
    47
    48           :param e: The `Encoder` that is being used.
    49           :return: A dictionary compliants to the Language Specification's serialization
    50           rules.
    51       """
    52        objdic = vars(self)
    53
    54        dic = {}
    55        for k,v in objdic.items():
    56            # Fix keywords corresponding to variable names that clash with Python keywords
    57            if isinstance(k, str) and k.endswith('_'):
    58                k = k.rstrip('_')
    59            # Remove empty and private elements; do not include non-string keys
    60            if not v is None and not k.startswith('_') and isinstance(k, str):
    61                dic[k] = v    
    62
    63        return e.todict(dic)
    64
    65    @classmethod
    66    def fromdict(clstype, dic, e):
    67        """ Builds instance from dictionary 
    68
    69           It is used during deserialization to create an openc2lib instance from the text message.
    70           It takes an `Encoder` instance that is used to recursively build instances of the inner
    71           objects (the `Encoder` provides standard methods to create instances of base objects like
    72           strings, integers, boolean).
    73
    74           :param dic: The intermediary dictionary representation from which the object is built.
    75           :param e: The `Encoder that is being used.
    76           :return: An instance of this class initialized from the dictionary values.
    77       """
    78        objdic = {}
    79        # Retrieve class type for each field in the dictionary
    80        fielddesc = None
    81        for tpl in inspect.getmembers(clstype):
    82            if tpl[0] == '__annotations__':
    83                fielddesc = tpl[1]
    84
    85        for k,v in dic.items():
    86            if k not in fielddesc:
    87                raise Exception("Unknown field '" + k + "' from message")
    88            objdic[k] = e.fromdict(fielddesc[k], v)
    89
    90
    91        # A record should always have more than one field, so the following statement 
    92        # should not raise exceptions
    93        return clstype(**objdic)
:::

::: docstring
OpenC2 Record

Implements OpenC2 Record:

> An ordered map from a list of keys with positions to values with
> positionally-defined semantics. Each key has a position and name, and
> is mapped to a type.

It expect keys to be public class attributes. All internal attributes
must be kept private by prefixing it with an \'\_\'.
:::

:::::: {#Record.todict .classattr}
::: {.attr .function}
[def]{.def} [todict]{.name}[([[self]{.bp},
]{.param}[[e]{.n}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
:::

[](#Record.todict){.headerlink}

::: {.pdoc-code .codehilite}
    40 def todict(self, e):
    41      """ Converts to dictionary 
    42     
    43         It is used to convert this object to an intermediary representation during 
    44         serialization. It takes an `Encoder` argument that is used to recursively
    45         serialize inner data and structures (the `Encoder` provides standard methods
    46         for converting base types to dictionaries).. 
    47
    48         :param e: The `Encoder` that is being used.
    49         :return: A dictionary compliants to the Language Specification's serialization
    50         rules.
    51     """
    52      objdic = vars(self)
    53
    54      dic = {}
    55      for k,v in objdic.items():
    56          # Fix keywords corresponding to variable names that clash with Python keywords
    57          if isinstance(k, str) and k.endswith('_'):
    58              k = k.rstrip('_')
    59          # Remove empty and private elements; do not include non-string keys
    60          if not v is None and not k.startswith('_') and isinstance(k, str):
    61              dic[k] = v    
    62
    63      return e.todict(dic)
:::

::: docstring
Converts to dictionary

It is used to convert this object to an intermediary representation
during serialization. It takes an `Encoder` argument that is used to
recursively serialize inner data and structures (the `Encoder` provides
standard methods for converting base types to dictionaries)..

###### Parameters

-   **e**: The `Encoder` that is being used.

###### Returns

> A dictionary compliants to the Language Specification\'s serialization
> rules.
:::
::::::

::::::: {#Record.fromdict .classattr}
:::: {.attr .function}
::: decorator
\@classmethod
:::

[def]{.def} [fromdict]{.name}[([[clstype]{.n}, ]{.param}[[dic]{.n},
]{.param}[[e]{.n}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
::::

[](#Record.fromdict){.headerlink}

::: {.pdoc-code .codehilite}
    65 @classmethod
    66  def fromdict(clstype, dic, e):
    67      """ Builds instance from dictionary 
    68
    69         It is used during deserialization to create an openc2lib instance from the text message.
    70         It takes an `Encoder` instance that is used to recursively build instances of the inner
    71         objects (the `Encoder` provides standard methods to create instances of base objects like
    72         strings, integers, boolean).
    73
    74         :param dic: The intermediary dictionary representation from which the object is built.
    75         :param e: The `Encoder that is being used.
    76         :return: An instance of this class initialized from the dictionary values.
    77     """
    78      objdic = {}
    79      # Retrieve class type for each field in the dictionary
    80      fielddesc = None
    81      for tpl in inspect.getmembers(clstype):
    82          if tpl[0] == '__annotations__':
    83              fielddesc = tpl[1]
    84
    85      for k,v in dic.items():
    86          if k not in fielddesc:
    87              raise Exception("Unknown field '" + k + "' from message")
    88          objdic[k] = e.fromdict(fielddesc[k], v)
    89
    90
    91      # A record should always have more than one field, so the following statement 
    92      # should not raise exceptions
    93      return clstype(**objdic)
:::

::: docstring
Builds instance from dictionary

It is used during deserialization to create an openc2lib instance from
the text message. It takes an `Encoder` instance that is used to
recursively build instances of the inner objects (the `Encoder` provides
standard methods to create instances of base objects like strings,
integers, boolean).

###### Parameters {#parameters}

-   **dic**: The intermediary dictionary representation from which the
    object is built.
-   **e**: The \`Encoder that is being used.

###### Returns {#returns}

> An instance of this class initialized from the dictionary values.
:::
:::::::
:::::::::::::::

::::::::::::::::::::::::::::::::::::::::: {#Choice .section}
::: {.attr .class}
[class]{.def} [Choice]{.name}([[Openc2Type](#Openc2Type)]{.base}): View
Source
:::

[](#Choice){.headerlink}

::: {.pdoc-code .codehilite}
     97class Choice(Openc2Type):
     98   """ OpenC2 Choice
     99      Implements the OpenC2 Choice:
    100        >One field selected from a set of named fields. The API value has a name and a type.
    101
    102        It expect all allowed values to be provided in a `Register` class, which must be defined
    103        as class attribute `register` in all derived classes (see `Target` and `Actuator` as examples).
    104    """
    105 register = None
    106 """ List of registered name/class options available """
    107
    108 def __init__(self, obj):
    109     """ Initialize the `Choice` object
    110
    111            Objects used as `Choice` must be registered in advance in the `register` dictionary.
    112
    113            :arg obj: An object among those defined in the `register`.
    114        """
    115     self.choice: str = self.register.getName(obj.__class__)
    116     """ Selected name for the `Choice` """
    117     self.obj = obj
    118     """ Class corresponding to the `choice` """
    119
    120 def getObj(self):
    121     """ Returns the objet instance embedded in the `register`."""
    122     return self.obj
    123 
    124 def getName(self):
    125     """Returns the name of the choice
    126
    127            Returns the name of object, which is the selector carried by the `Choice` element. 
    128            This does not include the object itself.
    129        """
    130     return self.choice
    131
    132 @classmethod
    133 def getClass(cls, choice):
    134     """ Get the class corresponding to the current `choice` 
    135            
    136            It may be implemented by any derived class, if a different logic than the `Register` class 
    137            is followed to store the name/class bindings.
    138            :param choice: The name of the alternative that is being looked for.
    139            :return: The class corresponding to the provided `choice`.
    140        """
    141     return cls.register.get(choice)
    142
    143 def __str__(self):
    144     return self.choice
    145
    146 def __repr__(self):
    147     return str(self.obj)
    148
    149 def todict(self, e):
    150     """ Converts to dictionary 
    151        
    152            It is used to convert this object to an intermediary representation during 
    153            serialization. It takes an `Encoder` argument that is used to recursively
    154            serialize inner data and structures (the `Encoder` provides standard methods
    155            for converting base types to dictionaries).. 
    156
    157            :param e: The `Encoder` that is being used.
    158            :return: A dictionary compliants to the Language Specification's serialization
    159            rules.
    160        """
    161     # In case of Choice, the specific choice may be the implementation of an additional type,
    162     # which affects its representation. So, first of all, get the representation of the inner
    163     # data type
    164     dic = {}
    165     dic[self.choice] = e.todict(self.obj)
    166     return dic
    167
    168 @classmethod
    169 def fromdict(cls, dic, e):
    170     """ Builds instance from dictionary 
    171
    172            It is used during deserialization to create an openc2lib instance from the text message.
    173            It takes an `Encoder` instance that is used to recursively build instances of the inner
    174            objects (the `Encoder` provides standard methods to create instances of base objects like
    175            strings, integers, boolean).
    176
    177            :param dic: The intermediary dictionary representation from which the object is built.
    178            :param e: The `Encoder that is being used.
    179            :return: An instance of this class initialized from the dictionary values.
    180        """
    181     if not len(dic) == 1:
    182         raise ValueError("Unexpected dict: ", dic)
    183
    184     for k, v in dic.items():
    185         # Expected to run one time only!
    186         objtype = cls.getClass(k)
    187         return cls(e.fromdict(objtype, v))
:::

::: docstring
OpenC2 Choice Implements the OpenC2 Choice:

> One field selected from a set of named fields. The API value has a
> name and a type.

It expect all allowed values to be provided in a `Register` class, which
must be defined as class attribute [`register`](#Choice.register) in all
derived classes (see `Target` and `Actuator` as examples).
:::

:::::: {#Choice.__init__ .classattr}
::: {.attr .function}
[Choice]{.name}[([[obj]{.n}]{.param})]{.signature .pdoc-code .condensed}
View Source
:::

[](#Choice.__init__){.headerlink}

::: {.pdoc-code .codehilite}
    108  def __init__(self, obj):
    109       """ Initialize the `Choice` object
    110
    111          Objects used as `Choice` must be registered in advance in the `register` dictionary.
    112
    113          :arg obj: An object among those defined in the `register`.
    114      """
    115       self.choice: str = self.register.getName(obj.__class__)
    116       """ Selected name for the `Choice` """
    117       self.obj = obj
    118       """ Class corresponding to the `choice` """
:::

::: docstring
Initialize the [`Choice`](#Choice) object

Objects used as [`Choice`](#Choice) must be registered in advance in the
[`register`](#Choice.register) dictionary.

:arg obj: An object among those defined in the
[`register`](#Choice.register).
:::
::::::

::::: {#Choice.register .classattr}
::: {.attr .variable}
[register]{.name} = [None]{.default_value}
:::

[](#Choice.register){.headerlink}

::: docstring
List of registered name/class options available
:::
:::::

::::: {#Choice.choice .classattr}
::: {.attr .variable}
[choice]{.name}[: str]{.annotation}
:::

[](#Choice.choice){.headerlink}

::: docstring
Selected name for the [`Choice`](#Choice)
:::
:::::

::::: {#Choice.obj .classattr}
::: {.attr .variable}
[obj]{.name}
:::

[](#Choice.obj){.headerlink}

::: docstring
Class corresponding to the [`choice`](#Choice.choice)
:::
:::::

:::::: {#Choice.getObj .classattr}
::: {.attr .function}
[def]{.def}
[getObj]{.name}[([[self]{.bp}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
:::

[](#Choice.getObj){.headerlink}

::: {.pdoc-code .codehilite}
    120  def getObj(self):
    121       """ Returns the objet instance embedded in the `register`."""
    122       return self.obj
:::

::: docstring
Returns the objet instance embedded in the
[`register`](#Choice.register).
:::
::::::

:::::: {#Choice.getName .classattr}
::: {.attr .function}
[def]{.def}
[getName]{.name}[([[self]{.bp}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
:::

[](#Choice.getName){.headerlink}

::: {.pdoc-code .codehilite}
    124    def getName(self):
    125     """Returns the name of the choice
    126
    127            Returns the name of object, which is the selector carried by the `Choice` element. 
    128            This does not include the object itself.
    129        """
    130     return self.choice
:::

::: docstring
Returns the name of the choice

Returns the name of object, which is the selector carried by the
[`Choice`](#Choice) element. This does not include the object itself.
:::
::::::

::::::: {#Choice.getClass .classattr}
:::: {.attr .function}
::: decorator
\@classmethod
:::

[def]{.def} [getClass]{.name}[([[cls]{.bp},
]{.param}[[choice]{.n}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
::::

[](#Choice.getClass){.headerlink}

::: {.pdoc-code .codehilite}
    132  @classmethod
    133   def getClass(cls, choice):
    134       """ Get the class corresponding to the current `choice` 
    135          
    136          It may be implemented by any derived class, if a different logic than the `Register` class 
    137          is followed to store the name/class bindings.
    138          :param choice: The name of the alternative that is being looked for.
    139          :return: The class corresponding to the provided `choice`.
    140      """
    141       return cls.register.get(choice)
:::

::: docstring
Get the class corresponding to the current [`choice`](#Choice.choice)

It may be implemented by any derived class, if a different logic than
the `Register` class is followed to store the name/class bindings.

###### Parameters {#parameters}

-   **choice**: The name of the alternative that is being looked for.

###### Returns {#returns}

> The class corresponding to the provided [`choice`](#Choice.choice).
:::
:::::::

:::::: {#Choice.todict .classattr}
::: {.attr .function}
[def]{.def} [todict]{.name}[([[self]{.bp},
]{.param}[[e]{.n}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
:::

[](#Choice.todict){.headerlink}

::: {.pdoc-code .codehilite}
    149  def todict(self, e):
    150       """ Converts to dictionary 
    151      
    152          It is used to convert this object to an intermediary representation during 
    153          serialization. It takes an `Encoder` argument that is used to recursively
    154          serialize inner data and structures (the `Encoder` provides standard methods
    155          for converting base types to dictionaries).. 
    156
    157          :param e: The `Encoder` that is being used.
    158          :return: A dictionary compliants to the Language Specification's serialization
    159          rules.
    160      """
    161       # In case of Choice, the specific choice may be the implementation of an additional type,
    162       # which affects its representation. So, first of all, get the representation of the inner
    163       # data type
    164       dic = {}
    165       dic[self.choice] = e.todict(self.obj)
    166       return dic
:::

::: docstring
Converts to dictionary

It is used to convert this object to an intermediary representation
during serialization. It takes an `Encoder` argument that is used to
recursively serialize inner data and structures (the `Encoder` provides
standard methods for converting base types to dictionaries)..

###### Parameters {#parameters}

-   **e**: The `Encoder` that is being used.

###### Returns {#returns}

> A dictionary compliants to the Language Specification\'s serialization
> rules.
:::
::::::

::::::: {#Choice.fromdict .classattr}
:::: {.attr .function}
::: decorator
\@classmethod
:::

[def]{.def} [fromdict]{.name}[([[cls]{.bp}, ]{.param}[[dic]{.n},
]{.param}[[e]{.n}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
::::

[](#Choice.fromdict){.headerlink}

::: {.pdoc-code .codehilite}
    168  @classmethod
    169   def fromdict(cls, dic, e):
    170       """ Builds instance from dictionary 
    171
    172          It is used during deserialization to create an openc2lib instance from the text message.
    173          It takes an `Encoder` instance that is used to recursively build instances of the inner
    174          objects (the `Encoder` provides standard methods to create instances of base objects like
    175          strings, integers, boolean).
    176
    177          :param dic: The intermediary dictionary representation from which the object is built.
    178          :param e: The `Encoder that is being used.
    179          :return: An instance of this class initialized from the dictionary values.
    180      """
    181       if not len(dic) == 1:
    182           raise ValueError("Unexpected dict: ", dic)
    183
    184       for k, v in dic.items():
    185           # Expected to run one time only!
    186           objtype = cls.getClass(k)
    187           return cls(e.fromdict(objtype, v))
:::

::: docstring
Builds instance from dictionary

It is used during deserialization to create an openc2lib instance from
the text message. It takes an `Encoder` instance that is used to
recursively build instances of the inner objects (the `Encoder` provides
standard methods to create instances of base objects like strings,
integers, boolean).

###### Parameters {#parameters}

-   **dic**: The intermediary dictionary representation from which the
    object is built.
-   **e**: The \`Encoder that is being used.

###### Returns {#returns}

> An instance of this class initialized from the dictionary values.
:::
:::::::
:::::::::::::::::::::::::::::::::::::::::

:::::::::::::::: {#Enumerated .section}
::: {.attr .class}
[class]{.def} [Enumerated]{.name}([[Openc2Type](#Openc2Type)]{.base},
[aenum.\_enum.Enum]{.base}): View Source
:::

[](#Enumerated){.headerlink}

::: {.pdoc-code .codehilite}
    189class Enumerated(Openc2Type, aenum.Enum):
    190 """ OpenC2 Enumerated
    191
    192        Implements OpenC2 Enumerated:
    193        >A set of named integral constants. The API value is a name.
    194
    195        The constants may be anything, including strings, integers, classes.
    196    """
    197
    198 # Convert enumerations to str
    199 def todict(self, e):
    200     """ Converts to dictionary 
    201        
    202            It is used to convert this object to an intermediary representation during 
    203            serialization. It takes an `Encoder` argument that is used to recursively
    204            serialize inner data and structures (the `Encoder` provides standard methods
    205            for converting base types to dictionaries).. 
    206
    207            :param e: The `Encoder` that is being used.
    208            :return: A dictionary compliants to the Language Specification's serialization
    209            rules.
    210        """
    211     return self.name
    212
    213 @classmethod
    214 def fromdict(cls, dic, e):
    215     """ Builds instance from dictionary 
    216
    217            It is used during deserialization to create an openc2lib instance from the text message.
    218            It takes an `Encoder` instance that is used to recursively build instances of the inner
    219            objects (the `Encoder` provides standard methods to create instances of base objects like
    220            strings, integers, boolean).
    221
    222            :param dic: The intermediary dictionary representation from which the object is built.
    223            :param e: The `Encoder that is being used.
    224            :return: An instance of this class initialized from the dictionary values.
    225        """
    226     try:
    227         return cls[str(dic)]
    228     except:
    229         raise TypeError("Unexpected enum value: ", dic)
:::

::: docstring
OpenC2 Enumerated

Implements OpenC2 Enumerated:

> A set of named integral constants. The API value is a name.

The constants may be anything, including strings, integers, classes.
:::

:::::: {#Enumerated.todict .classattr}
::: {.attr .function}
[def]{.def} [todict]{.name}[([[self]{.bp},
]{.param}[[e]{.n}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
:::

[](#Enumerated.todict){.headerlink}

::: {.pdoc-code .codehilite}
    199  def todict(self, e):
    200       """ Converts to dictionary 
    201      
    202          It is used to convert this object to an intermediary representation during 
    203          serialization. It takes an `Encoder` argument that is used to recursively
    204          serialize inner data and structures (the `Encoder` provides standard methods
    205          for converting base types to dictionaries).. 
    206
    207          :param e: The `Encoder` that is being used.
    208          :return: A dictionary compliants to the Language Specification's serialization
    209          rules.
    210      """
    211       return self.name
:::

::: docstring
Converts to dictionary

It is used to convert this object to an intermediary representation
during serialization. It takes an `Encoder` argument that is used to
recursively serialize inner data and structures (the `Encoder` provides
standard methods for converting base types to dictionaries)..

###### Parameters {#parameters}

-   **e**: The `Encoder` that is being used.

###### Returns {#returns}

> A dictionary compliants to the Language Specification\'s serialization
> rules.
:::
::::::

::::::: {#Enumerated.fromdict .classattr}
:::: {.attr .function}
::: decorator
\@classmethod
:::

[def]{.def} [fromdict]{.name}[([[cls]{.bp}, ]{.param}[[dic]{.n},
]{.param}[[e]{.n}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
::::

[](#Enumerated.fromdict){.headerlink}

::: {.pdoc-code .codehilite}
    213  @classmethod
    214   def fromdict(cls, dic, e):
    215       """ Builds instance from dictionary 
    216
    217          It is used during deserialization to create an openc2lib instance from the text message.
    218          It takes an `Encoder` instance that is used to recursively build instances of the inner
    219          objects (the `Encoder` provides standard methods to create instances of base objects like
    220          strings, integers, boolean).
    221
    222          :param dic: The intermediary dictionary representation from which the object is built.
    223          :param e: The `Encoder that is being used.
    224          :return: An instance of this class initialized from the dictionary values.
    225      """
    226       try:
    227           return cls[str(dic)]
    228       except:
    229           raise TypeError("Unexpected enum value: ", dic)
:::

::: docstring
Builds instance from dictionary

It is used during deserialization to create an openc2lib instance from
the text message. It takes an `Encoder` instance that is used to
recursively build instances of the inner objects (the `Encoder` provides
standard methods to create instances of base objects like strings,
integers, boolean).

###### Parameters {#parameters}

-   **dic**: The intermediary dictionary representation from which the
    object is built.
-   **e**: The \`Encoder that is being used.

###### Returns {#returns}

> An instance of this class initialized from the dictionary values.
:::
:::::::

::: inherited
##### Inherited Members

aenum.\_enum.Enum
:   name
:   value
:   values
:::
::::::::::::::::

:::::::::::::::: {#EnumeratedID .section}
::: {.attr .class}
[class]{.def} [EnumeratedID]{.name}([[Enumerated](#Enumerated)]{.base}):
View Source
:::

[](#EnumeratedID){.headerlink}

::: {.pdoc-code .codehilite}
    235class EnumeratedID(Enumerated):
    236 """ OpenC2 EnumeratedID
    237
    238        Implements OpenC2 EnumeratedID: 
    239        >A set of unnamed integral constants. The API value is an id.
    240
    241        The current implementation does not check the values to be integer.
    242        However, coversion to/from integer is explicitly done during the
    243        intermediary dictionary serialization, hence throwing an Exception if
    244        the IDs are not integers.
    245    """
    246
    247 def todict(self, e):
    248     """ Converts to dictionary 
    249        
    250            It is used to convert this object to an intermediary representation during 
    251            serialization. It takes an `Encoder` argument that is used to recursively
    252            serialize inner data and structures (the `Encoder` provides standard methods
    253            for converting base types to dictionaries).. 
    254
    255            :param e: The `Encoder` that is being used.
    256            :return: A dictionary compliants to the Language Specification's serialization
    257            rules.
    258        """
    259     return int(self.value)
    260
    261 @classmethod
    262 def fromdict(cls, dic, e):
    263     """ Builds instance from dictionary 
    264
    265            It is used during deserialization to create an openc2lib instance from the text message.
    266            It takes an `Encoder` instance that is used to recursively build instances of the inner
    267            objects (the `Encoder` provides standard methods to create instances of base objects like
    268            strings, integers, boolean).
    269
    270            :param dic: The intermediary dictionary representation from which the object is built.
    271            :param e: The `Encoder that is being used.
    272            :return: An instance of this class initialized from the dictionary values.
    273        """
    274     try:
    275         return cls(int(dic))
    276     except:
    277         raise TypeError("Unexpected enum value: ", dic)
:::

::: docstring
OpenC2 EnumeratedID

Implements OpenC2 EnumeratedID:

> A set of unnamed integral constants. The API value is an id.

The current implementation does not check the values to be integer.
However, coversion to/from integer is explicitly done during the
intermediary dictionary serialization, hence throwing an Exception if
the IDs are not integers.
:::

:::::: {#EnumeratedID.todict .classattr}
::: {.attr .function}
[def]{.def} [todict]{.name}[([[self]{.bp},
]{.param}[[e]{.n}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
:::

[](#EnumeratedID.todict){.headerlink}

::: {.pdoc-code .codehilite}
    247  def todict(self, e):
    248       """ Converts to dictionary 
    249      
    250          It is used to convert this object to an intermediary representation during 
    251          serialization. It takes an `Encoder` argument that is used to recursively
    252          serialize inner data and structures (the `Encoder` provides standard methods
    253          for converting base types to dictionaries).. 
    254
    255          :param e: The `Encoder` that is being used.
    256          :return: A dictionary compliants to the Language Specification's serialization
    257          rules.
    258      """
    259       return int(self.value)
:::

::: docstring
Converts to dictionary

It is used to convert this object to an intermediary representation
during serialization. It takes an `Encoder` argument that is used to
recursively serialize inner data and structures (the `Encoder` provides
standard methods for converting base types to dictionaries)..

###### Parameters {#parameters}

-   **e**: The `Encoder` that is being used.

###### Returns {#returns}

> A dictionary compliants to the Language Specification\'s serialization
> rules.
:::
::::::

::::::: {#EnumeratedID.fromdict .classattr}
:::: {.attr .function}
::: decorator
\@classmethod
:::

[def]{.def} [fromdict]{.name}[([[cls]{.bp}, ]{.param}[[dic]{.n},
]{.param}[[e]{.n}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
::::

[](#EnumeratedID.fromdict){.headerlink}

::: {.pdoc-code .codehilite}
    261  @classmethod
    262   def fromdict(cls, dic, e):
    263       """ Builds instance from dictionary 
    264
    265          It is used during deserialization to create an openc2lib instance from the text message.
    266          It takes an `Encoder` instance that is used to recursively build instances of the inner
    267          objects (the `Encoder` provides standard methods to create instances of base objects like
    268          strings, integers, boolean).
    269
    270          :param dic: The intermediary dictionary representation from which the object is built.
    271          :param e: The `Encoder that is being used.
    272          :return: An instance of this class initialized from the dictionary values.
    273      """
    274       try:
    275           return cls(int(dic))
    276       except:
    277           raise TypeError("Unexpected enum value: ", dic)
:::

::: docstring
Builds instance from dictionary

It is used during deserialization to create an openc2lib instance from
the text message. It takes an `Encoder` instance that is used to
recursively build instances of the inner objects (the `Encoder` provides
standard methods to create instances of base objects like strings,
integers, boolean).

###### Parameters {#parameters}

-   **dic**: The intermediary dictionary representation from which the
    object is built.
-   **e**: The \`Encoder that is being used.

###### Returns {#returns}

> An instance of this class initialized from the dictionary values.
:::
:::::::

::: inherited
##### Inherited Members

aenum.\_enum.Enum
:   name
:   value
:   values
:::
::::::::::::::::

:::::::::::::::::: {#Array .section}
::: {.attr .class}
[class]{.def} [Array]{.name}([[Openc2Type](#Openc2Type)]{.base},
[builtins.list]{.base}): View Source
:::

[](#Array){.headerlink}

::: {.pdoc-code .codehilite}
    279class Array(Openc2Type, list):
    280   """ OpenC2 Array
    281
    282      Implements OpenC2 Array:
    283      >An ordered list of unnamed fields with positionally-defined semantics. 
    284      Each field has a position, label, and type.
    285
    286      However, position does not matter in this implementation.
    287
    288      Derived classes must provide a `fieldtypes` dictionary that associate each field name
    289      to its class. This is strictly required in order to instantiate the object at
    290      deserialization time. However, no check is performed when new items are inserted.
    291  """
    292   fieldtypes = None
    293   """ Field types
    294
    295      A `dictionary` which keys are field names and which values are the corresponding classes.
    296      Must be provided by any derived class.
    297  """
    298
    299   def todict(self, e):
    300       """ Converts to dictionary 
    301      
    302          It is used to convert this object to an intermediary representation during 
    303          serialization. It takes an `Encoder` argument that is used to recursively
    304          serialize inner data and structures (the `Encoder` provides standard methods
    305          for converting base types to dictionaries).. 
    306
    307          :param e: The `Encoder` that is being used.
    308          :return: A dictionary compliants to the Language Specification's serialization
    309          rules.
    310      """
    311       lis = []
    312       for i in self:
    313           lis.append = e.todict(i)
    314       return lis
    315
    316   def fromdict(cls, dic, e):
    317       """ !!! WARNING !!!
    318          Currently not implemented because there are no examples of usage of this
    319          type (only Array/net, which is not clear)
    320      """
    321       raise Exception("Function not implemented")
:::

::: docstring
OpenC2 Array

Implements OpenC2 Array:

> An ordered list of unnamed fields with positionally-defined semantics.
> Each field has a position, label, and type.

However, position does not matter in this implementation.

Derived classes must provide a [`fieldtypes`](#Array.fieldtypes)
dictionary that associate each field name to its class. This is strictly
required in order to instantiate the object at deserialization time.
However, no check is performed when new items are inserted.
:::

::::: {#Array.fieldtypes .classattr}
::: {.attr .variable}
[fieldtypes]{.name} = [None]{.default_value}
:::

[](#Array.fieldtypes){.headerlink}

::: docstring
Field types

A `dictionary` which keys are field names and which values are the
corresponding classes. Must be provided by any derived class.
:::
:::::

:::::: {#Array.todict .classattr}
::: {.attr .function}
[def]{.def} [todict]{.name}[([[self]{.bp},
]{.param}[[e]{.n}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
:::

[](#Array.todict){.headerlink}

::: {.pdoc-code .codehilite}
    299    def todict(self, e):
    300     """ Converts to dictionary 
    301        
    302            It is used to convert this object to an intermediary representation during 
    303            serialization. It takes an `Encoder` argument that is used to recursively
    304            serialize inner data and structures (the `Encoder` provides standard methods
    305            for converting base types to dictionaries).. 
    306
    307            :param e: The `Encoder` that is being used.
    308            :return: A dictionary compliants to the Language Specification's serialization
    309            rules.
    310        """
    311     lis = []
    312     for i in self:
    313         lis.append = e.todict(i)
    314     return lis
:::

::: docstring
Converts to dictionary

It is used to convert this object to an intermediary representation
during serialization. It takes an `Encoder` argument that is used to
recursively serialize inner data and structures (the `Encoder` provides
standard methods for converting base types to dictionaries)..

###### Parameters {#parameters}

-   **e**: The `Encoder` that is being used.

###### Returns {#returns}

> A dictionary compliants to the Language Specification\'s serialization
> rules.
:::
::::::

:::::: {#Array.fromdict .classattr}
::: {.attr .function}
[def]{.def} [fromdict]{.name}[([[cls]{.bp}, ]{.param}[[dic]{.n},
]{.param}[[e]{.n}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
:::

[](#Array.fromdict){.headerlink}

::: {.pdoc-code .codehilite}
    316    def fromdict(cls, dic, e):
    317     """ !!! WARNING !!!
    318            Currently not implemented because there are no examples of usage of this
    319            type (only Array/net, which is not clear)
    320        """
    321     raise Exception("Function not implemented")
:::

::: docstring
!!! WARNING !!! Currently not implemented because there are no examples
of usage of this type (only Array/net, which is not clear)
:::
::::::

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
:::
::::::::::::::::::

:::::::::: {#ArrayOf .section}
::: {.attr .class}
[class]{.def} [ArrayOf]{.name}: View Source
:::

[](#ArrayOf){.headerlink}

::: {.pdoc-code .codehilite}
    323class ArrayOf:
    324   """ OpenC2 ArrayOf
    325
    326      Implements OpenC2 ArrayOf(*vtype*):
    327      >An ordered list of fields with the same semantics. 
    328      Each field has a position and type *vtype*.
    329
    330      It extends the `Array` type. However, to make its usage simpler and compliant 
    331      to the description given in the
    332      Language Specification, the implementation is quite different.
    333      Note that in many cases `ArrayOf` is only used to create arrays without the need
    334      to derive an additional data type.
    335  """
    336
    337   def __new__(self, fldtype):
    338       """ `ArrayOf` builder
    339
    340          Creates a unnamed derived class from `Array`, which `fieldtypes` is set to `fldtype`.
    341          :param fldtype: The type of the fields stored in the array (indicated as *vtype* in 
    342                  the Language Specification.
    343          :return: A new unnamed class definition.
    344      """
    345       class ArrayOf(Array):
    346           """ OpenC2 unnamed `ArrayOf`
    347
    348              This class inherits from `Array` and sets its `fieldtypes` to a given type.
    349      
    350              One might like to check the type of the elements before inserting them.
    351              However, this is not the Python-way. Python use the duck typing approach:
    352              https://en.wikipedia.org/wiki/Duck_typing
    353              We ask for the type of objects just to keep this information according to
    354              the OpenC2 data model.
    355
    356              Note: no `todict()` method is provided, since `Array.todict()` is fine here.
    357          """
    358           fieldtype = fldtype
    359           """ The type of values stored in this container """
    360
    361           @classmethod
    362           def fromdict(cls, lis, e):
    363               """ Builds instance from dictionary 
    364      
    365                  It is used during deserialization to create an openc2lib instance from the text message.
    366                  It takes an `Encoder` instance that is used to recursively build instances of the inner
    367                  objects (the `Encoder` provides standard methods to create instances of base objects like
    368                  strings, integers, boolean).
    369      
    370                  :param lis: The intermediary dictionary representation from which the object is built.
    371                  :param e: The `Encoder that is being used.
    372                  :return: An instance of this class initialized from the dictionary values.
    373              """
    374               objlis = cls()
    375               logger.debug('Building %s from %s in ArrayOf', cls, lis)
    376               logger.debug('-> instantiating: %s', cls.fieldtype)
    377               for k in lis:
    378                   objlis.append(e.fromdict(cls.fieldtype, k))
    379       
    380               return objlis
    381           
    382           # This is the code if I would like to do type checking
    383           # when inserting data
    384#         def append(self, item):
    385#             if isinstance(item, self.fieldtype):
    386#                 super().append(item)
    387#             else:
    388#                 raise ValueError(self.fieldtype,' allowed only')
    389#         
    390#         def insert(self, index, item):
    391#             if isinstance(item, self.fieldtype):
    392#                 super().insert(index, item)
    393#             else:
    394#                 raise ValueError(self.fieldtype,' allowed only')
    395#         
    396#         def __add__(self, item):
    397#             if isinstance(item, self.fieldtype):
    398#                 super().__add__(item)
    399#             else:
    400#                 raise ValueError(self.fieldtype,' allowed only')
    401#         
    402#         def __iadd__(self, item):
    403#             if isinstance(item, self.fieldtype):
    404#                 super().__iadd__(item)
    405#             else:
    406#                 raise ValueError(self.fieldtype,' allowed only')
    407
    408       return ArrayOf
:::

::: docstring
OpenC2 ArrayOf

Implements OpenC2 ArrayOf(*vtype*):

> An ordered list of fields with the same semantics. Each field has a
> position and type *vtype*.

It extends the [`Array`](#Array) type. However, to make its usage
simpler and compliant to the description given in the Language
Specification, the implementation is quite different. Note that in many
cases [`ArrayOf`](#ArrayOf) is only used to create arrays without the
need to derive an additional data type.
:::

:::::: {#ArrayOf.__init__ .classattr}
::: {.attr .function}
[ArrayOf]{.name}[([[fldtype]{.n}]{.param})]{.signature .pdoc-code
.condensed} View Source
:::

[](#ArrayOf.__init__){.headerlink}

::: {.pdoc-code .codehilite}
    337    def __new__(self, fldtype):
    338     """ `ArrayOf` builder
    339
    340            Creates a unnamed derived class from `Array`, which `fieldtypes` is set to `fldtype`.
    341            :param fldtype: The type of the fields stored in the array (indicated as *vtype* in 
    342                    the Language Specification.
    343            :return: A new unnamed class definition.
    344        """
    345     class ArrayOf(Array):
    346         """ OpenC2 unnamed `ArrayOf`
    347
    348                This class inherits from `Array` and sets its `fieldtypes` to a given type.
    349        
    350                One might like to check the type of the elements before inserting them.
    351                However, this is not the Python-way. Python use the duck typing approach:
    352                https://en.wikipedia.org/wiki/Duck_typing
    353                We ask for the type of objects just to keep this information according to
    354                the OpenC2 data model.
    355
    356                Note: no `todict()` method is provided, since `Array.todict()` is fine here.
    357            """
    358         fieldtype = fldtype
    359         """ The type of values stored in this container """
    360
    361         @classmethod
    362         def fromdict(cls, lis, e):
    363             """ Builds instance from dictionary 
    364        
    365                    It is used during deserialization to create an openc2lib instance from the text message.
    366                    It takes an `Encoder` instance that is used to recursively build instances of the inner
    367                    objects (the `Encoder` provides standard methods to create instances of base objects like
    368                    strings, integers, boolean).
    369        
    370                    :param lis: The intermediary dictionary representation from which the object is built.
    371                    :param e: The `Encoder that is being used.
    372                    :return: An instance of this class initialized from the dictionary values.
    373                """
    374             objlis = cls()
    375             logger.debug('Building %s from %s in ArrayOf', cls, lis)
    376             logger.debug('-> instantiating: %s', cls.fieldtype)
    377             for k in lis:
    378                 objlis.append(e.fromdict(cls.fieldtype, k))
    379     
    380             return objlis
    381         
    382         # This is the code if I would like to do type checking
    383         # when inserting data
    384#           def append(self, item):
    385#               if isinstance(item, self.fieldtype):
    386#                   super().append(item)
    387#               else:
    388#                   raise ValueError(self.fieldtype,' allowed only')
    389#           
    390#           def insert(self, index, item):
    391#               if isinstance(item, self.fieldtype):
    392#                   super().insert(index, item)
    393#               else:
    394#                   raise ValueError(self.fieldtype,' allowed only')
    395#           
    396#           def __add__(self, item):
    397#               if isinstance(item, self.fieldtype):
    398#                   super().__add__(item)
    399#               else:
    400#                   raise ValueError(self.fieldtype,' allowed only')
    401#           
    402#           def __iadd__(self, item):
    403#               if isinstance(item, self.fieldtype):
    404#                   super().__iadd__(item)
    405#               else:
    406#                   raise ValueError(self.fieldtype,' allowed only')
    407
    408     return ArrayOf
:::

::: docstring
[`ArrayOf`](#ArrayOf) builder

Creates a unnamed derived class from [`Array`](#Array), which
`fieldtypes` is set to `fldtype`.

###### Parameters {#parameters}

-   **fldtype**: The type of the fields stored in the array (indicated
    as *vtype* in the Language Specification.

###### Returns {#returns}

> A new unnamed class definition.
:::
::::::
::::::::::

::::::::::::::::::::::::: {#Map .section}
::: {.attr .class}
[class]{.def} [Map]{.name}([[Openc2Type](#Openc2Type)]{.base},
[builtins.dict]{.base}): View Source
:::

[](#Map){.headerlink}

::: {.pdoc-code .codehilite}
    411class Map(Openc2Type, dict):
    412   """ OpenC2 Map
    413
    414      Implements OpenC2 Map:
    415      >An unordered map from a set of specified keys to values with semantics 
    416          bound to each key. Each field has an id, name and type.
    417
    418      However, the id is not considered in this implementation.
    419
    420      The implementation follows a similar logic than `Array`. Each derived class
    421      is expected to provide a `fieldtypes` class attribute that associate field names 
    422      with their class definition. 
    423      
    424      Additionally, according to the Language Specification, `Map`s may be extended by
    425      Profiles. Such extensions must use the `extend` and `regext` class attributes to 
    426      bind to the base element they extend and the `Profile` in which they are defined.
    427  """
    428   fieldtypes: dict = None
    429   """ Field types
    430
    431      A `dictionary` which keys are field names and which values are the corresponding classes.
    432      Must be provided by any derived class.
    433  """
    434   extend = None
    435   """ Base class
    436
    437      Data types defined in the Language Specification shall not set this field. Data types defined in
    438      Profiles that extends a Data Type defined in the Language Specification, must set this field to
    439      the corresponding class of the base Data Type.
    440
    441      Note: Extensions defined in the openc2lib context are recommended to use the same name of the base
    442      Data Type, and to distinguish them through appropriate usage of the namespacing mechanism.
    443  """
    444   regext = {}
    445   """ Registered extensions
    446
    447      Classes that implement a Data Type defined in the Language Specification will use this field to
    448      register extensions defined by external Profiles. Classes that define extensions within Profiles
    449      shall register themselves according to the specific documentation of the base type class, but 
    450      shall not modify this field.
    451  """
    452
    453   def todict(self, e):
    454       """ Converts to dictionary 
    455      
    456          It is used to convert this object to an intermediary representation during 
    457          serialization. It takes an `Encoder` argument that is used to recursively
    458          serialize inner data and structures (the `Encoder` provides standard methods
    459          for converting base types to dictionaries).. 
    460
    461          :param e: The `Encoder` that is being used.
    462          :return: A dictionary compliants to the Language Specification's serialization
    463          rules.
    464      """
    465       newdic=dict()
    466
    467       # This is necessary because self.extend.fieldtypes does
    468       # not exist for non-extended classes
    469       if self.extend is None:
    470           return e.todict(dict(self))
    471           
    472       for k,v in self.items():
    473           if k not in self.fieldtypes:
    474               raise ValueError('Unknown field: ', k)
    475           if k in self.extend.fieldtypes:
    476               newdic[k] = v
    477           else:
    478               if self.nsid not in newdic:
    479                   newdic[self.nsid]={}
    480               newdic[self.nsid][k]=v
    481           
    482       return e.todict(newdic)
    483
    484   @classmethod
    485   def fromdict(cls, dic, e):
    486       """ Builds instance from dictionary 
    487
    488          It is used during deserialization to create an openc2lib instance from the text message.
    489          It takes an `Encoder` instance that is used to recursively build instances of the inner
    490          objects (the `Encoder` provides standard methods to create instances of base objects like
    491          strings, integers, boolean).
    492
    493          :param dic: The intermediary dictionary representation from which the object is built.
    494          :param e: The `Encoder that is being used.
    495          :return: An instance of this class initialized from the dictionary values.
    496      """
    497       objdic = {}
    498       extension = None
    499       logger.debug('Building %s from %s in Map', cls, dic)
    500       for k,v in dic.items():
    501           if k in cls.fieldtypes:
    502               objdic[k] = e.fromdict(cls.fieldtypes[k], v)
    503           elif k in cls.regext:
    504               logger.debug('   Using profile %s to decode: %s', k, v)
    505               extension = cls.regext[k]
    506               for l,w in v.items():
    507                   objdic[l] = e.fromdict(extension.fieldtypes[l], w)
    508           else:
    509               raise TypeError("Unexpected field: ", k)
    510
    511       if extension is not None:
    512           cls = extension
    513
    514       return cls(objdic)
:::

::: docstring
OpenC2 Map

Implements OpenC2 Map:

> An unordered map from a set of specified keys to values with semantics
> bound to each key. Each field has an id, name and type.

However, the id is not considered in this implementation.

The implementation follows a similar logic than [`Array`](#Array). Each
derived class is expected to provide a [`fieldtypes`](#Map.fieldtypes)
class attribute that associate field names with their class definition.

Additionally, according to the Language Specification, [`Map`](#Map)s
may be extended by Profiles. Such extensions must use the
[`extend`](#Map.extend) and [`regext`](#Map.regext) class attributes to
bind to the base element they extend and the `Profile` in which they are
defined.
:::

::::: {#Map.fieldtypes .classattr}
::: {.attr .variable}
[fieldtypes]{.name}[: dict]{.annotation} = [None]{.default_value}
:::

[](#Map.fieldtypes){.headerlink}

::: docstring
Field types

A `dictionary` which keys are field names and which values are the
corresponding classes. Must be provided by any derived class.
:::
:::::

::::: {#Map.extend .classattr}
::: {.attr .variable}
[extend]{.name} = [None]{.default_value}
:::

[](#Map.extend){.headerlink}

::: docstring
Base class

Data types defined in the Language Specification shall not set this
field. Data types defined in Profiles that extends a Data Type defined
in the Language Specification, must set this field to the corresponding
class of the base Data Type.

Note: Extensions defined in the openc2lib context are recommended to use
the same name of the base Data Type, and to distinguish them through
appropriate usage of the namespacing mechanism.
:::
:::::

::::: {#Map.regext .classattr}
::: {.attr .variable}
[regext]{.name} = [{}]{.default_value}
:::

[](#Map.regext){.headerlink}

::: docstring
Registered extensions

Classes that implement a Data Type defined in the Language Specification
will use this field to register extensions defined by external Profiles.
Classes that define extensions within Profiles shall register themselves
according to the specific documentation of the base type class, but
shall not modify this field.
:::
:::::

:::::: {#Map.todict .classattr}
::: {.attr .function}
[def]{.def} [todict]{.name}[([[self]{.bp},
]{.param}[[e]{.n}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
:::

[](#Map.todict){.headerlink}

::: {.pdoc-code .codehilite}
    453    def todict(self, e):
    454     """ Converts to dictionary 
    455        
    456            It is used to convert this object to an intermediary representation during 
    457            serialization. It takes an `Encoder` argument that is used to recursively
    458            serialize inner data and structures (the `Encoder` provides standard methods
    459            for converting base types to dictionaries).. 
    460
    461            :param e: The `Encoder` that is being used.
    462            :return: A dictionary compliants to the Language Specification's serialization
    463            rules.
    464        """
    465     newdic=dict()
    466
    467     # This is necessary because self.extend.fieldtypes does
    468     # not exist for non-extended classes
    469     if self.extend is None:
    470         return e.todict(dict(self))
    471         
    472     for k,v in self.items():
    473         if k not in self.fieldtypes:
    474             raise ValueError('Unknown field: ', k)
    475         if k in self.extend.fieldtypes:
    476             newdic[k] = v
    477         else:
    478             if self.nsid not in newdic:
    479                 newdic[self.nsid]={}
    480             newdic[self.nsid][k]=v
    481         
    482     return e.todict(newdic)
:::

::: docstring
Converts to dictionary

It is used to convert this object to an intermediary representation
during serialization. It takes an `Encoder` argument that is used to
recursively serialize inner data and structures (the `Encoder` provides
standard methods for converting base types to dictionaries)..

###### Parameters {#parameters}

-   **e**: The `Encoder` that is being used.

###### Returns {#returns}

> A dictionary compliants to the Language Specification\'s serialization
> rules.
:::
::::::

::::::: {#Map.fromdict .classattr}
:::: {.attr .function}
::: decorator
\@classmethod
:::

[def]{.def} [fromdict]{.name}[([[cls]{.bp}, ]{.param}[[dic]{.n},
]{.param}[[e]{.n}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
::::

[](#Map.fromdict){.headerlink}

::: {.pdoc-code .codehilite}
    484    @classmethod
    485 def fromdict(cls, dic, e):
    486     """ Builds instance from dictionary 
    487
    488            It is used during deserialization to create an openc2lib instance from the text message.
    489            It takes an `Encoder` instance that is used to recursively build instances of the inner
    490            objects (the `Encoder` provides standard methods to create instances of base objects like
    491            strings, integers, boolean).
    492
    493            :param dic: The intermediary dictionary representation from which the object is built.
    494            :param e: The `Encoder that is being used.
    495            :return: An instance of this class initialized from the dictionary values.
    496        """
    497     objdic = {}
    498     extension = None
    499     logger.debug('Building %s from %s in Map', cls, dic)
    500     for k,v in dic.items():
    501         if k in cls.fieldtypes:
    502             objdic[k] = e.fromdict(cls.fieldtypes[k], v)
    503         elif k in cls.regext:
    504             logger.debug('   Using profile %s to decode: %s', k, v)
    505             extension = cls.regext[k]
    506             for l,w in v.items():
    507                 objdic[l] = e.fromdict(extension.fieldtypes[l], w)
    508         else:
    509             raise TypeError("Unexpected field: ", k)
    510
    511     if extension is not None:
    512         cls = extension
    513
    514     return cls(objdic)
:::

::: docstring
Builds instance from dictionary

It is used during deserialization to create an openc2lib instance from
the text message. It takes an `Encoder` instance that is used to
recursively build instances of the inner objects (the `Encoder` provides
standard methods to create instances of base objects like strings,
integers, boolean).

###### Parameters {#parameters}

-   **dic**: The intermediary dictionary representation from which the
    object is built.
-   **e**: The \`Encoder that is being used.

###### Returns {#returns}

> An instance of this class initialized from the dictionary values.
:::
:::::::

::: inherited
##### Inherited Members

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
:::::::::::::::::::::::::

:::::::::: {#MapOf .section}
::: {.attr .class}
[class]{.def} [MapOf]{.name}: View Source
:::

[](#MapOf){.headerlink}

::: {.pdoc-code .codehilite}
    516class MapOf:
    517   """ OpenC2 MapOf
    518
    519      Implements OpenC2 MapOf(*ktype, vtype*):
    520      >An unordered set of keys to values with the same semantics. 
    521          Each key has key type *ktype* and is mapped to value type *vtype*.
    522
    523      It extends `Map` with the same approach already used for `ArrayOf`.
    524      `MapOf` for specific types are created as anonymous classes by passing
    525      `ktype` and `vtype` as arguments.
    526
    527      Note: `MapOf` implementation currently does not support extensins!.
    528  """
    529
    530   def __new__(self,ktype, vtype):
    531       """ `MapOf` builder
    532
    533          Creates a unnamed derived class from `Map`, which `fieldtypes` is set to a single value
    534          `ktype: vtype`.
    535          :param ktype: The key type of the items stored in the map.
    536          :param vtype: The value type of the items stored in the map.
    537          :return: A new unnamed class definition.
    538      """
    539       class MapOf(Map):
    540           """ OpenC2 unnamed `MapOf`
    541
    542              This class inherits from `Map` and sets its `fieldtypes` to a given type.
    543      
    544              Note: no `todict()` method is provided, since `Map.todict()` is fine here.
    545          """
    546           fieldtypes = {ktype: vtype}
    547           """ The type of values stored in this container """
    548
    549           @classmethod
    550           def fromdict(cls, dic, e):
    551               """ Builds instance from dictionary 
    552      
    553                  It is used during deserialization to create an openc2lib instance from the text message.
    554                  It takes an `Encoder` instance that is used to recursively build instances of the inner
    555                  objects (the `Encoder` provides standard methods to create instances of base objects like
    556                  strings, integers, boolean).
    557      
    558                  :param dic: The intermediary dictionary representation from which the object is built.
    559                  :param e: The `Encoder that is being used.
    560                  :return: An instance of this class initialized from the dictionary values.
    561              """
    562               objdic = {}
    563               logger.debug('Building %s from %s in MapOf', cls, dic)
    564               for k,v in dic.items():
    565                   kclass = list(cls.fieldtypes)[0]
    566                   objk = e.fromdict(kclass, k)
    567                   objdic[objk] = e.fromdict(cls.fieldtypes[kclass], v)
    568               return objdic
    569
    570       return MapOf
:::

::: docstring
OpenC2 MapOf

Implements OpenC2 MapOf(*ktype, vtype*):

> An unordered set of keys to values with the same semantics. Each key
> has key type *ktype* and is mapped to value type *vtype*.

It extends [`Map`](#Map) with the same approach already used for
[`ArrayOf`](#ArrayOf). [`MapOf`](#MapOf) for specific types are created
as anonymous classes by passing `ktype` and `vtype` as arguments.

Note: [`MapOf`](#MapOf) implementation currently does not support
extensins!.
:::

:::::: {#MapOf.__init__ .classattr}
::: {.attr .function}
[MapOf]{.name}[([[ktype]{.n},
]{.param}[[vtype]{.n}]{.param})]{.signature .pdoc-code .condensed} View
Source
:::

[](#MapOf.__init__){.headerlink}

::: {.pdoc-code .codehilite}
    530    def __new__(self,ktype, vtype):
    531     """ `MapOf` builder
    532
    533            Creates a unnamed derived class from `Map`, which `fieldtypes` is set to a single value
    534            `ktype: vtype`.
    535            :param ktype: The key type of the items stored in the map.
    536            :param vtype: The value type of the items stored in the map.
    537            :return: A new unnamed class definition.
    538        """
    539     class MapOf(Map):
    540         """ OpenC2 unnamed `MapOf`
    541
    542                This class inherits from `Map` and sets its `fieldtypes` to a given type.
    543        
    544                Note: no `todict()` method is provided, since `Map.todict()` is fine here.
    545            """
    546         fieldtypes = {ktype: vtype}
    547         """ The type of values stored in this container """
    548
    549         @classmethod
    550         def fromdict(cls, dic, e):
    551             """ Builds instance from dictionary 
    552        
    553                    It is used during deserialization to create an openc2lib instance from the text message.
    554                    It takes an `Encoder` instance that is used to recursively build instances of the inner
    555                    objects (the `Encoder` provides standard methods to create instances of base objects like
    556                    strings, integers, boolean).
    557        
    558                    :param dic: The intermediary dictionary representation from which the object is built.
    559                    :param e: The `Encoder that is being used.
    560                    :return: An instance of this class initialized from the dictionary values.
    561                """
    562             objdic = {}
    563             logger.debug('Building %s from %s in MapOf', cls, dic)
    564             for k,v in dic.items():
    565                 kclass = list(cls.fieldtypes)[0]
    566                 objk = e.fromdict(kclass, k)
    567                 objdic[objk] = e.fromdict(cls.fieldtypes[kclass], v)
    568             return objdic
    569
    570     return MapOf
:::

::: docstring
[`MapOf`](#MapOf) builder

Creates a unnamed derived class from [`Map`](#Map), which `fieldtypes`
is set to a single value `ktype: vtype`.

###### Parameters {#parameters}

-   **ktype**: The key type of the items stored in the map.
-   **vtype**: The value type of the items stored in the map.

###### Returns {#returns}

> A new unnamed class definition.
:::
::::::
::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
