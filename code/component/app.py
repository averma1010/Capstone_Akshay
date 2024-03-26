import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import network
import Charts_dashboard
import numpy as np
from datetime import datetime, timedelta
#import RAG_Insights



st.set_page_config(layout="wide")


st.title('Hate Speech Network Dashboard')

c_left, c_right = st.columns(2)

with c_left:
    physics_checkbox = st.sidebar.checkbox('Add Physics')

    start_date, end_date = st.sidebar.slider("Select Date Range", 
                                     min_value=datetime(2021, 1, 1),
                                     max_value=datetime(2021, 1, 10),
                                     value=(datetime(2021, 1, 1), datetime(2021, 1, 5)),
                                     format="YYYY-MM-DD")
   # network.pre_event(physics_checkbox, start_date, end_date)
    

    slider2_key = "slider2"
    
    start_date_1, end_date_1 = st.sidebar.slider("Select Date Range", 
                                        min_value=datetime(2021, 1, 1),
                                        max_value=datetime(2021, 1, 10),
                                        value=(datetime(2021, 1, 6), datetime(2021, 1, 10)),
                                        format="YYYY-MM-DD", key=slider2_key)
   # network.post_event(physics_checkbox, start_date_1, end_date_1)
    st.markdown("## Pre-event")

    network.network_vis(physics_checkbox,start_date,end_date,start_date_1,end_date_1)
    HtmlFile = open("preevent.html", 'r', encoding='utf-8')


    source_code = HtmlFile.read() 
    components.html(source_code, height = 500,width=750)
    st.markdown("## Post-event")

    HtmlFile = open("postevent.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height = 1200,width=750)
    


with c_right:    
    


    Charts_dashboard.edge_count_chart(start_date, end_date_1)


    Charts_dashboard.network_comparison(start_date, end_date, start_date_1, end_date_1)

    
#RAG_Insights.rag_openai()
    
    