import pytest
import parametrize_from_file

from otupy import IDNDomainName

@parametrize_from_file('parameters/test_idn_domain_name.yml')
def test_good_names(name):
	assert type(IDNDomainName(name)) == IDNDomainName

@parametrize_from_file('parameters/test_idn_domain_name.yml')
def test_bad_names(name):
	with pytest.raises(Exception):
		IDNDomainName(name)


