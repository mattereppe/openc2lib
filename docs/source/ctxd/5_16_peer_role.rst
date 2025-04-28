5.16 Peer-Role
==============

It defines the role of the Peer in the link with the service under
analysis.

Type: Peer-Role (Enumerated)

.. list-table::
   :widths: 3 5 45
   :header-rows: 1

   * - ID
     - Name
     - Description
   * - 1
     - client
     - The consumer operates as a client in the client-server model in this link.
   * - 2
     - server
     - The consumer operates as a server in the client-server model in this link.
   * - 3
     - guest
     - The service is hosted within another service.
   * - 4
     - host
     - The service hosts another service.
   * - 5
     - ingress
     - Ingress communication.
   * - 6
     - egress
     - Egress communication.
   * - 7
     - bidirectional
     - Both ingress and egress communication.
   * - 8
     - control
     - The service controls another service.
   * - 9
     - controlled
     - The service is controlled by another service.

