import pytest
import parametrize_from_file
import string
import random
import base64

from openc2.v10 import Artifact, File, URI, Payload
from openc2.properties import BinaryProperty, HashesProperty, PayloadProperty

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
	assert type(Artifact(mime_type=mime_type)) == Artifact

@pytest.mark.parametrize("rnd", random_strings())
def test_mime_types_random_strings(rnd):
	with pytest.raises(Exception):
		Artifact(mime_type=rnd)

@pytest.mark.parametrize("payload", [BinaryProperty().clean(base64.b64encode(b"hello")), BinaryProperty().clean(base64.b64encode(bytes(34)))])
def test_payload_bin(payload):
	assert type(Artifact(payload=PayloadProperty().clean(Payload(bin=payload)))) == Artifact

@pytest.mark.parametrize("payload", [ URI(uri="http://host.com/path#tag"), URI(uri="ldap://[2001:db8::7]/c=GB?objectClass?one"), URI(uri="urn:oasis:names:specification:docbook:dtd:xml:4.1.2")])
def test_payload(payload):
	assert type(Artifact(payload=PayloadProperty().clean(Payload(url=payload)))) == Artifact

class A:
	pass

@pytest.mark.parametrize("payload", ["hello", 34, True, A(), A ])
def test_payload_wrong(payload):
	with pytest.raises(Exception):
		Artifact(payload=payload)

@pytest.mark.parametrize("hashes", [{'md5': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899")}, {'sha1': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDD")}, {'sha256': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDDEEFF00112233445566778899")}, {'md5': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899"), 'sha1': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDD")}, {'md5': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899"), 'sha1': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDD"), 'sha256': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDDEEFF00112233445566778899")}])
def test_hashes(hashes):
	assert type(Artifact(hashes=hashes)) == Artifact

@pytest.mark.parametrize("hashes", [{'md5': BinaryProperty().clean("AABBCCDDEEFF001122334455")}, {'sha1': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABB")}, {'sha256': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDDEEFF001122334455")}, {'md5': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899"), 'sha1': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDDFF00")}, {'md5': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABB"), 'sha1': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDDEEFF"), 'sha256': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDDEEFF00112233445566778899AABB")}])
def test_hashes_wrong_len(hashes):
	with pytest.raises(Exception):
		Artifact(hashes=hashes) 

@pytest.mark.parametrize("mime_type", ["application/json", "application/xml"])
@pytest.mark.parametrize("payload", [BinaryProperty().clean(base64.b64encode(b"hello")), BinaryProperty().clean(base64.b64encode(bytes(34)))])
@pytest.mark.parametrize("hashes", [{'md5': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899")}, {'sha1': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDD")}, {'sha256': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDDEEFF00112233445566778899")}, {'md5': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899"), 'sha1': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDD")}, {'md5': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899"), 'sha1': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDD"), 'sha256': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDDEEFF00112233445566778899")}])
def test_artifact_uri(mime_type,payload,hashes):
	assert type(Artifact(mime_type=mime_type, payload=PayloadProperty().clean(Payload(bin=payload)), hashes=hashes)) == Artifact

@pytest.mark.parametrize("mime_type", ["application/json", "application/xml"])
@pytest.mark.parametrize("payload", [ URI(uri="http://host.com/path#tag"), URI(uri="ldap://[2001:db8::7]/c=GB?objectClass?one"), URI(uri="urn:oasis:names:specification:docbook:dtd:xml:4.1.2")])
@pytest.mark.parametrize("hashes", [{'md5': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899")}, {'sha1': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDD")}, {'sha256': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDDEEFF00112233445566778899")}, {'md5': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899"), 'sha1': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDD")}, {'md5': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899"), 'sha1': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDD"), 'sha256': BinaryProperty().clean("AABBCCDDEEFF00112233445566778899AABBCCDDEEFF00112233445566778899")}])
def test_artifact_bin(mime_type,payload,hashes):
	assert type(Artifact(mime_type=mime_type, payload=PayloadProperty().clean(Payload(url=payload)), hashes=hashes)) == Artifact

def test_void_artifact():
	with pytest.raises(Exception):
		Artifact()
