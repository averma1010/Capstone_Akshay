import os

import streamlit as st

from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_community.document_loaders import DirectoryLoader




os.environ["OPENAI_API_KEY"] = "" ## ENTER YOU OPENAI API KEY HERE


def get_vectorstore_from_url():
    """Retrieve vector store from the given URL.

    This function loads a document from the provided URL,
    splits it into chunks & creates a vector store.

    Args:
        url (str): The URL of the document.

    Returns:
        Chroma: The vector sgptore created from the document chunks.
    """
    # Get text-in documents
    file_path = r"Data"
    loader = DirectoryLoader(file_path)
    document = loader.load()

    # Split the documents into chunks
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(document)

    # Create Vector-store from the chunks:
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(document_chunks, embeddings)
    return vector_store


def get_context_retriever_chain(vector_store):
    """Create a context retriever chain using the given vector store.

    This function creates a history-aware retriever chain
    using a vector store and a chat prompt template.

    Args:
        vector_store (Chroma): The vector store to use.

    Returns:
        RetrievalChain: The context retriever chain.
    """
    llm = ChatOpenAI(model="gpt-4-turbo-preview")
    retriever = vector_store.as_retriever()

    prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),
        ("user", "Given the above conversation, generate a search query "
                 "to look up in order to get information relevant to "
                 "the conversation")
    ])

    retriever_chain = create_history_aware_retriever(llm, retriever, prompt)

    return retriever_chain


def get_conversational_rag_chain(retriever_chain):

    llm = ChatOpenAI(model="gpt-4-turbo-preview")

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are an Analyst working on how the online hate network changes after pivotal real world event, especifically looking at the 2020 US presidential election  and Jan 6 capitol attack. "
            "Give answers in an authoritative but gentle tone. Give the most prominant insights and relate it to real world events. Keep your answers technical and based on facts – do not hallucinate features."
            " on the below context:\n\n{context}"
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}")
    ])

    stuff_documents_chain = create_stuff_documents_chain(llm, prompt)

    return create_retrieval_chain(retriever_chain, stuff_documents_chain)


def get_response(user_input):
    """Get the response for the given user query.

    This function retrieves the response for the user query
    using the conversational RAG chain.

    Args:
        user_input (str): The user query.

    Returns:
        str: The response to the user query.
    """
    # Create Conversation Chain
    retriever_chain = get_context_retriever_chain(
        st.session_state.vector_store
        )
    conversation_rag_chain = get_conversational_rag_chain(retriever_chain)

    # Invoke conversational RAG chain
    inv_response = conversation_rag_chain.invoke({
          "chat_history": st.session_state.chat_history,
          "input": user_input
      })
    return inv_response['answer']




    # For persistent variables : Session State
if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content="Hello, chat with me to get insights about the data presented on the dashboard")
            ]

    # Persistent Vector Store
if "vector_store" not in st.session_state:
        st.session_state.vector_store = get_vectorstore_from_url()

    # User Input
user_query = st.chat_input("Type your message ✍")
if user_query is not None and user_query != "":
        response = get_response(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))

    # Conversation
for message in st.session_state.chat_history:
        MESSAGE_TYPE = "AI" if isinstance(message, AIMessage) else "Human"
        with st.chat_message(MESSAGE_TYPE):
            st.write(message.content)