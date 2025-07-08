3.4 Command Arguments
=====================

Type: Args (Map)

.. list-table::
   :widths: 3 4 4 3 40
   :header-rows: 1

   * - ID
     - Name
     - Type
     - #
     - Description
   * - 4
     - response_requested
     - Response-Type
     - 0
     - The type of Response required for the Command: none, ack, status, complete.
   * - 2
     - name_only
     - Boolean
     - 0
     - The response includes either only the name or all the details about the services and the links.

Command Arguments are optional, and a new one called “name_only” has
been defined, which is not present in the Language Specification.

Usage requirements:
===================

-  The “response_requested”: “complete” argument can be present in the
   “query features” Command. (Language specification 4.1)
-  The “query context” Command may include the “response_requested”:
   “complete” Argument.
-  The “query context” command may include the “name_only” argument:

   -  If TRUE, the Consumer must send a Response containing only the
      names of the services and/or links.
   -  If FALSE, the Consumer must send a Response containing all the
      details of the services and/or links.

