"""OpenC2 library

openc2lib provides an opensource implementation of the OpenC2 language and support for 
integration of encoding formats and protocol syntax.

All language elements are named according to the standard, with minor variations to
account for reserved keywords and characters.

All the target and data types defined by the standard are available for creating OpenC2 
commands.

This is the code documentation for using and extending open2lib.
Please read the [Getting started](https://github.com/mattereppe/openc2lib/blob/main/README.md#getting-started) 
guide, the quick start [Usage](https://github.com/mattereppe/openc2lib/blob/main/README.md#usage)  and the 
[Advanced usage](https://github.com/mattereppe/openc2lib/blob/main/README.md#advanced-usage) documentation for an overview of 
openc2lib operation. 

This documentation uses docstrings in the Python code. You can regenerate it by running 
`pdoc -o docs/code src/openc2lib`
or you can run your own websever with:
`pdoc src/openc2lib/`
(TODO: fix errors with the pdoc webserver).

"""


from openc2lib.types.base import Binary, Binaryx, Record, Choice, Enumerated, Array, ArrayOf, Map, MapOf
from openc2lib.types.data import Port, L4Protocol, DateTime, Duration, TargetEnum, Nsid, ActionTargets, ActionArguments, Version, ResponseType, Feature, Hashes, Payload, Hostname, IDNHostname
from openc2lib.types.targets import Artifact, CommandID, Device, DomainName, EmailAddr, Features, File, IDNDomainName, IDNEmailAddr, IPv4Net, IPv6Net, IPv4Connection, IPv6Connection, MACAddr, Process, URI, IRI, Properties

from openc2lib.core.actions import Actions
from openc2lib.core.producer import Producer
from openc2lib.core.consumer import Consumer
from openc2lib.core.message import Message
from openc2lib.core.content import MessageType, Content
from openc2lib.core.command import Command
from openc2lib.core.response import StatusCode, StatusCodeDescription, Response
from openc2lib.core.results import Results
from openc2lib.core.args import Args
from openc2lib.core.encoder import Encoder, Encoders, register_encoder, EncoderError
from openc2lib.core.transfer import Transfer
from openc2lib.core.profile import Profile
from openc2lib.core.target import target
from openc2lib.core.register import Register
from openc2lib.core.extensions import Extensions, extension
from openc2lib.core.actuator import actuator

from openc2lib.utils.log_formatting import LogFormatter
from openc2lib.utils.media_types import MediaTypes


