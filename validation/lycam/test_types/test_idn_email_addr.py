import pytest
import parametrize_from_file

from openc2.v10 import InternationalizedEmailAddress

@parametrize_from_file('parameters/test_idn_email_addr.yml')
def test_good_names(name):
	assert type(InternationalizedEmailAddress(idn_email_addr=name)) == InternationalizedEmailAddress

@parametrize_from_file('parameters/test_idn_email_addr.yml')
def test_bad_names(name):
	with pytest.raises(Exception):
		InternationalizedEmailAddress(idn_email_addr=name)


