Context Discovery Actuator Profile
-----------------------------------

1. Goals of Context Discovery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

5.6 VM
~~~~~~

It describes a Virtual Machine.

Type: VM (Record)

== =========== ======== = =============================
ID Name        Type     # Description
== =========== ======== = =============================
1  description String   1 Generic description of the VM
2  id          String   1 ID of the VM
3  hostname    Hostname 1 Hostname of the VM
4  os          OS       1 Operating System of the VM
== =========== ======== = =============================

Sample VM object represented in JSON Format:

.. code:: json

   {
     "description": "vm",
     "id": "123456",
     "hostname": "My-virtualbox",
     "os": {
       "name": "ubuntu",
       "version": "22.04.3",
       "family": "debian",
       "type": "linux"
     }
   }

5.7 Container
~~~~~~~~~~~~~

It describes a generic Container.

Type: Container (Record)

+---+---------+------+---+-----------------------------------------------+
| I | Name    | Type | # | Description                                   |
| D |         |      |   |                                               |
+===+=========+======+===+===============================================+
| 1 | desc    | St   | 1 | Generic description of the container          |
|   | ription | ring |   |                                               |
+---+---------+------+---+-----------------------------------------------+
| 2 | id      | St   | 1 | ID of the Container                           |
|   |         | ring |   |                                               |
+---+---------+------+---+-----------------------------------------------+
| 3 | h       | Host | 1 | Hostname of the Container                     |
|   | ostname | name |   |                                               |
+---+---------+------+---+-----------------------------------------------+
| 4 | runtime | St   | 1 | Runtime managing the Container                |
|   |         | ring |   |                                               |
+---+---------+------+---+-----------------------------------------------+
| 5 | os      | OS   | 1 | Operating System of the Container             |
+---+---------+------+---+-----------------------------------------------+

Sample Container object represented in JSON Format:

.. code:: json

   {
     "description": "container",
     "id": "123456",
     "hostname": "container_name",
     "runtime": "docker",
     "os": {
       "name": "ubuntu",
       "version": "22.04.3",
       "family": "debian",
       "type": "linux"
     }
   }

5.8 Web Service
~~~~~~~~~~~~~~~

It describes a generic web service.

Type: Web Service (Record)

+---+---------+-------+---+---------------------------------------------+
| I | Name    | Type  | # | Description                                 |
| D |         |       |   |                                             |
+===+=========+=======+===+=============================================+
| 1 | desc    | S     | 1 | Generic description of the web service      |
|   | ription | tring |   |                                             |
+---+---------+-------+---+---------------------------------------------+
| 2 | server  | S     | 1 | Hostname or IP address of the server        |
|   |         | erver |   |                                             |
+---+---------+-------+---+---------------------------------------------+
| 3 | port    | In    | 1 | The port used to connect to the web service |
|   |         | teger |   |                                             |
+---+---------+-------+---+---------------------------------------------+
| 4 | e       | S     | 1 | The endpoint used to connect to the web     |
|   | ndpoint | tring |   | service                                     |
+---+---------+-------+---+---------------------------------------------+
| 5 | owner   | S     | 1 | Owner of the web service                    |
|   |         | tring |   |                                             |
+---+---------+-------+---+---------------------------------------------+

Sample Web Service object represented in JSON Format:

.. code:: json

   {
     "description": "web_service",
     "server": "192.168.0.1",
     "port": 443,
     "endpoint": "maps/api/geocode/json",
     "owner": "Google"
   }

5.9 Cloud
~~~~~~~~~

It describes a generic Cloud service.

Type: Cloud (Record)

+---+---------+-------+---+----------------------------------------------+
| I | Name    | Type  | # | Description                                  |
| D |         |       |   |                                              |
+===+=========+=======+===+==============================================+
| 1 | desc    | S     | 1 | Generic description of the cloud service     |
|   | ription | tring |   |                                              |
+---+---------+-------+---+----------------------------------------------+
| 2 | id      | S     | 1 | Id of the cloud provider                     |
|   |         | tring |   |                                              |
+---+---------+-------+---+----------------------------------------------+
| 3 | name    | S     | 1 | Name of the cloud provider                   |
|   |         | tring |   |                                              |
+---+---------+-------+---+----------------------------------------------+
| 4 | type    | S     | 1 | Type of the cloud service                    |
|   |         | tring |   |                                              |
+---+---------+-------+---+----------------------------------------------+

