otupy: OpenC2 Utilities for Python
==================================

otupy (/’əʊtu:paɪ/) is an open-source implementation of the OpenC2
language written in Python. 

Description
-----------

otupy is explicitly designed with flexibility
and extensibility in mind, meaning that additional profiles and
actuators can be added without impacting the core library itself. For
this reason, it is particullary suited for: 

* developers that are looking for a common interface to control their remote cybersecurity functions; 
* researchers that design new profiles for cybersecurity functions; 
* system integrators that need a common language for their cybersecurity frameworks.

Usage and extension of otupy have a shallow learning curve because data
structures are explicitly designed to follow the language specification.
Differently from many other implementations publicly available,
introducing new transfer protocols, new message encoding formats, new
profiles, and new implementations of actuators does not require
modification to the core package; these extensions are easily to
introduce because they largely reflect the language specification, hence
minimal comprehension of the otupy is required to getting started.

The otupy currently provides:

* the implementation of the core functions that implement the OpenC2 Architecture and Language Specification; 
* an implementation of the json encoder; 
* an implementation of the HTTP transfer protocol; 
* the definition of the SLPF profile; 
* a dumb implementation of an actuator for the SLPF profile.

Getting started
---------------

Background
~~~~~~~~~~

Before using openc2lib you must be familiar with the `OpenC2 Language
Specification <https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.pdf>`__.
Even if not strictly required to getting started with the code, the
`OpenC2 Architecture
Specification <https://docs.oasis-open.org/openc2/oc2arch/v1.0/cs01/oc2arch-v1.0-cs01.pdf>`__
provides a good introduction to OpenC2 architectural patterns and
terminology. Other relevant documentation is listed in the `Related
documents <docs/relateddocuments.md>`__ Section.

Architecture
~~~~~~~~~~~~

The openc2lib provides the implementation of the *Producer* and
*Consumer* roles, as defined by the `Language
Specification <https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.pdf>`__.
The *Producer* creates and sends *Messages* to the *Consumer*; the
latter returns *Responses*. Within the *Consumer*, *Actuators* translate
the *Commands* into the specific instructions to control local or remote
*Security Functions*, and collect any feedback on their execution.

.. figure:: docs/Pictures/architecture.svg
   :alt: High-level architecture of the openc2lib and intended usage

   High-level architecture of the openc2lib and intended usage

The *Producer* and the *Consumer* usually run on different hosts
separated by a network. While the *Producer* is expected to be used as
Python library within existing code (for example, a controller), the
*Consumer* is a server process that listens on a given port waiting for
*Commands*.

openc2lib provides the ``Provider`` and ``Consumer`` classes that
implements the *Provider* and *Consumer* role, respectively. Each class
creates its own execution environment made of its own identifier, a
protocol stack, and the available *Actuators* (this last only for the
``Consumer``). According to the `OpenC2
Architecture <https://docs.oasis-open.org/openc2/oc2arch/v1.0/cs01/oc2arch-v1.0-cs01.pdf>`__,
a protocol stack includes an encoding language and a transfer protocol.
Note that in the openc2lib implementation, the security services and
transport protocols are already embedded in each specific transfer
protocol.

.. figure:: docs/Pictures/classes.svg
   :alt: Instantiation of the main openc2lib classes

   Instantiation of the main openc2lib classes

Building on the definitions in the OpenC2 Architecture and Language
Specification, the openc2lib defines a *profile* as the language
extension for a specific class of security functions, whereas an
*actuator* is the concrete implementation for a specific security
appliance. For instance, the `OpenC2 Profile for Stateless Packet
Filtering <https://docs.oasis-open.org/openc2/oc2slpf/v1.0/cs01/oc2slpf-v1.0-cs01.pdf>`__
is a *profile* that defines all grammar and syntax rules for adding and
removing rules from a packet firewall. The corresponding *actuators*
must translate this abstract interface to concrete commands (e.g., for
iptables, pfsense). A more detailed discussion is present in the
`Developing extensions <docs/developingextensions.md>`__ Section.

Software requirements
~~~~~~~~~~~~~~~~~~~~~

Python 3.9+ is required to run the openc2lib (Python 3.11 was used for
development).

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

Usage
-----

Basic usage description covers the step to instantiate the ``Producer``
and the ``Consumer``, and send messages. This requires the availability
of a minimal set of encoders, transfer protocols, profiles, and actuator
implementations. See the `Developing
extensions <docs/developingextensions.md>`__ Section to learn how to add
your custom extensions. In the following we refer to the implementation
of a ``Controller`` that sends *Commands* and a ``Server`` that controls
local security functions. Simple implementation of these functions are
provided in the ``examples`` folder.

