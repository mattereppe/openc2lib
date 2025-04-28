2. Data model
=============

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

