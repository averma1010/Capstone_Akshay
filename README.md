# Analyzing the Changes in Network Topology During 2020 US Presidential Election and 2021 Capitol Attacks

### Capstone Project Spring 2024

**Author:** Akshay Verma  
**Masters of Science in Data Science**  
**Supervisor:** Prof. Amir Jafari  
*Columbian College of Arts & Science, The George Washington University*  

---
 


```.
├── code
│   ├── component (Dashboard and Jupyter Notebook)
│   │   ├──  Data (Data for Data_Analysis_Notebook)
│   │   ├── Network.py
│   │   ├── Chart_Dashboard.py
│   │   ├──  Chat_with_Dashboard.py
│   |   ├──  app.py (Dashboard)
│   |   └──Data_Analysis_Notebook
├── Data (Data for RAG)
├── full_report
│   └── Word_Report
├── presentation
└── research_paper
    ├── Latex
    │   └── Fig
    └── Word
```


## Abstract
 In the digital age, online hate networks thrive as platforms for spreading extremist ideologies and hate speech, posing a significant threat tosocietal cohesion. This study examines the impact of key real-world events, notably the 2020 U.S. presidential election and the January 6 Capitol attack on the evolution of online hate networks. Using data collected from hate
 communities between November 1, 2020, and January 10, 2021, this research
 analyzes shifts in hate speech themes and network topology. Following the
 presidential election, an increase in hate speech targeting immigration, eth
nicity, and antisemitism was observed. The January 6 Capitol attack further
 intensified these trends. Central to this investigation is the examination of
 two key aspects of online hate networks: the content they disseminate and
 the underlying structure of their connections. By studying shifts in hate
 themes and network topology, including changes in centrality and com
munity structure, this study seeks to uncover the mechanisms driving the
 evolution of online hate networks. The analysis reveals significant changes
 in network cohesion post-attack, characterized by increased clustering and
 assortativity. This research sheds light on the role of online platforms in
 radicalization and mobilization efforts, emphasizing the need for proactive
 measures to combat hate speech online. Despite its niche presence, Telegram
 has become a key hub for propagating extremist ideologies and coordinating
 malicious activities.

## Using the Dashboard

To use the dashboard, follow these steps:

1. **Fork the Repository**: Start by forking the repository to your GitHub account. This will create a copy of the project in your own account.

2. **Obtain API Key**: You'll need to obtain your own API key for accessing the necessary data. The dashboard relies on external APIs for data retrieval. Instructions for obtaining the API key can be found in the documentation of the respective APIs used in the project.



4. **Command to run Dashboard**
    ```bash
    streamlit run app.py
