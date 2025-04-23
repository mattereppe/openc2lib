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

Usage Requirements
~~~~~~~~~~~~~~~~~~

-  Producer may send a “query” Command with no fields to the Consumer,
   which could return a heartbeat to this command.
-  A Producer may send a “query” Command containing an empty list of
   services. The Consumer should return all the services.
-  A Producer may send a “query” Command containing an empty list of
   links. The Consumer should return all the links.
-  A Producer may send a “query” Command containing an empty list of
   services and links. The Consumer should return all the services and
   links.

3.4 Command Arguments
~~~~~~~~~~~~~~~~~~~~~

Type: Args (Map)

+---+---------+-------+---+---------------------------------------------+
| I | Name    | Type  | # | Description                                 |
| D |         |       |   |                                             |
+===+=========+=======+===+=============================================+
| 4 | resp    | Res   | 0 | The type of Response required for the       |
|   | onse_re | ponse | . | Command: none, ack, status, complete.       |
|   | quested | -Type | . |                                             |
|   |         |       | 1 |                                             |
+---+---------+-------+---+---------------------------------------------+
| 2 | na      | Bo    | 0 | The response includes either only the name  |
| 0 | me_only | olean | . | or all the details about the services and   |
| 4 |         |       | . | the links.                                  |
| 8 |         |       | 1 |                                             |
+---+---------+-------+---+---------------------------------------------+

Command Arguments are optional, and a new one called “name_only” has
been defined, which is not present in the Language Specification.

.. _usage-requirements-1:

Usage requirements:
~~~~~~~~~~~~~~~~~~~

-  The “response_requested”: “complete” argument can be present in the
   “query features” Command. (Language specification 4.1)
-  The “query context” Command may include the “response_requested”:
   “complete” Argument.
-  The “query context” command may include the “name_only” argument:

   -  If TRUE, the Consumer must send a Response containing only the
      names of the services and/or links.
   -  If FALSE, the Consumer must send a Response containing all the
      details of the services and/or links.

3.5 Actuator Specifiers
~~~~~~~~~~~~~~~~~~~~~~~

List of Actuators Specifiers that are applicable to the Actuator. This
is an optional field. These specifiers are not present in the Language
Specification.

Type: Specifiers (Map)

+---+-------+-----+---+------------------------------------------------+
| I | Name  | T   | # | Description                                    |
| D |       | ype |   |                                                |
+===+=======+=====+===+================================================+
| 1 | d     | Str | 0 | Domain under the responsibility of the         |
|   | omain | ing | . | actuator                                       |
|   |       |     | . |                                                |
|   |       |     | 1 |                                                |
+---+-------+-----+---+------------------------------------------------+
| 2 | ass   | Str | 0 | Identifier of the actuator                     |
|   | et_id | ing | . |                                                |
|   |       |     | . |                                                |
|   |       |     | 1 |                                                |
+---+-------+-----+---+------------------------------------------------+

3.6 Response Components
~~~~~~~~~~~~~~~~~~~~~~~

This section defines the Response Components relevant to the CTXD
Actuator Profile. The table below outlines the fields that constitute an
OpenC2 Response.

Type: OpenC2-Response (Map)

+---+--------+-----------+---+------------------------------------------+
| I | Name   | Type      | # | Description                              |
| D |        |           |   |                                          |
+===+========+===========+===+==========================================+
| 1 | status | St        | 1 | Status code                              |
|   |        | atus-Code |   |                                          |
+---+--------+-----------+---+------------------------------------------+
| 2 | statu  | String    | 1 | Description of the Response status       |
|   | s_text |           |   |                                          |
+---+--------+-----------+---+------------------------------------------+
| 3 | r      | Results   | 1 | Results derived from the executed        |
|   | esults |           |   | Command                                  |
+---+--------+-----------+---+------------------------------------------+

.. _response-components-1:

4 Response Components
---------------------

This section defines the Response Components relevant to the CTXD
Actuator Profile. The table below outlines the fields that constitute an
OpenC2 Response.

Type: OpenC2-Response (Map)

