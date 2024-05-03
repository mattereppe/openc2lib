# Developer guide

This Section describes the main library structure and meaning, to serve as a reference for planning extensions and modifications to the core library. It does not provide user documentation to use openc2lib in your projects. For user documentation, see [here](userdocumentation.md).

## Mapping

The following table maps the OpenC2 elements and related Sections of the [OpenC2 Language Specification](https://docs.oa    sis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.pdf) to the openc2lib modules where they are defined.

-----------------------------------------------------------------------------------------------------
| Name                | Section           | Location                     | Module           |
-----------------------------------------------------------------------------------------------------




  2 3.3.1 OpenC2 Command -> message.py
  3 3.3.1.1 Action       -> actions.py
  4 3.3.1.2 Target       -> target.py, targets.py
  5 
  6 3.3.2 OpenC2 Response-> message.py
  7 3.3.2.1 Status-Code  -> response.py
  8 3.3.2.2 Results      -> response.py
  9 
 10 
 11 
 12 3.4 Types definition
 13 ====================
 14 3.4.1 Target types -> targettypes.py
 15 3.4.2 Data types   -> datatypes.py
~                                              


## Core components

Core components includes the implementation of the common language elements (i.e., those described in the [OpenC2 Language Specification](https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.pdf). 

### Actions

The Actions are now a simple enumeration of keywords, fully compliant with the standard. The original idea of associating a code to an action is not convincing because of the reasons discussed in Architecture. 
Additional actions envisioned by profiles should be added in the profile folder, using the static method provided by the Actions class.

## Types

Types are the definition of data structures compliant with the requirements and naming in the [OpenC2 Language Specification](https://docs.oa    sis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.pdf). This includes both data types and target types, listed in Sec. 3.4 (see [Mapping](#mapping)).


### Base Types

Base types defines the types and structures defined by the Language Specification in Sec.3.1 and that defines the type of all message elements. Every base type must implement two methods: “todict” and “fromdict” (the latter must be a class method).
These two methods implement the code to translate an object instance to a dictionary and to build an object instance from a dictionary. These operations represent the intermediary dictionary translation described in the Encoding Section.

TODO: add the main rules and guidelines to write todict/fromdict methods for additional objects.

TODO: the Openc2Type definition is likely useful at this stage (it was used in a previous version. This could me removed in the following, after final check of its uselessness.
