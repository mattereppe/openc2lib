# Developing extensions 

This Section gives basic guidelines to add extensions to the openc2lib. Extensions include:
- [encoders](https://github.com/mattereppe/openc2/blob/main/docs/developingextensions.md#add-new-encoding-formats)
- [transfer protocols](https://github.com/mattereppe/openc2/blob/main/docs/developingextensions.md#add-new-transfer-protocols)
- [profiles](https://github.com/mattereppe/openc2/blob/main/docs/developingextensions.md#add-new-profiles)
- [actuators](https://github.com/mattereppe/openc2/blob/main/docs/developingextensions.md#add-new-actuators)

Extensions may be included in and delivered with openc2lib, or developed separately. There is no significant difference between the two methods, apart from the delivery process; the latter is not covered in this guide. There is no strict naming conventions for the extension modules, althought following a common convention facilitate the maintenance of the code by different developers.

## Add new encoding formats

TODO

## Add new transfer protocols

TODO


## Add new profiles

To add a new profile within the openc2lib source code, create a new directory in the `src/openc2lib/profiles` folder. Preferably name the folder with the nsid of the profile to be developed (e.g., `slpf` for the Statless Packet Filter profile). 

### Create the actuator specifiers

The _specifiers_ are the structure of any `Actuator` that implements the profile. They are defined by the Profile Specification (e.g., see [Sec. 2.4.1](https://docs.oasis-open.org/openc2/oc2slpf/v1.0/cs01/oc2slpf-v1.0-cs01.pdf) for the SLPF specifier).

A specifier must be derived by `Profile` and the base structure it implements (likely it will be an OpenC2 `Map`). It is suggested to name it with the nsid of the profile:
```
class <nsid>(Profile, Map):
  ...
```
(see the [User Guide](userguide.md) for `Map` documentation)

The specifier must provide at least the following methods:
- `__init__` (MANDATORY) to initialize both the `Profile` and the base type. The `Profile` initialization is standard:
  ```
  Profile.__init__(self, 'slpf')
  ```
  The base type initialization will usually require to pass the initialization arguments to the base type. In the case of `Map`:
  ```
  Map.__init__(self, dic)
  ```
  where `dic` is the only argument passed to the specififer's ``__init__``.
- `__str__` (RECOMMENDED) to provide a human-readable representation of the profile in log messages.

### Define language extensions

Define extensions to common types and elements defined in the Language Specification. The following elements can be extended:
- targets;
- arguments;
- response results;
- actuator properties (already covered in the [specifier](https://github.com/mattereppe/openc2/blob/main/docs/developingextensions.md#create-the-actuator-specifiers) Section.
The list of Actions MUST NOT be extended (see Sec. 3.1.4 of the [Language Specification](https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.pdf)

Extensions are currently possible for `Map` and derived base structures (`MapOf`). The extension (`Ext`) declares what is extended (`Base`), makes a copy of base field types, add the list of additional fields, and sets the nsid:
```
class Ext(Base):
   extend = Base
   fieldtypes = Base.fieldtypes.copy()
   fieldtypes['new_field']=new_field_type
   ...
   nsid = profile_name
```
It is possible (and this is the preferred approach) to define the extension with the same name of the base class. By proper referring to base and extended elements within the corresponding namespace, name collisions are avoided and the naming remains more uniform.
For instance, the Args element and its extension could be unambigously referred to in the code in the following way:
```
import openc2lib as oc2

import openc2lib.profiles.slpf as slpf

args = Args(...)        # <- This instantiate the base Args class
args = slpf.Args(...)   # <- This instantiate the extended Args class derived in the slpf profile
```


targettypes


targets????


datatypes







## Add new actuators
