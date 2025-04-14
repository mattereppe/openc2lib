import pytest 
import json
import datetime

from otupy import *
import otupy.profiles.slpf as slpf
from otupy.transfers.http import HTTPTransfer
from otupy.encoders.json import  JSONEncoder

# Parameters to send bad messages to an OpenC2 Consumer
scheme='http'
host='127.0.0.1'
port=8080
endpoint='/.well-known/openc2'

@pytest.fixture
def query_feature():

	pf = slpf.Specifiers({'hostname': 'firewall', 'named_group': 'firewalls', 'asset_id': 'iptables'})
	
	arg = slpf.Args({'response_requested': ResponseType.complete})
	#	arg = slpf.Args({'response_requested': ResponseType.none})
	
	return Command(Actions.query, Features([Feature.versions, Feature.profiles, Feature.pairs]), arg, actuator=pf)

@pytest.fixture
def create_producer():
	producer = Producer("OpenC2_Producer",
	                     JSONEncoder(),
                        HTTPTransfer("127.0.0.1",
                                     8080,
                                     endpoint="/.well-known/openc2"))
	return producer


@pytest.fixture
def http_headers():
	return {'Content-Type': 'application/openc2+json;version=1.0', 'Accept': 'application/openc2+json;version=1.0', 'Date': datetime.datetime.now(datetime.timezone.utc).strftime('%a, %d %b %Y %H:%M:%S %Z') }

@pytest.fixture
def http_body():
	return  {'headers': { "request_id": "0e3d8fa8-0bae-4055-a341-9c97b4f328f7", "created": 1545257700000, "from": "test-producer", "to": [ "test-consumer" ] },
		"body": { "openc2": { "request": {} }}}


@pytest.fixture
def http_url():
	return f"{scheme}://{host}:{port}{endpoint}"
