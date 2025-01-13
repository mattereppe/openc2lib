import pytest
import openc2

import sys
sys.path.insert(0, "../profiles/")

@pytest.fixture
def action_notarget():
	return openc2.v10.Command(action="stop")

@pytest.fixture
def action_notarget_id():
	return openc2.v10.Command(action="stop", command_id="CB1BCDEE-C7B4-40B7-9128-64DB2B877C32")

@pytest.fixture
def allow_ipv4_net_badcidr():
	return openc2.v10.Command(action="allow", target=openc2.v10.IPv4Address(ipv4_net="127.0.0.1/64"))

@pytest.fixture
def allow_ipv4_net_badip():
	return openc2.v10.Command(action="allow", target=openc2.v10.IPv4Address(ipv4_net="127.0.0.300"))

@pytest.fixture
def allow_ipv4_net_cidr():
	return openc2.v10.Command(action="allow", target=openc2.v10.IPv4Address(ipv4_net="127.0.0.1/8"))

@pytest.fixture
def allow_ipv6_net_prefix():
	return openc2.v10.Command(action="allow", target=openc2.v10.IPv6Address(ipv6_net="3ffe:1900:4545:3:200:f8ff:fe21:67cf/64"))

@pytest.fixture
def allow_ipv6_net_wikipedia3():
	return openc2.v10.Command(action="allow", target=openc2.v10.IPv6Address(ipv6_net="2001::85a3::8a2e:370:7334"))

@pytest.fixture
def allow_ipv6_net_wikipedia8_prefix2():
	return openc2.v10.Command(action="allow", target=openc2.v10.IPv6Address(ipv6_net="2001:db8:a::123/64"))

@pytest.fixture
def deny_file_hashes_empty():
	return openc2.v10.Command(action="deny", target=openc2.v10.File(hashes=openc2.properties.HashesProperty()))

@pytest.fixture
def deny_file_hashes_sha512():
	return openc2.v10.Command(action="deny", target=openc2.v10.File({'hashes': openc2.properties.HashesProperty(**{'sha512': "96b74959340df1680ea15d9f66a907e0bf55f059e2e4184190aa1271021003bcefd02a9f924164b22954b54fc0fff36a68eae36d189173ca2df30fa4b1535700"})}))

@pytest.fixture
def deny_uri_actuator_empty():
	return openc2.v10.Command(action="deny", target=openc2.v10.URI("https://example.com"), actuator=openc2.v10.Actuator())

@pytest.fixture
def deny_uri_actuator_multiple():
	try: 
		eval ( 'return openc2.v10.Command(action=openc2.v10.Actions.deny, target=openc2.v10.URI("https://example.com"), actuator=slpf.Specifiers({"asset_id": "123456"}), actuator=acme.Specifiers({"endpoint_id": "567890"}))' )
	except SyntaxError:
		raise ValueError("Invalid syntax")

@pytest.fixture
def empty():
	return openc2.v10.Command()
	
@pytest.fixture
def empty_array():
	return openc2.v10.Command([])

@pytest.fixture
def empty_object():
	return openc2.v10.Command({})
	
@pytest.fixture
def number():
	return openc2.v10.Command(3.14159)

@pytest.fixture
def number_integer():
	return openc2.v10.Command(100)

@pytest.fixture
def openc2_response():
	return openc2.v10.Command(openc2.v10.Response(**{'status': 200}))

@pytest.fixture
def openc2_response_extra():
	return openc2.v10.Command(action='start',target=openc2.v10.IPv4Address(ipv4_net='127.0.0.1'),response=openc2.v10.Response(**{'status': 200}))

@pytest.fixture
def openc2_response_text():
	return openc2.v10.Command(action=openc2.v10.Response(**{'status': 200, 'status_text': 'OK'}), target=openc2.v10.IPv4Address(ipv4_net='127.0.0.1'))

@pytest.fixture
def query_feature_ext_args_capX():
	import mycompany_capX
	import uuid
	
	id=mycompany_capX.UuidProperty().clean(uuid.uuid4())
	argp=mycompany_capX.DebugArgsProperty(debug_logging=True)
	act=mycompany_capX.MyCompanyActuator(asset_id=id)
	t=openc2.v10.Features(features=["versions", "rate_limit", "profiles", "pairs"])
	arg = mycompany_capX.MyCompanyArgs(**{"x-mycompany":argp})

	return openc2.v10.Command(action="query", target=t, args=arg, actuator=act)

@pytest.fixture
def query_feature_ext_args_dots():
	import mycompany_dots
	import uuid

	id=mycompany_dots.UuidProperty().clean(uuid.uuid4())
	argp=mycompany_dots.DebugArgsProperty(debug_logging=True)
	act=mycompany_dots.MyCompanyActuator(asset_id=id)
	t=openc2.v10.Features(features=["versions", "rate_limit", "profiles", "pairs"])
	arg = mycompany_dots.MyCompanyArgs(**{"x-mycompany.example.com":argp})

	return openc2.v10.Command(action="query", target=t, args=arg, actuator=act)

