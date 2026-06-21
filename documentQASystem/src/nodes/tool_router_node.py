# tool router agent

from src.state.state import AgentState
from src.LLM.llm import llm

def tool_router_agent(state: AgentState):
    question = state["question"]
    prompt = f"""
    Decide the best tool for the user question and answer the following question clearly:
    {question}
    
    Tools available :
    1.retriever_tool_pdf
    2.tavily
    3.retriever_tool_url
    
    """
    response = llm.invoke(prompt)
    # tool_choice = response.content.strip().lower()
    # return {"tool_choice":tool_choice}
    # return {"tool":tool_choice}
    return {
        "question": question,
        "answer": response.content
    }
    