Sample Cloud object represented in JSON Format:

.. code:: json

   {
     "description": "cloud",
     "cloud_id": "123456",
     "name": "aws",
     "type": "lambda"
   }

5.10 Network
~~~~~~~~~~~~

It describes a generic network service. The Network-Type is described in
the following sections.

Type: Network (Record)

+---+----------+-----------+---+-----------------------------------------+
| I | Name     | Type      | # | Description                             |
| D |          |           |   |                                         |
+===+==========+===========+===+=========================================+
| 1 | des      | String    | 1 | Generic description of the network      |
|   | cription |           |   |                                         |
+---+----------+-----------+---+-----------------------------------------+
| 2 | name     | String    | 1 | Name of the network provider            |
+---+----------+-----------+---+-----------------------------------------+
| 3 | type     | Net       | 1 | Type of the network service             |
|   |          | work-Type |   |                                         |
+---+----------+-----------+---+-----------------------------------------+

Sample Network object represented in JSON Format:

.. code:: json

   {
     "description": "network",
     "name": "The Things Network",
     "type": "LoRaWAN"
   }

5.11 IOT
~~~~~~~~

It describes an IoT device.

Type: IOT (Record)

+---+-----------+-----+---+---------------------------------------------+
| I | Name      | T   | # | Description                                 |
| D |           | ype |   |                                             |
+===+===========+=====+===+=============================================+
| 1 | de        | Str | 1 | Identifier of the IoT function              |
|   | scription | ing |   |                                             |
+---+-----------+-----+---+---------------------------------------------+
| 2 | name      | Str | 1 | Name of the IoT service provider            |
|   |           | ing |   |                                             |
+---+-----------+-----+---+---------------------------------------------+
| 3 | type      | Str | 1 | Type of the IoT device                      |
|   |           | ing |   |                                             |
+---+-----------+-----+---+---------------------------------------------+

Sample IOT object represented in JSON Format:

.. code:: json

   {
     "description": "IoT",
     "name": "Azure IoT",
     "type": "sensor"
   }

5.12 Network-Type
~~~~~~~~~~~~~~~~~

This class describes the type of the network service. The details of
these types are not further elaborated upon in this document.

Type: Network-Type (Choice)

+---+---------+--------+---+---------------------------------------------+
| I | Name    | Type   | # | Description                                 |
| D |         |        |   |                                             |
+===+=========+========+===+=============================================+
| 1 | e       | Et     | 1 | The network type is Ethernet                |
|   | thernet | hernet |   |                                             |
+---+---------+--------+---+---------------------------------------------+
| 2 | 802.11  | 802.11 | 1 | The network type is 802.11                  |
+---+---------+--------+---+---------------------------------------------+
| 3 | 802.15  | 802.15 | 1 | The network type is 802.15                  |
+---+---------+--------+---+---------------------------------------------+
| 4 | zigbee  | Zigbee | 1 | The network type is Zigbee                  |
+---+---------+--------+---+---------------------------------------------+
| 5 | vlan    | Vlan   | 1 | The network type is VLAN                    |
+---+---------+--------+---+---------------------------------------------+
| 6 | vpn     | Vpn    | 1 | The network type is VPN                     |
+---+---------+--------+---+---------------------------------------------+
| 7 | lorawan | L      | 1 | The network type is LoRaWAN                 |
|   |         | orawan |   |                                             |
+---+---------+--------+---+---------------------------------------------+
| 8 | wan     | Wan    | 1 | The network type is WAN                     |
+---+---------+--------+---+---------------------------------------------+

5.13 Link
~~~~~~~~~

A Service can be connected to one or more Services, the module Link
describes the type of the connection, and the security features applied
on the link.

Type: Link (Record)

