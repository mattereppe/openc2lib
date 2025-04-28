4.3 CTXD Results
================

These results are not included in the Language Specification and are
introduced specifically for the CTXD Actuator Profile.

Type: Results (Map0..*)

.. list-table::
   :widths: 3 4 4 3 40
   :header-rows: 1

   * - I
     - Name
     - Type
     - #
     - Description
   * - 2
     - services
     - ArrayOf(Service)
     - 0
     - List all the services.
   * - 2
     - links
     - ArrayOf(Link)
     - 0
     - List all the links of the services.
   * - 2
     - services_names
     - ArrayOf(Name)
     - 0
     - List the names of all services.
   * - 2
     - link_names
     - ArrayOf(Name)
     - 0
     - List the names of all links.

Usage requirements:
~~~~~~~~~~~~~~~~~~~

-  The response “services” can only be used when the target is “context”.
-  The response “links” can only be used when the target is “context”.
-  The response “services_names” can only be used when the target is “context”.
-  The response “link_names” can only be used when the target is “context”.
-  service_names/link_names are mutually exclusive with services/links,
   respectively. The choice is based on the value of the “name_only”
   argument in the query.

