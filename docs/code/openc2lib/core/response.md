![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAzMCAzMCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLW1pdGVybGltaXQ9IjEwIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik00IDdoMjJNNCAxNWgyMk00IDIzaDIyIiAvPjwvc3ZnPg==)

<div>

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0iYmkgYmktYm94LWFycm93LWluLWxlZnQiIHZpZXdib3g9IjAgMCAxNiAxNiI+CiAgPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMTAgMy41YS41LjUgMCAwIDAtLjUtLjVoLThhLjUuNSAwIDAgMC0uNS41djlhLjUuNSAwIDAgMCAuNS41aDhhLjUuNSAwIDAgMCAuNS0uNXYtMmEuNS41IDAgMCAxIDEgMHYyQTEuNSAxLjUgMCAwIDEgOS41IDE0aC04QTEuNSAxLjUgMCAwIDEgMCAxMi41di05QTEuNSAxLjUgMCAwIDEgMS41IDJoOEExLjUgMS41IDAgMCAxIDExIDMuNXYyYS41LjUgMCAwIDEtMSAwdi0yeiIgLz4KICA8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00LjE0NiA4LjM1NGEuNS41IDAgMCAxIDAtLjcwOGwzLTNhLjUuNSAwIDEgMSAuNzA4LjcwOEw1LjcwNyA3LjVIMTQuNWEuNS41IDAgMCAxIDAgMUg1LjcwN2wyLjE0NyAyLjE0NmEuNS41IDAgMCAxLS43MDguNzA4bC0zLTN6IiAvPgo8L3N2Zz4=){.bi
.bi-box-arrow-in-left}  openc2lib.core](../core.html){.pdoc-button
.module-list-button}

## API Documentation

