import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import pandas as pd
import streamlit as st



def pre_event(start_date, end_date):
    Jan6 = pd.read_csv(r"C:\Users\Akshay\OneDrive\Desktop\Capstone_Akshay\code\component\df.csv") ## Debt
    Jan6 = Jan6[Jan6['hate_core'] == True]

    Jan6['Day'] = pd.to_datetime(Jan6['Day'])
    Jan6 = Jan6[(Jan6['Day'] >= start_date) & (Jan6['Day'] <= end_date)]


    df = Jan6[['Source','Target']]
    df = df[df['Source'] != df['Target']]
    unique_pairs = df.groupby(['Source', 'Target']).size().reset_index(name='Weights')
    unique_pairs = unique_pairs[unique_pairs['Weights'] > 1]

    #############################################################################################################################################################

    got_net = Network( notebook=True,cdn_resources="remote", height="500px", width="100%",  bgcolor="black",  font_color="red",)

    # set the physics layout of the network
    got_net.repulsion()
    got_data = unique_pairs
    sources = unique_pairs["Source"]
    targets = unique_pairs["Target"]
    weights = unique_pairs['Weights']

    edge_data = zip(sources, targets, weights)

    for e in edge_data:
        src = str(e[0])
        dst = str(e[1])
        w = e[2]
        got_net.add_node(src, src, title=src)
        got_net.add_node(dst, dst, title=dst)
        got_net.add_edge(src, dst, value=w)
    

    
    neighbor_map = got_net.get_adj_list()
    got_net.show("preevent.html")
'''    if physics:
        got_net.show_buttons(filter_=['physics'])
    '''


def post_event( start_date, end_date):
    Jan6 = pd.read_csv(r"C:\Users\Akshay\OneDrive\Desktop\Capstone_Akshay\code\component\df.csv") ## Debt
    Jan6 = Jan6[Jan6['hate_core'] == True]
    Jan6['Day'] = pd.to_datetime(Jan6['Day'])
    Jan6 = Jan6[(Jan6['Day'] >= start_date) & (Jan6['Day'] <= end_date)]
    

    df = Jan6[['Source','Target']]
    df = df[df['Source'] != df['Target']]
    unique_pairs = df.groupby(['Source', 'Target']).size().reset_index(name='Weights')

    #############################################################################################################################################################
    got_net = Network( notebook=True,cdn_resources="remote", height="500px", width="100%",  bgcolor="black",  font_color="red",)

    # set the physics layout of the network
    got_net.repulsion()
    got_data = unique_pairs
    sources = unique_pairs["Source"]
    targets = unique_pairs["Target"]
    weights = unique_pairs['Weights']

    edge_data = zip(sources, targets, weights)

    for e in edge_data:
        src = str(e[0])
        dst = str(e[1])
        w = e[2]
        got_net.add_node(src, src, title=src)
        got_net.add_node(dst, dst, title=dst)
        got_net.add_edge(src, dst, value=w)

    
    neighbor_map = got_net.get_adj_list()
    got_net.show("postevent.html")

    '''if physics:
        got_net.show_buttons(filter_=['physics'])'''
    

 
  
def network_vis( physics, start_date_1, end_date_1, start_date_2, end_date_2):

    Jan6 = pd.read_csv(r"C:\Users\Akshay\OneDrive\Desktop\Capstone_Akshay\code\component\df.csv") ## Debt
    Jan6 = Jan6[Jan6['hate_core'] == True]
    Jan6 = Jan6[(Jan6['SNS Source'] == 'TG') |(Jan6['SNS Target'] == 'TG') ]
    Jan6['Day'] = pd.to_datetime(Jan6['Day'])
    pre_event = Jan6[(Jan6['Day'] >= start_date_1) & (Jan6['Day'] <= end_date_1)]
    post_event = Jan6[(Jan6['Day'] >= start_date_2) & (Jan6['Day'] <= end_date_2)]



    df_pre_event = pre_event[['Source','Target']]
    #df_pre_event = df_pre_event[df_pre_event['Source'] != df_pre_event['Target']]
    unique_pairs_pre_event = df_pre_event.groupby(['Source', 'Target']).size().reset_index(name='Weights')
    unique_pairs_pre_event = unique_pairs_pre_event[unique_pairs_pre_event['Weights'] > 1]

    df_post_event = post_event[['Source','Target']]
    #df_post_event = df_post_event[df_pre_event['Source'] != df_post_event['Target']]
    unique_pairs_post_event = df_post_event.groupby(['Source', 'Target']).size().reset_index(name='Weights')
    unique_pairs_post_event = unique_pairs_post_event[unique_pairs_post_event['Weights'] > 1]

    pre_net = Network( notebook=True,cdn_resources="remote", height="500px", width="100%",  bgcolor="white",  font_color="red", directed= True)

    # set the physics layout of the network
    pre_net.repulsion()
    got_data = unique_pairs_pre_event
    sources = unique_pairs_pre_event["Source"]
    targets = unique_pairs_pre_event["Target"]
    weights = unique_pairs_pre_event['Weights']

    edge_data = zip(sources, targets, weights)

    for e in edge_data:
        src = str(e[0])
        dst = str(e[1])
        w = e[2]
        pre_net.add_node(src, src, title=src)
        pre_net.add_node(dst, dst, title=dst)
        pre_net.add_edge(src, dst, value=w)

    
    neighbor_map = pre_net.get_adj_list()

    
######################################################################################################################################################################
    post_net = Network( notebook=True,cdn_resources="remote", height="500px", width="100%",  bgcolor="white",  font_color="red", directed= True)
    post_net.repulsion()

    got_data = unique_pairs_post_event
    sources = unique_pairs_post_event["Source"]
    targets = unique_pairs_post_event["Target"]
    weights = unique_pairs_post_event['Weights']

    edge_data = zip(sources, targets, weights)

    for e in edge_data:
        src = str(e[0])
        dst = str(e[1])
        w = e[2]
        post_net.add_node(src, src, title=src)
        post_net.add_node(dst, dst, title=dst)
        post_net.add_edge(src, dst, value=w)

    
    neighbor_map = post_net.get_adj_list()

    if physics:
        pre_net.force_atlas_2based( spring_strength=0.50)
        post_net.force_atlas_2based( spring_strength=0.50)

    


    pre_net.show("preevent.html")
    post_net.show("postevent.html")



 
        
    