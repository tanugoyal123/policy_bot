from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from embedding_model import embedding_model
import os
from dotenv import load_dotenv
import faiss
load_dotenv()

# setting the enviroment variable
os.environ['HF_TOKEN']= os.getenv("HF_TOKEN")
embeddings=embedding_model()
# function for creating databases
def get_faiss_database(embedding_model,directory): # function will take embedding model and refrence directory
    loader=PyPDFDirectoryLoader(directory,extract_images=True) # loading the files for directory
    docs=loader.load() # loading documents
    print("loader done")
    embeddings=embedding_model # loading embedding model
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200) # loading a splitter to split documents
    final_documents=text_splitter.split_documents(docs) #splitting a documents
    vectors=FAISS.from_documents(final_documents,embeddings) # storing embeddings in faiss vector database
    faiss_index_path = "faiss_index"
    if not os.path.exists(faiss_index_path): # creating a directory woth faiss index name to save vector database 
        os.makedirs(faiss_index_path)
    vectors.save_local(faiss_index_path)
    return faiss_index_path # return the path of directory where faiss vector database is stored

s=get_faiss_database(embeddings,"gov_data") # creating the embeddings ans storing 
