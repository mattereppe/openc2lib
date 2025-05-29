5.7 Container
=============

It describes a generic Container.

Type: Container (Record)

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
     - Generic description of the container.
   * - 2
     - id
     - String
     - 1
     - ID of the Container.
   * - 3
     - hostname
     - Hostname
     - 1
     - Hostname of the Container.
   * - 4
     - runtime
     - String
     - 1
     - Runtime managing the Container.
   * - 5
     - os
     - OS
     - 1
     - Operating System of the Container.

Sample Container object represented in JSON Format:

.. code:: json

   {
     "description": "container",
     "id": "123456",
     "hostname": "container_name",
     "runtime": "docker",
     "os": {
       "name": "ubuntu",
       "version": "22.04.3",
       "family": "debian",
       "type": "linux"
     }
   }

