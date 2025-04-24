Architecture
============

The ``otupy`` provides the implementation of the *Producer* and *Consumer* roles, as defined by the `Language
Specification <https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.pdf>`__.
The *Producer* creates and sends *Messages* to the *Consumer*; the latter returns *Responses*. 
Within the *Consumer*, *Actuators* translate the *Commands* into the specific instructions to control local or remote
*Security Functions*, and collect any feedback on their execution.

.. figure:: Pictures/architecture.png
   :alt: High-level architecture of the ``otupy`` and intended usage

   High-level architecture of the ``otupy`` and intended usage

The *Producer* and the *Consumer* usually run on different hosts
separated by a network. While the *Producer* is expected to be used as
Python library within existing code (for example, a controller), the
*Consumer* is a server process that listens on a given port waiting for
*Commands*.

``otupy`` provides the ``Provider`` and ``Consumer`` classes that
implements the *Provider* and *Consumer* role, respectively. Each class
creates its own execution environment made of its own identifier, a
protocol stack, and the available *Actuators* (this last only for the
``Consumer``). According to the `OpenC2
Architecture <https://docs.oasis-open.org/openc2/oc2arch/v1.0/cs01/oc2arch-v1.0-cs01.pdf>`__,
a protocol stack includes an encoding language and a transfer protocol.
Note that in the ``otupy`` implementation, the security services and
transport protocols are already embedded in each specific transfer
protocol.

.. figure:: Pictures/classes.png
   :alt: Instantiation of the main ``otupy`` classes

   Instantiation of the main ``otupy`` classes

Building on the definitions in the OpenC2 Architecture and Language
Specification, the ``otupy`` defines a *profile* as the language
extension for a specific class of security functions, whereas an
*actuator* is the concrete implementation for a specific security
appliance. For instance, the `OpenC2 Profile for Stateless Packet
Filtering <https://docs.oasis-open.org/openc2/oc2slpf/v1.0/cs01/oc2slpf-v1.0-cs01.pdf>`__
is a *profile* that defines all grammar and syntax rules for adding and
removing rules from a packet firewall. The corresponding *actuators*
must translate this abstract interface to concrete commands (e.g., for
iptables, pfsense). A more detailed discussion is present in the
:doc:`developingextensions` Section.


