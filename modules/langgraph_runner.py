import os
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.messages import HumanMessage

from dotenv import load_dotenv
load_dotenv()

mistral_api_key = os.getenv("MISTRAL_API_KEY")


# Mistral Chat LLM setup
llm = ChatMistralAI(api_key=mistral_api_key)

# Define LangGraph schema
class CaptionState(TypedDict):
    prompt: str
    caption: str

# Node logic
def generate_response(state: CaptionState) -> CaptionState:
    prompt = state["prompt"]
    response = llm.invoke([HumanMessage(content=prompt)])
    return {"prompt": prompt, "caption": response.content.strip()}

# LangGraph definition
graph_builder = StateGraph(CaptionState)
graph_builder.add_node("generate", RunnableLambda(generate_response))
graph_builder.set_entry_point("generate")
graph_builder.add_edge("generate", END)
graph = graph_builder.compile()

# Final callable function
def generate_caption(prompt: str) -> str:
    result = graph.invoke({"prompt": prompt})
    return result["caption"]
