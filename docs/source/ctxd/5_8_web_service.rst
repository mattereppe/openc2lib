5.8 Web Service
===============

It describes a generic web service.

Type: Web Service (Record)

.. list-table::
   :widths: 3 4 4 3 40
   :header-rows: 1

   * - ID
     - Name
     - Type
     - #
     - Description
   * - 1
     - description
     - String
     - 1
     - Generic description of the web service.
   * - 2
     - server
     - String
     - 1
     - Hostname or IP address of the server.
   * - 3
     - port
     - Integer
     - 1
     - The port used to connect to the web service.
   * - 4
     - endpoint
     - String
     - 1
     - The endpoint used to connect to the web service.
   * - 5
     - owner
     - String
     - 1
     - Owner of the web service.

Sample Web Service object represented in JSON Format:

.. code:: json

   {
     "description": "web_service",
     "server": "192.168.0.1",
     "port": 443,
     "endpoint": "maps/api/geocode/json",
     "owner": "Google"
   }

