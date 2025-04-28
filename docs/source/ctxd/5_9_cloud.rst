5.9 Cloud
==========

It describes a generic Cloud service.

Type: Cloud (Record)

.. list-table::
   :widths: 3 4 4 3 40
   :header-rows: 1

   * - ID
     - Name
     - Type
     - #
     - Description
   * - 1
     - desc
     - String
     - 1
     - Generic description of the cloud service.
   * - 2
     - id
     - String
     - 1
     - Id of the cloud provider.
   * - 3
     - name
     - String
     - 1
     - Name of the cloud provider.
   * - 4
     - type
     - String
     - 1
     - Type of the cloud service.

Sample Cloud object represented in JSON Format:

.. code:: json

   {
     "description": "cloud",
     "cloud_id": "123456",
     "name": "aws",
     "type": "lambda"
   }

