#!../.oc2-env/bin/python3
# Example to use the OpenC2 library
#
from graphviz import Digraph
import json
import logging
import os
import sys

import openc2lib as oc2

from openc2lib.encoders.json import JSONEncoder
from openc2lib.transfers.http import HTTPTransfer
import openc2lib.profiles.ctxd as ctxd
from openc2lib.profiles.ctxd.data.name import Name
from openc2lib.types.base.array_of import ArrayOf
from openc2lib.transfers.http.message import Message

from pymongo import MongoClient


logger = logging.getLogger()
# Ask for 4 levels of logging: INFO, WARNING, ERROR, CRITICAL
logger.setLevel(logging.WARNING)
# Create stdout handler for logging to the console 
stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(logging.WARNING)
stdout_handler.setFormatter(oc2.LogFormatter(datetime=True,name=True))
hdls = [ stdout_handler ]
# Add both handlers to the logger
logger.addHandler(stdout_handler)

edges_set = set()  # Track visited edges
processed_links_set = set()  # Track processed links to avoid recursion on the same links
nodes_visited = set() #track all visited nodes

def add_edge(graph, source, target, relationship_type="", dir_type="forward", color="black", fontcolor="black"):
    edge = (source, target, relationship_type, dir_type)
    if edge not in edges_set:
        graph.edge(source, target, label=relationship_type, dir=dir_type, color = color, fontcolor = fontcolor)
        edges_set.add(edge)

def edge_exists(source, target, relationship_type="", dir_type="forward"):
    return (source, target, relationship_type, dir_type) in edges_set

def get_unprocessed_links(links, parent_node):
    """Return only the unprocessed links based on the link's name."""
    unprocessed_links = []
    for it_link in links:
        # Assuming each link has a unique name or identifier we can use
        link_key = (parent_node, it_link.link_type.name, it_link.name.obj)  # Use the link's name in the key
        
        if link_key not in processed_links_set:
            unprocessed_links.append(it_link)
    return unprocessed_links

def connect_to_database(username, password, ip, port, database_name, collection_name):

        try:
            client = MongoClient("mongodb://"+ip+":"+str(port)+"/")
        except Exception:
            client = MongoClient("mongodb://"+username+":"+password+"@"+ip+":"+str(port)+"/")    

        # Create or switch to a database
        db = client[database_name]

        # Create or switch to a collection
        collection = db[collection_name]

        # Delete all documents in the collection
        collection.delete_many({})

        #return an empty collection
        return collection 


def insert_data_database(collection, response, peer_hostname =None):
        #if the node is not already visited -> add to the database
        if peer_hostname not in nodes_visited:
            m = Message()
            m.set(response)
            data = JSONEncoder().encode(m)
            parsed_data = json.loads(data)
            #insert only the results into the database
            result = parsed_data['body']['openc2']['response']['results']['x-ctxd']
            collection.insert_one(result).inserted_id
            nodes_visited.add(peer_hostname)


