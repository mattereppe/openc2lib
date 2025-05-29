otupy: Running the Context Discovery Actuator Profile in a Real Case Scenario
=================================================================================

1. Description
--------------

Two of the most popular open-source CMS were considered: OpenStack and Kubernetes.

OpenStack is an open-source cloud computing platform that enables users to build and manage their own cloud infrastructure. It provides Infrastructure-as-a-Service (IaaS), which offers a framework for creating and controlling virtualized resources such as computing power, storage, and networking on demand.

Kubernetes is an open-source container orchestration system. It can manage containerized applications across multiple hosts for deploying, monitoring, and scaling containers. Containers are portable units that include the code and everything the application needs to run.

The goal of CTXD is to discover the relationships between OpenStack, Kubernetes, cloud-based virtual machines (VMs), and containers. Additionally, the types of connections between these resources are documented.

It is also possible to find the relationships between VMs and the Docker service.

Docker is a tool that lets developers package applications with all their dependencies into lightweight containers, ensuring they run consistently across different environments.

2. Pre-requisites
-----------------

To run the OpenStack actuator, the following Python library is needed:

.. code-block:: bash

    pip install openstacksdk

To run the Kubernetes actuator, the following Python library is needed:

.. code-block:: bash

    pip install kubernetes

To run the Docker actuator, the following Python library is needed:

.. code-block:: bash

    pip install docker

3. Running the Consumer
-----------------------

3.1 Configuration File
^^^^^^^^^^^^^^^^^^^^^^

In the file ``otupy/applications/ctxd/configuration.json`` at the position ``consumer["ip"], consumer["port"], consumer["endpoint"]`` are specified all the useful parameters to run the consumer. The default encoder format is JSON while the transfer protocol is HTTP.

3.2 Setting up the Consumer
^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. The consumer, in order to connect to OpenStack, is able to retrieve the environment variables of the running system or it is possible to insert the full path of the configuration file into the file ``otupy/applications/ctxd/configuration.json`` in the field ``["clusters"][]["file_enviroment_variables"]``.

2. Specify the namespaces of interest in the file ``otupy/applications/ctxd/configuration.json`` and the field is ``["clusters"][]["namespace"]``. If no namespaces are specified, all namespaces will be displayed.

3. The consumer, in order to connect to Kubernetes, will use by default the configuration file contained in ``~/.kube/config``. It is also possible to specify the configuration file into ``otupy/applications/ctxd/configuration.json`` in the field ``["clusters"][]["config_file"]``.

4. Specify the Kubernetes context into the file ``otupy/applications/ctxd/configuration.json`` in the field ``["clusters"][]["kube_context"]``. If not specified, the function uses the current context in the kubeconfig file.

5. It is possible to add Kubernetes, OpenStack and Docker elements to ``["clusters"][]`` but the ``type`` field must be equal to "kubernetes", "openstack" or "docker".

6. The consumer parameters (asset_id, hostname, ip, port, protocol, endpoint, transfer, encoding) in the file ``otupy/applications/ctxd/configuration.json`` in the field ``["clusters"][]`` allow to specify how to connect to the consumer that is running Kubernetes, OpenStack or Docker. Transfer and encoding must be in numeric format. To know which integer to use, see ``/otupy/docs/CTXD documentation.md`` file, specifically paragraphs 5.19 and 5.20.

7. To connect to the MongoDB database, the file ``otupy/applications/ctxd/configuration.json`` in the field ``["mongodb"][]`` allows specifying the parameters useful for the connection. It is possible to connect to the MongoDB database without username and password.

8. Run the consumer:

.. code-block:: bash

    python otupy/applications/ctxd/ctxd_consumers.py

4. Running the Producer
-----------------------

4.1 Setting up the Producer
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run the producer:

.. code-block:: bash

    python otupy/applications/ctxd/ctxd_producer.py

No configuration files are associated with the producer.

4.2 Collecting the Output
^^^^^^^^^^^^^^^^^^^^^^^^^

1. If it is not possible to visualize the PDF because the code is executed on a remote machine, export the ``.gv`` to a local machine.

2. Convert the ``.gv`` file with the following Python script:

.. code-block:: python

    import graphviz

    def gv_to_pdf(input_gv, output_pdf):
        # Read the .gv file and create a Graphviz object
        with open(input_gv, 'r') as file:
            dot_data = file.read()

        # Create a Graph object
        graph = graphviz.Source(dot_data)

        # Render the graph to PDF
        graph.render(output_pdf, format='pdf', cleanup=True)

    # Convert example.gv to PDF
    input_gv = "<your_gf_local_path>"  # Replace with your .gv file path
    output_pdf = "<your_pdf_local_path>"  # Output file without the .pdf extension
    gv_to_pdf(input_gv, output_pdf)

3. The PDF is ready.
