# Context Discovery Actuator Profile

## 1. Goals of Context Discovery

To fill the gap left by the OpenC2 specifications, a new Actuator Profile has been introduced with the goal to abstract the services that are running into the network, the interactions between them and the security features that they implement. Identifying a service involves determining its type and the specific characteristics of that type. The service also provides essential information, such as hostname, encoding format, and transfer protocol, for connecting to it and to any linked services. In this way, the context in which the service is operating is identified. This new Actuator Profile has been named “Context Discovery”, herein referred as CTXD, with the nsid “ctxd”.

The Context Discovery employs a recursive function to achieve this task, querying each digital resource to determine its features. Thus, once the Producer has obtained from the Consumer the information on how to connect to the digital resources linked to the Consumer, it will query each new digital resource to determine its features, thereby producing a map.

The Context Discovery profile is implemented on the Consumer side and is one of the possible Actuator Profiles that the Consumer can support. Communication follows the OpenC2 standard, where a Producer sends a Command specifying that the Actuator to execute it is CTXD. If the Consumer implements CTXD, it will return a Response.

## 2. Data model

A data model is implemented to define which data the CTXD stores and the relationship between them. The most important data stored are:

- **Service:** It is the main class of the data model, and it describes the environment where the service is located, its links to other services, its subservices, the owner, the release, the security functions, and the actuator.
- **Service-Type:** This class identifies the specific type of service. Each instance has its own parameters, and the Service has only one type. Examples: VM, Container, Cloud, etc.
- **Link:** This class describes the connection between the services. The field “peers” specifies the services that are on the other side of the link, so this class is useful for recursive discovery. Also, security functions applied on the link are specified and they are described as OpenC2 Actuator Profiles.
- **Consumer:** It manages information about various services, including the security functions that protect them.
- **OpenC2-Endpoint:** They are described in the OpenC2-Endpoint class and correspond to both the OpenC2 Actuator Profile and the endpoint that implements it. A service can implement multiple security functions.
- **Peer:** This class describes the service that is connected to the service under analysis.

![Centered Image](data%20model.png)

## 3. Command Components

This section identifies the applicable components of an OpenC2 Command. The components of an OpenC2 Command include:

- **Action:** List of Actions that are relevant for the CTXD. This Profile cannot define Actions that are not included in the OpenC2 Language Specification, but it may extend their definitions.
- **Target:** List of Targets included in the Language Specification and one Target (and its associated Specifiers) that is defined only for the CTXD.
- **Arguments:** List of Command Arguments that are relevant for the CTXD.
- **Actuator:** List of Actuator Specifiers that are relevant for the CTXD.

### 3.1 Actions

Action is a mandatory field in Command message and no Actuator Profile can add a new Action that is not present in the specifications.

Type: Action (Enumerated)

| ID  | Name    | Description                       |
| --- | ------- | --------------------------------- |
| 3   | query   | Initiate a request for information. |

### 3.2 Target

Target is a mandatory field in Command message, and it is possible to define new Targets that are not present in the specifications. Only one Target is allowed in a Command, and that’s why the cardinality of each one equals to 1.

Type: Target (Choice)

| ID    | Name    | Type    | #  | Description                                                                   |
| ----- | ------- | ------- | --- | ----------------------------------------------------------------------------- |
| 9     | features| Features| 1   | A set of items used with the query Action to determine an Actuator’s capabilities. |
| 2048  | context | Context | 1   | It describes the service environment, its connections and security capabilities. |

A new target, called “context” is inserted because the Target “features” refers only to the Actuator capabilities and not to the characteristics of the execution environment.

### 3.3 Context

Type: Context (Record)

| ID  | Name    | Type             | #    | Description                                           |
| --- | ------- | ---------------- | ---- | ----------------------------------------------------- |
| 1   | services| ArrayOf(Name)    | 0..1 | List the service names that the command refers to.    |
| 2   | links   | ArrayOf(Name)    | 0..1 | List the link names that the command refers to.       |

