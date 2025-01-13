import pytest

import openc2


@pytest.mark.parametrize("status", [102, 200, 400, 401, 403, 404, 500, 501, 503 ])
def test_valid_status(status):
	assert type(openc2.v10.Response(status= status)) == openc2.v10.Response

@pytest.mark.parametrize("status", [200, 102])
@pytest.mark.parametrize("status_text", [ "", None, "OK", "Processing" ])
def test_valid_text(status, status_text):
	assert type(openc2.v10.Response(**{'status': status, 'status_text': status_text})) == openc2.v10.Response

def test_invalid_empty_response():
	with pytest.raises(openc2.exceptions.MissingPropertiesError):
		openc2.v10.Response(**{})

def test_invalid_empty_response2():
	with pytest.raises(openc2.exceptions.MissingPropertiesError):
		openc2.v10.Response(**{'status_text': "OK"})

def test_invalid_empty_response3():
	with pytest.raises(openc2.exceptions.MissingPropertiesError):
		openc2.v10.Response(**{'results': {'versions': '1.0'}})

def test_invalid_empty_response4():
	with pytest.raises(openc2.exceptions.MissingPropertiesError):
		openc2.v10.Response(**{'status_text': "OK", 'results': {'versions': '1.0'}})

def test_invalid_empty_response5():
	with pytest.raises(openc2.exceptions.ExtraPropertiesError):
		openc2.v10.Response(**{'statuss': 200})


@pytest.mark.parametrize("status", ["OK", "", None])
def test_invalid_status(status):
	with pytest.raises(Exception) as e:
		print("Exception: ", e.type)
		openc2.v10.Response(**{'status': status})


