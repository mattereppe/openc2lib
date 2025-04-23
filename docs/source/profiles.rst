Define new profiles (language extensions)
-----------------------------------------

Language extensions are typically defined as part of the definition of an Actuator profile. The following elements can be extended: 

- targets;
- arguments; 
- response results; 
- actuator properties (already covered in the `specifier <https://github.com/mattereppe/openc2/blob/main/docs/developingextensions.md#create-the-actuator-specifiers>`__ Section).

The list of ``Actions`` MUST NOT be extended (see Sec. 3.1.4 of the
`Language
Specification <https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.pdf>`__).

It is strongly recommended to follow the same naming conventions as
adopted by ``otupy`` (see the `Developer
Guide <https://github.com/mattereppe/openc2/blob/main/docs/developerguide.md#naming-conventions>`__).

Add new actuator profiles
~~~~~~~~~~~~~~~~~~~~~~~~~

To add a new profile within ``otupy`` source code, create a new
directory in the ``src/otupy/profiles`` folder. Preferably name the
folder with the nsid of the profile to be developed (e.g., ``slpf`` for
the Statless Packet Filter profile).

Define the profile
^^^^^^^^^^^^^^^^^^

A Profile is identified by its namespace identifier and a unique name.
Although there are not specific data structure defined by the
specification, ``otupy`` wrap this information in a ``Profile`` class.
The idea is to keep track of all profiles available within the system.

When a new profile is being defined, a new class can be defined and
derived from the base base ``Profile`` class. It must be registered as a
new profile by the ``@extension`` decorator. Just define the ``nsid``
and ``name`` class attributes in the new profile. This is an example of
profile definition for the SLPF:

::

   import otupy as oc2

   nsid = 'slpf'

   @oc2.extension(nsid = nsid)
   class Profile(oc2.Profile):
       """ SLPF Profile

           Defines the namespace identifier and the name of the SLPF Profile.
       """
       nsid = nsid
       name = 'http://docs.oasis-open.org/openc2/oc2slpf/v1.0/oc2slpf-v1.0.md'

(see below for additional information about the ``extension``
decorator.)

Create the actuator specifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The core specification does not dictate the internal structure of an
``Actuator``. Indeed, the ``Actuator`` field in the ``Command`` can be
assigned different types, depending on the specific actuator profile. A
new type must therefore be defined for each actuator profile, and it
must be declared as such to allow otupy to correctly encode/decode
it. The *specifiers* are the structure of any ``Actuator`` that
implements the profile. They are defined by the Profile Specification
(e.g., see `Sec.
2.1.4 <https://docs.oasis-open.org/openc2/oc2slpf/v1.0/cs01/oc2slpf-v1.0-cs01.pdf>`__
for the SLPF specifier).

To declare a Actuator specifier, use the ``@actuator`` decorator. This
decorator automatically registers the new ``Actuator``, enriches its
definition with internal data, and makes it available to both
``Producer``\ s and ``Consumer``\ s. The following is an example for the
SLPF actuator:

::

   @oc2.actuator(nsid=Profile.nsid)
   class Specifiers(oc2.Map):
       fieldtypes = dict(hostname=str, named_group=str, asset_id=str, asset_tuple = [str])

In this case, the actuator specifiers are derived from ``Map``,
according to the definition in the SLPF specification (see the `User
Guide <userguide.md>`__ for ``Map`` documentation).

The specifier definition should also implement the ``__init__`` method
to initialize class instances. It is also recommended to define a
``__str__`` function to provide a human-readable representation of the
actuator profile in log messages.

Define new types
~~~~~~~~~~~~~~~~

Adding new types can be done within each new Profile. Beaware that new
types usually needs to support the “copy-constructor”, i.e., they must
support initialization from an object of the same type.

Define new targets
~~~~~~~~~~~~~~~~~~

Targets are just specific OpenC2 data types that can be used as
``Target`` in ``Command``\ s. Any data type can be made a ``Target`` by
decorating it with the ``@target(name, nsid)`` tag. This decorator
automatically manages all the stuff to register new targets in
``otupy``. It takes two arguments, namely: 

- ``name``: the name associated to each type (e.g., see Sec. 3.3.1.2 in the `Language Specification <https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.pdf>`__);
- ``nsid``: the namespace identifier of the profile that defines the ``Target`` (default to ``None``, which means a ``Target`` defined in the
core specification).

