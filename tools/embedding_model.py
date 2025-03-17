#Importing specific librraies 
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os 
from dotenv import load_dotenv
load_dotenv()
#Setting the environment variable
os.environ['HF_TOKEN']= os.getenv("HF_TOKEN")

#defining the embedding model function using a pre-trained model from hugging face
def embedding_model():

    model_name = "sentence-transformers/all-MiniLM-L6-v2" # model from hugging face
    model_kwargs = {'device': 'cpu', "trust_remote_code": True} # defining the configuration settings
    encode_kwargs = {'normalize_embeddings': False}
    #loading the model
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
        )
    return embeddings # function will return the embedding model 




