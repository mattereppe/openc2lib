""" OpenC2 target types

	Definition of the target types in the OpenC2 (Sec. 3.4.1).
	The naming strictly follows the definition of the Language Specification
	as close as possible. The relevant exception is represented by hyphens
	that are always dropped.
"""


from otupy.types.targets.artifact import Artifact
from otupy.types.data.command_id import CommandID
from otupy.types.targets.device import Device
from otupy.types.targets.domain_name import DomainName
from otupy.types.targets.email_addr import EmailAddr
from otupy.types.targets.features import Features
from otupy.types.targets.file import File
from otupy.types.targets.idn_domain_name import IDNDomainName
from otupy.types.targets.idn_email_addr import IDNEmailAddr
from otupy.types.targets.ipv4_net import IPv4Net
from otupy.types.targets.ipv6_net import IPv6Net
from otupy.types.targets.ipv4_connection import IPv4Connection
from otupy.types.targets.ipv6_connection import IPv6Connection
from otupy.types.targets.mac_addr import MACAddr
from otupy.types.targets.process import Process
from otupy.types.targets.uri import URI
from otupy.types.targets.iri import IRI
from otupy.types.targets.properties import Properties

