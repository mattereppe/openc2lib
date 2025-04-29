# openc2lib: Running the Context Discovery Actuator Profile in a real case scenario

## 1 Description

Two of the most popular open-source CMS were considered: OpenStack and Kubernetes.

OpenStack is an open-source cloud computing platform that enables users to build and manage their own cloud infrastructure. It provides Infrastructure-as-a-Service (IaaS), which offers a framework for creating and controlling virtualized resources such as computing power, storage, and networking on demand. 

Kubernetes is an open-source container orchestration system, and it can manage containerized applications across multiple hosts for deploying, monitoring, and scaling containers. Containers are portable units that include the code and everything the application needs to run.

The goal of CTXD is to discover the relationships between OpenStack, Kubernetes, cloud-based virtual machines (VMs), and containers. Additionally, the types of connections between these resources are documented.

It is also possible to find the relationships between VMs and the Docker service.

Docker is a tool that lets developers package applications with all their dependencies into lightweight containers, ensuring they run consistently across different environments.

## 2 Pre-requisities
To run correctly the Opestack actuator the following python library is needed:

```pip install openstacksdk```


To run correctly the Kubernetes actuator the following python library is needed:

```pip install kubernetes```

To run correctly the Docker actuator the following python library is needed:

```pip install docker```


## Running the Consumer

### 3.1 Configuration file

1. In the file ```openc2lib/applications/ctxd/configuration.json``` at the position ```consumer["ip"], consumer["port"], consumer["endpoint"]``` are specified all the useful parameters to run the consumer. The default encoder format is JSON while the transfer protocol is HTTP.

### 3.2 Setting up the consumer

1. The consumer, in order to connect to openstack, is able to retrieve the enviroment variables of the running system or it is possible to insert the full path of the configuration file into the file ```openc2lib/applications/ctxd/configuration.json``` in the field ```["clusters"][]["file_enviroment_variables"]```.

2. Specify the namespaces of interest in the file ```openc2lib/applications/ctxd/configuration.json``` and the field is ```["clusters"][]["namespace"]```. If no namespaces are specified, all namespaces will be displayed.

3. The consumer, in order to connect to kubernetes, will use by default the configuration file contained in ```~/.kube/config```. It is also possible to specifify the configuration file into ```openc2lib/applications/ctxd/configuration.json``` in the field ```["clusters"][]["config_file"]```.

4. Specify the kubernetes context into the file ```openc2lib/applications/ctxd/configuration.json``` in the field ```["clusters"][]["kube_context"]```. If not specified, the function uses the current context in the kubeconfig file.

5. It is possible to add kubernetes, openstack and docker elements to ```["clusters"][]``` but the ```type``` field must be equal to "kubernetes", "openstack" or "docker".

6. The consumer parameters (asset_id, hostname, ip, port, protocol, endpoint, transfer, encoding) in the file ```openc2lib/applications/ctxd/configuration.json``` in the field ```["clusters"][]``` allow to specify how to connect to the consumer that is running kubernetes, openstack or docker. Transfer and encoding must be in numeric format. To know which integer to use, see ```/openc2lib/docs/CTXD documentation.md``` file, specifically paragraphs 5.19 and 5.20

8. To connect to the mongodb database, the file ```openc2lib/applications/ctxd/configuration.json``` in the field ```["mongodb"][]``` allow to specify the parameters useful for the connection. It is possible to connect to the mongodb database without username and password.

7. Run the consumer python ```openc2lib/applications/ctxd/ctxd_consumers.py```

## 4 Running the producer

### 4.1 Setting up the Producer

1. Run the producer ```python openc2lib/applications/ctxd/ctxd_producer.py```. No configuration file are associated with the producer.

### 4.2 Collecting the output

1. if it is not possible not possible to visualize the pdf because the code is executed on a remote machine, export the .gv to a local machine

2. convert the file .gv with this python script
```
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

```
3. The .pdf is ready
