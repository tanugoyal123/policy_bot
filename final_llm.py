import os 
from dotenv import load_dotenv
from langchain_google_vertexai import ChatVertexAI

load_dotenv()
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
GOOGLE_API_KEY = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

def get_llm():
    llm = ChatVertexAI(
        model="gemini-1.5-flash-001", 
        temperature=0, 
        max_tokens=1500,
        stop=None,
    )
    return llm