-   [StatusCode](#StatusCode){.class}
    -   [PROCESSING](#StatusCode.PROCESSING){.variable}
    -   [OK](#StatusCode.OK){.variable}
    -   [BADREQUEST](#StatusCode.BADREQUEST){.variable}
    -   [UNAUTHORIZED](#StatusCode.UNAUTHORIZED){.variable}
    -   [FORBIDDEN](#StatusCode.FORBIDDEN){.variable}
    -   [NOTFOUND](#StatusCode.NOTFOUND){.variable}
    -   [INTERNALERROR](#StatusCode.INTERNALERROR){.variable}
    -   [NOTIMPLEMENTED](#StatusCode.NOTIMPLEMENTED){.variable}
    -   [SERVICEUNAVAILABLE](#StatusCode.SERVICEUNAVAILABLE){.variable}
-   [StatusCodeDescription](#StatusCodeDescription){.variable}
-   [ExtResultsDict](#ExtResultsDict){.class}
    -   [add](#ExtResultsDict.add){.function}
-   [ExtendedResults](#ExtendedResults){.variable}
-   [Results](#Results){.class}
    -   [fieldtypes](#Results.fieldtypes){.variable}
    -   [extend](#Results.extend){.variable}
    -   [regext](#Results.regext){.variable}
    -   [set](#Results.set){.function}

[built with [pdoc]{.visually-hidden}![pdoc
logo](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20role%3D%22img%22%20aria-label%3D%22pdoc%20logo%22%20width%3D%22300%22%20height%3D%22150%22%20viewBox%3D%22-1%200%2060%2030%22%3E%3Ctitle%3Epdoc%3C/title%3E%3Cpath%20d%3D%22M29.621%2021.293c-.011-.273-.214-.475-.511-.481a.5.5%200%200%200-.489.503l-.044%201.393c-.097.551-.695%201.215-1.566%201.704-.577.428-1.306.486-2.193.182-1.426-.617-2.467-1.654-3.304-2.487l-.173-.172a3.43%203.43%200%200%200-.365-.306.49.49%200%200%200-.286-.196c-1.718-1.06-4.931-1.47-7.353.191l-.219.15c-1.707%201.187-3.413%202.131-4.328%201.03-.02-.027-.49-.685-.141-1.763.233-.721.546-2.408.772-4.076.042-.09.067-.187.046-.288.166-1.347.277-2.625.241-3.351%201.378-1.008%202.271-2.586%202.271-4.362%200-.976-.272-1.935-.788-2.774-.057-.094-.122-.18-.184-.268.033-.167.052-.339.052-.516%200-1.477-1.202-2.679-2.679-2.679-.791%200-1.496.352-1.987.9a6.3%206.3%200%200%200-1.001.029c-.492-.564-1.207-.929-2.012-.929-1.477%200-2.679%201.202-2.679%202.679A2.65%202.65%200%200%200%20.97%206.554c-.383.747-.595%201.572-.595%202.41%200%202.311%201.507%204.29%203.635%205.107-.037.699-.147%202.27-.423%203.294l-.137.461c-.622%202.042-2.515%208.257%201.727%2010.643%201.614.908%203.06%201.248%204.317%201.248%202.665%200%204.492-1.524%205.322-2.401%201.476-1.559%202.886-1.854%206.491.82%201.877%201.393%203.514%201.753%204.861%201.068%202.223-1.713%202.811-3.867%203.399-6.374.077-.846.056-1.469.054-1.537zm-4.835%204.313c-.054.305-.156.586-.242.629-.034-.007-.131-.022-.307-.157-.145-.111-.314-.478-.456-.908.221.121.432.25.675.355.115.039.219.051.33.081zm-2.251-1.238c-.05.33-.158.648-.252.694-.022.001-.125-.018-.307-.157-.217-.166-.488-.906-.639-1.573.358.344.754.693%201.198%201.036zm-3.887-2.337c-.006-.116-.018-.231-.041-.342.635.145%201.189.368%201.599.625.097.231.166.481.174.642-.03.049-.055.101-.067.158-.046.013-.128.026-.298.004-.278-.037-.901-.57-1.367-1.087zm-1.127-.497c.116.306.176.625.12.71-.019.014-.117.045-.345.016-.206-.027-.604-.332-.986-.695.41-.051.816-.056%201.211-.031zm-4.535%201.535c.209.22.379.47.358.598-.006.041-.088.138-.351.234-.144.055-.539-.063-.979-.259a11.66%2011.66%200%200%200%20.972-.573zm.983-.664c.359-.237.738-.418%201.126-.554.25.237.479.548.457.694-.006.042-.087.138-.351.235-.174.064-.694-.105-1.232-.375zm-3.381%201.794c-.022.145-.061.29-.149.401-.133.166-.358.248-.69.251h-.002c-.133%200-.306-.26-.45-.621.417.091.854.07%201.291-.031zm-2.066-8.077a4.78%204.78%200%200%201-.775-.584c.172-.115.505-.254.88-.378l-.105.962zm-.331%202.302a10.32%2010.32%200%200%201-.828-.502c.202-.143.576-.328.984-.49l-.156.992zm-.45%202.157l-.701-.403c.214-.115.536-.249.891-.376a11.57%2011.57%200%200%201-.19.779zm-.181%201.716c.064.398.194.702.298.893-.194-.051-.435-.162-.736-.398.061-.119.224-.3.438-.495zM8.87%204.141c0%20.152-.123.276-.276.276s-.275-.124-.275-.276.123-.276.276-.276.275.124.275.276zm-.735-.389a1.15%201.15%200%200%200-.314.783%201.16%201.16%200%200%200%201.162%201.162c.457%200%20.842-.27%201.032-.653.026.117.042.238.042.362a1.68%201.68%200%200%201-1.679%201.679%201.68%201.68%200%200%201-1.679-1.679c0-.843.626-1.535%201.436-1.654zM5.059%205.406A1.68%201.68%200%200%201%203.38%207.085a1.68%201.68%200%200%201-1.679-1.679c0-.037.009-.072.011-.109.21.3.541.508.935.508a1.16%201.16%200%200%200%201.162-1.162%201.14%201.14%200%200%200-.474-.912c.015%200%20.03-.005.045-.005.926.001%201.679.754%201.679%201.68zM3.198%204.141c0%20.152-.123.276-.276.276s-.275-.124-.275-.276.123-.276.276-.276.275.124.275.276zM1.375%208.964c0-.52.103-1.035.288-1.52.466.394%201.06.64%201.717.64%201.144%200%202.116-.725%202.499-1.738.383%201.012%201.355%201.738%202.499%201.738.867%200%201.631-.421%202.121-1.062.307.605.478%201.267.478%201.942%200%202.486-2.153%204.51-4.801%204.51s-4.801-2.023-4.801-4.51zm24.342%2019.349c-.985.498-2.267.168-3.813-.979-3.073-2.281-5.453-3.199-7.813-.705-1.315%201.391-4.163%203.365-8.423.97-3.174-1.786-2.239-6.266-1.261-9.479l.146-.492c.276-1.02.395-2.457.444-3.268a6.11%206.11%200%200%200%201.18.115%206.01%206.01%200%200%200%202.536-.562l-.006.175c-.802.215-1.848.612-2.021%201.25-.079.295.021.601.274.837.219.203.415.364.598.501-.667.304-1.243.698-1.311%201.179-.02.144-.022.507.393.787.213.144.395.26.564.365-1.285.521-1.361.96-1.381%201.126-.018.142-.011.496.427.746l.854.489c-.473.389-.971.914-.999%201.429-.018.278.095.532.316.713.675.556%201.231.721%201.653.721.059%200%20.104-.014.158-.02.207.707.641%201.64%201.513%201.64h.013c.8-.008%201.236-.345%201.462-.626.173-.216.268-.457.325-.692.424.195.93.374%201.372.374.151%200%20.294-.021.423-.068.732-.27.944-.704.993-1.021.009-.061.003-.119.002-.179.266.086.538.147.789.147.15%200%20.294-.021.423-.069.542-.2.797-.489.914-.754.237.147.478.258.704.288.106.014.205.021.296.021.356%200%20.595-.101.767-.229.438.435%201.094.992%201.656%201.067.106.014.205.021.296.021a1.56%201.56%200%200%200%20.323-.035c.17.575.453%201.289.866%201.605.358.273.665.362.914.362a.99.99%200%200%200%20.421-.093%201.03%201.03%200%200%200%20.245-.164c.168.428.39.846.68%201.068.358.273.665.362.913.362a.99.99%200%200%200%20.421-.093c.317-.148.512-.448.639-.762.251.157.495.257.726.257.127%200%20.25-.024.37-.071.427-.17.706-.617.841-1.314.022-.015.047-.022.068-.038.067-.051.133-.104.196-.159-.443%201.486-1.107%202.761-2.086%203.257zM8.66%209.925a.5.5%200%201%200-1%200c0%20.653-.818%201.205-1.787%201.205s-1.787-.552-1.787-1.205a.5.5%200%201%200-1%200c0%201.216%201.25%202.205%202.787%202.205s2.787-.989%202.787-2.205zm4.4%2015.965l-.208.097c-2.661%201.258-4.708%201.436-6.086.527-1.542-1.017-1.88-3.19-1.844-4.198a.4.4%200%200%200-.385-.414c-.242-.029-.406.164-.414.385-.046%201.249.367%203.686%202.202%204.896.708.467%201.547.7%202.51.7%201.248%200%202.706-.392%204.362-1.174l.185-.086a.4.4%200%200%200%20.205-.527c-.089-.204-.326-.291-.527-.206zM9.547%202.292c.093.077.205.114.317.114a.5.5%200%200%200%20.318-.886L8.817.397a.5.5%200%200%200-.703.068.5.5%200%200%200%20.069.703l1.364%201.124zm-7.661-.065c.086%200%20.173-.022.253-.068l1.523-.893a.5.5%200%200%200-.506-.863l-1.523.892a.5.5%200%200%200-.179.685c.094.158.261.247.432.247z%22%20transform%3D%22matrix%28-1%200%200%201%2058%200%29%22%20fill%3D%22%233bb300%22/%3E%3Cpath%20d%3D%22M.3%2021.86V10.18q0-.46.02-.68.04-.22.18-.5.28-.54%201.34-.54%201.06%200%201.42.28.38.26.44.78.76-1.04%202.38-1.04%201.64%200%203.1%201.54%201.46%201.54%201.46%203.58%200%202.04-1.46%203.58-1.44%201.54-3.08%201.54-1.64%200-2.38-.92v4.04q0%20.46-.04.68-.02.22-.18.5-.14.3-.5.42-.36.12-.98.12-.62%200-1-.12-.36-.12-.52-.4-.14-.28-.18-.5-.02-.22-.02-.68zm3.96-9.42q-.46.54-.46%201.18%200%20.64.46%201.18.48.52%201.2.52.74%200%201.24-.52.52-.52.52-1.18%200-.66-.48-1.18-.48-.54-1.26-.54-.76%200-1.22.54zm14.741-8.36q.16-.3.54-.42.38-.12%201-.12.64%200%201.02.12.38.12.52.42.16.3.18.54.04.22.04.68v11.94q0%20.46-.04.7-.02.22-.18.5-.3.54-1.7.54-1.38%200-1.54-.98-.84.96-2.34.96-1.8%200-3.28-1.56-1.48-1.58-1.48-3.66%200-2.1%201.48-3.68%201.5-1.58%203.28-1.58%201.48%200%202.3%201v-4.2q0-.46.02-.68.04-.24.18-.52zm-3.24%2010.86q.52.54%201.26.54.74%200%201.22-.54.5-.54.5-1.18%200-.66-.48-1.22-.46-.56-1.26-.56-.8%200-1.28.56-.48.54-.48%201.2%200%20.66.52%201.2zm7.833-1.2q0-2.4%201.68-3.96%201.68-1.56%203.84-1.56%202.16%200%203.82%201.56%201.66%201.54%201.66%203.94%200%201.66-.86%202.96-.86%201.28-2.1%201.9-1.22.6-2.54.6-1.32%200-2.56-.64-1.24-.66-2.1-1.92-.84-1.28-.84-2.88zm4.18%201.44q.64.48%201.3.48.66%200%201.32-.5.66-.5.66-1.48%200-.98-.62-1.46-.62-.48-1.34-.48-.72%200-1.34.5-.62.5-.62%201.48%200%20.96.64%201.46zm11.412-1.44q0%20.84.56%201.32.56.46%201.18.46.64%200%201.18-.36.56-.38.9-.38.6%200%201.46%201.06.46.58.46%201.04%200%20.76-1.1%201.42-1.14.8-2.8.8-1.86%200-3.58-1.34-.82-.64-1.34-1.7-.52-1.08-.52-2.36%200-1.3.52-2.34.52-1.06%201.34-1.7%201.66-1.32%203.54-1.32.76%200%201.48.22.72.2%201.06.4l.32.2q.36.24.56.38.52.4.52.92%200%20.5-.42%201.14-.72%201.1-1.38%201.1-.38%200-1.08-.44-.36-.34-1.04-.34-.66%200-1.24.48-.58.48-.58%201.34z%22%20fill%3D%22green%22/%3E%3C/svg%3E)](https://pdoc.dev "pdoc: Python API documentation generator"){.attribution
target="_blank"}

</div>

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.pdoc role="main"}
::::: {.section .module-info}
# [openc2lib](./../../openc2lib.html).[core](./../core.html).response {#openc2lib.core.response .modulename}

::: docstring
OpenC2 Response elements

This module defines the elements beard by a `Response`.
:::

View Source

::: {.pdoc-code .codehilite}
      1""" OpenC2 Response elements
      2
      3  This module defines the elements beard by a `Response`.
      4"""
      5from openc2lib.types.basetypes import EnumeratedID, Map, ArrayOf
      6from openc2lib.types.datatypes import Version, ActionTargets, Nsid
      7
      8class StatusCode(EnumeratedID):
      9   """ Status codes
     10
     11        Status codes provide indication about the processing of the OpenC2 Command.
     12        They follow the same logic and values of HTTP status code, since they are copied
     13        in HTTP headers.
     14"""
     15 PROCESSING = 102
     16 OK = 200
     17 BADREQUEST = 400
     18 UNAUTHORIZED = 401
     19 FORBIDDEN = 403
     20 NOTFOUND = 404
     21 INTERNALERROR =500
     22 NOTIMPLEMENTED = 501
     23 SERVICEUNAVAILABLE = 503
     24
     25StatusCodeDescription = {StatusCode.PROCESSING: 'Processing', 
     26                                     StatusCode.OK: 'OK',
     27                                     StatusCode.BADREQUEST: 'Bad Request',
     28                                     StatusCode.UNAUTHORIZED: 'Unauthorized',
     29                                     StatusCode.FORBIDDEN: 'Forbidden',
     30                                     StatusCode.NOTFOUND: 'Not Found',
     31                                     StatusCode.INTERNALERROR: 'Internal Error',
     32                                     StatusCode.NOTIMPLEMENTED: 'Not Implemented',
     33                                     StatusCode.SERVICEUNAVAILABLE: 'Service Unavailable'}
     34""" Status code description
     35
     36    Human-readable description of `StatusCode`s. The values are only provided as base values, since any `Actuator`
     37    can freely use different descriptions.
     38"""
     39
     40class ExtResultsDict(dict):
     41 """ Extended Results
     42
     43        This class is used to extend the basic `Results` definition. If follows the same logic as 
     44        other extended class in the openc2lib. 
     45    """
     46 def add(self, profile: str, extresults):
     47     """ Add extension
     48
     49            Add a new extension for a given `Profile`. The extension must be registered only once.
     50            :param profile: The name of the profile for which the extension is registered.
     51            :param extresults: The Extension to be registered.
     52            :return: None
     53        """
     54     if profile in self:
     55         raise ValueError("ExtResults already registered")
     56     self[profile] = extresults
     57 
     58ExtendedResults = ExtResultsDict()
     59""" List of Extended Results
     60
     61    List of registered extensions to `Results`. It is only used internally the openc2lib to correctly
     62    parse incoming Rensponses.
     63"""
     64
     65class Results(Map):
     66 """ OpenC2 Response Results
     67
     68        This class implements the definition in Sec. 3.3.2.2 of the Language Specification. The `Results` carry
     69        the output of an OpenC2 Command. This definition only includes basic fields and it is expected to
     70        be extended for each `Profile`.
     71
     72        Extensions must be derived class that define the following member:
     73            - `fieldtypes`
     74            - `extend`
     75            - `nsid`
     76        `nsid` must be set to the profile name.
     77    """
     78 fieldtypes = dict(versions= ArrayOf(Version), profiles= ArrayOf(Nsid), pairs= ActionTargets, rate_limit= int)
     79 """ Field types
     80    
     81        This is the definition of the fields beard by the `Results`. This definition is for internal use only,
     82        to parse OpenC2 messages. Extensions must include these fields and add additional definitions.
     83    """
     84 extend = None
     85 """ Extension
     86
     87        This field must be set to None in the base class, and to `Results` in the derived class that defines an extension.
     88    """
     89 regext = ExtendedResults
     90 """ Extended NameSpace
     91
     92        This field is for internal use only and must not be set by any derived class.
     93    """
     94
     95 def set(self, version=None, profiles=None, pairs=None, rate_limit=None):
     96     """ Set values
     97
     98            This function may be used to set specific values of the `Results`, with a key=value syntax.
     99            :param version: List of OpenC2 Versions supported by the Actuator.
    100          :param profiles: List of OpenC2 Profiles supported by the Actuator.
    101          :param pairs: List of `Targets` applicable to each supported `Action`.
    102          :param rate_limit: Maximum number of requests per minute supported by design or policy.
    103          :return: None
    104      """
    105       self['version']=version
    106       self['profiles']=profiles
    107       self['pairs']=pairs
    108       self['rate_limit']=rate_limit
:::
:::::

::::::::::::::::::::::::: {#StatusCode .section}
::: {.attr .class}
[class]{.def}
[StatusCode]{.name}([[openc2lib.types.basetypes.EnumeratedID](../types/basetypes.html#EnumeratedID)]{.base}):
View Source
:::

[](#StatusCode){.headerlink}

::: {.pdoc-code .codehilite}
     9class StatusCode(EnumeratedID):
    10    """ Status codes
    11
    12       Status codes provide indication about the processing of the OpenC2 Command.
    13       They follow the same logic and values of HTTP status code, since they are copied
    14       in HTTP headers.
    15"""
    16    PROCESSING = 102
    17    OK = 200
    18    BADREQUEST = 400
    19    UNAUTHORIZED = 401
    20    FORBIDDEN = 403
    21    NOTFOUND = 404
    22    INTERNALERROR =500
    23    NOTIMPLEMENTED = 501
    24    SERVICEUNAVAILABLE = 503
:::

::: docstring
Status codes

Status codes provide indication about the processing of the OpenC2
Command. They follow the same logic and values of HTTP status code,
since they are copied in HTTP headers.
:::

:::: {#StatusCode.PROCESSING .classattr}
::: {.attr .variable}
[PROCESSING]{.name} =
[\<[StatusCode.PROCESSING](#StatusCode.PROCESSING):
102\>]{.default_value}
:::

[](#StatusCode.PROCESSING){.headerlink}
::::

:::: {#StatusCode.OK .classattr}
::: {.attr .variable}
[OK]{.name} = [\<[StatusCode.OK](#StatusCode.OK): 200\>]{.default_value}
:::

[](#StatusCode.OK){.headerlink}
::::

:::: {#StatusCode.BADREQUEST .classattr}
::: {.attr .variable}
[BADREQUEST]{.name} =
[\<[StatusCode.BADREQUEST](#StatusCode.BADREQUEST):
400\>]{.default_value}
:::

[](#StatusCode.BADREQUEST){.headerlink}
::::

:::: {#StatusCode.UNAUTHORIZED .classattr}
::: {.attr .variable}
[UNAUTHORIZED]{.name} =
[\<[StatusCode.UNAUTHORIZED](#StatusCode.UNAUTHORIZED):
401\>]{.default_value}
:::

[](#StatusCode.UNAUTHORIZED){.headerlink}
::::

:::: {#StatusCode.FORBIDDEN .classattr}
::: {.attr .variable}
[FORBIDDEN]{.name} = [\<[StatusCode.FORBIDDEN](#StatusCode.FORBIDDEN):
403\>]{.default_value}
:::

[](#StatusCode.FORBIDDEN){.headerlink}
::::

:::: {#StatusCode.NOTFOUND .classattr}
::: {.attr .variable}
[NOTFOUND]{.name} = [\<[StatusCode.NOTFOUND](#StatusCode.NOTFOUND):
404\>]{.default_value}
:::

[](#StatusCode.NOTFOUND){.headerlink}
::::

:::: {#StatusCode.INTERNALERROR .classattr}
::: {.attr .variable}
[INTERNALERROR]{.name} =
[\<[StatusCode.INTERNALERROR](#StatusCode.INTERNALERROR):
500\>]{.default_value}
:::

[](#StatusCode.INTERNALERROR){.headerlink}
::::

:::: {#StatusCode.NOTIMPLEMENTED .classattr}
::: {.attr .variable}
[NOTIMPLEMENTED]{.name} =
[\<[StatusCode.NOTIMPLEMENTED](#StatusCode.NOTIMPLEMENTED):
501\>]{.default_value}
:::

[](#StatusCode.NOTIMPLEMENTED){.headerlink}
::::

:::: {#StatusCode.SERVICEUNAVAILABLE .classattr}
::: {.attr .variable}
[SERVICEUNAVAILABLE]{.name} =
[\<[StatusCode.SERVICEUNAVAILABLE](#StatusCode.SERVICEUNAVAILABLE):
503\>]{.default_value}
:::

[](#StatusCode.SERVICEUNAVAILABLE){.headerlink}
::::

::: inherited
##### Inherited Members

[openc2lib.types.basetypes.EnumeratedID](../types/basetypes.html#EnumeratedID)
:   [todict](../types/basetypes.html#EnumeratedID.todict)
:   [fromdict](../types/basetypes.html#EnumeratedID.fromdict)

aenum.\_enum.Enum
:   name
:   value
:   values
:::
:::::::::::::::::::::::::

::::: {#StatusCodeDescription .section}
::: {.attr .variable}
[StatusCodeDescription]{.name} =

[{\<[StatusCode.PROCESSING](#StatusCode.PROCESSING): 102\>:
\'Processing\', \<[StatusCode.OK](#StatusCode.OK): 200\>: \'OK\',
\<[StatusCode.BADREQUEST](#StatusCode.BADREQUEST): 400\>: \'Bad
Request\', \<[StatusCode.UNAUTHORIZED](#StatusCode.UNAUTHORIZED): 401\>:
\'Unauthorized\', \<[StatusCode.FORBIDDEN](#StatusCode.FORBIDDEN):
403\>: \'Forbidden\', \<[StatusCode.NOTFOUND](#StatusCode.NOTFOUND):
404\>: \'Not Found\',
\<[StatusCode.INTERNALERROR](#StatusCode.INTERNALERROR): 500\>:
\'Internal Error\',
\<[StatusCode.NOTIMPLEMENTED](#StatusCode.NOTIMPLEMENTED): 501\>: \'Not
Implemented\',
\<[StatusCode.SERVICEUNAVAILABLE](#StatusCode.SERVICEUNAVAILABLE):
503\>: \'Service Unavailable\'}]{.default_value}
:::

[](#StatusCodeDescription){.headerlink}

::: docstring
Status code description

Human-readable description of [`StatusCode`](#StatusCode)s. The values
are only provided as base values, since any `Actuator` can freely use
different descriptions.
:::
:::::

::::::::::: {#ExtResultsDict .section}
::: {.attr .class}
[class]{.def} [ExtResultsDict]{.name}([builtins.dict]{.base}): View
Source
:::

[](#ExtResultsDict){.headerlink}

::: {.pdoc-code .codehilite}
    41class ExtResultsDict(dict):
    42    """ Extended Results
    43
    44       This class is used to extend the basic `Results` definition. If follows the same logic as 
    45       other extended class in the openc2lib. 
    46   """
    47    def add(self, profile: str, extresults):
    48        """ Add extension
    49
    50           Add a new extension for a given `Profile`. The extension must be registered only once.
    51           :param profile: The name of the profile for which the extension is registered.
    52           :param extresults: The Extension to be registered.
    53           :return: None
    54       """
    55        if profile in self:
    56            raise ValueError("ExtResults already registered")
    57        self[profile] = extresults
:::

::: docstring
Extended Results

This class is used to extend the basic [`Results`](#Results) definition.
If follows the same logic as other extended class in the openc2lib.
:::

:::::: {#ExtResultsDict.add .classattr}
::: {.attr .function}
[def]{.def} [add]{.name}[([[self]{.bp}, ]{.param}[[profile]{.n}[:]{.p}
[str]{.nb},
]{.param}[[extresults]{.n}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
:::

[](#ExtResultsDict.add){.headerlink}

::: {.pdoc-code .codehilite}
    47   def add(self, profile: str, extresults):
    48        """ Add extension
    49
    50           Add a new extension for a given `Profile`. The extension must be registered only once.
    51           :param profile: The name of the profile for which the extension is registered.
    52           :param extresults: The Extension to be registered.
    53           :return: None
    54       """
    55        if profile in self:
    56            raise ValueError("ExtResults already registered")
    57        self[profile] = extresults
:::

::: docstring
Add extension

Add a new extension for a given `Profile`. The extension must be
registered only once.

###### Parameters

-   **profile**: The name of the profile for which the extension is
    registered.
-   **extresults**: The Extension to be registered.

###### Returns

> None
:::
::::::

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
:::::::::::

::::: {#ExtendedResults .section}
::: {.attr .variable}
[ExtendedResults]{.name} = [{\'slpf\': \<class
\'[openc2lib.profiles.slpf.response.Results](../profiles/slpf/response.html#Results)\'\>}]{.default_value}
:::

[](#ExtendedResults){.headerlink}

::: docstring
List of Extended Results

List of registered extensions to [`Results`](#Results). It is only used
internally the openc2lib to correctly parse incoming Rensponses.
:::
:::::

:::::::::::::::::::: {#Results .section}
::: {.attr .class}
[class]{.def}
[Results]{.name}([[openc2lib.types.basetypes.Map](../types/basetypes.html#Map)]{.base}):
View Source
:::

[](#Results){.headerlink}

::: {.pdoc-code .codehilite}
     66class Results(Map):
     67 """ OpenC2 Response Results
     68
     69        This class implements the definition in Sec. 3.3.2.2 of the Language Specification. The `Results` carry
     70        the output of an OpenC2 Command. This definition only includes basic fields and it is expected to
     71        be extended for each `Profile`.
     72
     73        Extensions must be derived class that define the following member:
     74            - `fieldtypes`
     75            - `extend`
     76            - `nsid`
     77        `nsid` must be set to the profile name.
     78    """
     79 fieldtypes = dict(versions= ArrayOf(Version), profiles= ArrayOf(Nsid), pairs= ActionTargets, rate_limit= int)
     80 """ Field types
     81    
     82        This is the definition of the fields beard by the `Results`. This definition is for internal use only,
     83        to parse OpenC2 messages. Extensions must include these fields and add additional definitions.
     84    """
     85 extend = None
     86 """ Extension
     87
     88        This field must be set to None in the base class, and to `Results` in the derived class that defines an extension.
     89    """
     90 regext = ExtendedResults
     91 """ Extended NameSpace
     92
     93        This field is for internal use only and must not be set by any derived class.
     94    """
     95
     96 def set(self, version=None, profiles=None, pairs=None, rate_limit=None):
     97     """ Set values
     98
     99            This function may be used to set specific values of the `Results`, with a key=value syntax.
    100          :param version: List of OpenC2 Versions supported by the Actuator.
    101          :param profiles: List of OpenC2 Profiles supported by the Actuator.
    102          :param pairs: List of `Targets` applicable to each supported `Action`.
    103          :param rate_limit: Maximum number of requests per minute supported by design or policy.
    104          :return: None
    105      """
    106       self['version']=version
    107       self['profiles']=profiles
    108       self['pairs']=pairs
    109       self['rate_limit']=rate_limit
:::

::: docstring
OpenC2 Response Results

This class implements the definition in Sec. 3.3.2.2 of the Language
Specification. The [`Results`](#Results) carry the output of an OpenC2
Command. This definition only includes basic fields and it is expected
to be extended for each `Profile`.

Extensions must be derived class that define the following member: -
[`fieldtypes`](#Results.fieldtypes) - [`extend`](#Results.extend) -
`nsid` `nsid` must be set to the profile name.
:::

::::: {#Results.fieldtypes .classattr}
::: {.attr .variable}
[fieldtypes]{.name} =

[{\'versions\': \<class
\'openc2lib.types.basetypes.ArrayOf.\_\_new\_\_.\<locals\>.ArrayOf\'\>,
\'profiles\': \<class
\'openc2lib.types.basetypes.ArrayOf.\_\_new\_\_.\<locals\>.ArrayOf\'\>,
\'pairs\': \<class
\'[openc2lib.types.datatypes.ActionTargets](../types/datatypes.html#ActionTargets)\'\>,
\'rate_limit\': \<class \'int\'\>}]{.default_value}
:::

[](#Results.fieldtypes){.headerlink}

::: docstring
Field types

This is the definition of the fields beard by the [`Results`](#Results).
This definition is for internal use only, to parse OpenC2 messages.
Extensions must include these fields and add additional definitions.
:::
:::::

::::: {#Results.extend .classattr}
::: {.attr .variable}
[extend]{.name} = [None]{.default_value}
:::

[](#Results.extend){.headerlink}

::: docstring
Extension

This field must be set to None in the base class, and to
[`Results`](#Results) in the derived class that defines an extension.
:::
:::::

::::: {#Results.regext .classattr}
::: {.attr .variable}
[regext]{.name} = [{\'slpf\': \<class
\'[openc2lib.profiles.slpf.response.Results](../profiles/slpf/response.html#Results)\'\>}]{.default_value}
:::

[](#Results.regext){.headerlink}

::: docstring
Extended NameSpace

This field is for internal use only and must not be set by any derived
class.
:::
:::::

:::::: {#Results.set .classattr}
::: {.attr .function}
[def]{.def} [set]{.name}[([[self]{.bp},
]{.param}[[version]{.n}[=]{.o}[None]{.kc},
]{.param}[[profiles]{.n}[=]{.o}[None]{.kc},
]{.param}[[pairs]{.n}[=]{.o}[None]{.kc},
]{.param}[[rate_limit]{.n}[=]{.o}[None]{.kc}]{.param}[):]{.return-annotation}]{.signature
.pdoc-code .condensed} View Source
:::

[](#Results.set){.headerlink}

::: {.pdoc-code .codehilite}
     96    def set(self, version=None, profiles=None, pairs=None, rate_limit=None):
     97     """ Set values
     98
     99            This function may be used to set specific values of the `Results`, with a key=value syntax.
    100          :param version: List of OpenC2 Versions supported by the Actuator.
    101          :param profiles: List of OpenC2 Profiles supported by the Actuator.
    102          :param pairs: List of `Targets` applicable to each supported `Action`.
    103          :param rate_limit: Maximum number of requests per minute supported by design or policy.
    104          :return: None
    105      """
    106       self['version']=version
    107       self['profiles']=profiles
    108       self['pairs']=pairs
    109       self['rate_limit']=rate_limit
:::

::: docstring
Set values

This function may be used to set specific values of the
[`Results`](#Results), with a key=value syntax.

###### Parameters {#parameters}

-   **version**: List of OpenC2 Versions supported by the Actuator.
-   **profiles**: List of OpenC2 Profiles supported by the Actuator.
-   **pairs**: List of `Targets` applicable to each supported `Action`.
-   **rate_limit**: Maximum number of requests per minute supported by
    design or policy.

###### Returns {#returns}

> None
:::
::::::

::: inherited
##### Inherited Members

[openc2lib.types.basetypes.Map](../types/basetypes.html#Map)
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
::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