The Target Context is used when the Producer wants to know the information of all active services and links of the Consumer. The Producer can specify the names of the services and links it is interested in.

### Usage Requirements

- Producer may send a “query” Command with no fields to the Consumer, which could return a heartbeat to this command.
- A Producer may send a “query” Command containing an empty list of services. The Consumer should return all the services.
- A Producer may send a “query” Command containing an empty list of links. The Consumer should return all the links.
- A Producer may send a “query” Command containing an empty list of services and links. The Consumer should return all the services and links.

### 3.4 Command Arguments

Type: Args (Map)

| ID    | Name              | Type           | #    | Description                                                                 |
| ----- | ----------------- | -------------- | ---- | --------------------------------------------------------------------------- |
| 4     | response_requested | Response-Type  | 0..1 | The type of Response required for the Command: none, ack, status, complete.  |
| 2048  | name_only          | Boolean        | 0..1 | The response includes either only the name or all the details about the services and the links. |

Command Arguments are optional, and a new one called “name_only” has been defined, which is not present in the Language Specification.

### Usage requirements:

- The "response_requested": "complete" argument can be present in the "query features" Command. (Language specification 4.1)
- The “query context” Command may include the "response_requested": "complete" Argument.
- The “query context” command may include the “name_only” argument:
  - If TRUE, the Consumer must send a Response containing only the names of the services and/or links.
  - If FALSE, the Consumer must send a Response containing all the details of the services and/or links.

### 3.5 Actuator Specifiers

List of Actuators Specifiers that are applicable to the Actuator. This is an optional field. These specifiers are not present in the Language Specification.

Type: Specifiers (Map)

| ID  | Name     | Type   | #    | Description                                    |
| --- | -------- | ------ | ---- | ---------------------------------------------- |
| 1   | domain   | String | 0..1 | Domain under the responsibility of the actuator |
| 2   | asset_id | String | 0..1 | Identifier of the actuator                    |

### 3.6 Response Components

This section defines the Response Components relevant to the CTXD Actuator Profile. The table below outlines the fields that constitute an OpenC2 Response.

Type: OpenC2-Response (Map)

| ID  | Name        | Type           | #    | Description                                      |
| --- | ----------- | -------------- | ---- | ------------------------------------------------ |
| 1   | status      | Status-Code    | 1    | Status code                                      |
| 2   | status_text | String         | 1    | Description of the Response status               |
| 3   | results     | Results        | 1    | Results derived from the executed Command        |

## 4 Response Components

This section defines the Response Components relevant to the CTXD Actuator Profile. The table below outlines the fields that constitute an OpenC2 Response.

Type: OpenC2-Response (Map)

| ID  | Name         | Type          | #    | Description                                         |
| --- | ------------ | ------------- | ---- | --------------------------------------------------- |
| 1   | status       | Status-Code   | 1    | Status code                                         |
| 2   | status_text  | String        | 1    | Description of the Response status                  |
| 3   | results      | Results       | 1    | Results derived from the executed Command           |

### 4.1 Response status code

Type: Status-Code (Enumerated.ID)

| ID   | Description                                                                                                      |
| ---- | ---------------------------------------------------------------------------------------------------------------- |
| 102  | Processing - an interim Response used to inform the Producer that the Consumer has accepted the Command but has not yet completed it. |
| 200  | OK - the Command has succeeded.                                                                                   |
| 400  | Bad Request - the Consumer cannot process the Command due to something that is perceived to be a Producer error (e.g., malformed Command syntax). |
| 401  | Unauthorized - the Command Message lacks valid authentication credentials for the target resource or authorization has been refused for the submitted credentials. |
| 403  | Forbidden - the Consumer understood the Command but refuses to authorize it.                                      |
| 404  | Not Found - the Consumer has not found anything matching the Command.                                             |
| 500  | Internal Error - the Consumer encountered an unexpected condition that prevented it from performing the Command.  |
| 501  | Not Implemented - the Consumer does not support the functionality required to perform the Command.               |
| 503  | Service Unavailable - the Consumer is currently unable to perform the Command due to a temporary overloading or maintenance of the Consumer. |

