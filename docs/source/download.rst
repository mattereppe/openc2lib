Download and setup
~~~~~~~~~~~~~~~~~~

``otupy`` is currently available as Python package and source code.

Install the package with `pip`:

.. code-block:: bash

   pip install otupy


Alternatively, download it from ``github``:

.. code-block:: bash

   git clone https://github.com/mattereppe/otupy.git

(this creates an ``otupy`` folder).
In this case, you have to manually install all dependencies:

.. code-block:: bash

   pip install -r requirements.txt

If you installed from ``github``, you might want to create and run it in a virtual environment.
First, create a virtual environment and populate it with Python
dependecies:

.. code-block:: bash

   python3 -m venv .env
   . .env/bin/activate
   pip install -r requirements.txt

To use the library, you must include the ``<installdir>/src/`` in the Python path. 
You can either: 

- add the library path in your code (this must be done for every module):

.. code-block:: python3

   import sys   
   sys.path.append('<_your_path_here_>') 

- add the library path to the ``PYTHONPATH`` environmental variable (this is not persistent when you close the shell):

.. code-block:: bash

   export PYTHONPATH=$PYTHONPATH':<_your_path_here_>'

- add the library path to the venv (this is my preferred option):

.. code-block:: bash

   echo '<_your_path_here_>/src' > .env/lib/python3.11/site-packages/otupy.pth

A few scripts are available in the ``examples`` folder of the repository for sending a simple commmand to a remote actuator (see
:doc:`usage`).
