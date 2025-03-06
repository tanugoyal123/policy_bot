from policy_bot_backend.tools.rag_tool import get_retriever_tool
from policy_bot_backend.tools.wiki_tool import wiki_tool
from policy_bot_backend.f_prompt import f_prompt
from policy_bot_backend.final_llm import get_llm
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['HF_TOKEN']= os.getenv("HF_TOKEN")

def get_response(query,history):
    context_rag=get_retriever_tool(query)
    context_wiki = wiki_tool(query)
    final_context=context_rag+context_wiki
    final_prompt=f_prompt(query,final_context,history)
    llm=get_llm()
    response=llm.invoke(final_prompt)
    return response