### 4.2 Common Results

This section refers to the Results that are meaningful in the context of a CTXD and that are listed in the Language Specification.

Type: Results (Record0..*)

| ID   | Name        | Type                | #    | Description                                                   |
| ---- | ----------- | ------------------- | ---- | ------------------------------------------------------------- |
| 1    | versions    | Version unique       | 0..* | List of OpenC2 language versions supported by this Actuator    |
| 2    | profiles    | ArrayOf(Nsid)        | 0..1 | List of profiles supported by this Actuator                   |
| 3    | pairs       | Action-Targets       | 0..1 | List of targets applicable to each supported Action           |
| 4    | rate_limit  | Number{0..*}         | 0..1 | Maximum number of requests per minute supported by design or policy |
| 1024 | slpf        | slpf:Results         | 0..1 | Example: Result properties defined in the Stateless Packet Filtering Profile |

### 4.3 CTXD Results

These results are not included in the Language Specification and are introduced specifically for the CTXD Actuator Profile.

Type: Results (Map0..*)

| ID   | Name            | Type               | #    | Description                                          |
| ---- | --------------- | ------------------ | ---- | ---------------------------------------------------- |
| 2048 | services        | ArrayOf(Service)    | 0..1 | List all the services                                |
| 2049 | links           | ArrayOf(Link)       | 0..1 | List all the links of the services                   |
| 2050 | services_names  | ArrayOf(Name)       | 0..1 | List the names of all services                       |
| 2051 | link_names      | ArrayOf(Name)       | 0..1 | List the names of all services                       |

Usage requirements:

- The response "services" can only be used when the target is "context".
- The response "links" can only be used when the target is "context".
- The response "services_names" can only be used when the target is "context".
- The response "services_names" can only be used when the target is "context".
- service_names/link_names are mutually exclusive with services/links, respectively. The choice is based on the value of the "name_only" argument in the query.

## 5 CTXD data types

With the introduction of new data types that are not specified in the original specifications, it is necessary to define these types along with their attributes, base type, and eventually the conformance clauses. In this section, each new data type is defined, and for some, a use case example is provided.

### 5.1 Name

The Name type is used to indicate the name of any object. When the Command Argument is "name_only", an array of Name is returned to the Producer.

Type: Name (Choice)

| ID   | Name         | Type        | #    | Description                                        |
| ---- | ------------ | ----------- | ---- | -------------------------------------------------- |
| 1    | uri          | URI         | 1    | Uniform Resource Identifier of the service         |
| 2    | reverse_dns  | Hostname    | 1    | Reverse domain name notation                       |
| 3    | uuid         | UUID        | 1    | Universally unique identifier of the service       |
| 4    | local        | String      | 1    | Name without guarantee of uniqueness               |

### 5.2 Operating System (OS)

It describes an Operating System.

Type: OS (Record)

| ID   | Name    | Type     | #    | Description                  |
| ---- | ------- | -------- | ---- | ---------------------------- |
| 1    | name    | String   | 1    | Name of the OS               |
| 2    | version | String   | 1    | Version of the OS            |
| 3    | family  | String   | 1    | Family of the OS             |
| 4    | type    | String   | 1    | Type of the OS               |

### 5.3 Service

Digital resources can implement one or more services, with each service described by a Service type. This type is a key element of the data model, as it provides the information the Producer is seeking about the services.

Type: Service (Record)

