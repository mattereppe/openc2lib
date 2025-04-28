3.3 Context
===========

Type: Context (Record)

.. list-table::
   :widths: 3 4 4 3 40
   :header-rows: 1

   * - I
     - Name
     - Type
     - #
     - Description
   * - 1
     - servi
     - ArrayOf(Name)
     - 0
     - List the service names that the command refers to.
   * - 2
     - links
     - ArrayOf(Name)
     - 0
     - List the link names that the command refers to.

The Target Context is used when the Producer wants to know the
information of all active services and links of the Consumer. The
Producer can specify the names of the services and links it is
interested in.

Usage Requirements
=================

-  Producer may send a “query” Command with no fields to the Consumer,
   which could return a heartbeat to this command.
-  A Producer may send a “query” Command containing an empty list of
   services. The Consumer should return all the services.
-  A Producer may send a “query” Command containing an empty list of
   links. The Consumer should return all the links.
-  A Producer may send a “query” Command containing an empty list of
   services and links. The Consumer should return all the services and
   links.

