import streamlit as st
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from load import load_pdf
from split import split_page
from indexing import indexing_page
from retrieve import retriever
from generate import generator

from dotenv import load_dotenv
load_dotenv()
import os
Huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")

REPO_ID = "mistralai/Mixtral-8x7B-Instruct-v0.1"
PDF_PATH = r"C:\Users\CVHS\pavan\it's me\Chat-with-your-docs-main\docs\Module 1 - Anatomy and Physiology of the Heart.pdf"  # <-- Set your static PDF path here

# Page config
st.set_page_config(page_title="PDF Chatbot", layout="centered")
st.title("📚 Chat with your PDF")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Load the system once and cache it
@st.cache_resource
def setup_rag_chain():
    docs = load_pdf(PDF_PATH)
    splits = split_page(docs)
    vector_store = indexing_page(splits, HUGGINGFACE_API_KEY)
    retriever_chain = retriever(vector_store)
    llm = HuggingFaceEndpoint(
        repo_id=REPO_ID,
        temperature=0.5,
        max_new_tokens=128,
        huggingfacehub_api_token=HUGGINGFACE_API_KEY
    )
    return generator(retriever_chain, llm)

# Load the chain
with st.spinner("Initializing the RAG system..."):
    chain = setup_rag_chain()
st.success("Ready to chat!")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input box for user message
if prompt := st.chat_input("Ask something about the document..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chain.invoke(prompt)
            st.markdown(response)

    # Add assistant message to history
    st.session_state.messages.append({"role": "assistant", "content": response})
