from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
import faiss
load_dotenv()


os.environ['HF_TOKEN']= os.getenv("HF_TOKEN")



model_name = "sentence-transformers/all-MiniLM-L6-v2"
model_kwargs = {'device': 'cpu', "trust_remote_code": True}
encode_kwargs = {'normalize_embeddings': False}
embeddings = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
    )


def get_faiss_database(embedding_model,directory):
    loader=PyPDFDirectoryLoader(directory,extract_images=True)
    docs=loader.load()
    print("loader done")
    embeddings=embedding_model
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    final_documents=text_splitter.split_documents(docs)
    vectors=FAISS.from_documents(final_documents,embeddings)
    faiss_index_path = "faiss_index"
    if not os.path.exists(faiss_index_path):
        os.makedirs(faiss_index_path)
    vectors.save_local(faiss_index_path)
    return faiss_index_path

s=get_faiss_database(embeddings,"gov_data")
