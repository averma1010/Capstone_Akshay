import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import network
import numpy as np
from datetime import datetime, timedelta
st.set_page_config(layout="wide")

st.title('Hate Speech Network Dashboard')

c_left, c_right = st.columns(2)
with c_left:
    physics = st.checkbox('Add Physics')
    start_date, end_date = st.slider("Select Date Range", 
                                     min_value=datetime(2021, 1, 1),
                                     max_value=datetime(2021, 1, 10),
                                     value=(datetime(2021, 1, 1), datetime(2021, 1, 5)),
                                     format="YYYY-MM-DD")
    network.pre_event(physics, start_date, end_date)
    HtmlFile = open("gameofthrones.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height = 1200,width=750)
    

with c_right:    
    slider2_key = "slider2"
    physics = st.checkbox('Add Physics', key='physics_checkbox')
    start_date_1, end_date_1 = st.slider("Select Date Range", 
                                        min_value=datetime(2021, 1, 1),
                                        max_value=datetime(2021, 1, 10),
                                        value=(datetime(2021, 1, 6), datetime(2021, 1, 10)),
                                        format="YYYY-MM-DD", key=slider2_key)
    network.post_event(physics, start_date_1, end_date_1)
    HtmlFile = open("postevent.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height = 1200,width=750)