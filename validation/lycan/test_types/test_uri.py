import pytest
import parametrize_from_file

from openc2.v10 import URI


@parametrize_from_file('parameters/test_uri.yml')
def test_good_uris(uri):
	assert type(URI(uri=uri)) == URI


@parametrize_from_file('parameters/test_uri.yml')
def test_bad_uris(uri):
	with pytest.raises(Exception):
		URI(uri=uri)
