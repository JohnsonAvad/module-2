import chromadb
from pprint import pprint


from langchain.text_splitter import RecursiveCharacterTextSplitter

import os
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction





from langchain_community.document_loaders import PDFPlumberLoader

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import warnings
from pdfminer.pdfinterp import PDFGraphicState
# import os
from dotenv import dotenv_values


import numpy as np
import chromadb


from langchain.chains import create_retrieval_chain

from langchain_community.vectorstores import Chroma



CHROMA_DIR = "./data_store"

embedding_function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# 1. Combine the multiline string into one 

def load_pdf_text(file_path: str) -> str:
    with warnings.catch_warnings():
    
         warnings.filterwarnings("ignore",
             message=".*Cannot set gray non-stroke color.*"
)

         
         loader = PDFPlumberLoader(file_path)
         docs = loader.load()
         
    text = "\n\n".join(doc.page_content for doc in docs)

    return text



def setup_chroma_collection(pdf_path: str):
    chroma_client = chromadb.PersistentClient(path=CHROMA_DIR)
    collection = chroma_client.get_or_create_collection(name="texts")

    existing = collection.count()
    if existing == 0:
       
        raw_text = load_pdf_text("./data/the-seven-habits.pdf")

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        texts = text_splitter.split_text(raw_text)


# os.makedirs(CHROMA_DIR, exist_ok=True)




        vectors = np.array(embedding_function(texts))


# we instantiate a Chromadb Client which allows 
# us interact with the underlying Chromadb database


 




# We can then execute a set of
#  commands on our collection "documents" to either get
# (if they exist already) or add them if they dont.
# Avoid re-adding if already added


        collection.add(
            documents=texts,
            ids=[f"doc_{i}" for i in range(len(texts))],
            embeddings=vectors
        ) 

        print("Documents added to Chroma.")
    else:
        print("Chromacollection already exists.")
    return collection, embedding_function
   
    # when we execute this the Chromadb to download the 
    # default vector model and convert each of 
    # these documents into vectors

# query = "how engineering helps build software systems"
# query_embeddings = embedding_function([query]) 

# results = collection.query(
#     query_embeddings = query_embeddings, 
#     n_results=4
# )

 
# we use a collection.add method 
# to add documents and their ids

# pprint(results)
# chroma will embed this and 
# return the most similar results.