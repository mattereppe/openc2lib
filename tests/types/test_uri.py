import pytest
import parametrize_from_file

from openc2lib import URI


@parametrize_from_file
def test_good_uris(uri):
	assert type(URI(uri=uri)) == URI


@parametrize_from_file
def test_bad_uris(uri):
	with pytest.raises(Exception):
		URI(uri=uri)
