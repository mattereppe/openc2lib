Mapping
-------

The following table maps the OpenC2 elements and related Sections of the
`OpenC2 Language
Specification <https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.pdf>`__
to ``otupy`` modules where they are defined.

=============== ======= ======== ================
Name            Section Location Module
=============== ======= ======== ================
Message         3.2     core     core/message.py
Content         3.3     core     core/content.py
OpenC2 Command  3.3.1   core     core/command.py
Action          3.3.1.1 core     core/actions.py
Target          3.3.1.2 core     core/target.py
Arguments       3.3.1.4 core     core/args.py
Actuator        3.3.1.3 core     core/actuator.py
OpenC2 Response 3.3.2   core     core/response.py
Status Code     3.3.2.1 core     core/response.py
Results         3.3.2.2 core     core/results.py
Target types    3.4.1   types    types/targets
Data types      3.4.2   types    types/data
Base structures 3.1     types    types/base
=============== ======= ======== ================

