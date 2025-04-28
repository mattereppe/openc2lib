3.2 Target
==========

Target is a mandatory field in Command message, and it is possible to
define new Targets that are not present in the specifications. Only one
Target is allowed in a Command, and that’s why the cardinality of each
one equals to 1.

Type: Target (Choice)

.. list-table::
   :widths: 3 4 4 3 40
   :header-rows: 1

   * - I
     - Name
     - Type
     - #
     - Description
   * - 9
     - feat
     - Feat
     - 1
     - A set of items used with the query Action to determine an Actuator’s capabilities.
   * - 2
     - con
     - Con
     - 1
     - It describes the service environment, its connections and security capabilities.

A new target, called “context” is inserted because the Target “features”
refers only to the Actuator capabilities and not to the characteristics
of the execution environment.

