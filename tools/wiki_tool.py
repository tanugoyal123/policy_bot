from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

api_wrapper_wiki=WikipediaAPIWrapper(top_k_results=3)
wiki=WikipediaQueryRun(api_wrapper=api_wrapper_wiki)

def wiki_tool(query):
    context_wiki = wiki.run(query)
    return context_wiki