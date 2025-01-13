import pytest
import openc2
import base64


@pytest.mark.parametrize('args', [ [], (3,), [4], [3, 4], "battery", ["battery"], ["battery", 35], ["property1", "property2", "property3", "property4"] ])
def test_list(args):
	assert type(openc2.v10.Properties(properties=args)) == openc2.v10.Properties

#@pytest.mark.parametrize('args', [ Array("battery"), Array(["battery"]), Array(["property1", "property2", "property3"]) ])
#def test_array(args):
#	assert type(Properties(args)) == Properties


#@pytest.mark.parametrize('args', [ ArrayOf(str)("battery"), Array((3,)), Array([3,4]), ArrayOf(int)([3,4]), ArrayOf(str)(["battery"]), Array(["property1", "property2", "property3"]) ])
#def test_arrayof(args):
#	assert type(Properties(args)) == Properties

@pytest.mark.parametrize('args', [(openc2.v10.IPv4Address(ipv4_net="192.168.0.1"),)] )
def test_arrayof(args):
	assert type(openc2.v10.Properties(properties=args)) == openc2.v10.Properties

# Only iterables can be used as arguments
# (the following objects have the `___str__` method, but are not iterable by themselves
@pytest.mark.parametrize('args', [ 3, openc2.v10.IPv4Address(ipv4_net="192.168.0.1"), openc2.properties.PayloadProperty().clean({'bin': base64.b64encode(b'helloworld')})])
def test_illegal_types(args):
	with pytest.raises(Exception):
		openc2.v10.Properties(properties=args)