| ID   | Name          | Type               | #    | Description                             |
| ---- | ------------- | ------------------ | ---- | --------------------------------------- |
| 1    | name          | Name               | 1    | Id of the service                      |
| 2    | type          | Service-Type       | 1    | It identifies the type of the service  |
| 3    | links         | ArrayOf(Name)      | 0..1 | Links associated with the service      |
| 4    | subservices   | ArrayOf(Name)      | 0..1 | Subservices of the main service        |
| 5    | owner         | String             | 0..1 | Owner of the service                   |
| 6    | release       | String             | 0..1 | Release version of the service         |
| 7    | security_functions | ArrayOf(OpenC2-Endpoint) | 0..1 | Actuator Profiles associated with the service |
| 8    | actuator      | Consumer           | 1    | It identifies who is carrying out the service |

### 5.4 Service-Type

It represents the type of service, where each service type is further defined with additional information that provides a more detailed description of the service’s characteristics.

Type: Service-Type (Choice)

| ID   | Name         | Type        | #    | Description                           |
| ---- | ------------ | ----------- | ---- | ------------------------------------- |
| 1    | application  | Application | 1    | Software application                  |
| 2    | vm           | VM          | 1    | Virtual Machine                       |
| 3    | container    | Container   | 1    | Container                             |
| 4    | web_service  | Web-Service | 1    | Web service                           |
| 5    | cloud        | Cloud       | 1    | Cloud                                 |
| 6    | network      | Network     | 1    | Connectivity service                  |
| 7    | iot          | IOT         | 1    | IOT device                            |

### 5.5 Application

It describes a generic application.

Type: Application (Record)

| ID   | Name        | Type     | #    | Description                            |
| ---- | ----------- | -------- | ---- | -------------------------------------- |
| 1    | description | string   | 1    | Generic description of the application|
| 2    | name        | String   | 1    | Name of the application                |
| 3    | version     | string   | 1    | Version of the application             |
| 4    | owner       | string   | 1    | Owner of the application               |
| 5    | type        | String   | 1    | Type of the application                |

Sample Application object represented in JSON Format:

```json
{
    "description": "application",
    "name": "iptables",
    "version": "1.8.10",
    "owner": "Netfilter",
    "type": "Packet Filtering"
}
```

### 5.6 VM

It describes a Virtual Machine.

Type: VM (Record)

| ID  | Name      | Type   | #  | Description                        |
| --- | --------- | ------ | -- | ---------------------------------- |
| 1   | description | String | 1  | Generic description of the VM      |
| 2   | id        | String | 1  | ID of the VM                       |
| 3   | hostname  | Hostname | 1  | Hostname of the VM                |
| 4   | os        | OS     | 1  | Operating System of the VM         |

Sample VM object represented in JSON Format:

```json
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
```

### 5.7 Container

It describes a generic Container.

Type: Container (Record)

| ID  | Name      | Type   | #  | Description                              |
| --- | --------- | ------ | -- | ---------------------------------------- |
| 1   | description | String | 1  | Generic description of the container     |
| 2   | id        | String | 1  | ID of the Container                      |
| 3   | hostname  | Hostname | 1  | Hostname of the Container               |
| 4   | runtime   | String | 1  | Runtime managing the Container           |
| 5   | os        | OS     | 1  | Operating System of the Container        |

Sample Container object represented in JSON Format:

```json
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
```

### 5.8 Web Service

It describes a generic web service.

Type: Web Service (Record)

| ID  | Name       | Type     | #  | Description                                 |
| --- | ---------- | -------- | -- | ------------------------------------------- |
| 1   | description | String   | 1  | Generic description of the web service      |
| 2   | server     | Server   | 1  | Hostname or IP address of the server        |
| 3   | port       | Integer  | 1  | The port used to connect to the web service |
| 4   | endpoint   | String   | 1  | The endpoint used to connect to the web service |
| 5   | owner      | String   | 1  | Owner of the web service                    |

Sample Web Service object represented in JSON Format:

```json
{
  "description": "web_service",
  "server": "192.168.0.1",
  "port": 443,
  "endpoint": "maps/api/geocode/json",
  "owner": "Google"
}
```

### 5.9 Cloud

It describes a generic Cloud service.

Type: Cloud (Record)