+---+---------+-----------+---+-------------------------------------------+
| I | Name    | Type      | # | Description                               |
| D |         |           |   |                                           |
+===+=========+===========+===+===========================================+
| 1 | name    | Name      | 1 | Id of the link                            |
+---+---------+-----------+---+-------------------------------------------+
| 2 | desc    | String    | 0 | Generic description of the relationship   |
|   | ription |           | . |                                           |
|   |         |           | . |                                           |
|   |         |           | 1 |                                           |
+---+---------+-----------+---+-------------------------------------------+
| 3 | v       | ArrayOf   | 0 | Subset of service features used in this   |
|   | ersions | (version) | . | relationship (e.g., version of an API or  |
|   |         |           | . | network protocol)                         |
|   |         |           | 1 |                                           |
+---+---------+-----------+---+-------------------------------------------+
| 4 | li      | Link-Type | 1 | Type of the link                          |
|   | nk_type |           |   |                                           |
+---+---------+-----------+---+-------------------------------------------+
| 5 | peers   | Arra      | 1 | Services connected on the link            |
|   |         | yOf(Peer) |   |                                           |
+---+---------+-----------+---+-------------------------------------------+
| 6 | secu    | ArrayO    | 0 | Security functions applied on the link    |
|   | rity_fu | f(OpenC2- | . |                                           |
|   | nctions | Endpoint) | . |                                           |
|   |         |           | 1 |                                           |
+---+---------+-----------+---+-------------------------------------------+

5.14 Peers
~~~~~~~~~~

The Peer object is useful for iteratively discovering the services
connected on the other side of the link, enabling the Producer to build
a map of the entire network.

Type: Peer (Record)

+---+-------------+----------+---+---------------------------------------+
| I | Name        | Type     | # | Description                           |
| D |             |          |   |                                       |
+===+=============+==========+===+=======================================+
| 1 | s           | Name     | 1 | Id of the service                     |
|   | ervice_name |          |   |                                       |
+---+-------------+----------+---+---------------------------------------+
| 2 | role        | P        | 1 | Role of this peer in the link         |
|   |             | eer-Role |   |                                       |
+---+-------------+----------+---+---------------------------------------+
| 3 | consumer    | Consumer | 1 | Consumer connected on the other side  |
|   |             |          |   | of the link                           |
+---+-------------+----------+---+---------------------------------------+

5.15 Link-Type
~~~~~~~~~~~~~~

This data type describes the type of the link between the peer and the
service under analysis.

Type: Link-Type (Enumerated)

+---+-----------+----------+---+-------------------------------------------+
| I | Name      | Type     | # | Description                               |
| D |           |          |   |                                           |
+===+===========+==========+===+===========================================+
| 1 | api       | API      | 1 | The connection is an API                  |
+---+-----------+----------+---+-------------------------------------------+
| 2 | hosting   | Hosting  | 1 | The service is hosted in an               |
|   |           |          |   | infrastructure                            |
+---+-----------+----------+---+-------------------------------------------+
| 3 | pa        | Pac      | 1 | Network flow                              |
|   | cket_flow | ket-Flow |   |                                           |
+---+-----------+----------+---+-------------------------------------------+
| 4 | control   | Control  | 1 | The service controls another resource     |
+---+-----------+----------+---+-------------------------------------------+
| 5 | protect   | Protect  | 1 | The service protects another resource     |
+---+-----------+----------+---+-------------------------------------------+

The types of API, Hosting, Packet-Flow, Control and Protect are not
defined in this document.

5.16 Peer-Role
~~~~~~~~~~~~~~

It defines the role of the Peer in the link with the service under
analysis.

Type: Peer-Role (Enumerated)

+---+----------+--------------------------------------------------------+
| I | Name     | Description                                            |
| D |          |                                                        |
+===+==========+========================================================+
| 1 | client   | The consumer operates as a client in the client-server |
|   |          | model in this link                                     |
+---+----------+--------------------------------------------------------+
| 2 | server   | The consumer operates as a server in the client-server |
|   |          | model in this link                                     |
+---+----------+--------------------------------------------------------+
| 3 | guest    | The service is hosted within another service.          |
+---+----------+--------------------------------------------------------+
| 4 | host     | The service hosts another service                      |
+---+----------+--------------------------------------------------------+
| 5 | ingress  | Ingress communication                                  |
+---+----------+--------------------------------------------------------+
| 6 | egress   | Egress communication                                   |
+---+----------+--------------------------------------------------------+
| 7 | bidir    | Both ingress and egress communication                  |
|   | ectional |                                                        |
+---+----------+--------------------------------------------------------+
| 8 | control  | The service controls another service                   |
+---+----------+--------------------------------------------------------+
| 9 | co       | The service is controlled by another service           |
|   | ntrolled |                                                        |
+---+----------+--------------------------------------------------------+

