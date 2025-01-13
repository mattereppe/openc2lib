import pytest
import base64

from openc2.properties import BinaryProperty


@pytest.mark.parametrize("b", [base64.b64encode(b"hello"), base64.b64encode(bytes(34))])
def test_payload(b):
	print(b)
	assert type(BinaryProperty().clean(b)) == bytes

class A:
	pass

@pytest.mark.parametrize("b", ["hello", 34, True, A() , '', A])
def test_payload_wrong(b):
	with pytest.raises(Exception):
		Artifact(b=b)
