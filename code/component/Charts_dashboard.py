import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import resample
import datetime
import seaborn as sns

import networkx as nx
import copy
import random
import getpass
import psycopg2 as ps
import os
import re
from scipy.stats import pearsonr

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from pandas.plotting import register_matplotlib_converters
from scipy.ndimage.filters import gaussian_filter1d
from matplotlib.dates import DateFormatter, DayLocator
import streamlit as st

class EdgeCountAnalyzer:
    def __init__(self):
        self.data = pd.read_csv(r"C:\Users\Akshay\OneDrive\Desktop\Capstone_Akshay\code\component\Jan6.csv")
        self.data['Day'] = pd.to_datetime(self.data['Day'])

    def calculate_relative_increase(self, start_date, end_date):
        # Converting to Datetime format
        
        

        Jan6 = self.data[(self.data['Day'] >= start_date) & (self.data['Day'] <= end_date)]

        # Group by 'Day' and count the number of rows for each day
        daily_counts_Jan6 = Jan6.groupby('Day').size()

        # Calculate the increase relative to the first day
        relative_increase_Jan6 = ((daily_counts_Jan6 - daily_counts_Jan6.iloc[0])/(daily_counts_Jan6.iloc[0]))*100.00

        return relative_increase_Jan6.index, relative_increase_Jan6.values

    def edge_count_chart(self, start_date, end_date):
        index_values, chart_values = self.calculate_relative_increase(start_date, end_date)

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(index_values, chart_values, marker='o', linestyle='-', alpha=0.7, markersize=6)
        ax.set_title('Increase in Hate Links Relative to Jan 1, 2021')
        ax.set_xlabel('Day')
        ax.set_ylabel('Increase in Number of Hate Links (%)')
        ax.tick_params(axis='x', rotation=45)
        ax.set_yticklabels(['{:.0f}%'.format(x) for x in ax.get_yticks()])  # Add '%' symbol to y-axis labels
        ax.grid(False)  # Removing gridlines

        # Display the plot in Streamlit
        st.pyplot(fig)

class Network_comparison:
    def __init__(self):
        self.data = pd.read_csv(r"C:\Users\Akshay\OneDrive\Desktop\Capstone_Akshay\code\component\Jan6.csv")
        self.data['Day'] = pd.to_datetime(self.data['Day'])


    def network_comparison_metrics(self,start_date1, end_date1, start_date2, end_date2):
        Jan6 = self.data

        pre_Jan6 = Jan6[(Jan6['Day'] >= start_date1) & (Jan6['Day'] <= end_date1)]
        post_Jan6 = Jan6[(Jan6['Day'] >= start_date2) & (Jan6['Day'] <= end_date2)]

        Graph_pre_Jan6 = nx.from_pandas_edgelist(pre_Jan6, 'Source', 'Target',  create_using=nx.Graph())
        Graph_post_Jan6 = nx.from_pandas_edgelist(post_Jan6, 'Source', 'Target',  create_using=nx.Graph())



        # Calculate properties for Graph_pre_Jan6
        pre_density = nx.density(Graph_pre_Jan6)
        pre_cliques = list(nx.find_cliques(Graph_pre_Jan6))
        pre_max_clique_size = max(len(clique) for clique in pre_cliques)
        pre_num_communities = nx.number_connected_components(Graph_pre_Jan6)
        pre_largest_community = max(len(c) for c in nx.connected_components(Graph_pre_Jan6))
        pre_clustering_coefficient = nx.average_clustering(Graph_pre_Jan6)
        pre_assortativity = nx.assortativity.degree_assortativity_coefficient(Graph_pre_Jan6)

        # Calculate properties for Graph_post_Jan6
        post_density = nx.density(Graph_post_Jan6)
        post_cliques = list(nx.find_cliques(Graph_post_Jan6))
        post_max_clique_size = max(len(clique) for clique in post_cliques)
        post_num_communities = nx.number_connected_components(Graph_post_Jan6)
        post_largest_community = max(len(c) for c in nx.connected_components(Graph_post_Jan6))
        post_clustering_coefficient = nx.average_clustering(Graph_post_Jan6)
        post_assortativity = nx.assortativity.degree_assortativity_coefficient(Graph_post_Jan6)

        
        data = {
            'Property': ['Density', 'Number of Cliques', 'Max Clique Size', 'Number of Communities',
                        'Size of Largest Community', 'Clustering Coefficient', 'Assortativity'],
            f'{start_date1} to {end_date1}': [pre_density, len(pre_cliques), pre_max_clique_size, pre_num_communities,
                        pre_largest_community, pre_clustering_coefficient, pre_assortativity],
            f'{start_date2} to {end_date2}': [post_density, len(post_cliques), post_max_clique_size, post_num_communities,
                        post_largest_community, post_clustering_coefficient, post_assortativity]
        }

        return data
        

    def network_comparison_df(self,start_date1, end_date1, start_date2, end_date2):
        data = self.network_comparison_metrics(start_date1, end_date1, start_date2, end_date2)

        df = pd.DataFrame(data)

        st.write(df)

