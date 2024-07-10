import pytest
import parametrize_from_file
import string
import random

from openc2lib import Artifact, Binary, Binaryx,  Hashes, File
from openc2lib.types.data.uri import URI

def random_strings():
	rnd = []
	for i in range (0,10):
		for length in range (3,15):
			rnd.append(  ''.join(random.choices(string.ascii_lowercase, k=length)) )
			rnd.append(''.join(random.choices(string.ascii_lowercase + string.digits, k=length)))
			rnd.append(''.join(random.choices(string.printable, k=length)))
	return rnd

@parametrize_from_file('test_mime_types.yml')
def test_mime_types(mime_type):
	Artifact.validate_syntax = True
	Artifact.validate_iana = True
	assert type(Artifact(mime_type=mime_type)) == Artifact

@pytest.mark.parametrize("rnd", random_strings())
def test_mime_types_random_strings(rnd):
	with pytest.raises(Exception):
		Artifact(mime_type=rnd)

@pytest.mark.parametrize("payload", [Binary(b"hello"), Binary(bytes(34)), Binary(), URI("http://host.com/path#tag"), URI("ldap://[2001:db8::7]/c=GB?objectClass?one"), URI("urn:oasis:names:specification:docbook:dtd:xml:4.1.2")])
def test_payload(payload):
	assert type(Artifact(payload=payload)) == Artifact

class A:
	pass

@pytest.mark.parametrize("payload", ["hello", 34, True, A(), A ])
def test_payload_wrong(payload):
	with pytest.raises(Exception):
		Artifact(payload=payload)

@pytest.mark.parametrize("hashes", [{'md5': Binaryx(b"mychecksum")}, {'sha1': Binaryx(b"mychecksum")}, {'sha256': Binaryx(b"mychecksum")}, {'md5': Binaryx(b"mychecksum"), 'sha1': Binaryx(b"mychecksum")}, {'md5': Binaryx(b"mychecksum"), 'sha1': Binaryx(b"mychecksum"), 'sha256': Binaryx(b"mychecksum")}])
def test_hashes(hashes):
	assert type(Artifact(hashes=hashes)) == Artifact

@pytest.mark.parametrize("mime_type", ["application/json", "application/xml"])
@pytest.mark.parametrize("payload", [Binary(b"hello"), Binary(bytes(34)), Binary(), URI("http://host.com/path#tag"), URI("ldap://[2001:db8::7]/c=GB?objectClass?one"), URI("urn:oasis:names:specification:docbook:dtd:xml:4.1.2")])
@pytest.mark.parametrize("hashes", [{'md5': Binaryx(b"mychecksum")}, {'sha1': Binaryx(b"mychecksum")}, {'sha256': Binaryx(b"mychecksum")}, {'md5': Binaryx(b"mychecksum"), 'sha1': Binaryx(b"mychecksum")}, {'md5': Binaryx(b"mychecksum"), 'sha1': Binaryx(b"mychecksum"), 'sha256': Binaryx(b"mychecksum")}])
def test_artifact(mime_type,payload,hashes):
	assert type(Artifact(mime_type=mime_type, payload=payload, hashes=hashes)) == Artifact

def test_void_artifact():
	with pytest.raises(Exception):
		Artifact()
