# Developer guide

This Section describes the main library structure and meaning, to serve as a reference for planning extensions and modifications to the core library. It does not provide user documentation to use openc2lib in your projects. For user documentation, see [here](userdocumentation.md).

## Mapping

The following table maps the OpenC2 elements and related Sections of the [OpenC2 Language Specification](https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.pdf) to the openc2lib modules where they are defined.


| Name                | Section   | Location   | Module           |
|---------------------|-----------|------------|------------------|
| Message             | 3.2       | core       | message.py       |
| Content             | 3.3       | core       | content.py       |
| OpenC2 Command      | 3.3.1     | core       | message.py       |
| Action              | 3.3.1.1   | core       | actions.py       |
| Target              | 3.3.1.2   | core       | target.py        |
| Arguments           | 3.3.1.4   | core       | args.py          |
| Actuator            | 3.3.1.3   | core       | actuator.py      |
| OpenC2 Resposne     | 3.3.2     | core       | message.py       |
| Status Code         | 3.3.2.1   | core       | response.py      |
| Results             | 3.3.2.2   | core       | response.py      |
| Target types        | 3.4.1     | types      | targettypes.py   |
| Data types          | 3.4.2     | types      | datatypes.py     |
| Base structures     | 3.1       | types      | basetypes.py     |



  
                                               


## Core components

Core components includes the implementation of the common language elements (i.e., those described in the [OpenC2 Language Specification](https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.pdf). 

### Actions

The Actions are now a simple enumeration of keywords, fully compliant with the standard. The original idea of associating a code to an action is not convincing because of the reasons discussed in Architecture. 
Additional actions envisioned by profiles should be added in the profile folder, using the static method provided by the Actions class.

## Types

Types are the definition of data structures compliant with the requirements and naming in the [OpenC2 Language Specification](https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.pdf). This includes both data types and target types, listed in Sec. 3.4 (see [Mapping](#mapping)).


### Base Types

Base types defines the types and structures defined by the Language Specification in Sec.3.1 and that defines the type of all message elements. Every base type must implement two methods: “todict” and “fromdict” (the latter must be a class method).
These two methods implement the code to translate an object instance to a dictionary and to build an object instance from a dictionary. These operations represent the intermediary dictionary translation described in the Encoding Section.

TODO: add the main rules and guidelines to write todict/fromdict methods for additional objects.

TODO: the Openc2Type definition is likely useful at this stage (it was used in a previous version. This could me removed in the following, after final check of its uselessness.
