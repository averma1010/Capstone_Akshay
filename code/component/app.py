import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import network
import Charts_dashboard
import numpy as np
from datetime import datetime, timedelta
import RAG_Insights
from streamlit_date_picker import date_range_picker, PickerType, Unit, date_picker

import pandas as pd


st.set_page_config(layout="wide")


#st.title('Hate Speech Network Dashboard')

c1, c2, c3 = st.columns([2,2,1])

with c3:    
    st.markdown('#')
    st.markdown('#')
    ccc1, ccc2 = st.columns([1,1])
    with ccc1:
        physics_checkbox = st.checkbox('Add Physics')
    with ccc2:
        sns_names = ['all' , '4Chan', 'TG', 'Youtube', 'Gab', 'Twitter']

        # Sidebar dropdown to select social networking site
        selected_sns = st.selectbox("Select Social Networking Site", sns_names)

    cc1, cc2 = st.columns([1,1])
    st.empty()
    with cc1:
        start_date = pd.Timestamp(st.date_input("Select Start Date for Pre Event", datetime(2021, 1, 1)))
        start_date_1 = pd.Timestamp(st.date_input("Select Start Date for Pre Event", datetime(2021, 1, 6)))
    with cc2:
        end_date = pd.Timestamp(st.date_input("Select End Date for Pre Event", datetime(2021, 1, 5)))
        end_date_1 = pd.Timestamp(st.date_input("Select End Date for Pre Event", datetime(2021, 1, 10)))
        
    slider2_key = "slider2"
    
    
    network.network_vis(selected_sns, physics_checkbox,start_date, end_date, start_date_1, end_date_1)
    
    Charts_dashboard.Network_comparison().network_comparison_df( start_date, end_date, start_date_1, end_date_1)

with c1:

   # network.pre_event(start_date, end_date)
    st.markdown("## Pre-event (Hate Core)")

    
    HtmlFile = open("preevent.html", 'r', encoding='utf-8')


    source_code = HtmlFile.read() 
    components.html(source_code, height = 500,width=600) 
    
with c2:
   # network.post_event( start_date_1, end_date_1)
    
    st.markdown("## Post-event (Hate Core)")

    HtmlFile = open("postevent.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height = 500,width=600)
    


st.markdown('#')
st.markdown('#')

c4, c5 = st.columns([2,2])
with c4:
    Charts_dashboard.EdgeCountAnalyzer().edge_count_chart(start_date, end_date_1)  
with c5:  
    Charts_dashboard.hate_line_plot().hate_type_relative_increase(start_date, end_date_1)


c6,c7 = st.columns([1,1])

with c6:
    if st.button("Generate AI Insight"):
        data = Charts_dashboard.Network_comparison().network_comparison_metrics(start_date, end_date, start_date_1, end_date_1)
        RAG_Insights.rag_openai(data)


        

with c7:         
    Charts_dashboard.corr_plot().correlation_plot(start_date, end_date_1)
    

