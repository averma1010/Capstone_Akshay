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


def load_data():
    """
    Load data from CSV file and perform necessary preprocessing.
    """
    file_path = r"C:\Users\Akshay\OneDrive\Desktop\Capstone_Akshay\code\component\Jan6.csv"
    data = pd.read_csv(file_path)
    data['Day'] = pd.to_datetime(data['Day'])
    return data

class EdgeCountAnalyzer:
    def __init__(self):
        self.data = load_data()


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
        ax.set_title(f'Increase in Hate type relative to {start_date}')        
        ax.set_xlabel('Day')
        ax.set_ylabel('Increase in Number of Hate Links (%)')
        ax.tick_params(axis='x', rotation=45)
        ax.set_yticklabels(['{:.0f}%'.format(x) for x in ax.get_yticks()])  # Add '%' symbol to y-axis labels
        ax.grid(False)  # Removing gridlines

        # Display the plot in Streamlit
        st.pyplot(fig)

class Network_comparison:
    def __init__(self):
        self.data = load_data()



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


class hate_line_plot:
    def __init__(self) -> None:
        self.data = load_data()

    
    def hate_type_relative_increase(self, start_date, end_date):
        Jan6 = self.data[(self.data['Day'] >= start_date) & (self.data['Day'] <= end_date)]

        boolean_columns = [ 'race_prediction', 'giso_prediction', 'immigration_prediction']
        boolean_df = Jan6[['Day'] + boolean_columns]

        # Assuming 'day' is the column containing the day information
        first_day = boolean_df['Day'].iloc[0]

        # Calculate the increase in true values relative to the first day for each boolean column
        increase = boolean_df.groupby('Day').sum() - boolean_df[boolean_df['Day'] == first_day].sum()

        # Reset index to make 'day' a column again
        increase.reset_index(inplace=True)

        # Plotting
        fig, ax = plt.subplots(figsize=(10, 6))
        for col in boolean_columns:
            ax.plot(increase['Day'], increase[col], label=col)

        ax.set_title(f'Increase in Hate type relative to {start_date}')
        ax.set_xlabel('Day')
        ax.set_ylabel('Increase')
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

        
class corr_plot:
    def __init__(self) -> None:
        self.data = load_data()

    def corr_plot(self, start_date, end_date):
        Jan6 = self.data[(self.data['Day'] >= start_date) & (self.data['Day'] <= end_date)]

        prediction_columns = ['religion_prediction', 'race_prediction', 'gender_prediction',
                      'giso_prediction', 'immigration_prediction', 'ein_prediction',
                      'antisemitism_prediction']

        Daily_count_flavors_df = pd.DataFrame()
        for column in prediction_columns:
            
            # Filter DataFrame to get rows where the current column is True, then group by day and get the size of each group
            true_counts = Jan6[Jan6[column]].groupby('Day').size()
            Daily_count_flavors_df[column] = true_counts

        SNS_columns  = Jan6['SNS Source'].unique().tolist()
        Daily_count_sns_df = pd.DataFrame()

        for column in SNS_columns:

            true_counts = Jan6[Jan6['SNS Source'] == column].groupby('Day').size()
            Daily_count_sns_df[column] = true_counts

                
        correlations = {}
        for col1 in Daily_count_flavors_df.columns:
            for col2 in Daily_count_sns_df.columns:
                correlation = Daily_count_flavors_df[col1].corr(Daily_count_sns_df[col2])
                correlations[(col1, col2)] = correlation



        columns1, columns2 = zip(*correlations.keys())

        # Extract correlation values
        correlation_values = list(correlations.values())

        # Create a DataFrame from the correlation values with columns as the original column names
        correlation_df = pd.DataFrame({'Column1': columns1, 'Column2': columns2, 'Correlation': correlation_values})

        # Pivot the DataFrame to create a correlation matrix
        correlation_matrix = correlation_df.pivot('Column1', 'Column2', 'Correlation')

        # Remove the 'Instagram' column and row from the correlation matrix
        try:
            correlation_matrix = correlation_matrix.drop('Instagram', axis=1)
        except:
            pass

        # Plot the heatmap
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        ax.set_title('Correlation Heatmap between the count of links and hate type detected across different SNS')
        st.pyplot(fig)







