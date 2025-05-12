# process_ext.py

from openc2lib.types.targets.process import Process as BaseProcess
from openc2lib.types.base import Map
from openc2lib.profiles.rcli.profile import Profile  # Assuming this exists
from openc2lib.profiles.rcli.data.state import State  # Assuming this exists

class Process(BaseProcess):
    base = BaseProcess
    fieldtypes = dict(BaseProcess.fieldtypes)
    fieldtypes.update({
        'state': State, 
    })

# Register under your namespace (e.g., 'myprof')
BaseProcess.register = {
    Profile.nsid: Process
}
