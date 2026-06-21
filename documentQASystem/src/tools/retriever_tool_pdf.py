import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import OllamaEmbeddings
# from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
# from langchain.chains import create_retrieval_chain
from langchain_classic.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
import openai
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document
from langchain_core.tools.retriever import create_retriever_tool

from pprint import pprint
from langchain_core.messages import AIMessage, HumanMessage
### Tavily Search Tool
from langchain_community.tools.tavily_search import TavilySearchResults

# combine pdf docs
folder_path = "document source"

pdf_docs = []

for file in os.listdir(folder_path):
    if file.endswith(".pdf"):
        file_path = os.path.join(folder_path, file)
        
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        
        pdf_docs.extend(docs)

text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
final_documents=text_splitter.split_documents(pdf_docs)

vectorstore_pdf = FAISS.from_documents(documents=final_documents,embedding=OpenAIEmbeddings())
retriver_pdf = vectorstore_pdf.as_retriever()

retriever_tool_pdf=create_retriever_tool(
    retriver_pdf,
    "retriever_vector_pdf",
    "Search and run information about sigma"
)