This is an example for the SLPF profile:

::

   @target(name='rule_number', nsid=Profile.nsid)
   class RuleID(int):
       pass

(note that the ``@target`` decorator must be imported with its namespace
according to common Python rules.)

Extend Map-based types
~~~~~~~~~~~~~~~~~~~~~~

Extensions are currently possible for ``Map`` and derived base
structures (``MapOf``). For instance, both arguments (``Args``) and
response results (``Results``) are currently extensible. To make
additional data types extensible, they must be decorated with the
``@extensible`` tag.

An extension must be declared with the ``@extension(nsid)`` decorator,
where ``nsid`` is an argument that provides the namespace identifier
where the extension is defined. Then, the extension class is derived
from the base class. The extension must define only the additional
fields that are not included in the base type.

The following is a generic example for an extension (``Ext``) of the
base type (``Base``) in the namespace ``xxxx``:

::

   @extension(nsid='xxxx')
   class Ext(Base):
      fieldtypes = {'new_field': new_field_type, ... }

The decorator manages all additional fields and declaration that are
necessary to use the extension in ``otupy``.

It is possible (and this is the preferred approach) to define the
extension with the same name of the base class. By proper referring to
base and extended elements within the corresponding namespace, name
collisions are avoided and the naming remains more uniform. For
instance, the Args element and its extension could be unambigously
referred to in the code in the following way:

::

   import otupy as oc2

   import otupy.profiles.slpf as slpf

   args = Args(...)        # <- This instantiate the base Args class
   args = slpf.Args(...)   # <- This instantiate the extended Args class derived in the slpf profile

The extension of ``Args`` and ``Results`` will likely be based on
additional structures. Define them as well in the profile folder. As
best practice, data and target types should be defined in two different
modules (datatypes and targettypes, respecitvely, see the `Developer
guide <https://github.com/mattereppe/openc2/blob/main/docs/developerguide.md>`__.

Recursive definitions
~~~~~~~~~~~~~~~~~~~~~

There may singular cases where an object is recursive, namely it
contains another object of the same time. Such an example is represented
by the ``Process`` target, which internally may carry an instance of its
parent. However, Python does not allow to define such types in a
straighforward way.

Recursion should be used with care, to avoid infinite or anyway too deep
dependencies. ``otupy`` addresses this issue by providing a specific
design pattern. It is based on the Python ``typing.Self`` annotation and
the ``@make_recursive`` decorator provided by some ``otupy`` classes
(e.g., ``Map``). The design pattern entails the following step - use the
``typing.Self`` annotation for any field that should be instantiated to
the same class in which it is defined; - use the ``@make_recursive``
decorator in front of the class definition.

This is an example for the ``Process`` target:

.. code-block:: python3

   from typing import Self
   ...
   @Map.make_recursive
   class Process(Map):
      fieldtypes = {'pid': int, 'name': str, 'cwd': str, 'executable': File, 'parent': <b>Self</b>, 'command_line': str}

As a result, the ``Map`` class has the following ``fieldtypes``
definition:

.. code-block:: python3

   fieldtypes = {'pid': int, 'name': str, 'cwd': str, 'executable': File, 'parent': <b>Process</b>, 'command_line': str}
  

The ``@make_recursive`` decorator is implemented for each base type
(e.g., ``Map``). Check the code documentation to know what base types
actually implement this helper.

Syntax validation
~~~~~~~~~~~~~~~~~

Profiles are likely to restrict the possible combination of ``Actions``,
``Target``, and ``Args``. Since these restrictions are common to all
``Actuator``s, they can be defined only once within the profile.
Specific functions must be exported to perform the validation; the
internal implementation does not need to follow any specific template.
Note, however, that actuators are not expected to implement any possible
Action/Target pair and support all Arguments described by the profile.
For this reason, behind profile validation, each specific actuator will
implement its internal validation.

Export modules and data
~~~~~~~~~~~~~~~~~~~~~~~

Even if this step is not strictly required, it is recommended to pack
every new definition under the main profile namespace. This simplifies
access to exported data and structures. This operation can be done by
importing all data, classes, and functions to be exported in the
``__init__.py`` module. Such elements can then be imported and used in a
very simple and natural way under their profile namespace (which is very
similar to what expected by the specifications):

.. code-block:: python3

   import otupy.profiles.slpf as slpf

   Command(target=slpf.rule_number, ...)
   slpf.Args(...)

