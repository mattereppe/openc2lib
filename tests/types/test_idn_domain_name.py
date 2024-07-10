import pytest
import parametrize_from_file

from openc2lib import IDNDomainName

@parametrize_from_file
def test_good_names(name):
	assert type(IDNDomainName(name)) == IDNDomainName

@parametrize_from_file
def test_bad_names(name):
	with pytest.raises(Exception):
		IDNDomainName(name)


