import pytest
import parametrize_from_file

from openc2.v10 import EmailAddress

@parametrize_from_file('parameters/test_email_addr.yml') 
def test_good_names(name):
	assert type(EmailAddress(email_addr=name)) == EmailAddress

@parametrize_from_file('parameters/test_email_addr.yml') 
def test_bad_names(name):
	with pytest.raises(Exception):
		EmailAddress(email_addr=name)


