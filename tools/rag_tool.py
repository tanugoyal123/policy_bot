import faiss
import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.tools.retriever import create_retriever_tool
from policy_bot_backend.tools.embedding_model import embedding_model
from dotenv import load_dotenv

load_dotenv()

# setting the enviroment variable
os.environ['HF_TOKEN']= os.getenv("HF_TOKEN")

#loading the embedding model
embeddings=embedding_model()

# loading a vector database 
vector_store=FAISS.load_local(
    "policy_bot_backend/faiss_index", embeddings, allow_dangerous_deserialization=True
)

# using vector database as a retriever
retriever = vector_store.as_retriever()

# using in-built function to create tool of retriever to retrieve data
ragtool=create_retriever_tool(retriever,"ragtool","retrieve data according to query")

#defining a function to input query and use tool to give context.
def get_retriever_tool(query):
    rag_context=ragtool.run(query)
    return rag_context # return the text context 
