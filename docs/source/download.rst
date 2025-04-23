Download and setup
~~~~~~~~~~~~~~~~~~

The openc2lib is currently available as source code only. Dowload it
from github:

::

   git clone https://github.com/mattereppe/openc2.git

(this creates an ``openc2`` folder).

First, create a virtual environment and populate it with Python
dependecies:

::

   python3 -m venv .oc2-env
   . .oc2-env/bin/activate
   pip install -r requirements.txt

To use the library you must include the ``<installdir>/src/`` the Python
path according to the download directory. You can either: - add the
library path in your code (this must be done for every module):
``import sys   sys.path.append('<_your_path_here_>')`` - add the library
path to the PYTHONPATH environmental variable (this is not persistent
when you close the shell):
``export PYTHONPATH=$PYTHONPATH':<_your_path_here_>'`` - add the library
path to the venv (this is my preferred option):
``echo '<_your_path_here_>/src' > .oc2-env/lib/python3.11/site-packages/openc2lib.pth``

A few scripts are available in the ``examples`` folder of the repository
for sending a simple commmand to a remote actuator (see
`Usage <#usage>`__).
