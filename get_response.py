from policy_bot_backend.tools.rag_tool import get_retriever_tool
from policy_bot_backend.tools.wiki_tool import wiki_tool
from policy_bot_backend.f_prompt import f_prompt
from policy_bot_backend.final_llm import get_llm
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['HF_TOKEN']= os.getenv("HF_TOKEN")

# function for getting output of the query asked by user
def get_response(query,history):
    context_rag=get_retriever_tool(query) # fetching rag context using get retriever tool functionfrom rag_tool file
    context_wiki = wiki_tool(query) # fetching wikipedia context using wiki_tool function from wiki tool file
    final_context=context_rag+context_wiki # combining both the context
    final_prompt=f_prompt(query,final_context,history) # using the combined context in prompt
    llm=get_llm() # loading llm
    response=llm.invoke(final_prompt) # invoke the llm and get output
    return response # return the final response from the llm