def recursive_process_links(links, cmd, pf, p, dot, parent_node):
    for it_link in links:
        link_key = (parent_node, it_link.link_type.name, it_link.name.obj)  # Create a unique key for the link

        # Skip if the link has been processed to avoid redundant recursion
        if link_key in processed_links_set:
            continue
        
        # Mark this link as processed
        processed_links_set.add(link_key)

        for it_peer in it_link.peers:
            peer_hostname = str(it_peer.consumer.server.obj._hostname)
            peer_service_name = str(it_peer.service_name.obj)

            #set the style of nodes and edges
            edge_color = "black"
            edge_font_color = "black"
            if(peer_service_name == "slpf"): #all edges for slpf must be red
                edge_color = "red" 
                edge_font_color = "red"

            text_color= None
            font_color = "black"
            if(peer_service_name == "slpf"):
                text_color = "red"
                font_color = "red"

            # Add the node if it doesn't exist
            pf['asset_id'] = peer_hostname
            pf.fieldtypes['asset_id'] = peer_hostname
            if(peer_hostname != peer_service_name):
                dot.node(peer_hostname, peer_hostname + "\n"+peer_service_name, color= text_color, fontcolor=font_color)
            else:
                dot.node(peer_hostname, peer_hostname, color= text_color, fontcolor=font_color)
            # Only process if the edge has not been visited
            if not edge_exists(parent_node, peer_hostname):
                if str(it_link.link_type.name) == 'packet_flow':
                    add_edge(dot, parent_node, peer_hostname, str(it_link.link_type.name), dir_type='both',color=edge_color, fontcolor=edge_font_color)
                elif str(it_link.link_type.name) == 'hosting' and it_peer.role.name == 'host':
                    add_edge(dot, parent_node, peer_hostname, str(it_link.link_type.name), dir_type='back',color=edge_color, fontcolor=edge_font_color)
                elif str(it_link.link_type.name) == 'protect' and it_peer.role.name == 'control':
                    add_edge(dot, parent_node, peer_hostname, str(it_link.link_type.name), dir_type='back', color=edge_color, fontcolor=edge_font_color)
                else:
                    add_edge(dot, parent_node, peer_hostname, str(it_link.link_type.name), color=edge_color, fontcolor=edge_font_color)

                # Send command and log response
                tmp_resp = p.sendcmd(cmd)
                logger.info("Got response: %s", tmp_resp)

                #insert data into database
                insert_data_database(collection, tmp_resp, peer_hostname)

                # Safeguard for recursive calls
                if 'results' in tmp_resp.content and 'links' in tmp_resp.content['results']:
                    new_links = tmp_resp.content['results']['links']
                    # Get only the unprocessed links
                    unprocessed_links = get_unprocessed_links(new_links, peer_hostname)
                    # Only recurse if unprocessed links exist
                    if unprocessed_links:
                        recursive_process_links(unprocessed_links, cmd, pf, p, dot, peer_hostname)

    return

def main(openstack_parameters, collection):
    logger.info("Creating Producer")

    p = oc2.Producer("producer.example.net", JSONEncoder(), HTTPTransfer(openstack_parameters['ip'],
                                                                          openstack_parameters['port'],
                                                                          openstack_parameters['endpoint']))
    pf = ctxd.Specifiers({'asset_id': openstack_parameters['asset_id']})
    pf.fieldtypes['asset_id'] = openstack_parameters['asset_id']  # I have to repeat a second time to have no bugs
    arg = ctxd.Args({'name_only': False})
    context = ctxd.Context(services=ArrayOf(Name)(), links=ArrayOf(Name)())  # expected all services and links
    cmd = oc2.Command(action=oc2.Actions.query, target=context, args=arg, actuator=pf)

    logger.info("Sending command: %s", cmd)
    resp_openstack = p.sendcmd(cmd)
    logger.info("Got response: %s", resp_openstack)

    insert_data_database(collection, resp_openstack, openstack_parameters['asset_id'])


    if not arg['name_only']: #explore actuators only if it is false
        dot = Digraph("example_graph", graph_attr={'rankdir': 'LR'})
        dot.node('openstack', 'OpenStack')
        recursive_process_links(resp_openstack.content['results']['links'], cmd, pf, p, dot, 'openstack')

        with dot.subgraph() as s:
            s.attr(rank='min')
            s.node('os-fw')
            s.node('kubernetes')
            s.node('openstack')


        dot.render(os.path.dirname(os.path.abspath(__file__))+'/example_graph' , view=False)
        dot.save(os.path.dirname(os.path.abspath(__file__))+'/example_graph.gv')

if __name__ == '__main__':
	
    configuration_file = os.path.dirname(os.path.abspath(__file__))+"/configuration.json"
    with open(configuration_file, 'r') as file:
        configuration_parameters = json.load(file)

    collection = connect_to_database(username=configuration_parameters['mongodb']['username'],
                                     password=configuration_parameters['mongodb']['password'],
                                     ip = configuration_parameters['mongodb']['ip'],
                                     port = configuration_parameters['mongodb']['port'],
                                     database_name= configuration_parameters['mongodb']['database_name'],
                                     collection_name= configuration_parameters['mongodb']['collection_name'])

    for element in configuration_parameters['clusters']:
        if (element["type"] == "openstack"):      
            main(element, collection) #start the discovery at the openstack service

