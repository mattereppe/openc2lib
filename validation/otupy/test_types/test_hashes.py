import pytest
import parametrize_from_file
import string
import random

from otupy import Binary, Binaryx, Hashes

@pytest.mark.parametrize("hashes", [{'md5': Binaryx("AABBCCDDEEFF00112233445566778899")}, {'sha1': Binaryx("AABBCCDDEEFF00112233445566778899AABBCCDD")}, {'sha256': Binaryx("AABBCCDDEEFF00112233445566778899AABBCCDDEEFF00112233445566778899")}, {'md5': Binaryx("aabbccddeeff00112233445566778899"), 'sha1': Binaryx("AABBCCDDEEFF00112233445566778899AABBCCDD")}, {'md5': Binaryx("AABBCCDDEEFF00112233445566778899"), 'sha1': Binaryx("AABBCCDDEEFF00112233445566778899AABBCCDD"), 'sha256': Binaryx("aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899")}])
def test_hashes(hashes):
	assert type(Hashes(hashes)) == Hashes

@pytest.mark.parametrize("hashes", [{'md5': b"mymd5checksumxxx"}, {'sha1': b"mychecksummychecksum"}, {'sha256': b"mychecksumbbmychecksummychecksum"} , {'md5': b"mymd5checksumxxx", 'sha1': b"mychecksummychecksum"}, {'md5': Binary(b"mymd5checksumxxx"), 'sha1': Binary(b"mychecksummychecksum"), 'sha256': Binary(b"mychecksummychecksummychecksumxx")}])
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
def test_hashes_empty(hashes):
	assert type(Hashes(hashes)) == Hashes
