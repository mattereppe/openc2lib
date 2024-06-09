# Developing extensions 

This Section gives basic guidelines to add extensions to the openc2lib. Extensions include:
- [encoders](https://github.com/mattereppe/openc2/blob/main/docs/developingextensions.md#add-new-encoding-formats)
- [transfer protocols](https://github.com/mattereppe/openc2/blob/main/docs/developingextensions.md#add-new-transfer-protocols)
- [profiles](https://github.com/mattereppe/openc2lib/blob/main/docs/developingextensions.md#adding-new-profiles)
- [actuators](https://github.com/mattereppe/openc2/blob/main/docs/developingextensions.md#add-new-actuators)

Extensions may be included in and delivered with openc2lib, or developed separately. There is no significant difference between the two methods, apart from the delivery process; the latter is not covered in this guide. There is no strict naming conventions for the extension modules, althought following a common convention facilitate the maintenance of the code by different developers.

## Adding new encoding formats

Encoders are necessary to support new encoding formats. The definition of an `Encoder` must follows the general architecture described in the [Developer guide](https://github.com/mattereppe/openc2/blob/main/docs/developerguide.md#developer-guide). In a nutshell, each `Encoder` is expected to serialize OpenC2 messages. The translation between Python objects and dictionaries is already provided by the base `Encoder` class (by the `Encoder.todict()` and `Encoder.fromdict()` methods, which new Encoders are expected to extend.

The definition of a new `Encoder` must provide:
- a method `encode` for serializing OpenC2 commands;
- a method `decode` for deserializing OpenC2 messages;
- a class member `encoder_type` with the name of the Encoder;
- registration of the new `Encoder` via the `@register_encoder` decorator.

 ```
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
```

See the [Developer guide](https://github.com/mattereppe/openc2/blob/main/docs/developerguide.md#developer-guide) for more detail about the base `Encoder` class and the available Encoders.


## Adding new transfer protocols

A transfer protocol is derived from the `Transfer` class:
```
class Transfer:

   def send(self, msg, encoder):
      pass

  def receive(self, callback, encode):
     pass

```

A `Transfer` implementation is used for both sending and receiving OpenC2 messages, by using the  the `send()` and `receive()` method, respectively. The `receive()` method is expected to be blocking and to wait for messages until termination of the application.

The `send()` takes an OpenC2 `Message` as first argument, which is expected to carry a `Content`. It returns the `Response` within another `Message`. The `Encoder` must be passed as second argument, and it is possible to use a different `Encoder` for each individual message. The `send()` message is used by the `Producer`. 

The `receive()` takes a callback function from the `Consumer`, which is used to dispatch incoming messages to the corresponding `Actuator`. The `Encoder` must be passed as second argument, but it is only used when the encoding format is not present in the metadata; it is also used to answer messages in unknown formats. 

The implementation of a `Transfer` is expected to:
- perform any protocol-specific initialization, including loading configurations (e.g., certificates to be used in TLS/SSL handshakes);
- manage the transmission and reception of `Message` metadata in a protocol-dependent way (this is defined by each corresponding OpenC2 specification).

Implementation of new `Transfer`s included in the openc2lib must be placed in the `transfers` folder and be self-contained in a single module.




## Adding new profiles

To add a new profile within the openc2lib source code, create a new directory in the `src/openc2lib/profiles` folder. Preferably name the folder with the nsid of the profile to be developed (e.g., `slpf` for the Statless Packet Filter profile). 

### Create the actuator specifiers

The _specifiers_ are the structure of any `Actuator` that implements the profile. They are defined by the Profile Specification (e.g., see [Sec. 2.1.4](https://docs.oasis-open.org/openc2/oc2slpf/v1.0/cs01/oc2slpf-v1.0-cs01.pdf) for the SLPF specifier).

A specifier must be derived from `Profile` and the base structure it implements (likely, it will be an OpenC2 `Map`). It is suggested to name it with the nsid of the profile:
```
class <nsid>(Profile, Map):
  ...
```
(see the [User Guide](userguide.md) for `Map` documentation)

The specifier can provide the following methods:
- `__init__` (MANDATORY) to initialize both the `Profile` and the base type. The `Profile` initialization is standard:
  ```
  Profile.__init__(self, 'slpf')
  ```
  The base type initialization will usually require to pass the initialization arguments to the base type. In the case of `Map`:
  ```
  Map.__init__(self, dic)
  ```
  where `dic` is the only argument passed to the specifier's ``__init__``.
- `__str__` (RECOMMENDED) to provide a human-readable representation of the profile in log messages.

### Define language extensions

Define extensions to common types and elements described in the Language Specification. The following elements can be extended:
- targets;
- arguments;
- response results;
- actuator properties (already covered in the [specifier](https://github.com/mattereppe/openc2/blob/main/docs/developingextensions.md#create-the-actuator-specifiers) Section).

The list of `Actions` MUST NOT be extended (see Sec. 3.1.4 of the [Language Specification](https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.pdf)).

It is strongly recommended to follow the same naming conventions as adopted by the openc2lib (see the [Developer Guide](https://github.com/mattereppe/openc2/blob/main/docs/developerguide.md#naming-conventions)).

Extensions are currently possible for `Map` and derived base structures (`MapOf`). This applies to both arguments (`Args`) and response results (`Results`). The extension (`Ext`) declares what is extended (`Base`), makes a copy of base field types, adds the list of additional fields, and sets the nsid:
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

The extension of `Argument` and `Result` will likely be based on additional structures. Define them as well in the profile folder. As best practice, data and target types should be defined in two different modules (datatypes and targettypes, respecitvely, see the [Developer guide](https://github.com/mattereppe/openc2/blob/main/docs/developerguide.md).

### Register extensions

Extensions to `Target`, `Args`, and `Results` must be known to openc2lib to properly encode and decode messages that use these elements. 

The registration of a new `Target` includes its name, class, id, and nsid. For instance, to register the 'rule_number' target defined by the SLPF profile:
```
from openc2lib import Targets

Targets.add('rule_number', RuleID, 1024, nsid)
```
The id is taken from the specification (Table 2.1.2-2 in this case). 

The registration of new `Args` and `Results` is even simpler:
```
from openc2lib.profiles.slpf.args import Args

ExtendedArguments.add(nsid, Args)

from openc2lib import ExtendedResults 
 
ExtendedResults.add(nsid, Results)
```
(assuming the local extensions within the profiles have been named `Args` and `Results`).

Registration can be done in the `__init__.py` file. 

### Syntax validation

Profiles are likely to restrict the possible combination of `Actions`, `Target`, and `Args`. Since these restrictions are common to all `Actuator`s, they can be defined only once within the profile. Specific functions must be exported to perform the validation; the internal implementation does not need to follow any specific template. Note, however, that actuators are not expected to implement any possible Action/Target pair and support all Arguments described by the profile. For this reason, behind profile validation, each specific actuator will implement its internal validation.


### Export modules and data

Even if this step is not strictly required, it is recommended to pack every new definition under the main profile namespace. This simplifies access to exported data and structures. This operation can be done by importing all data, classes, and functions to be exported in the `__init__.py` module. Such elements can then be imported and used in a very simple and natural way under their profile namespace (which is very similar to what expected by the specifications):
```
import openc2lib.profiles.slpf as slpf

Command(target=slpf.rule_number, ...)
slpf.Args(...)
```

## Adding new actuators

Implementing an `Actuator` is really straightforward. There are only two requirements for its interface:
- an `Actuator` must set the class member `profile` to the profile it implements;
- an `Actuator` must implement a `run(cmd)` method that processes a command and returns the response.
```
class Actuator:
  profile = slpf
 
  
  def run(self, cmd):
     ...
    return response
```

Internally, an `Actuator` is expected to have the configuration to locate the device it is controlling and the code to control it. It is also expected to perform command validation, to detect any action or option that it does not support (which may be more restrictive than the generic profile validation).

