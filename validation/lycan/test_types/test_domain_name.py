import pytest
import parametrize_from_file

from openc2.v10 import DomainName

@parametrize_from_file('parameters/test_domain_name.yml')
def test_good_names(name):
	assert type(DomainName(domain_name=name)) == DomainName

@parametrize_from_file('parameters/test_domain_name.yml') 
def test_bad_names(name):
	with pytest.raises(Exception):
		DomainName(domain_name=name)