| ID  | Name       | Type     | #  | Description                                  |
| --- | ---------- | -------- | -- | -------------------------------------------- |
| 1   | description | String   | 1  | Generic description of the cloud service     |
| 2   | id         | String   | 1  | Id of the cloud provider                     |
| 3   | name       | String   | 1  | Name of the cloud provider                   |
| 4   | type       | String   | 1  | Type of the cloud service                    |

Sample Cloud object represented in JSON Format:

```json
{
  "description": "cloud",
  "cloud_id": "123456",
  "name": "aws",
  "type": "lambda"
}
```

### 5.10 Network

It describes a generic network service. The Network-Type is described in the following sections.

Type: Network (Record)

| ID  | Name        | Type         | #  | Description                               |
| --- | ----------- | ------------ | -- | ----------------------------------------- |
| 1   | description | String       | 1  | Generic description of the network       |
| 2   | name        | String       | 1  | Name of the network provider             |
| 3   | type        | Network-Type | 1  | Type of the network service              |

Sample Network object represented in JSON Format:

```json
{
  "description": "network",
  "name": "The Things Network",
  "type": "LoRaWAN"
}
```

### 5.11 IOT

It describes an IoT device.

Type: IOT (Record)

| ID  | Name        | Type   | #  | Description                               |
| --- | ----------- | ------ | -- | ----------------------------------------- |
| 1   | description | String | 1  | Identifier of the IoT function            |
| 2   | name        | String | 1  | Name of the IoT service provider          |
| 3   | type        | String | 1  | Type of the IoT device                    |

Sample IOT object represented in JSON Format:

```json
{
  "description": "IoT",
  "name": "Azure IoT",
  "type": "sensor"
}
```

### 5.12 Network-Type

This class describes the type of the network service. The details of these types are not further elaborated upon in this document.

Type: Network-Type (Choice)

| ID  | Name      | Type     | #  | Description                              |
| --- | --------- | -------- | -- | ---------------------------------------- |
| 1   | ethernet  | Ethernet | 1  | The network type is Ethernet             |
| 2   | 802.11    | 802.11   | 1  | The network type is 802.11               |
| 3   | 802.15    | 802.15   | 1  | The network type is 802.15               |
| 4   | zigbee    | Zigbee   | 1  | The network type is Zigbee               |
| 5   | vlan      | Vlan     | 1  | The network type is VLAN                 |
| 6   | vpn       | Vpn      | 1  | The network type is VPN                  |
| 7   | lorawan   | Lorawan  | 1  | The network type is LoRaWAN              |
| 8   | wan       | Wan      | 1  | The network type is WAN                  |

### 5.13 Link

A Service can be connected to one or more Services, the module Link describes the type of the connection, and the security features applied on the link.

Type: Link (Record)

| ID  | Name               | Type                   | #    | Description                                                                 |
| --- | ------------------ | ---------------------- | ---- | --------------------------------------------------------------------------- |
| 1   | name               | Name                   | 1    | Id of the link                                                              |
| 2   | description        | String                 | 0..1 | Generic description of the relationship                                     |
| 3   | versions           | ArrayOf(version)       | 0..1 | Subset of service features used in this relationship (e.g., version of an API or network protocol) |
| 4   | link_type          | Link-Type              | 1    | Type of the link                                                            |
| 5   | peers              | ArrayOf(Peer)          | 1    | Services connected on the link                                               |
| 6   | security_functions | ArrayOf(OpenC2-Endpoint) | 0..1 | Security functions applied on the link                                       |

### 5.14 Peers

The Peer object is useful for iteratively discovering the services connected on the other side of the link, enabling the Producer to build a map of the entire network.

Type: Peer (Record)

| ID  | Name            | Type         | #  | Description                                |
| --- | --------------- | ------------ | -- | ------------------------------------------ |
| 1   | service_name    | Name         | 1  | Id of the service                          |
| 2   | role            | Peer-Role    | 1  | Role of this peer in the link              |
| 3   | consumer        | Consumer     | 1  | Consumer connected on the other side of the link |

