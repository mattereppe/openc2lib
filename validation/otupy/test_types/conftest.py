import pytest
import otupy as oc2

import sys
sys.path.insert(0, "../profiles/")

import acme
import acme_noprofile
import acme_specialchar1
import acme_specialchar2
import acme_underscore_first1
import acme_underscore_first2
import mycompany_dots
import mycompany_nox
import mycompany_capX
import mycompany_specialchar

@pytest.fixture
def action_notarget():
	return oc2.Command(action=oc2.Actions.stop)

@pytest.fixture
def action_notarget_id():
	return oc2.Command(action=oc2.Actions.stop, command_id="CB1BCDEE-C7B4-40B7-9128-64DB2B877C32")

@pytest.fixture
def allow_ipv4_net_badcidr():
	return oc2.Command(action=oc2.Actions.allow, target=oc2.IPv4Net("127.0.0.1/64"))

@pytest.fixture
def allow_ipv4_net_badip():
	return oc2.Command(action=oc2.Actions.allow, target=oc2.IPv4Net("127.0.0.300"))

@pytest.fixture
def allow_ipv4_net_cidr():
	return oc2.Command(action=oc2.Actions.allow, target=oc2.IPv4Net("127.0.0.1/8"))

@pytest.fixture
def allow_ipv6_net_prefix():
	return oc2.Command(action=oc2.Actions.allow, target=oc2.IPv6Net("3ffe:1900:4545:3:200:f8ff:fe21:67cf/64"))

@pytest.fixture
def allow_ipv6_net_wikipedia3():
	return oc2.Command(action=oc2.Actions.allow, target=oc2.IPv6Net("2001::85a3::8a2e:370:7334"))

@pytest.fixture
def allow_ipv6_net_wikipedia8_prefix2():
	return oc2.Command(action=oc2.Actions.allow, target=oc2.IPv6Net("2001:db8:a::123/64"))

@pytest.fixture
def deny_file_hashes_empty():
	return oc2.Command(action=oc2.Actions.deny, target=oc2.File({'hashes': oc2.Hashes()}))

@pytest.fixture
def deny_file_hashes_sha512():
	return oc2.Command(action=oc2.Actions.deny, target=oc2.File({'hashes': oc2.Hashes({'sha512': "96b74959340df1680ea15d9f66a907e0bf55f059e2e4184190aa1271021003bcefd02a9f924164b22954b54fc0fff36a68eae36d189173ca2df30fa4b1535700"})}))

@pytest.fixture
def deny_uri_actuator_empty():
	return oc2.Command(action=oc2.Actions.deny, target=oc2.URI("https://example.com"), actuator=oc2.Actuator())

@pytest.fixture
def deny_uri_actuator_multiple():
	try: 
		eval ( 'return oc2.Command(action=oc2.Actions.deny, target=oc2.URI("https://example.com"), actuator=slpf.Specifiers({"asset_id": "123456"}), actuator=acme.Specifiers({"endpoint_id": "567890"}))' )
	except SyntaxError:
		raise ValueError("Invalid syntax")

@pytest.fixture
def empty():
	return oc2.Command()
	
@pytest.fixture
def empty_array():
	return oc2.Command([])

@pytest.fixture
def empty_object():
	return oc2.Command({})
	
@pytest.fixture
def number():
	return oc2.Command(3.14159)

@pytest.fixture
def number_integer():
	return oc2.Command(100)

@pytest.fixture
def openc2_response():
	return oc2.Command(oc2.Response({'status': oc2.StatusCode.OK}))

@pytest.fixture
def openc2_response_text():
	return oc2.Command(oc2.Response({'status': oc2.StatusCode.OK, 'status_text': 'OK'}))

@pytest.fixture
def query_feature_ext_args_capX():
	return oc2.Command(oc2.Actions.query, oc2.Features([oc2.Feature.versions, oc2.Feature.profiles, oc2.Feature.pairs, oc2.Feature.rate_limit]), args=mycompany_capX.Args({"debug_logging": True}))

