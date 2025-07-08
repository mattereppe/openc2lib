5.10 Network
=============

It describes a generic network service. The Network-Type is described in
the following sections.

Type: Network (Record)

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
     - Generic description of the network.
   * - 2
     - name
     - String
     - 1
     - Name of the network provider.
   * - 3
     - type
     - Network-Type
     - 1
     - Type of the network service.

Sample Network object represented in JSON Format:

.. code:: json

   {
     "description": "network",
     "name": "The Things Network",
     "type": "LoRaWAN"
   }

