from langchain.text_splitter import RecursiveCharacterTextSplitter
def split_page(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, add_start_index=True
    )
    # print(docs)
    all_splits = text_splitter.split_documents(docs)
    # print('--------------------------')
    # print(all_splits)
    # print('--------------------------')
    return all_splits


