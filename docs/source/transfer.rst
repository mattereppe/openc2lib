Adding new transfer protocols
-----------------------------

A transfer protocol is derived from the ``Transfer`` class:

.. code-block:: python3

   class Transfer:

      def send(self, msg, encoder):
         pass

     def receive(self, callback, encode):
        pass

A ``Transfer`` implementation is used for both sending and receiving
OpenC2 messages, by using the the ``send()`` and ``receive()`` method,
respectively. The ``receive()`` method is expected to be blocking and to
wait for messages until termination of the application.

The ``send()`` takes an OpenC2 ``Message`` as first argument, which is
expected to carry a ``Content``. It returns the ``Response`` within
another ``Message``. The ``Encoder`` must be passed as second argument,
and it is possible to use a different ``Encoder`` for each individual
message. The ``send()`` message is used by the ``Producer``.

The ``receive()`` takes a callback function from the ``Consumer``, which
is used to dispatch incoming messages to the corresponding ``Actuator``.
The ``Encoder`` must be passed as second argument, but it is only used
when the encoding format is not present in the metadata; it is also used
to answer messages in unknown formats.

The implementation of a ``Transfer`` is expected to: - perform any
protocol-specific initialization, including loading configurations
(e.g., certificates to be used in TLS/SSL handshakes); - manage the
transmission and reception of ``Message`` metadata in a
protocol-dependent way (this is defined by each corresponding OpenC2
specification).

Implementation of new ``Transfer``\ s included in ``otupy`` must be
placed in the ``transfers`` folder and be self-contained in a single
module.

