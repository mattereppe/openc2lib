5.13 Link
=========

A Service can be connected to one or more Services, the module Link
describes the type of the connection, and the security features applied
on the link.

Type: Link (Record)

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
     - Id of the link.
   * - 2
     - desc
     - String
     - 0
     - Generic description of the relationship.
   * - 3
     - versions
     - ArrayOf(version)
     - 0
     - Subset of service features used in this relationship (e.g., version of an API or network protocol).
   * - 4
     - link_type
     - Link-Type
     - 1
     - Type of the link.
   * - 5
     - peers
     - ArrayOf(Peer)
     - 1
     - Services connected on the link.
   * - 6
     - security_functions
     - ArrayOf(OpenC2-Endpoint)
     - 0
     - Security functions applied on the link.

