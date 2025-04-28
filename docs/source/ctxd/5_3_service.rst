5.3 Service
============

Digital resources can implement one or more services, with each service
described by a Service type. This type is a key element of the data
model, as it provides the information the Producer is seeking about the
services.

Type: Service (Record)

.. list-table::
   :widths: 3 4 4 3 40
   :header-rows: 1

   * - ID
     - Name
     - Type
     - #
     - Description
   * - 1
     - name
     - Name
     - 1
     - Id of the service.
   * - 2
     - type
     - Service-Type
     - 1
     - It identifies the type of the service.
   * - 3
     - links
     - ArrayOf(Name)
     - 0
     - Links associated with the service.
   * - 4
     - subservices
     - ArrayOf(Name)
     - 0
     - Subservices of the main service.
   * - 5
     - owner
     - String
     - 0
     - Owner of the service.
   * - 6
     - release
     - String
     - 0
     - Release version of the service.
   * - 7
     - security_functions
     - ArrayOf(OpenC2-Endpoint)
     - 0
     - Actuator Profiles associated with the service.
   * - 8
     - actuator
     - Consumer
     - 1
     - It identifies who is carrying out the service.

