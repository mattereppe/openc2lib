import pytest
import parametrize_from_file
import string
import random

from openc2lib import Binary, Binaryx, Hashes

@pytest.mark.parametrize("hashes", [{'md5': Binaryx(b"mychecksum")}, {'sha1': Binaryx(b"mychecksum")}, {'sha256': Binaryx(b"mychecksum")}, {'md5': Binaryx(b"mychecksum"), 'sha1': Binaryx(b"mychecksum")}, {'md5': Binaryx(b"mychecksum"), 'sha1': Binaryx(b"mychecksum"), 'sha256': Binaryx(b"mychecksum")}])
def test_hashes(hashes):
	assert type(Hashes(hashes)) == Hashes

@pytest.mark.parametrize("hashes", [{'md5': b"mychecksum"}, {'sha1': b"mychecksum"}, {'sha256': b"mychecksum"}, {'md5': b"mychecksum", 'sha1': b"mychecksum"}, {'md5': Binary(b"mychecksum"), 'sha1': Binary(b"mychecksum"), 'sha256': Binary(b"mychecksum")}])
def test_hashes_binary(hashes):
	assert type(Hashes(hashes)) == Hashes

@pytest.mark.parametrize("hashes", [{'md5': "mychecksum"}, {'sha1': "mychecksum"}, {'sha256': "mychecksum"}, {'md5': "mychecksum", 'sha1': "mychecksum"}])
def test_hashes_text(hashes):
	with pytest.raises(Exception): 
		Hashes(hashes)

@pytest.mark.parametrize("hashes", [{'md5': 454354354}, {'sha1': 454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098}, {'sha256': 4532543}, {'md5': 89999, 'sha1': 0} ] )
def test_hashes_text(hashes):
	with pytest.raises(Exception): 
		Hashes(hashes)

@pytest.mark.parametrize("hashes", [{'md5': None}, {'sha1': None}, {'sha256': None}])
def test_hashes_binary(hashes):
	assert type(Hashes(hashes)) == Hashes
