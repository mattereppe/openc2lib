4.1 Response status code
=========================

Type: Status-Code (Enumerated.ID)

.. list-table::
   :widths: 3 60
   :header-rows: 1

   * - ID
     - Description
   * - 102
     - Processing - an interim Response used to inform the Producer that the Consumer has accepted the Command but has not yet completed it.
   * - 200
     - OK - the Command has succeeded.
   * - 400
     - Bad Request - the Consumer cannot process the Command due to something that is perceived to be a Producer error (e.g., malformed Command syntax).
   * - 401
     - Unauthorized - the Command Message lacks valid authentication credentials for the target resource or authorization has been refused for the submitted credentials.
   * - 403
     - Forbidden - the Consumer understood the Command but refuses to authorize it.
   * - 404
     - Not Found - the Consumer has not found anything matching the Command.
   * - 500
     - Internal Error - the Consumer encountered an unexpected condition that prevented it from performing the Command.
   * - 501
     - Not Implemented - the Consumer does not support the functionality required to perform the Command.
   * - 503
     - Service Unavailable - the Consumer is currently unable to perform the Command due to a temporary overloading or maintenance of the Consumer.

