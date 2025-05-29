5.21 OpenC2-Endpoint
====================

This data type corresponds to both the OpenC2 Actuator Profile and the
endpoint that implements it.

Type: OpenC2-Endpoint (Record)

+---+-------+--------+---+--------------------------------------------------+
| I | Name  | Type   | # | Description                                      |
| D |       |        |   |                                                  |
+===+=======+========+===+==================================================+
| 1 | actu  | Actuator | 1 | It specifies the Actuator Profile                |
+---+-------+--------+---+--------------------------------------------------+
| 2 | cons  | Consumer | 1 | It specifies the Consumer that implements the    |
|   |       |         |   | security functions                               |
+---+-------+--------+---+--------------------------------------------------+

“Actuator” type is described in Language Specification (section 3.3.1.3).

