import pytest
import parametrize_from_file
import string
import random

from otupy import Artifact, Binary, Binaryx,  Hashes, File
from otupy.types.data.uri import URI

def random_strings():
	rnd = []
	for i in range (0,10):
		for length in range (3,15):
			rnd.append(  ''.join(random.choices(string.ascii_lowercase, k=length)) )
			rnd.append(''.join(random.choices(string.ascii_lowercase + string.digits, k=length)))
			rnd.append(''.join(random.choices(string.printable, k=length)))
	return rnd

@parametrize_from_file('parameters/test_mime_types.yml')
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

# The Base16 alphabet does not include lower-case letters (pag. 25 LS, but I want to take
# lowercase as well in input
@pytest.mark.parametrize("hashes", [{'md5': Binaryx("AABBCCDDEEFF00112233445566778899")}, {'sha1': Binaryx("AABBCCDDEEFF00112233445566778899AABBCCDD")}, {'sha256': Binaryx("AABBCCDDEEFF00112233445566778899AABBCCDDEEFF00112233445566778899")}, {'md5': Binaryx("aabbccddeeff00112233445566778899"), 'sha1': Binaryx("AABBCCDDEEFF00112233445566778899AABBCCDD")}, {'md5': Binaryx("AABBCCDDEEFF00112233445566778899"), 'sha1': Binaryx("AABBCCDDEEFF00112233445566778899AABBCCDD"), 'sha256': Binaryx("aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899")}])
def test_hashes(hashes):
	assert type(Artifact(hashes=hashes)) == Artifact

@pytest.mark.parametrize("hashes", [{'md5': Binaryx("AABBCCDDEEFF001122334455")}, {'sha1': Binaryx("AABBCCDDEEFF00112233445566778899AABB")}, {'sha256': Binaryx("AABBCCDDEEFF00112233445566778899AABBCCDDEEFF001122334455")}, {'md5': Binaryx("AABBCCDDEEFF00112233445566778899"), 'sha1': Binaryx("AABBCCDDEEFF00112233445566778899AABBCCDDFF00")}, {'md5': Binaryx("AABBCCDDEEFF00112233445566778899AABB"), 'sha1': Binaryx("AABBCCDDEEFF00112233445566778899AABBCCDD"), 'sha256': Binaryx("AABBCCDDEEFF00112233445566778899AABBCCDDEEFF00112233445566778899AABB")}])
def test_wrong_hashes(hashes):
	with pytest.raises(Exception):
		Artifact(hashes=hashes)

@pytest.mark.parametrize("mime_type", ["application/json", "application/xml"])
@pytest.mark.parametrize("payload", [Binary(b"hello"), Binary(bytes(34)), Binary(), URI("http://host.com/path#tag"), URI("ldap://[2001:db8::7]/c=GB?objectClass?one"), URI("urn:oasis:names:specification:docbook:dtd:xml:4.1.2")])
@pytest.mark.parametrize("hashes", [{'md5': Binaryx("AABBCCDDEEFF00112233445566778899")}, {'sha1': Binaryx("AABBCCDDEEFF00112233445566778899AABBCCDD")}, {'sha256': Binaryx("AABBCCDDEEFF00112233445566778899AABBCCDDEEFF00112233445566778899")}, {'md5': Binaryx("AABBCCDDEEFF00112233445566778899"), 'sha1': Binaryx("AABBCCDDEEFF00112233445566778899AABBCCDD")}, {'md5': Binaryx("AABBCCDDEEFF00112233445566778899"), 'sha1': Binaryx("AABBCCDDEEFF00112233445566778899AABBCCDD"), 'sha256': Binaryx("AABBCCDDEEFF00112233445566778899AABBCCDDEEFF00112233445566778899")}])
def test_artifact(mime_type,payload,hashes):
	assert type(Artifact(mime_type=mime_type, payload=payload, hashes=hashes)) == Artifact

def test_void_artifact():
	with pytest.raises(Exception):
		Artifact()