+---+---------+----------+---+-------------------------------------------+
| I | Name    | Type     | # | Description                               |
| D |         |          |   |                                           |
+===+=========+==========+===+===========================================+
| 1 | status  | Sta      | 1 | Status code                               |
|   |         | tus-Code |   |                                           |
+---+---------+----------+---+-------------------------------------------+
| 2 | stat    | String   | 1 | Description of the Response status        |
|   | us_text |          |   |                                           |
+---+---------+----------+---+-------------------------------------------+
| 3 | results | Results  | 1 | Results derived from the executed Command |
+---+---------+----------+---+-------------------------------------------+

4.1 Response status code
~~~~~~~~~~~~~~~~~~~~~~~~

Type: Status-Code (Enumerated.ID)

+---+--------------------------------------------------------------------+
| I | Description                                                        |
| D |                                                                    |
+===+====================================================================+
| 1 | Processing - an interim Response used to inform the Producer that  |
| 0 | the Consumer has accepted the Command but has not yet completed    |
| 2 | it.                                                                |
+---+--------------------------------------------------------------------+
| 2 | OK - the Command has succeeded.                                    |
| 0 |                                                                    |
| 0 |                                                                    |
+---+--------------------------------------------------------------------+
| 4 | Bad Request - the Consumer cannot process the Command due to       |
| 0 | something that is perceived to be a Producer error (e.g.,          |
| 0 | malformed Command syntax).                                         |
+---+--------------------------------------------------------------------+
| 4 | Unauthorized - the Command Message lacks valid authentication      |
| 0 | credentials for the target resource or authorization has been      |
| 1 | refused for the submitted credentials.                             |
+---+--------------------------------------------------------------------+
| 4 | Forbidden - the Consumer understood the Command but refuses to     |
| 0 | authorize it.                                                      |
| 3 |                                                                    |
+---+--------------------------------------------------------------------+
| 4 | Not Found - the Consumer has not found anything matching the       |
| 0 | Command.                                                           |
| 4 |                                                                    |
+---+--------------------------------------------------------------------+
| 5 | Internal Error - the Consumer encountered an unexpected condition  |
| 0 | that prevented it from performing the Command.                     |
| 0 |                                                                    |
+---+--------------------------------------------------------------------+
| 5 | Not Implemented - the Consumer does not support the functionality  |
| 0 | required to perform the Command.                                   |
| 1 |                                                                    |
+---+--------------------------------------------------------------------+
| 5 | Service Unavailable - the Consumer is currently unable to perform  |
| 0 | the Command due to a temporary overloading or maintenance of the   |
| 3 | Consumer.                                                          |
+---+--------------------------------------------------------------------+

4.2 Common Results
~~~~~~~~~~~~~~~~~~

This section refers to the Results that are meaningful in the context of
a CTXD and that are listed in the Language Specification.

Type: Results (Record0..\*)

+---+-------+------------+---+-------------------------------------------+
| I | Name  | Type       | # | Description                               |
| D |       |            |   |                                           |
+===+=======+============+===+===========================================+
| 1 | ver   | Version    | 0 | List of OpenC2 language versions          |
|   | sions | unique     | . | supported by this Actuator                |
|   |       |            | . |                                           |
|   |       |            | \ |                                           |
|   |       |            | * |                                           |
+---+-------+------------+---+-------------------------------------------+
| 2 | pro   | Arr        | 0 | List of profiles supported by this        |
|   | files | ayOf(Nsid) | . | Actuator                                  |
|   |       |            | . |                                           |
|   |       |            | 1 |                                           |
+---+-------+------------+---+-------------------------------------------+
| 3 | pairs | Acti       | 0 | List of targets applicable to each        |
|   |       | on-Targets | . | supported Action                          |
|   |       |            | . |                                           |
|   |       |            | 1 |                                           |
+---+-------+------------+---+-------------------------------------------+
| 4 | rate_ | Num        | 0 | Maximum number of requests per minute     |
|   | limit | ber{0..\*} | . | supported by design or policy             |
|   |       |            | . |                                           |
|   |       |            | 1 |                                           |
+---+-------+------------+---+-------------------------------------------+
| 1 | slpf  | sl         | 0 | Example: Result properties defined in the |
| 0 |       | pf:Results | . | Stateless Packet Filtering Profile        |
| 2 |       |            | . |                                           |
| 4 |       |            | 1 |                                           |
+---+-------+------------+---+-------------------------------------------+

