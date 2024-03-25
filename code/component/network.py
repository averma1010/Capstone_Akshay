import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import pandas as pd
import streamlit as st



def got_func(physics, start_date, end_date):
    pre_Jan6 = pd.read_csv(r'C:\Users\Akshay\OneDrive\Desktop\Capstone_Akshay\pre_jan6.csv')
    pre_Jan6 = pre_Jan6[pre_Jan6['hate_core'] == True]
    pre_Jan6['Day'] = pd.to_datetime(pre_Jan6['Day'])
    pre_Jan6 = pre_Jan6[(pre_Jan6['Day'] >= start_date) & (pre_Jan6['Day'] <= end_date)]


    df = pre_Jan6[['Source','Target']]
    df = df[df['Source'] != df['Target']]
    unique_pairs = df.groupby(['Source', 'Target']).size().reset_index(name='Weights')
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

    if physics:
        got_net.show_buttons(filter_=['physics'])
    got_net.show("gameofthrones.html")

 
  
