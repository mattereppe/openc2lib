5.14 Peers
==========

The Peer object is useful for iteratively discovering the services
connected on the other side of the link, enabling the Producer to build
a map of the entire network.

Type: Peer (Record)

.. list-table::
   :widths: 3 4 4 3 40
   :header-rows: 1

   * - ID
     - Name
     - Type
     - #
     - Description
   * - 1
     - service_name
     - Name
     - 1
     - Id of the service.
   * - 2
     - role
     - Peer-Role
     - 1
     - Role of this peer in the link.
   * - 3
     - consumer
     - Consumer
     - 1
     - Consumer connected on the other side of the link.