4.3 CTXD Results
~~~~~~~~~~~~~~~~

These results are not included in the Language Specification and are
introduced specifically for the CTXD Actuator Profile.

Type: Results (Map0..\*)

+---+----------+------------+---+---------------------------------------+
| I | Name     | Type       | # | Description                           |
| D |          |            |   |                                       |
+===+==========+============+===+=======================================+
| 2 | services | ArrayO     | 0 | List all the services                 |
| 0 |          | f(Service) | . |                                       |
| 4 |          |            | . |                                       |
| 8 |          |            | 1 |                                       |
+---+----------+------------+---+---------------------------------------+
| 2 | links    | Arr        | 0 | List all the links of the services    |
| 0 |          | ayOf(Link) | . |                                       |
| 4 |          |            | . |                                       |
| 9 |          |            | 1 |                                       |
+---+----------+------------+---+---------------------------------------+
| 2 | servic   | Arr        | 0 | List the names of all services        |
| 0 | es_names | ayOf(Name) | . |                                       |
| 5 |          |            | . |                                       |
| 0 |          |            | 1 |                                       |
+---+----------+------------+---+---------------------------------------+
| 2 | li       | Arr        | 0 | List the names of all services        |
| 0 | nk_names | ayOf(Name) | . |                                       |
| 5 |          |            | . |                                       |
| 1 |          |            | 1 |                                       |
+---+----------+------------+---+---------------------------------------+

Usage requirements:

-  The response “services” can only be used when the target is
   “context”.
-  The response “links” can only be used when the target is “context”.
-  The response “services_names” can only be used when the target is
   “context”.
-  The response “services_names” can only be used when the target is
   “context”.
-  service_names/link_names are mutually exclusive with services/links,
   respectively. The choice is based on the value of the “name_only”
   argument in the query.

5 CTXD data types
-----------------

With the introduction of new data types that are not specified in the
original specifications, it is necessary to define these types along
with their attributes, base type, and eventually the conformance
clauses. In this section, each new data type is defined, and for some, a
use case example is provided.

5.1 Name
~~~~~~~~

The Name type is used to indicate the name of any object. When the
Command Argument is “name_only”, an array of Name is returned to the
Producer.

Type: Name (Choice)

+---+---------+--------+---+-------------------------------------------+
| I | Name    | Type   | # | Description                               |
| D |         |        |   |                                           |
+===+=========+========+===+===========================================+
| 1 | uri     | URI    | 1 | Uniform Resource Identifier of the        |
|   |         |        |   | service                                   |
+---+---------+--------+---+-------------------------------------------+
| 2 | reve    | Ho     | 1 | Reverse domain name notation              |
|   | rse_dns | stname |   |                                           |
+---+---------+--------+---+-------------------------------------------+
| 3 | uuid    | UUID   | 1 | Universally unique identifier of the      |
|   |         |        |   | service                                   |
+---+---------+--------+---+-------------------------------------------+
| 4 | local   | String | 1 | Name without guarantee of uniqueness      |
+---+---------+--------+---+-------------------------------------------+

5.2 Operating System (OS)
~~~~~~~~~~~~~~~~~~~~~~~~~

It describes an Operating System.

Type: OS (Record)

== ======= ====== = =================
ID Name    Type   # Description
== ======= ====== = =================
1  name    String 1 Name of the OS
2  version String 1 Version of the OS
3  family  String 1 Family of the OS
4  type    String 1 Type of the OS
== ======= ====== = =================

5.3 Service
~~~~~~~~~~~

Digital resources can implement one or more services, with each service
described by a Service type. This type is a key element of the data
model, as it provides the information the Producer is seeking about the
services.

Type: Service (Record)

