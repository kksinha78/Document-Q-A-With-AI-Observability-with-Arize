from src.observability import arize
import streamlit as st
from src.graph.builder_graph import build_graph


# Load LangGraph agent
graph = build_graph()

st.set_page_config(page_title="Document Q & A")
st.title("🔎 Document Q & A")
st.write("Good Day ! Ask your question, I would happy to assist you.")

user_input = st.chat_input("Ask a question")
if user_input:
    with st.spinner("Thinking..."):
        result = graph.invoke({"question": user_input})
    st.chat_message("user").write(user_input)
    # st.chat_message("assistant").write(result["research_data"])
    # st.chat_message("assistant").write(result)
    # st.write(result)
    st.chat_message("assistant").write(result["answer"])