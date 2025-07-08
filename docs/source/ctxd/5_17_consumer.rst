5.17 Consumer
=============

The Consumer provides all the networking parameters to connect to an
OpenC2 Consumer.

Type: Consumer (Record)


.. list-table::
   :widths: 3 5 5 5 45
   :header-rows: 1

   * - ID
     - Name
     - Type
     - #
     - Description
   * - 1
     - server
     - Server
     - 1
     - Hostname or IP address of the server
   * - 2
     - port
     - Integer
     - 1
     - Port used to connect to the actuator
   * - 3
     - protocol
     - L4-Protocol
     - 1
     - Protocol used to connect to the actuator
   * - 4
     - endpoint
     - String
     - 1
     - Path to the endpoint (e.g., /.wellknown/openc2)
   * - 5
     - transfer
     - Transfer
     - 1
     - Transfer protocol used to connect to the actuator
   * - 6
     - encoding
     - Encoding
     - 1
     - Encoding format used to connect to the actuator
