# BUILD GRAP

from langgraph.graph import StateGraph,START,END
from IPython.display import Image, display
from src.state.state import AgentState
from src.nodes.tool_router_node import tool_router_agent
def build_graph():
    builder = StateGraph(AgentState)
    #add nodes
    builder.add_node("tool_router",tool_router_agent)
    # add adges
    builder.add_edge(START,"tool_router")
    builder.add_edge("tool_router",END)
    return builder.compile()
    display(Image(graph.get_graph().draw_mermaid_png()))
    

