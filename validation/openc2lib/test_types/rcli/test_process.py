import pytest
from openc2lib.profiles.rcli.data.process import Process
from openc2lib.types.targets import File
from openc2lib.profiles.rcli.data.state import State
import pytest
import string
import random

def random_params(args):
	""" Generate random argument patterns

		For all possible number of arguments (1 to 6), this function creates random tuples by picking the corresponding number of arguments from the 
		list provided below.
		Running the test multiple times, will consist of different selections, but this is not much useful, since the parameters are 
		always the same.
	"""
	params = []
	for i in range(1, len(args)):
		param = {}
		for j in range(1,i+1):
			idx = random.randint(0,len(args)-1)
			k = list(args)[idx]
			v = args[list(args)[idx]]
			print("arg: ", k, v)
			print({k: v})
			param.update({k: v})
			print(param)
		params.append(param)
	return params

def random_strings():
	rnd = []
	for i in range (0,1):
		for length in range (10,12):
			rnd.append(  ''.join(random.choices(string.ascii_lowercase, k=length)) )
			rnd.append(''.join(random.choices(string.ascii_lowercase + string.digits, k=length)))
			rnd.append(''.join(random.choices(string.printable, k=length)))
	return rnd


@pytest.mark.parametrize("state", [State.running, State.sleeping, State.zombie])
@pytest.mark.parametrize("name", random_strings())
@pytest.mark.parametrize("pid", [random.randint(0, 65535) for _ in range(1)])
@pytest.mark.parametrize("cwd", random_strings())
@pytest.mark.parametrize("executable", [File({'name': 'program.exe'}), {'path': '/usr/sbin/program'}])
@pytest.mark.parametrize("parent", [Process({'name':"parent", 'pid':0, 'cwd':'/var/run', 'command_line':'/usr/bin/run'})])
@pytest.mark.parametrize("command_line", random_strings())
def test_random_input_with_state(pid, name, cwd, executable, parent, command_line, state):
    p = Process({
        'name': name, 'pid': pid, 'cwd': cwd, 'parent': parent,
        'command_line': command_line, 'state': state,
        'executable': executable
    })
    assert isinstance(p, Process)
    assert isinstance(p['state'], State)



@pytest.mark.parametrize("state", [State.zombie])
@pytest.mark.parametrize("name", ["process"])
@pytest.mark.parametrize("pid", [64])
@pytest.mark.parametrize("cwd", ["/var/run/myprocess"])
@pytest.mark.parametrize("executable", [{"name": "process.exe"}])
@pytest.mark.parametrize("parent", [{'name':"parent", 'pid':0, 'cwd':'/var/run', 'command_line':'/usr/bin/run'}])
@pytest.mark.parametrize("command_line", ["/usr/local/bin/process.exe"])
def test_random_parameters_with_state(pid, name, cwd, executable, parent, command_line, state):
    p = Process({
        'name': name, 'pid': pid, 'cwd': cwd, 'executable': executable,
        'parent': parent, 'command_line': command_line, 'state': state
    })
    assert isinstance(p, Process)
    assert isinstance(p['state'], State)


@pytest.mark.parametrize("args" , random_params({'name': "process.exe", 'pid': 45, 'cwd': "/var/run/process", 'executable': {'name': "/usr/local/bin/executable.exe"}, 'parent': {'name':"parent", 'pid':0, 'cwd':'/var/run', 'command_line':'/usr/bin/run'} , 'command_line': 'usr/local/bin/executable.exe -a param1 -b param2'} ) )
def test_random_parameters(args):
	p = Process(args)	
	assert type(p) == Process

def test_void_process():
	with pytest.raises(Exception):
		Process()
