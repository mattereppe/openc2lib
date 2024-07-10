import pytest
import parametrize_from_file

from openc2lib import EmailAddr

@parametrize_from_file
def test_good_names(name):
	assert type(EmailAddr(email=name)) == EmailAddr

@parametrize_from_file
def test_bad_names(name):
	with pytest.raises(Exception):
		EmailAddr(email=name)


