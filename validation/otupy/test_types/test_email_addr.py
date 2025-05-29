import pytest
import parametrize_from_file

from otupy import EmailAddr

@parametrize_from_file('parameters/test_email_addr.yml') 
def test_good_names(name):
	assert type(EmailAddr(email=name)) == EmailAddr

@parametrize_from_file('parameters/test_email_addr.yml') 
def test_bad_names(name):
	with pytest.raises(Exception):
		EmailAddr(email=name)


