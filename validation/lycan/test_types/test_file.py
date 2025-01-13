import pytest
import random
import string

import utils

from openc2.v10 import File
from openc2.properties import BinaryProperty, HashesProperty

def random_strings():
	rnd = []
	for i in range (0,5):
		for length in range (10,15):
			rnd.append(  ''.join(random.choices(string.ascii_lowercase, k=length)) )
			rnd.append(''.join(random.choices(string.ascii_lowercase + string.digits, k=length)))
			rnd.append(''.join(random.choices(string.printable, k=length)))
	return rnd

hashes = {'md5': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899"), 'sha1': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDD"), 'sha256': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDDEEFF00112233445566778899")}

@pytest.mark.parametrize("name", random_strings())
@pytest.mark.parametrize("path", random_strings())
def test_random_strings(name, path):
		assert type(File(name=name, path=path)) == File

@pytest.mark.parametrize("hashes", utils.random_params(hashes))
def test_hashes(hashes):
	assert type(File(hashes=hashes)) == File

@pytest.mark.parametrize('args', utils.random_params({'name': "test.txt", 'path': "/var/run/", 'hashes': hashes}))
def test_random_params(args):
	assert type(File(**args)) == File

def test_void_file():
	with pytest.raises(Exception):
		File()
