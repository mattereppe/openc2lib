Adding new encoding formats
---------------------------

Encoders are necessary to support new encoding formats. The definition
of an ``Encoder`` must follows the general architecture described in the
`Developer
guide <https://github.com/mattereppe/openc2/blob/main/docs/developerguide.md#developer-guide>`__.
In a nutshell, each ``Encoder`` is expected to serialize OpenC2
messages. The translation between Python objects and dictionaries is
already provided by the base ``Encoder`` class (by the
``Encoder.todict()`` and ``Encoder.fromdict()`` methods, which new
Encoders are expected to extend.

The definition of a new ``Encoder`` must provide: - a method ``encode``
for serializing OpenC2 commands; - a method ``decode`` for deserializing
OpenC2 messages; - a class member ``encoder_type`` with the name of the
Encoder; - registration of the new ``Encoder`` via the
``@register_encoder`` decorator.

.. code-block:: python3

   @register_encoder
   class MyEncoder(Encoder):
     encoder_type = 'json'

     @staticmethod
     def encode(obj):
         (dic =  Encoder.todict(obj) )
         ...

     @staticmethod
     def decode(msg, msgtype=None):
        ...
        ( return Encoder.fromdict(msgtype, msg) )

See the `Developer
guide <https://github.com/mattereppe/openc2/blob/main/docs/developerguide.md#developer-guide>`__
for more detail about the base ``Encoder`` class and the available
Encoders.

