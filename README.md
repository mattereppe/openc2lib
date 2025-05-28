# otupy: OpenC2 Utilities for Python

## Description

otupy (/'əʊtu:paɪ/) is an open-source implementation of the OpenC2 language written in Python. It is particullary suited for:
- developers that are looking for a common interface to control their remote cybersecurity functions;
- researchers that design new profiles for cybersecurity functions;
- system integrators that need a common language for their cybersecurity frameworks. 

The otupy framework is build around a pluggable and powerful core library, designed with flexibility and extensibility in mind. Profiles, transfer protocols, serialization formats, and actuators can be easily added without impacting the core library itself. The framework currently includes:
- the core library that  implements the OpenC2 Architecture and Language Specification;
- json serialization;
- an implementation of the HTTP transfer protocol;
- the definition of the SLPF profile;
- the Context Discovery profile and its actuators for OpenStack and Kubernetes;
- a dumb implementation of an actuator for the SLPF profile.

Usage and extension of otupy have a shallow learning curve because data structures are explicitly designed to follow the language specification.


## Quick start

Before using otupy you must be familiar with the [OpenC2 Language Specification](https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.pdf). Even if not strictly required to getting started with the code, the [OpenC2 Architecture Specification](https://docs.oasis-open.org/openc2/oc2arch/v1.0/cs01/oc2arch-v1.0-cs01.pdf) provides a good introduction to OpenC2 architectural patterns and terminology.

While the Language Specification is somehow confusing about the concept of _profile_ and _actuator_, otupy makes a sharp distinction between these terms:
- a _profile_ is a language extension that abstract a specific class of security functions (this is also indicated ad `Actuator Profile` by the standard);
- an  _actuator_ is the concrete implementation of a _profile_ for a specific security appliance; it may be either integrated in the appliance itself or act as a proxy to a legacy implementation (in this last case it is also referred as `Actuator Manager`.

### Software requirements

Python 3.11+ is required to use otupy.

### Download and setup

Otupy is available as source code and Python package. 

Install it and its dependencies from TestPyPi:
```
pip install -i https://test.pypi.org/simple/ otupy
```

Alternatively, dowload it from github:
```
git clone https://github.com/mattereppe/openc2.git
```
and install the necessary dependecies:
```
python3 -m venv .oc2-env
. .oc2-env/bin/activate
pip install -r requirements.txt
```

## Usage 

A few scripts are available in the `examples` folder of the repository for sending a simple commmand from a controller to a remote server (hosting the actuator). 

Basic usage consists in instantiating the `Provider` and `Consumer` classes that implements the OpenC2 _Provider_ and _Consumer_ role, respectively. This includes the creation of a protocol stack, namely the serialization format and transfer protocol. The `Consumer` also loads the available _Actuators_. Note that in the otupy implementation, the security services and transport protocols are already embedded in each specific transfer protocol.


### Create the Server

A `Server` instantiates and runs the OpenC2 `Consumer`.

The `otupy` module only includes the core libraries, while all extensions for serialization, transfer protocols, profile definition, and actuator implementations are grouped in specific modules (`encoders`, `trasfers`, `profiles`, and `actuators`). 
```
import otupy as oc2

from otupy.encoders.json_encoder import JSONEncoder
from otupy.transfers.http_transfer import HTTPTransfer

import otupy.profiles.slpf as slpf
from otupy.actuators.iptables_actuator import IptablesActuator
```

First, we instantiate the `IptablesActuator` as an implementation of the `slpf` profile:
```
 actuators = {}
 actuators[(slpf.nsid,'iptables')]=IptablesActuator()
```
(there is no specific configuration here because the `IptablesActuator` is currently a mockup)

Next, we create the `Consumer` by instantiating its execution environment with the list of served `Actuator`s and the protocol stack. We also provide an identification string:
```
consumer = oc2.Consumer("consumer.example.net", actuators, JSONEncoder(), HTTPTransfer("127.0.0.1", 8080))
```
(the server will be listening on the loopback interface, port 8080)

Finally, start the server:
```
 consumer.run()
```

### Create the Controller

A `Controller` instantiates an OpenC2 `Producer` and to use it to control a remote security function. Note that the `Producer` is totally unaware of the concrete actuators and its implementation.
```
from otupy.encoders.json_encoder import JSONEncoder
from otupy.transfers.http_transfer import HTTPTransfer

import otupy.profiles.slpf as slpf

producer = oc2.Producer("producer.example.net", JSONEncoder(), HTTPTransfer("127.0.0.1", 8080))
```

Next we create a `Command`, by combining the _Action_, _Target_, _Arguments_, and _Actuator_. We will query the remote `slpf` actuator for its capabilities. Note how we mix common language elements with specific extensions for the `slpf` profile, as expected by the Specification:
```
pf = slpf.slpf({'hostname':'firewall', 'named_group':'firewalls', 'asset_id':'iptables'})
arg = slpf.ExtArgs({'response_requested': oc2.ResponseType.complete})
 
cmd = oc2.Command(oc2.Actions.query, oc2.Features(), actuator=pf)
```

Finally, we send the command and catch the response:
```
resp = p.sendcmd(cmd)
```
(print out `resp` to check what the server returned)

A more useful implementation of a _Controller_ would also include the business logic to update rules on specific events (even by specific input from the user).


# Advanced usage

See the full documentation available from [readthedocs.io](https://otupy.readthedocs.io).


## Authors and acknowledgment

- The Context Discovery profile, its actuators and use cases have been developed by Silvio Tanzarella.

## License

Licensed under the [EUPL v1.2](https://eupl.eu/1.2/en/).


