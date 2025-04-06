# ⚡ ChatPDF-Genius ⚡

Have you ever wanted to talk to your documents like they actually *get you*?  
With **ChatPDF-Genius**, you can ask questions directly to a PDF and get intelligent, context-aware answers — all powered by open-source LLMs and RAG (Retrieval-Augmented Generation) techniques. 🧠💬

This version is optimized to work with static PDFs, making it fast, clean, and easy to integrate into any workflow.

If you find this project useful, consider giving it a ⭐ on GitHub!

---

## 🚀 Quick Install

Before you begin, this repo uses LLM models and embedding models from HuggingFace through the inference API. You’ll need a HuggingFace API token to proceed — it’s free and can be created [here](https://huggingface.co/settings/tokens).

### 🔁 Clone the Repository

```bash
git clone https://github.com/PavanVenkataSai/ChatDATA/.git
cd src
```

## 📦 Install Dependencies
This project uses pip for package management. All dependencies are listed in requirements.txt.

```bash

pip install -r requirements.txt
```

```bash

python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install -r requirements.txt
```
▶️ Run the App with Streamlit
Launch the chatbot interface:

```bash
streamlit run main_streamlit.py
```
By default, main_streamlit.py is set to use a static PDF path. You can change the file path directly in the script.

## 📚 What's Inside?
This repo uses LangChain as the framework to integrate with open-source LLMs and Retrieval-Augmented Generation (RAG). Here's a brief of what it does:

- 🔍 PDF Parsing using PyMuPDF

- 🧩 Contextual Chunking for better information retrieval

- 🧠 FAISS Vector Store for similarity search

- 🤖 Mixtral-8x7B-Instruct from HuggingFace for generating accurate, contextual responses

- 🧾 Streamlit UI for clean and continuous chat interface

## 📁 Project Structure
```bash
ChatDATA/
├── .gitignore                  # Ignore venv, __pycache__, PDFs, etc.
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── src/                        # Source code folder
    ├── generator.py            # Generates final responses using context + LLM
    ├── indexing.py             # Indexes chunks into a vector store
    ├── load.py                 # Loads and parses the PDF file
    ├── split.py                # Splits documents into chunks
    ├── retrieve.py             # Retrieves relevant chunks for a given query
    ├── main_pdf_web.py         # CLI version with choice of PDF or web input
    ├── main_PDF.py             # CLI version for PDF-only flow
    └── main_streamlit.py       # Streamlit-based chat UI

```
