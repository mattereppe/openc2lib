import random
import string
import pytest
from openc2lib.profiles.rcli.data.process import Process
from openc2lib.profiles.rcli.targets.processes import Processes
from openc2lib.profiles.rcli.data.state import State
from openc2lib.types.base import ArrayOf, Array
from openc2lib.types.targets import File

def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_command_line():
    return f"/usr/bin/{random_string(5)} --arg1 val1 --arg2 {random.randint(1, 100)}"

def create_random_process(index=0):
    return Process({
        "name": f"proc_{index}_{random_string(4)}",
        "pid": random.randint(1, 65535),
        "cwd": f"/var/tmp/{random_string(5)}",
        "executable": File({"name": f"exec_{index}.bin"}),
        "parent": {
            "name": f"parent_{index}",
            "pid": random.randint(1, 1000),
            "cwd": "/",
            "command_line": "/init"
        },
        "command_line": random_command_line(),
        "state": random.choice(list(State))
    })

def generate_array_of_processes(n=5):
    processes = [create_random_process(i) for i in range(n)]
    return Processes(processes)

def test_array_of_processes_type():
    array = generate_array_of_processes(5)
    assert isinstance(array, Processes)  # Or ArrayOf(Process)
    assert all(isinstance(p, Process) for p in array)

def test_array_of_processes_too_many():
    with pytest.raises(ValueError):
        array = generate_array_of_processes(20)
        array.validate(types=True, num_max=10)

# Test for Large Arrays of Processes
def test_large_array_of_processes():
    array = generate_array_of_processes(10)
    assert isinstance(array, Processes)
    assert all(isinstance(p, Process) for p in array)
