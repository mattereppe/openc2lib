import pytest
import random
import string

import utils
from openc2.v10 import Process, File

def random_strings():
	rnd = []
	for i in range (0,1):
		for length in range (10,12):
			rnd.append(  ''.join(random.choices(string.ascii_lowercase, k=length)) )
			rnd.append(''.join(random.choices(string.ascii_lowercase + string.digits, k=length)))
			rnd.append(''.join(random.choices(string.printable, k=length)))
	return rnd


@pytest.mark.parametrize("name", random_strings())
@pytest.mark.parametrize("pid", [random.randint(3, 65535) for i in range (0,1)])
@pytest.mark.parametrize("cwd", random_strings())
@pytest.mark.parametrize("executable", [ File(**{'name': 'program.exe'}), {'path': '/usr/sbin/program'}])
@pytest.mark.parametrize("parent", [Process(**{'name':"parent", 'pid':0, 'cwd':'/var/run', 'command_line':'/usr/bin/run'})])
@pytest.mark.parametrize("command_line", random_strings())
def test_random_input(pid, name, cwd, executable, parent, command_line):
	print(name)
	assert type(Process(name=name, pid=pid, cwd=cwd, parent=parent, command_line=command_line)) == Process



@pytest.mark.parametrize("name", ["process"])
@pytest.mark.parametrize("pid", [ 64 ])
@pytest.mark.parametrize("cwd", ["/var/run/myprocess"])
@pytest.mark.parametrize("executable", [ {"name": "process.exe"} ])
@pytest.mark.parametrize("parent", [{'name':"parent", 'pid':0, 'cwd':'/var/run', 'command_line':'/usr/bin/run'}])
@pytest.mark.parametrize("command_line", ["/usr/local/bin/process.exe"])
def test_random_parameters(pid, name, cwd, executable, parent, command_line):
	p = Process(**{'name': name, 'pid': pid, 'cwd': cwd, 'executable': File(**executable), 'parent': Process(**parent), 'command_line': command_line})
	assert type(p) == Process
	assert type(p['pid']) == int
	assert type(p['name']) == str
	assert type(p['cwd']) == str
	assert type(p['executable']) == File
	assert type(p['parent']) == Process
	assert type(p['command_line']) == str

@pytest.mark.parametrize("args" , utils.random_params({'name': "process.exe", 'pid': 45, 'cwd': "/var/run/process", 'executable': File(**{'name': "/usr/local/bin/executable.exe"}), 'parent': Process(**{'name':"parent", 'pid':0, 'cwd':'/var/run', 'command_line':'/usr/bin/run'}) , 'command_line': 'usr/local/bin/executable.exe -a param1 -b param2'} ) )
def test_random_parameters(args):
	p = Process(**args)	
	assert type(p) == Process

def test_void_process():
	with pytest.raises(Exception):
		Process()
