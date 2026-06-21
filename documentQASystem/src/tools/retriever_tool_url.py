

from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.tools.retriever import create_retriever_tool
#loading urls:

urls=[
    "https://langchain-ai.github.io/langgraph/tutorials/introduction/",
    "https://langchain-ai.github.io/langgraph/tutorials/workflows/",
    "https://langchain-ai.github.io/langgraph/how-tos/map-reduce/"
]

docs_url = [WebBaseLoader(url).load() for url in urls]
#docs_url
docs_list_url = [item for sublist in docs_url for item in sublist]

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
doc_splits = text_splitter.split_documents(docs_list_url)
## Add alll these text to vectordb
vectorstore = FAISS.from_documents(documents=doc_splits,embedding=OpenAIEmbeddings())
retriver_url = vectorstore.as_retriever()

# ### Retriever To Retriever Tools
#converting this retriver to Retriver tool to intregrate with LLM
# from langchain.tools.retriever import create_retriever_tool - no longer exist


retriever_tool_url=create_retriever_tool(
    retriver_url,
    "retriever_vector_db_blog",
    "Search and run information about Langgraph"
)