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

repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    temperature=0.5,
    max_new_tokens=128,
    huggingfacehub_api_token=Huggingface_api_key
)

# Load PDF as default knowledge base
path = r"C:\Users\CVHS\pavan\it's me\Chat-with-your-docs-main\docs\Module 1 - Anatomy and Physiology of the Heart.pdf"
docs = load_pdf(path)

# RAG Flow
splits = split_page(docs)
vector_store = indexing_page(splits, Huggingface_api_key)
print('-------->')
print(vector_store)
print('-------->')
retrieved = retriever(vector_store)

chain = generator(retrieved, llm)

# Chat Loop
print("Chatbot is initializing...")
print("Type 'q' to quit the conversation.")
question = str(input("User: "))
while question.lower() != "q":
    print("AI:", chain.invoke(question))
    question = str(input("User: "))