@pytest.fixture
def query_feature_ext_args_dots():
	return oc2.Command(oc2.Actions.query, oc2.Features([oc2.Feature.versions, oc2.Feature.profiles, oc2.Feature.pairs, oc2.Feature.rate_limit]), args=mycompany_dots.Args({"debug_logging": True}))

@pytest.fixture
def query_feature_ext_args_nox():
	return oc2.Command(oc2.Actions.query, oc2.Features([oc2.Feature.versions, oc2.Feature.profiles, oc2.Feature.pairs, oc2.Feature.rate_limit]), args=mycompany_nox.Args({"debug_logging": True}))

@pytest.fixture
def query_feature_ext_args_specialchar():
	return oc2.Command(oc2.Actions.query, oc2.Features([oc2.Feature.versions, oc2.Feature.profiles, oc2.Feature.pairs, oc2.Feature.rate_limit]), args=mycompany_specialchar.Args({"debug_logging": True}))

@pytest.fixture
def query_feature_notunique():
	return oc2.Command(oc2.Actions.query, oc2.Features([oc2.Feature.versions, oc2.Feature.versions]))

@pytest.fixture
def query_feature_unknown():
	return oc2.Command(oc2.Actions.query, oc2.Features([oc2.Feature.unknown]))

@pytest.fixture
def query_feature_multiple_target_extensions():
	try: 
		eval ( 'return oc2.Command(action=Actions.query, target=acme.Features([Feature.versions]), target=mycompany.Features([Feature.versions])) ')
	except SyntaxError:
		raise ValueError("Invalid syntax")

@pytest.fixture
def query_feature_multiple_targets():
	try:
		eval ('return oc2.Command(action=Actions.query, target=oc2.Features([Feature.versions]), target=oc2.Properties(["some_property"]))')
	except SyntaxError:
		raise ValueError("Invalid syntax")

@pytest.fixture
def start_container_ext_nocolon():
	return oc2.Command(action=oc2.Actions.start, target=oc2.Container({"container_id": "E57C0116-D291-4AF3-BEF9-0F5B604A2C85"}))

@pytest.fixture
def start_container_ext_noprofile():
	return oc2.Command(action=oc2.Actions.start, target=acme_noprofile.Container({"container_id": "E57C0116-D291-4AF3-BEF9-0F5B604A2C85"}))

@pytest.fixture
def start_container_ext_specialchar1():
	return oc2.Command(action=oc2.Actions.start, target=acme_specialchar1.Container({"container_id": "E57C0116-D291-4AF3-BEF9-0F5B604A2C85"}))

@pytest.fixture
def start_container_ext_specialchar2():
	return oc2.Command(action=oc2.Actions.start, target=acme_specialchar2.Container({"container_id": "E57C0116-D291-4AF3-BEF9-0F5B604A2C85"}))

@pytest.fixture
def start_container_ext_underscore_first1():
	return oc2.Command(action=oc2.Actions.start, target=acme_underscore_first1.Container({"container_id": "E57C0116-D291-4AF3-BEF9-0F5B604A2C85"}))

@pytest.fixture
def start_container_ext_underscore_first2():
	cmd =  oc2.Command(action=oc2.Actions.start, target=acme_underscore_first2.Container({"container_id": "E57C0116-D291-4AF3-BEF9-0F5B604A2C85"}))
	return cmd

@pytest.fixture
def string():
	return oc2.Command("foo")

@pytest.fixture
def target_multiple():
	try:
		eval ('return oc2.Command(action=oc2.Actions.contain, target=oc2.File({"hashes": oc2.Hashes({"sha256": "5c2d6daaf85a710605678f8e7ef0b725b33303f3234197b9dc4b46196734a4f0"})}), target=oc2.Device({"device_id": "9BCE8431AC106FAA3861C7E771D20E53"}))' )
	except SyntaxError:
		raise ValueError("Invalid syntax")

