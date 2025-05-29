import pytest

from otupy import Device, Hostname, IDNHostname


@pytest.mark.parametrize("hostname", ["localhost", "localhost.localdomain"])
@pytest.mark.parametrize("idn_hostname",["lòcalhøst", "lùcàl-èst", "håsçø"])
@pytest.mark.parametrize("device_id", ["device", "dxe-dfa-xffd-xffdf", "ffeeddccbbaa99887766554433221100"])
def test_device(hostname,idn_hostname, device_id):
	assert type(Device({'hostname':Hostname(hostname), 'idn_hostname':IDNHostname(idn_hostname), 'device_id':device_id}))

@pytest.mark.parametrize("hostname", ["localhost"])
@pytest.mark.parametrize("idn_hostname",["lòcalhøst"])
def test_device_types(hostname, idn_hostname):
	assert type(Device(hostname=Hostname(hostname), idn_hostname=idn_hostname))
	assert type(Device({'hostname': hostname}, idn_hostname=idn_hostname))


@pytest.mark.parametrize("hostname", ["localhost", "localhost.localdomain"])
@pytest.mark.parametrize("idn_hostname",["lòcalhøst", "lùcàl-èst", "håsçø"])
@pytest.mark.parametrize("device_id", ["device", "dxe-dfa-xffd-xffdf", "ffeeddccbbaa99887766554433221100"])
def test_device2(hostname,idn_hostname, device_id):
	assert type(Device({'hostname':Hostname(hostname), 'idn_hostname':IDNHostname(idn_hostname), 'device_id':hostname}))

@pytest.mark.parametrize("hostname", ["localhost", "localhost.localdomain"])
@pytest.mark.parametrize("idn_hostname",["lòcalhøst", "lùcàl-èst", "håsçø"])
@pytest.mark.parametrize("device_id", ["device", "dxe-dfa-xffd-xffdf", "ffeeddccbbaa99887766554433221100"])
def test_device3(hostname,idn_hostname, device_id):
		assert type(Device({'hostname':hostname, 'idn_hostname':IDNHostname(idn_hostname), 'device_id':device_id})) == Device

@pytest.mark.parametrize("hostname", ["localhost", "localhost.localdomain"])
@pytest.mark.parametrize("idn_hostname",["lòcalhøst", "lùcàl-èst", "håsçø"])
@pytest.mark.parametrize("device_id", ["device", "dxe-dfa-xffd-xffdf", "ffeeddccbbaa99887766554433221100"])
def test_device4(hostname,idn_hostname, device_id):
		assert type(Device({'hostname':Hostname(hostname), 'idn_hostname':idn_hostname, 'device_id':device_id})) == Device

@pytest.mark.parametrize("hostname", ["localhost", "localhost.localdomain"])
@pytest.mark.parametrize("idn_hostname",["lòcalhøst", "lùcàl-èst", "håsçø"])
@pytest.mark.parametrize("device_id", ["device", "dxe-dfa-xffd-xffdf", "ffeeddccbbaa99887766554433221100"])
def test_device5(hostname,idn_hostname, device_id):
		assert type(Device({'hostname':Hostname(hostname), 'idn_hostname':idn_hostname, 'device_id':Hostname(hostname)})) == Device

@pytest.mark.parametrize("hostname", ["localhost", "localhost.localdomain"])
@pytest.mark.parametrize("idn_hostname",["lòcalhøst", "lùcàl-èst", "håsçø"])
@pytest.mark.parametrize("device_id", ["device", "dxe-dfa-xffd-xffdf", "ffeeddccbbaa99887766554433221100"])
def test_device6(hostname,idn_hostname, device_id):
	with pytest.raises(Exception):
		Device({'hostname':IDNHostname(idn_hostname), 'idn_hostname':IDNHostname(idn_hostname), 'device_id':device_id})


def test_void_device():
	with pytest.raises(Exception):
		Device()
