import pytest

from otupy import Features, Feature, IPv4Net

def all_feature():
	return [f for f in Feature]

@pytest.mark.parametrize("feature", [ 5, Feature.versions, IPv4Net("10.0.0.1")])
def test_feature_type_wrong(feature):
	with pytest.raises(Exception):
		Features(feature)

@pytest.mark.parametrize("feature", [(1,), (4,), "versions", ["versions"], (Feature.versions,) ])
def test_feature_type(feature):
	assert type(Features(feature) ) == Features

@pytest.mark.parametrize("feature", [f for f in Feature])
def test_feature_type_ok(feature):
	assert type(Features([feature]) ) == Features

@pytest.mark.parametrize("feature", [f for f in Feature])
def test_feature_type_num(feature):
	assert type(Features([feature]*10) ) == Features

@pytest.mark.parametrize("feature", [f for f in Feature])
def test_feature_type_max(feature):
	with pytest.raises(Exception): 
		type(Features([feature]*11) ) == Features

