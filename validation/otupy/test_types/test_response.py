import pytest

from otupy import Response, StatusCode, Results, Version


@pytest.mark.parametrize("status", [StatusCode.OK, StatusCode.PROCESSING, 
		StatusCode.UNAUTHORIZED, StatusCode.FORBIDDEN, StatusCode.NOTFOUND, 
		StatusCode.INTERNALERROR, StatusCode.NOTIMPLEMENTED, 
		StatusCode.SERVICEUNAVAILABLE ])
def test_valid_status(status):
	assert type(Response({'status': status})) == Response

@pytest.mark.parametrize("status", [StatusCode.OK, StatusCode.PROCESSING ])
@pytest.mark.parametrize("status_text", [ "", None, "OK", "Processing" ])
def test_valid_text(status, status_text):
	assert type(Response({'status': status, 'status_text': status_text})) == Response

def test_invalid_empty_response():
	with pytest.raises(ValueError):
		Response({})

def test_invalid_empty_response2():
	with pytest.raises(ValueError):
		Response({'status_text': "OK"})

def test_invalid_empty_response3():
	with pytest.raises(ValueError):
		Response({'results': Results({'versions': Version(1,0)})})

def test_invalid_empty_response4():
	with pytest.raises(ValueError):
		Response({'status_text': "OK", 'results': Results({'versions': Version(1,0)})})

def test_invalid_empty_response5():
	with pytest.raises(KeyError):
		Response({'statuss': StatusCode.OK})


@pytest.mark.parametrize("status", ["OK", "", None])
def test_invalid_status(status):
	with pytest.raises(Exception) as e:
		print("Exception: ", e.type)
		Response({'status': status})