Create a Server
~~~~~~~~~~~~~~~

A ``Server`` is intended to instantiate and run the OpenC2 ``Consumer``.
Instantiation requires the definition of the protocol stack and the
configuration of the ``Actuator``\ s that will be exposed.

As a preliminary step, the necessary modules must be imported. Note that
the openc2lib only includes core grammar and syntax elements, and all
the necessary extensions (including encoders, trasfer protocols,
profiles, and actuators) must be imported separetely. We will use json
encoding and HTTP for our protocol stack, and an iptables actuator for
stateless packet filtering:

::

   import openc2lib as oc2

   from openc2lib.encoders.json_encoder import JSONEncoder
   from openc2lib.transfers.http_transfer import HTTPTransfer

   import openc2lib.profiles.slpf as slpf
   from openc2lib.actuators.iptables_actuator import IptablesActuator

First, we instantiate the ``IptablesActuator`` as an implementation of
the ``slpf`` profile:

::

    actuators = {}
    actuators[(slpf.nsid,'iptables')]=IptablesActuator()

(there is no specific configuration here because the
``IptablesActuator`` is currently a mockup)

Next, we create the ``Consumer`` by instantiating its execution
environment with the list of served ``Actuator``\ s and the protocol
stack. We also provide an identification string:

::

   consumer = oc2.Consumer("consumer.example.net", actuators, JSONEncoder(), HTTPTransfer("127.0.0.1", 8080))

(the server will be listening on the loopback interface, port 8080)

Finally, start the server:

::

    consumer.run()

The server code can indeed be improved by loading the configuration from
file and setting up `Logging for openc2lib <docs/logging.md>`__.

Create the Controller
~~~~~~~~~~~~~~~~~~~~~

A ``Controller`` is intended to instantiate an OpenC2 ``Producer`` and
to use it to control a remote security function. Instantiation requires
the definition of the same protocol stack we used for the server, and an
identifier:

::

   producer = oc2.Producer("producer.example.net", JSONEncoder(), HTTPTransfer("127.0.0.1", 8080))

(the same modules must be imported as for the ``Server`` but the
``iptables_actuator``)

Next we create the ``Command``, by combining the *Action*, *Target*,
*Arguments*, and *Actuator*. We will query the remote ``slpf`` actuator
for its capabilities. Note how we mix common language elements with
specific extensions for the ``slpf`` profile, as expected by the
Specification:

::

   pf = slpf.slpf({'hostname':'firewall', 'named_group':'firewalls', 'asset_id':'iptables'})
   arg = slpf.ExtArgs({'response_requested': oc2.ResponseType.complete})
    
   cmd = oc2.Command(oc2.Actions.query, oc2.Features(), actuator=pf)

Finally, we send the command and catch the response:

::

   resp = p.sendcmd(cmd)

(print out ``resp`` to check what the server returned)

A concrete implementation of a *Controller* would also include the
business logic to update rules on specific events (even by specific
input from the user).

Advanced usage
--------------

Advanced usage of the openc2lib requires knowledge of its data
structures and functions. Data structures are very straightforward to
learn, because they strictly follow the definition and requirements in
the common Language Specification and Profile extensions. See the
`Developer guide <docs/developerguide.md>`__ for a comprehensive
description of the library structure.

[comment]: <> User documentation of the openc2lib is available
`here <docs/code/index.html>`__. User documentation of the openc2lib
code can be generated by running the following command in the root tree:

::

   pdoc src/openc2lib/ -o docs/code/

To view the documentation, open the ``docs/code/index.html`` in your
browser.

Extensions
----------

openc2lib comes with several extensions and use cases: - The Context
Discovery profile and its actuators for OpenStack and Kubernetes
(documentation
`here <https://github.com/mattereppe/openc2lib/blob/main/docs/CTXD%20documentation.md>`__)

Support
-------

TODO

Limitations, main issues, and known bugs
----------------------------------------

Too many to be listed here! :-(

Contributing
------------

Contributions are wellcome for the implementation of the following
extensions: - encoding format beyond json (no specification available);
- transfer protocols (MQTT first); - implementation of SLPF
``Actuator``\ s for different firewall technologies (both opensource and
proprietary). - implementation of new and draft profiles.

Authors and acknowledgment
--------------------------

-  The Context Discovery profile, its actuators and use cases have been
   developed by Silvio Tanzarella.

License
-------

Licensed under the `EUPL v1.2 <https://eupl.eu/1.2/en/>`__.
