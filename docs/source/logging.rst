Logging for ``otupy``
=====================

Logging in ``otupy`` leverages the Python
`logging <https://docs.python.org/3/library/logging.html>`_
framework. Applications that use ``otupy`` can trigger and configure
logging for all ``otupy`` modules according to the usual hierarchical
logging approach.

The basic configuration of logging for ``otupy`` may use
``basicConfig``. These are a few examples: 

- set the logging level to DEBUG and output to a file:

.. code-block:: python3

     logging.basicConfig(filename='openc2.log',level=logging.DEBUG)

- set the logging level to INFO and output to console:

.. code-block:: python3

     logging.basicConfig(stream=sys.stdout,level=logging.INFO)

Openc2lib also provides its own ``Formatter`` which is nicer to look
than the default plain version. However, this means a more complex
configuration must be done. You have to define your own logging handler:

.. code-block:: python3

     # Create stdout handler for logging to the console
     stdout_handler = logging.StreamHandler()
     # Set 4 levels of logging: INFO, WARNING, ERROR, CRITICAL
     stdout_handler.setLevel(logging.INFO)
     # Load the otupy logFormatter, and set its options
     stdout_handler.setFormatter(logFormatter(datetime=True,name=True))

and then load such handler (if can either apply the to a specific logger
(e.g, the code in the example below) or to all loggers (if you
don’t give any argument to the ``getLogger`` function):

.. code-block:: python3

     # Declare the logger name (you may select a name that enables logging in just a tree of the logging hierarchy)
     logger = logging.getLogger('otupy')
     # Add the handler to the current logger 
     logger.addHandler(stdout_handler)

or via standard or ``basicConfig`` configuration to the root logger
(this example applies the handler to all loggers in the hierarcy):

.. code-block:: python3

     # Create an iterable (required by basicConfig)
     hdls = [ stdout_handler ]
     # Perform basic config
     logging.basicConfig(handlers=hdls)

More complex configurations can be achieved. Please refer to the
`logging tutorials <https://docs.python.org/3/howto/logging.html>`__ for
a full guide.
