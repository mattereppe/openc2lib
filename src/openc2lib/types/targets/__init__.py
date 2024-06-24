""" OpenC2 target types

	Definition of the target types in the OpenC2 (Sec. 3.4.1).
	The naming strictly follows the definition of the Language Specification
	as close as possible. The relevant exception is represented by hyphens
	that are always dropped.
"""


from openc2lib.core.target import Targets

from openc2lib.types.targets.artifact import Artifact
from openc2lib.types.data.command_id import CommandID
from openc2lib.types.targets.device import Device
from openc2lib.types.targets.domain_name import DomainName
from openc2lib.types.targets.email_addr import EmailAddr
from openc2lib.types.targets.features import Features
from openc2lib.types.targets.file import File
from openc2lib.types.targets.idn_domain_name import IDNDomainName
from openc2lib.types.targets.idn_email_addr import IDNEmailAddr
from openc2lib.types.targets.ipv4_net import IPv4Net
from openc2lib.types.targets.ipv6_net import IPv6Net
from openc2lib.types.targets.ipv4_connection import IPv4Connection
from openc2lib.types.targets.ipv6_connection import IPv6Connection
from openc2lib.types.targets.mac_addr import MACAddr
from openc2lib.types.targets.process import Process
from openc2lib.types.targets.uri import URI
from openc2lib.types.targets.iri import IRI
from openc2lib.types.targets.properties import Properties



# Register the list of available Targets
Targets.add('artifact', Artifact, 1)
Targets.add('command', CommandID, 2)
Targets.add('device', Device, 3)
Targets.add('domain_name', DomainName, 7)
Targets.add('email_addr', EmailAddr, 8)
Targets.add('features', Features, 9)
Targets.add('file', File, 10)
Targets.add('idn_domain_name', IDNDomainName, 11)
Targets.add('idn_email_addr', IDNEmailAddr, 12)
Targets.add('ipv4_net', IPv4Net, 13)
Targets.add('ipv6_net', IPv6Net, 14)
Targets.add('ipv4_connection', IPv4Connection, 15)
Targets.add('ipv6_connection', IPv6Connection, 16)
Targets.add('mac_addr', MACAddr, 17)
Targets.add('process', Process, 18)
Targets.add('uri', URI, 19)
Targets.add('iri', IRI, 20)
Targets.add('properties', Properties, 25)