@pytest.fixture
def query_feature_ext_args_nox():
	import mycompany_nox
	import uuid

	id=mycompany_nox.UuidProperty().clean(uuid.uuid4())
	argp=mycompany_nox.DebugArgsProperty(debug_logging=True)
	act=mycompany_nox.MyCompanyActuator(asset_id=id)
	t=openc2.v10.Features(features=["versions", "rate_limit", "profiles", "pairs"])
	arg = mycompany_nox.MyCompanyArgs(**{"mycompany":argp})

	return openc2.v10.Command(action="query", target=t, args=arg, actuator=act)

@pytest.fixture
def query_feature_ext_args_specialchar():
	import mycompany_specialchar
	import uuid

	id=mycompany_specialchar.UuidProperty().clean(uuid.uuid4())
	argp=mycompany_specialchar.DebugArgsProperty(debug_logging=True)
	act=mycompany_specialchar.MyCompanyActuator(asset_id=id)
	t=openc2.v10.Features(features=["versions", "rate_limit", "profiles", "pairs"])
	arg = mycompany_specialchar.MyCompanyArgs(**{"x-mycompany/foo;bar":argp})

	return openc2.v10.Command(action="query", target=t, args=arg, actuator=act)


@pytest.fixture
def query_feature_notunique():
	return openc2.v10.Command(action="query", target=openc2.v10.Features(["versions", "versions"]))

@pytest.fixture
def query_feature_unknown():
	return openc2.v10.Command(action="query", target=openc2.v10.Features(["unknown" ]))

@pytest.fixture
def query_feature_multiple_target_extensions():
	import mycompany
	import acme
	try:
		eval ('return openc2.v10.Command(action="query", target=acme.FeaturesTarget(["versions"]), target=mycompany.FeaturesTarget(["versions"]))')
	except SyntaxError:
		raise ValueError("Invalid syntax")

@pytest.fixture
def query_feature_multiple_targets():
	try:
		eval ('return openc2.v10.Command(action=Actions.query, target=openc2.v10.Features([Feature.versions]), target=openc2.v10.Properties(["some_property"]))')
	except SyntaxError:
		raise ValueError("Invalid syntax")

@pytest.fixture
def start_container_ext_nocolon():
	import acme

	return openc2.v10.Command(action="start", target=openc2.v10.ContainerTarget({"container_id": "E57C0116-D291-4AF3-BEF9-0F5B604A2C85"}))

@pytest.fixture
def start_container_ext_noprofile():
	import acme_noprofile 

	p2 = cme_noprofile.ContainerProperty(container_id="E57C0116-D291-4AF3-BEF9-0F5B604A2C85")
	return openc2.v10.Command(action="start", target=acme_noprofile.Container({"container_id": "E57C0116-D291-4AF3-BEF9-0F5B604A2C85"}))

@pytest.fixture
def start_container_ext_specialchar1():
	import acme_specialchar1

	p2=acme_specialchar1.ContainerProperty(container_id="E57C0116-D291-4AF3-BEF9-0F5B604A2C85")
	t2=acme_specialchar1.ContainerTarget(container=p2)
	return openc2.v10.Command(action="start", target=t2)

@pytest.fixture
def start_container_ext_specialchar2():
	import acme_specialchar2

	p2=acme_specialchar2.ContainerProperty(container_id="E57C0116-D291-4AF3-BEF9-0F5B604A2C85")
	t2=acme_specialchar2.ContainerTarget(**{"contai$ner": p2})
	return openc2.v10.Command(action="start", target=t2)

@pytest.fixture
def start_container_ext_underscore_first1():
	import acme_underscore_first1

	p2=acme_underscore_first1.ContainerProperty(container_id="E57C0116-D291-4AF3-BEF9-0F5B604A2C85")
	t2=acme_underscore_first1.ContainerTarget(**{"container": p2})
	return openc2.v10.Command(action="start", target=t2)

@pytest.fixture
def start_container_ext_underscore_first2():
	import acme_underscore_first2

	p2=acme_underscore_first2.ContainerProperty(container_id="E57C0116-D291-4AF3-BEF9-0F5B604A2C85")
	t2=acme_underscore_first2.ContainerTarget(**{"_container": p2})
	return openc2.v10.Command(action="start", target=t2)

@pytest.fixture
def string():
	return openc2.v10.Command("foo")

@pytest.fixture
def target_multiple():
	try:
		h=openc2.properties.HashesProperty().clean({"sha256": "5C2D6DAAF85A710605678F8E7EF0B725B33303F3234197B9DC4B46196734A4F0"})
		d=openc2.v10.Device(device_id="9BCE8431AC106FAA3861C7E771D20E53")
		
		eval ('return openc2.v10.Command(action="contain", target=t, target=d)')
	except SyntaxError:
		raise ValueError("Invalid syntax")

