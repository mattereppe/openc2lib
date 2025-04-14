import pytest

from otupy import Binary


@pytest.mark.parametrize("b", [b"hello", bytes(34), None])
def test_payload(b):
	assert type(Binary(b=b)) == Binary

class A:
	pass

@pytest.mark.parametrize("b", ["hello", 34, True, A() , '', A])
def test_payload_wrong(b):
	with pytest.raises(Exception):
		Artifact(b=b)
