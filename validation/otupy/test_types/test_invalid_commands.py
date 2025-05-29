import pytest
from ipaddress import NetmaskValueError, AddressValueError


# Associate the expected exception to each command to be sure the failure is really
# due to the invalid command and not to other errors.
# - 10 tests fail, all releated to the use of special characters in the nsid or 
#   object name. This is set in the json schema, but I did not see any indication
# 		about valid characters in the LS
@pytest.mark.parametrize('cmd, ex', [ 
		("action_notarget", TypeError),
		("action_notarget_id", TypeError),
		("allow_ipv4_net_badcidr", NetmaskValueError),
		("allow_ipv4_net_badip", AddressValueError),
		("allow_ipv4_net_cidr", ValueError),
		("allow_ipv6_net_prefix", ValueError),
		("allow_ipv6_net_wikipedia3", AddressValueError),
		("allow_ipv6_net_wikipedia8_prefix2", ValueError),
		("deny_file_hashes_empty", TypeError),
		("deny_file_hashes_sha512", KeyError),
		("deny_uri_actuator_empty", TypeError),
		("deny_uri_actuator_multiple", ValueError),
		("empty", TypeError),
		("empty_array", TypeError),
		("empty_object", TypeError),
		("number", TypeError),
		("number_integer", TypeError),
		("openc2_response", TypeError),
		("openc2_response_text", TypeError),
		("query_feature_ext_args_capX", None),
		("query_feature_ext_args_dots", Exception),
		("query_feature_ext_args_nox", Exception),
		("query_feature_ext_args_specialchar", Exception),
		("query_feature_notunique", Exception),
		("query_feature_unknown", AttributeError),
		("query_feature_multiple_target_extensions", ValueError),
		("query_feature_multiple_targets", ValueError),
		("start_container_ext_nocolon", AttributeError),
		("start_container_ext_noprofile", Exception),
		("start_container_ext_specialchar1", Exception),
		("start_container_ext_specialchar2", Exception),
		("start_container_ext_underscore_first1", Exception),
		("start_container_ext_underscore_first2", Exception),
		("string", TypeError),
		("target_multiple", ValueError)
		] )
def test_invalid_command(cmd, ex, request):
	""" Test invalid commands

		(Run this test with `python -s` to get detail of each exception raised.
	"""
	print("Testing: ", cmd)
#with pytest.raises(Exception) as e:
	with pytest.raises(ex) as e:
		request.getfixturevalue(cmd)
	print("		>>>> Got exception: ", e.type, ": ", e.value)
#assert ex == e.type



