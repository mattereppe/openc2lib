import pytest
import parametrize_from_file

from otupy import DomainName

@parametrize_from_file('parameters/test_domain_name.yml')
def test_good_names(name):
	assert type(DomainName(domainname=name)) == DomainName

@parametrize_from_file('parameters/test_domain_name.yml') 
def test_bad_names(name):
	with pytest.raises(Exception):
		DomainName(domainname=name)


