import streamlit as st
#from llama_index import Document
from llama_index.core import VectorStoreIndex, ServiceContext,SimpleDirectoryReader, ListIndex
from llama_index.llms.openai  import OpenAI
import openai

def rag_openai(data):

    openai.api_key = 'sk-'

    key1 = list(data.keys())[1]
    key2 = list(data.keys())[2]
    prompt = f"Looking at the network data give insights in 2-3 bullet points as to how the network changed from {key1} to {key2}. Looking at the data give one bullet point about how some social networking sites are correlated with certain hate types. relate to real world events Mention data and percentage changes. Give contextual background to the data with real world event. Mention any pivotal events that happened in the time frame. Hint: Talk about how the clustering coeffecient increase or the number of communities decreased. "



    
    st.session_state.messages = []
        
    @st.cache_resource(show_spinner=False)
    def load_data():
        with st.spinner(text="Loading the insights – hang tight! This should take 1-2 minutes."):
            reader = SimpleDirectoryReader(input_dir=r"C:\Users\Akshay\OneDrive\Desktop\Capstone_Akshay\Data", recursive=True)
            docs = reader.load_data()
            # llm = OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert o$
            # index = VectorStoreIndex.from_documents(docs)
            service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo-0125", temperature=0.3, system_prompt="You are an Analyst. You are also an expert on the timeline of the 2020 presidential election and following events from Nov 1 2020 to Jan 10 2021, and on the hate speech propogated online because of it. You are also an expert on Network Science and Graph Theory. Assume that all questions are related to the timeline of the presidential election and Hate speech propogated online because of real world events and about difference in two networks. Keep your answers technical and based on facts – do not hallucinate features. "))
            index = VectorStoreIndex    .from_documents(docs, service_context=service_context)
            return index

    index = load_data()
    if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)


    

        

    
    st.session_state.messages.append({"role": "user", "content": prompt})
    if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

    for message in st.session_state.messages: # Display the prior chat messages
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # If last message is not from assistant, generate a new response
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.chat_engine.chat(prompt)
                st.write(response.response)
                message = {"role": "assistant", "content": response.response}
                st.session_state.messages.append(message) # Add response to message history


