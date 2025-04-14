""" OpenC2 data types

	Definition of the data types in the OpenC2 DataModels (Sec. 3.4.2).
	The naming strictly follows the definition of the Language Specification
	as close as possible. The relevant exception is represented by hyphens
	that are always dropped.
"""

import aenum
import dataclasses


from otupy.types.data.ipv4_addr import IPv4Addr
from otupy.types.data.ipv6_addr import IPv6Addr
from otupy.types.data.port import Port
from otupy.types.data.l4_protocol import L4Protocol
from otupy.types.data.datetime import DateTime
from otupy.types.data.duration import Duration
from otupy.types.data.version import Version
from otupy.types.data.feature import Feature
from otupy.types.data.nsid import Nsid
from otupy.types.data.response_type import ResponseType
from otupy.types.data.target_enum import TargetEnum
from otupy.types.data.action_targets import ActionTargets
from otupy.types.data.action_arguments import ActionArguments
from otupy.types.data.payload import Payload
from otupy.types.data.hashes import Hashes
from otupy.types.data.uri import URI
from otupy.types.data.hostname import Hostname
from otupy.types.data.idn_hostname import IDNHostname
from otupy.types.data.command_id import CommandID

import otupy.types.data.mime_types
		
