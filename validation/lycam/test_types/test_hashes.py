import pytest
import parametrize_from_file
import string
import random

from openc2.properties import BinaryProperty,  HashesProperty

@pytest.mark.parametrize("hashes", [{'md5': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899")}, {'sha1': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDD")}, {'sha256': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDDEEFF00112233445566778899")}, {'md5': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899"), 'sha1': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDD")}, {'md5': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899"), 'sha1': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDD"), 'sha256': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDDEEFF00112233445566778899")}])
def test_hashes(hashes):
	assert type(HashesProperty().clean(hashes)) == dict

#@pytest.mark.parametrize("hashes", [{'md5': b"mychecksum"}, {'sha1': b"mychecksum"}, {'sha256': b"mychecksum"}, {'md5': b"mychecksum", 'sha1': b"mychecksum"}, {'md5': Binary(b"mychecksum"), 'sha1': Binary(b"mychecksum"), 'sha256': Binary(b"mychecksum")}])
#def test_hashes_binary(hashes):
#	assert type(HashesProperty(hashes)) == HashesProperty

@pytest.mark.parametrize("hashes", [{'md5': "mychecksum"}, {'sha1': "mychecksum"}, {'sha256': "mychecksum"}, {'md5': "mychecksum", 'sha1': "mychecksum"}])
def test_hashes_text(hashes):
	with pytest.raises(Exception): 
		HashesProperty().clean(hashes)

@pytest.mark.parametrize("hashes", [{'md5': 454354354}, {'sha1': 454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098454250984542509845425098}, {'sha256': 4532543}, {'md5': 89999, 'sha1': 0} ] )
def test_hashes_num(hashes):
	with pytest.raises(Exception): 
		HashesProperty().clean(hashes)

#@pytest.mark.parametrize("hashes", [{'md5': None}, {'sha1': None}, {'sha256': None}])
#def test_hashes_binary(hashes):
#	assert type(Hashes(hashes)) == Hashes