### 5.15 Link-Type

This data type describes the type of the link between the peer and the service under analysis.

Type: Link-Type (Enumerated)

| ID  | Name         | Type        | #  | Description                                  |
| --- | ------------ | ----------- | -- | -------------------------------------------- |
| 1   | api          | API         | 1  | The connection is an API                    |
| 2   | hosting      | Hosting     | 1  | The service is hosted in an infrastructure  |
| 3   | packet_flow  | Packet-Flow | 1  | Network flow                                |
| 4   | control      | Control     | 1  | The service controls another resource       |

The types of API, Hosting, Packet-Flow, and Control are not defined in this document.

### 5.16 Peer-Role

It defines the role of the Peer in the link with the service under analysis.

Type: Peer-Role (Enumerated)

| ID  | Name        | Description                                               |
| --- | ----------- | --------------------------------------------------------- |
| 1   | client      | The consumer operates as a client in the client-server model in this link |
| 2   | server      | The consumer operates as a server in the client-server model in this link |
| 3   | guest       | The service is hosted within another service.             |
| 4   | host        | The service hosts another service                         |
| 5   | ingress     | Ingress communication                                      |
| 6   | egress      | Egress communication                                       |
| 7   | bidirectional | Both ingress and egress communication                    |
| 8   | control     | The service controls another service                       |
| 9   | controlled  | The service is controlled by another service              |

### 5.17 Consumer

The Consumer provides all the networking parameters to connect to an OpenC2 Consumer.

Type: Consumer (Record)

| ID  | Name      | Type        | #  | Description                                             |
| --- | --------- | ----------- | --- | ------------------------------------------------------- |
| 1   | server    | Server      | 1   | Hostname or IP address of the server                    |
| 2   | port      | Integer     | 1   | Port used to connect to the actuator                    |
| 3   | protocol  | L4-Protocol | 1   | Protocol used to connect to the actuator                |
| 4   | endpoint  | String      | 1   | Path to the endpoint (e.g., /.wellknown/openc2)         |
| 5   | transfer  | Transfer    | 1   | Transfer protocol used to connect to the actuator       |
| 6   | encoding  | Encoding    | 1   | Encoding format used to connect to the actuator         |

### 5.18 Server

It specifies the hostname or the IPv4 address of a server.

Type: Server (Choice)

| ID  | Name        | Type       | #   | Description                                  |
| --- | ----------- | ---------- | --- | -------------------------------------------- |
| 1   | hostname    | hostname   | 1   | Hostname of the server                      |
| 2   | ipv4-addr   | IPv4-Addr  | 1   | 32-bit IPv4 address as defined in [RFC0791]  |

### 5.19 Transfer

This data type defines the transfer protocol. This list can be extended with other transfer protocols.

Type: Transfer (Enumerated)

| ID  | Name  | Description      |
| --- | ----- | ---------------- |
| 1   | http  | HTTP protocol    |
| 2   | https | HTTPS protocol   |
| 3   | mqtt  | MQTT protocol    |

### 5.20 Encoding

This data type defines the encoding format to be used. Other encodings are permitted, the type Encoding can be extended with other encoders (e.g., XML).

Type: Encoding (Enumerated)

| ID  | Name  | Description    |
| --- | ----- | -------------- |
| 1   | json  | JSON encoding  |

### 5.21 OpenC2-Endpoint

This data type corresponds to both the OpenC2 Actuator Profile and the endpoint that implements it.

Type: OpenC2-Endpoint (Record)

| ID  | Name     | Type     | #   | Description                                               |
| --- | -------- | -------- | --- | --------------------------------------------------------- |
| 1   | actuator | Actuator | 1   | It specifies the Actuator Profile                         |
| 2   | consumer | Consumer | 1   | It specifies the Consumer that implements the security functions |

“Actuator” type is described in Language Specification (section 3.3.1.3).
