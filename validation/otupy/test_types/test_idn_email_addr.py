import pytest
import parametrize_from_file

from otupy import IDNEmailAddr

@parametrize_from_file('parameters/test_idn_email_addr.yml')
def test_good_names(name):
	assert type(IDNEmailAddr(name)) == IDNEmailAddr

@parametrize_from_file('parameters/test_idn_email_addr.yml')
def test_bad_names(name):
	with pytest.raises(Exception):
		IDNEmailAddr(name)


