4.1 Response status code
=========================

Type: Status-Code (Enumerated.ID)

.. list-table::
   :widths: 3 60
   :header-rows: 1

   * - I
     - Description
   * - 1
     - Processing - an interim Response used to inform the Producer that the Consumer has accepted the Command but has not yet completed it.
   * - 2
     - OK - the Command has succeeded.
   * - 4
     - Bad Request - the Consumer cannot process the Command due to something that is perceived to be a Producer error (e.g., malformed Command syntax).
   * - 4
     - Unauthorized - the Command Message lacks valid authentication credentials for the target resource or authorization has been refused for the submitted credentials.
   * - 4
     - Forbidden - the Consumer understood the Command but refuses to authorize it.
   * - 4
     - Not Found - the Consumer has not found anything matching the Command.
   * - 5
     - Internal Error - the Consumer encountered an unexpected condition that prevented it from performing the Command.
   * - 5
     - Not Implemented - the Consumer does not support the functionality required to perform the Command.
   * - 5
     - Service Unavailable - the Consumer is currently unable to perform the Command due to a temporary overloading or maintenance of the Consumer.

