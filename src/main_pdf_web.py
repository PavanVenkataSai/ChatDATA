from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from getpass import getpass
from load import load_page, load_pdf
from split import split_page
from indexing import indexing_page
from retrieve import retriever
from generate import generator
from dotenv import load_dotenv
load_dotenv()
import os
Huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")

repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
llm = HuggingFaceEndpoint(repo_id = repo_id, temperature = 0.5, max_new_tokens = 128, huggingfacehub_api_token = Huggingface_api_key)
print("Choose your Knowledge base: \n If your knowledge base is in the form of Documents, choose 1 \n If your knowledge base is a website choose 2.")
choice = int(input('Enter your choice:'))
if choice in [1,2]:
    if choice == 1:
        path = str(input(("please provide your document's location : ")))
        docs = load_pdf(path)
    if choice == 2:
        page = str(input('Please provide website/page URL: '))
        docs = load_page(page)
    splits  =  split_page(docs)
    vector_store = indexing_page(splits,Huggingface_api_key)
    retrieved  = retriever(vector_store)
    chain = generator(retrieved,llm)
    print("Chatbot is initialising....")
    print("give 'q' to stop conversation")
    question = str(input("User : "))
    while question != "q":
        print("AI : ", chain.invoke(question))
        question = str(input("User : "))
else:
    print("Wrong Choice!!!, start again.")