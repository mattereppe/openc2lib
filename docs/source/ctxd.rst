Context Discovery Actuator Profile
----------------------------------



1. Goals of Context Discovery
-----------------------------

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

2. Data model
-------------

A data model is implemented to define which data the CTXD stores and the
relationship between them. The most important data stored are:

-  **Service:** It is the main class of the data model, and it describes
   the environment where the service is located, its links to other
   services, its subservices, the owner, the release, the security
   functions, and the actuator.
-  **Service-Type:** This class identifies the specific type of service.
   Each instance has its own parameters, and the Service has only one
   type. Examples: VM, Container, Cloud, etc.
-  **Link:** This class describes the connection between the services.
   The field “peers” specifies the services that are on the other side
   of the link, so this class is useful for recursive discovery. Also,
   security functions applied on the link are specified and they are
   described as OpenC2 Actuator Profiles.
-  **Consumer:** It manages information about various services,
   including the security functions that protect them.
-  **OpenC2-Endpoint:** They are described in the OpenC2-Endpoint class
   and correspond to both the OpenC2 Actuator Profile and the endpoint
   that implements it. A service can implement multiple security
   functions.
-  **Peer:** This class describes the service that is connected to the
   service under analysis.

.. figure:: data%20model.png
   :alt: Centered Image

   Centered Image

3. Command Components
---------------------

This section identifies the applicable components of an OpenC2 Command.
The components of an OpenC2 Command include:

-  **Action:** List of Actions that are relevant for the CTXD. This
   Profile cannot define Actions that are not included in the OpenC2
   Language Specification, but it may extend their definitions.
-  **Target:** List of Targets included in the Language Specification
   and one Target (and its associated Specifiers) that is defined only
   for the CTXD.
-  **Arguments:** List of Command Arguments that are relevant for the
   CTXD.
-  **Actuator:** List of Actuator Specifiers that are relevant for the
   CTXD.

3.1 Actions
~~~~~~~~~~~

Action is a mandatory field in Command message and no Actuator Profile
can add a new Action that is not present in the specifications.

Type: Action (Enumerated)

== ===== ===================================
ID Name  Description
== ===== ===================================
3  query Initiate a request for information.
== ===== ===================================

3.2 Target
~~~~~~~~~~

Target is a mandatory field in Command message, and it is possible to
define new Targets that are not present in the specifications. Only one
Target is allowed in a Command, and that’s why the cardinality of each
one equals to 1.
Type: Target (Choice)

+---+----+----+---+-------------------------------------------------------+
| I | Na | Ty | # | Description                                           |
| D | me | pe |   |                                                       |
+===+====+====+===+=======================================================+
| 9 | fe | Fe | 1 | A set of items used with the query Action to          |
|   | at | at |   | determine an Actuator’s capabilities.                 |
|   | ur | ur |   |                                                       |
|   | es | es |   |                                                       |
+---+----+----+---+-------------------------------------------------------+
| 2 | c  | C  | 1 | It describes the service environment, its connections |
| 0 | on | on |   | and security capabilities.                            |
| 4 | te | te |   |                                                       |
| 8 | xt | xt |   |                                                       |
+---+----+----+---+-------------------------------------------------------+
A new target, called “context” is inserted because the Target “features”
refers only to the Actuator capabilities and not to the characteristics
of the execution environment.

3.3 Context
~~~~~~~~~~~

Type: Context (Record)

+---+-----+------------+---+--------------------------------------------+
| I | N   | Type       | # | Description                                |
| D | ame |            |   |                                            |
+===+=====+============+===+============================================+
| 1 | se  | Arr        | 0 | List the service names that the command    |
|   | rvi | ayOf(Name) | . | refers to.                                 |
|   | ces |            | . |                                            |
|   |     |            | 1 |                                            |
+---+-----+------------+---+--------------------------------------------+
| 2 | li  | Arr        | 0 | List the link names that the command       |
|   | nks | ayOf(Name) | . | refers to.                                 |
|   |     |            | . |                                            |
|   |     |            | 1 |                                            |
+---+-----+------------+---+--------------------------------------------+

The Target Context is used when the Producer wants to know the
information of all active services and links of the Consumer. The
Producer can specify the names of the services and links it is
interested in.
