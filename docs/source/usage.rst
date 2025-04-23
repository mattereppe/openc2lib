Usage
-----

Basic usage description covers the step to instantiate the ``Producer`` and the ``Consumer``, and to send messages. 
This requires the availability of a minimal set of encoders, transfer protocols, profiles, and actuator implementations. 
See the `Developing extensions <docs/developingextensions.md>`__ Section to learn how to add your custom extensions. 
  
In the following we refer to the implementation of a ``Controller`` that sends *Commands* and a ``Server`` that controls
local security functions. Simple implementation of these functions are provided in the ``examples`` folder.

Create a Server
~~~~~~~~~~~~~~~

A ``Server`` is intended to instantiate and run the OpenC2 ``Consumer``.
Instantiation requires the definition of the protocol stack and the
configuration of the ``Actuator``s that will be exposed.

As a preliminary step, the necessary modules must be imported. Note that
``otupy`` only includes core grammar and syntax elements, and all
the necessary extensions (including encoders, trasfer protocols,
profiles, and actuators) must be imported separetely. We will use json
encoding and HTTP for our protocol stack, and an iptables actuator for
stateless packet filtering:

.. code-block:: python3

   import otupy as oc2

   from otupy.encoders.json_encoder import JSONEncoder
   from otupy.transfers.http_transfer import HTTPTransfer

   import otupy.profiles.slpf as slpf
   from otupy.actuators.iptables_actuator import IptablesActuator

First, we instantiate the ``IptablesActuator`` as an implementation of
the ``slpf`` profile:

.. code-block:: python3

    actuators = {}
    actuators[(slpf.nsid,'iptables')]=IptablesActuator()

(there is no specific configuration here because the
``IptablesActuator`` is currently a mockup)

Next, we create the ``Consumer`` by instantiating its execution
environment with the list of served ``Actuator``s and the protocol
stack. We also provide an identification string:

.. code-block:: python3

   consumer = oc2.Consumer("consumer.example.net", actuators, JSONEncoder(), HTTPTransfer("127.0.0.1", 8080))

(the server will be listening on the loopback interface, port 8080)

Finally, start the server:

.. code-block:: python3

    consumer.run()

The server code can indeed be improved by loading the configuration from
file and setting up `Logging for otupy <docs/logging.md>`__.

Create the Controller
~~~~~~~~~~~~~~~~~~~~~

A ``Controller`` is intended to instantiate an OpenC2 ``Producer`` and
to use it to control a remote security function. Instantiation requires
the definition of the same protocol stack we used for the server, and an
identifier:

.. code-block:: python3

   producer = oc2.Producer("producer.example.net", JSONEncoder(), HTTPTransfer("127.0.0.1", 8080))

(the same modules must be imported as for the ``Server`` but the
``iptables_actuator``)

Next we create the ``Command``, by combining the *Action*, *Target*,
*Arguments*, and *Actuator*. We will query the remote ``slpf`` actuator
for its capabilities. Note how we mix common language elements with
specific extensions for the ``slpf`` profile, as expected by the
Specification:

.. code-block:: python3

   pf = slpf.slpf({'hostname':'firewall', 'named_group':'firewalls', 'asset_id':'iptables'})
   arg = slpf.ExtArgs({'response_requested': oc2.ResponseType.complete})
    
   cmd = oc2.Command(oc2.Actions.query, oc2.Features(), actuator=pf)

Finally, we send the command and catch the response:

.. code-block:: python3

   resp = p.sendcmd(cmd)

(print out ``resp`` to check what the server returned)

A concrete implementation of a *Controller* would also include the
business logic to update rules on specific events (even by specific
input from the user).

