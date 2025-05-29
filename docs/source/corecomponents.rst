Core components
---------------

Core components includes the implementation of the common language
elements (i.e., those described in the `OpenC2 Language
Specification <https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.pdf>`__.

Producer
~~~~~~~~

Producer is the entry point abstraction to send Commands to a peer and
receive its responses. It should kept all relevant data of the
communication (e.g., name of the producer). However, each message can be
sent to a different endpoint from the same producer (hence, the
corresponding attributes should be passed to the send method).

Messages
~~~~~~~~

This is another major change to my previous understanding. After
re-considering the code in a more thorough manner, I came to these
conclusions: 

1. The correct terminology used by the language specification is Command and Response, so we will use these from now on. Indeed, the transfer specification for HTTP might seem ambiguous on this point, since it refers to Request/Response. However, this terminology is referred to HTTP, not OpenC2: an HTTP Request carries an OpenC2 Command, and an HTTP Response carries an OpenC2 Response (same term in the second case). 
2. Command/Response are a type of content, so they are now derived from this base class. Indeed, the class Content is empty, but we use it to have a common reference to hold both a Command and a Response element (this is used in the Message class). 
3. Message is indeed poorly defined in the standard, and I really realized that only recently. The language specification lists the fields of the  Message element at the beginning of Sec. 3.2, but does not dictates its structure as for the other elements. I came to the conclusion that there is not explicit definition of a Message structure (this intuition is confirmed by the fact the all examples in the language specification only show Commands/Responses, but not full Messages). Only after reading carefully the text, I noticed that “transfer specifications define the on-the-wire format of a Message”, which means that only the concrete transfer specification defines the full Message structure (e.g., HTTP in Sec. 3.3.2). The class Message is therefore now conceived to carry the metadata that will be used to create the Message, but their usage is left to the specific transfer protocols (see the current example for HTTP/HTTPS).

Actions
~~~~~~~

The Actions are now a simple enumeration of keywords, fully compliant
with the standard. The original idea of associating a code to an action
is not convincing because of the reasons discussed in Architecture.
Additional actions envisioned by profiles should be added in the profile
folder, using the static method provided by the Actions class.

Encoding
~~~~~~~~

Encoding is perhaps the major change from the previous approach. I was
not totally satisfied of the approach of adding a tojson (and in the
future, toyaml, toxml, …) method to all basic elements, since this is
not easily maintainable in time. However, I insisted with this approach
because in case new elements are added, their conversion could be
defined by their implementors, without changing the base Encoder class.
However, while playing with Python, I discovered that every object
(=class) comes with a dictionary representation, where all field names
and value are present. And the conversion of a dictionary to json is
trivial with the json package. This suggested me the idea of using an
intermediary representation of all messages as dictionary, and then
translate this representation to json or any other format:

::

  Python objection → dictionary → json, xml, yaml, …

So now a to_json method for each object is no more necessary, because
the conversion to dictionary is standard and can be done in a general
way for any element. There is therefore a todict method in the base
Encoding class, which can be called by the concrete encoder
implementations to get the dictionary before encoding it. The
encoding/decoding operations happen on two layers. At the bottom layer,
the Encoder defines the main rules to iteratively traverse complex
object definitions and dictionaries. On the top layer, each OpenC2 type
defines the rule to convert an instance to a dictionary and vice versa
(todict, fromdict). The top layer relies on the bottom layer to
recursively translate instances to a dictionary; the bottom layer relies
in turn on the top layer to recursively create instances from a
dictionary.

Important note. This approach works if every element perfectly matches
the terminology and field order required by the language specification.
Some constraints on fields order in a Record could be related, but it is
better to keep the same order of the Language Specification to avoid
misordering in the final encoded format. The drawback of this approach
is that any field that is not foreseen by the specification must be kept
private, to easily remove it from the dictionary. The todict method
indeed has a number of tricks to solve common issues with this approach
(e.g., the from field that cannot be used because it is a Python
keyword). In this case, the suggestion is to append an underscore, as
already happens for the from field, which is easy to remove. There are
also other issues that come out when combining multiple fields together
(e.g., Action, Target, Args, Actuator in a Command, or IPv4Net in a
Target). This is now solved for all base types currently defined, but
additional rules must be added when the missing base types are added..

Transfer
~~~~~~~~

TODO

