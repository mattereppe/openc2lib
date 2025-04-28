5.15 Link-Type
==============

This data type describes the type of the link between the peer and the
service under analysis.

Type: Link-Type (Enumerated)

.. list-table::
   :widths: 3 4 4 3 40
   :header-rows: 1

   * - ID
     - Name
     - Type
     - #
     - Description
   * - 1
     - api
     - API
     - 1
     - The connection is an API.
   * - 2
     - hosting
     - Hosting
     - 1
     - The service is hosted in an infrastructure.
   * - 3
     - packet_flow
     - Packet-Flow
     - 1
     - Network flow.
   * - 4
     - control
     - Control
     - 1
     - The service controls another resource.
   * - 5
     - protect
     - Protect
     - 1
     - The service protects another resource.

The types of API, Hosting, Packet-Flow, Control, and Protect are not
defined in this document.

