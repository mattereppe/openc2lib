Implement concrete actuators
----------------------------

Concrete actuators are server applications that translate an
``Actuator`` profile into commands and configurations on security
functions. The same ``Actuator`` profile may be implemented by multiple
concrete actuators, depending on the technology of the security function
(e.g., an SLPF actuator may be used to control ``iptables``,
``pfsense``, etc.).

Implementing an ``Actuator`` is really straightforward. There is only
one requirement for its interface: - an ``Actuator`` must implement a
``run(cmd)`` method that processes a command and returns the response.

::

   class Actuator:
     
     def run(self, cmd):
        ...
       return response

Internally, an ``Actuator`` is expected to have the configuration to
locate the device it is controlling and the code to control it. It is
also expected to perform command validation, to detect any action or
option that it does not support (which may be more restrictive than the
generic profile validation).
