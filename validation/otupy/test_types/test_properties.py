import pytest

from otupy import Properties, Array, ArrayOf, IPv4Net, Payload, Binary

@pytest.mark.parametrize('args', [ [], (3,), [4], [3, 4], "battery", ["battery"], ["battery", 35], ["property1", "property2", "property3", "property4"] ])
def test_list(args):
	assert type(Properties(args)) == Properties

@pytest.mark.parametrize('args', [ Array("battery"), Array(["battery"]), Array(["property1", "property2", "property3"]) ])
def test_array(args):
	assert type(Properties(args)) == Properties


@pytest.mark.parametrize('args', [ ArrayOf(str)("battery"), Array((3,)), Array([3,4]), ArrayOf(int)([3,4]), ArrayOf(str)(["battery"]), Array(["property1", "property2", "property3"]) ])
def test_arrayof(args):
	assert type(Properties(args)) == Properties

@pytest.mark.parametrize('args', [(IPv4Net("192.168.0.1"),), ArrayOf(IPv4Net)(["10.0.0.1", "172.16.0.0/16"])])
def test_arrayof(args):
	assert type(Properties(args)) == Properties

# Only iterables can be used as arguments
# (the following objects have the `___str__` method, but are not iterable by themselves
@pytest.mark.parametrize('args', [ 3, IPv4Net("192.168.0.1"), Payload(Binary(b'helloworld'))])
def test_illegal_types(args):
	with pytest.raises(Exception):
		Properties(args)

