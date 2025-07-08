3.6 Response Components
=======================

This section defines the Response Components relevant to the CTXD
Actuator Profile. The table below outlines the fields that constitute an
OpenC2 Response.

Type: OpenC2-Response (Map)

.. list-table::
   :widths: 3 4 4 3 40
   :header-rows: 1

   * - ID
     - Name
     - Type
     - #
     - Description
   * - 1
     - status
     - Status-Code
     - 1
     - Status code.
   * - 2
     - status_text
     - String
     - 1
     - Description of the Response status.
   * - 3
     - results
     - Results
     - 1
     - Results derived from the executed Command.

.. _response-components-1:

