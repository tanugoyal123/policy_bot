import faiss
import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.tools.retriever import create_retriever_tool
from policy_bot_backend.tools.embedding_model import embedding_model
from dotenv import load_dotenv

load_dotenv()


os.environ['HF_TOKEN']= os.getenv("HF_TOKEN")

embeddings=embedding_model()
vector_store=FAISS.load_local(
    "policy_bot_backend/faiss_index", embeddings, allow_dangerous_deserialization=True
)

retriever = vector_store.as_retriever()
ragtool=create_retriever_tool(retriever,"ragtool","retrieve data according to query")

def get_retriever_tool(query):
    rag_context=ragtool.run(query)
    return rag_context
