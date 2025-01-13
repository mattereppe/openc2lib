import pytest
from ipaddress import NetmaskValueError, AddressValueError

import openc2

# Associate the expected exception to each command to be sure the failure is really
# due to the invalid command and not to other errors.
# - 10 tests fail, all releated to the use of special characters in the nsid or 
#   object name. This is set in the json schema, but I did not see any indication
# 		about valid characters in the LS
@pytest.mark.parametrize('cmd, ex', [ 
		("action_notarget", openc2.exceptions.MissingPropertiesError),
		("action_notarget_id", openc2.exceptions.MissingPropertiesError),
		("allow_ipv4_net_badcidr", Exception),
		("allow_ipv4_net_badip", Exception),
		("allow_ipv4_net_cidr", Exception),
		("allow_ipv6_net_prefix", Exception),
		("allow_ipv6_net_wikipedia3", Exception),
		("allow_ipv6_net_wikipedia8_prefix2", Exception),
		("deny_file_hashes_empty", Exception),
		("deny_file_hashes_sha512", TypeError),
		("deny_uri_actuator_empty", openc2.exceptions.MissingPropertiesError),
		("deny_uri_actuator_multiple", ValueError),
		("empty", openc2.exceptions.MissingPropertiesError),
		("empty_array", openc2.exceptions.MissingPropertiesError),
		("empty_object", openc2.exceptions.MissingPropertiesError),
		("number", openc2.exceptions.MissingPropertiesError),
		("number_integer", openc2.exceptions.MissingPropertiesError),
		("openc2_response", openc2.exceptions.MissingPropertiesError),
		("openc2_response_extra", openc2.exceptions.ExtraPropertiesError),
		("openc2_response_text", openc2.exceptions.InvalidValueError),
		("query_feature_ext_args_capX", ValueError),
		("query_feature_ext_args_dots", Exception),
		("query_feature_ext_args_nox", ValueError),
		("query_feature_ext_args_specialchar", Exception),
		("query_feature_notunique", openc2.exceptions.InvalidValueError),
		("query_feature_unknown", openc2.exceptions.InvalidValueError),
		("query_feature_multiple_target_extensions", ValueError),
		("query_feature_multiple_targets", ValueError),
		("start_container_ext_nocolon", AttributeError),
		("start_container_ext_noprofile", ValueError),
		("start_container_ext_specialchar1", Exception),
		("start_container_ext_specialchar2", Exception),
		("start_container_ext_underscore_first1", Exception),
		("start_container_ext_underscore_first2", Exception),
		("string", openc2.exceptions.MissingPropertiesError),
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



