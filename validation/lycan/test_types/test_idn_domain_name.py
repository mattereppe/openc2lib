import pytest
import parametrize_from_file

from openc2.v10 import InternationalizedDomainName

@parametrize_from_file('parameters/test_idn_domain_name.yml')
def test_good_names(name):
	assert type(InternationalizedDomainName(idn_domain_name=name)) == InternationalizedDomainName

@parametrize_from_file('parameters/test_idn_domain_name.yml')
def test_bad_names(name):
	with pytest.raises(Exception):
		InternationalizedDomainName(idn_domain_name=name)


