"""

otupy provides an opensource implementation of the OpenC2 language and support for 
integration of encoding formats and protocol syntax.

All language elements are named according to the standard, with minor variations to
account for reserved keywords and characters.

All the target and data types defined by the standard are available for creating OpenC2 
commands.

This is the code documentation for using and extending open2lib.
Please read the the quick start (:doc:`usage`)  and the advanced documentation (:doc:`developerguide`) 
for an overview of otupy operation. 

This documentation uses docstrings in the Python code. You can regenerate it by running 

.. code-block:: python3

	pdoc -o docs/code src/otupy

or you can run your own websever with:
.. code-block:: python3

	pdoc src/otupy/

(TODO: fix errors with the pdoc webserver).

"""


from otupy.types.base import Binary, Binaryx, Record, Choice, Enumerated, Array, ArrayOf, Map, MapOf
from otupy.types.data import Port, L4Protocol, DateTime, Duration, TargetEnum, Nsid, ActionTargets, ActionArguments, Version, ResponseType, Feature, Hashes, Payload, Hostname, IDNHostname
from otupy.types.targets import Artifact, CommandID, Device, DomainName, EmailAddr, Features, File, IDNDomainName, IDNEmailAddr, IPv4Net, IPv6Net, IPv4Connection, IPv6Connection, MACAddr, Process, URI, IRI, Properties

from otupy.core.actions import Actions
from otupy.core.actuator import Actuator
from otupy.core.producer import Producer
from otupy.core.consumer import Consumer
from otupy.core.message import Message
from otupy.core.content import MessageType, Content
from otupy.core.command import Command
from otupy.core.response import StatusCode, StatusCodeDescription, Response
from otupy.core.results import Results
from otupy.core.args import Args
from otupy.core.encoder import Encoder, Encoders, register_encoder, EncoderError
from otupy.core.transfer import Transfer
from otupy.core.profile import Profile
from otupy.core.target import target
from otupy.core.register import Register
from otupy.core.extensions import Extensions, extension
from otupy.core.actuator import actuator

from otupy.utils.log_formatting import LogFormatter
from otupy.utils.media_types import MediaTypes


