import pytest
import parametrize_from_file
from openc2lib.profiles.fclm.targets.monitor_id import MonitorID

@parametrize_from_file("parameters/test_monitor_id_target.yml")
def test_good_monitor_id_target(monitor_id):
    obj = MonitorID(monitor_id)
    assert isinstance(obj, MonitorID)
    assert str(obj) == monitor_id

@parametrize_from_file("parameters/test_monitor_id_target.yml")
def test_bad_monitor_id_target(bad_monitor_id):
    with pytest.raises((TypeError, ValueError)):
        MonitorID(bad_monitor_id)

