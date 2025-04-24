Types
-----

Types are the definition of data structures compliant with the
requirements and naming in the `OpenC2 Language
Specification <https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.pdf>`__.
This includes both data types and target types, listed in Sec. 3.4 (see
:doc:`mapping`).

Base Types
~~~~~~~~~~

Base types defines the types and structures defined by the Language
Specification in Sec.3.1 and that defines the type of all message
elements. Every base type must implement two methods: “todict” and
“fromdict” (the latter must be a class method). These two methods
implement the code to translate an object instance to a dictionary and
to build an object instance from a dictionary. These operations
represent the intermediary dictionary translation described in the
Encoding Section.

TODO: add the main rules and guidelines to write todict/fromdict methods
for additional objects.

TODO: the Openc2Type definition is likely useful at this stage (it was
used in a previous version. This could me removed in the following,
after final check of its uselessness.
