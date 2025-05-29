1. Goals of Context Discovery
=============================

To fill the gap left by the OpenC2 specifications, a new Actuator
Profile has been introduced with the goal to abstract the services that
are running into the network, the interactions between them and the
security features that they implement. Identifying a service involves
determining its type and the specific characteristics of that type. The
service also provides essential information, such as hostname, encoding
format, and transfer protocol, for connecting to it and to any linked
services. In this way, the context in which the service is operating is
identified. This new Actuator Profile has been named “Context
Discovery”, herein referred as CTXD, with the nsid “ctxd”.

The Context Discovery employs a recursive function to achieve this task,
querying each digital resource to determine its features. Thus, once the
Producer has obtained from the Consumer the information on how to
connect to the digital resources linked to the Consumer, it will query
each new digital resource to determine its features, thereby producing a
map.

The Context Discovery profile is implemented on the Consumer side and is
one of the possible Actuator Profiles that the Consumer can support.
Communication follows the OpenC2 standard, where a Producer sends a
Command specifying that the Actuator to execute it is CTXD. If the
Consumer implements CTXD, it will return a Response.

