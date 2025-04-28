5.5 Application
===============

It describes a generic application.

Type: Application (Record)

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
     - Generic description of the application.
   * - 2
     - name
     - String
     - 1
     - Name of the application.
   * - 3
     - version
     - String
     - 1
     - Version of the application.
   * - 4
     - owner
     - String
     - 1
     - Owner of the application.
   * - 5
     - type
     - String
     - 1
     - Type of the application.

Sample Application object represented in JSON Format:

.. code:: json

   {
       "description": "application",
       "name": "iptables",
       "version": "1.8.10",
       "owner": "Netfilter",
       "type": "Packet Filtering"
   }

