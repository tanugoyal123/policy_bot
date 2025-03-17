from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# loading the wikiperdiaAPIWrapper to fetch context from wikipedia
api_wrapper_wiki=WikipediaAPIWrapper(top_k_results=3)
wiki=WikipediaQueryRun(api_wrapper=api_wrapper_wiki)

#defining a function to retrieve the context from wikipedia
def wiki_tool(query):
    context_wiki = wiki.run(query)
    return context_wiki #return the text context form wikipedia