+---+-----------+---------------+---+-----------------------------------+
| I | Name      | Type          | # | Description                       |
| D |           |               |   |                                   |
+===+===========+===============+===+===================================+
| 1 | name      | Name          | 1 | Id of the service                 |
+---+-----------+---------------+---+-----------------------------------+
| 2 | type      | Service-Type  | 1 | It identifies the type of the     |
|   |           |               |   | service                           |
+---+-----------+---------------+---+-----------------------------------+
| 3 | links     | ArrayOf(Name) | 0 | Links associated with the service |
|   |           |               | . |                                   |
|   |           |               | . |                                   |
|   |           |               | 1 |                                   |
+---+-----------+---------------+---+-----------------------------------+
| 4 | su        | ArrayOf(Name) | 0 | Subservices of the main service   |
|   | bservices |               | . |                                   |
|   |           |               | . |                                   |
|   |           |               | 1 |                                   |
+---+-----------+---------------+---+-----------------------------------+
| 5 | owner     | String        | 0 | Owner of the service              |
|   |           |               | . |                                   |
|   |           |               | . |                                   |
|   |           |               | 1 |                                   |
+---+-----------+---------------+---+-----------------------------------+
| 6 | release   | String        | 0 | Release version of the service    |
|   |           |               | . |                                   |
|   |           |               | . |                                   |
|   |           |               | 1 |                                   |
+---+-----------+---------------+---+-----------------------------------+
| 7 | security_ | ArrayOf(Ope   | 0 | Actuator Profiles associated with |
|   | functions | nC2-Endpoint) | . | the service                       |
|   |           |               | . |                                   |
|   |           |               | 1 |                                   |
+---+-----------+---------------+---+-----------------------------------+
| 8 | actuator  | Consumer      | 1 | It identifies who is carrying out |
|   |           |               |   | the service                       |
+---+-----------+---------------+---+-----------------------------------+

5.4 Service-Type
~~~~~~~~~~~~~~~~

It represents the type of service, where each service type is further
defined with additional information that provides a more detailed
description of the service’s characteristics.

Type: Service-Type (Choice)

+---+-----------+----------+---+--------------------------------------+
| I | Name      | Type     | # | Description                          |
| D |           |          |   |                                      |
+===+===========+==========+===+======================================+
| 1 | ap        | App      | 1 | Software application                 |
|   | plication | lication |   |                                      |
+---+-----------+----------+---+--------------------------------------+
| 2 | vm        | VM       | 1 | Virtual Machine                      |
+---+-----------+----------+---+--------------------------------------+
| 3 | container | C        | 1 | Container                            |
|   |           | ontainer |   |                                      |
+---+-----------+----------+---+--------------------------------------+
| 4 | we        | Web      | 1 | Web service                          |
|   | b_service | -Service |   |                                      |
+---+-----------+----------+---+--------------------------------------+
| 5 | cloud     | Cloud    | 1 | Cloud                                |
+---+-----------+----------+---+--------------------------------------+
| 6 | network   | Network  | 1 | Connectivity service                 |
+---+-----------+----------+---+--------------------------------------+
| 7 | iot       | IOT      | 1 | IOT device                           |
+---+-----------+----------+---+--------------------------------------+

5.5 Application
~~~~~~~~~~~~~~~

It describes a generic application.

Type: Application (Record)

+---+-----------+-------+---+-----------------------------------------+
| I | Name      | Type  | # | Description                             |
| D |           |       |   |                                         |
+===+===========+=======+===+=========================================+
| 1 | de        | s     | 1 | Generic description of the application  |
|   | scription | tring |   |                                         |
+---+-----------+-------+---+-----------------------------------------+
| 2 | name      | S     | 1 | Name of the application                 |
|   |           | tring |   |                                         |
+---+-----------+-------+---+-----------------------------------------+
| 3 | version   | s     | 1 | Version of the application              |
|   |           | tring |   |                                         |
+---+-----------+-------+---+-----------------------------------------+
| 4 | owner     | s     | 1 | Owner of the application                |
|   |           | tring |   |                                         |
+---+-----------+-------+---+-----------------------------------------+
| 5 | type      | S     | 1 | Type of the application                 |
|   |           | tring |   |                                         |
+---+-----------+-------+---+-----------------------------------------+

Sample Application object represented in JSON Format:

.. code:: json

   {
       "description": "application",
       "name": "iptables",
       "version": "1.8.10",
       "owner": "Netfilter",
       "type": "Packet Filtering"
   }