5.17 Consumer
~~~~~~~~~~~~~

The Consumer provides all the networking parameters to connect to an
OpenC2 Consumer.

Type: Consumer (Record)

+---+-------+--------+---+-----------------------------------------------+
| I | Name  | Type   | # | Description                                   |
| D |       |        |   |                                               |
+===+=======+========+===+===============================================+
| 1 | s     | Server | 1 | Hostname or IP address of the server          |
|   | erver |        |   |                                               |
+---+-------+--------+---+-----------------------------------------------+
| 2 | port  | I      | 1 | Port used to connect to the actuator          |
|   |       | nteger |   |                                               |
+---+-------+--------+---+-----------------------------------------------+
| 3 | pro   | L4-Pr  | 1 | Protocol used to connect to the actuator      |
|   | tocol | otocol |   |                                               |
+---+-------+--------+---+-----------------------------------------------+
| 4 | end   | String | 1 | Path to the endpoint (e.g.,                   |
|   | point |        |   | /.wellknown/openc2)                           |
+---+-------+--------+---+-----------------------------------------------+
| 5 | tra   | Tr     | 1 | Transfer protocol used to connect to the      |
|   | nsfer | ansfer |   | actuator                                      |
+---+-------+--------+---+-----------------------------------------------+
| 6 | enc   | En     | 1 | Encoding format used to connect to the        |
|   | oding | coding |   | actuator                                      |
+---+-------+--------+---+-----------------------------------------------+

5.18 Server
~~~~~~~~~~~

It specifies the hostname or the IPv4 address of a server.

Type: Server (Choice)

+---+----------+---------+---+-------------------------------------------+
| I | Name     | Type    | # | Description                               |
| D |          |         |   |                                           |
+===+==========+=========+===+===========================================+
| 1 | hostname | h       | 1 | Hostname of the server                    |
|   |          | ostname |   |                                           |
+---+----------+---------+---+-------------------------------------------+
| 2 | i        | IP      | 1 | 32-bit IPv4 address as defined in         |
|   | pv4-addr | v4-Addr |   | [RFC0791]                                 |
+---+----------+---------+---+-------------------------------------------+

5.19 Transfer
~~~~~~~~~~~~~

This data type defines the transfer protocol. This list can be extended
with other transfer protocols.

Type: Transfer (Enumerated)

== ===== ==============
ID Name  Description
== ===== ==============
1  http  HTTP protocol
2  https HTTPS protocol
3  mqtt  MQTT protocol
== ===== ==============

5.20 Encoding
~~~~~~~~~~~~~

This data type defines the encoding format to be used. Other encodings
are permitted, the type Encoding can be extended with other encoders
(e.g., XML).

Type: Encoding (Enumerated)

== ==== =============
ID Name Description
== ==== =============
1  json JSON encoding
== ==== =============

5.21 OpenC2-Endpoint
~~~~~~~~~~~~~~~~~~~~

This data type corresponds to both the OpenC2 Actuator Profile and the
endpoint that implements it.

Type: OpenC2-Endpoint (Record)

+---+------+------+---+--------------------------------------------------+
| I | Name | Type | # | Description                                      |
| D |      |      |   |                                                  |
+===+======+======+===+==================================================+
| 1 | actu | Actu | 1 | It specifies the Actuator Profile                |
|   | ator | ator |   |                                                  |
+---+------+------+---+--------------------------------------------------+
| 2 | cons | Cons | 1 | It specifies the Consumer that implements the    |
|   | umer | umer |   | security functions                               |
+---+------+------+---+--------------------------------------------------+

“Actuator” type is described in Language Specification (section
3.3.1.3).
