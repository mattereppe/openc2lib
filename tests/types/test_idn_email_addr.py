import pytest
import parametrize_from_file

from openc2lib import IDNEmailAddr

@parametrize_from_file
def test_good_names(name):
	assert type(IDNEmailAddr(name)) == IDNEmailAddr

@parametrize_from_file
def test_bad_names(name):
	with pytest.raises(Exception):
		IDNEmailAddr(name)


