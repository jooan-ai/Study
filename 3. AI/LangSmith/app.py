from typing_extensions import TypedDict, List, Annotated, NotRequired
from typing import Literal

from pydantic import BaseModel, Field
import operator
import os

from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI

from langchain_core.messages import AnyMessage, HumanMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from langgraph.types import Send

from dotenv import load_dotenv

# ===== LLM =====
load_dotenv() # .env파일에서 환경설정 가져오기

llm = ChatOpenAI(model="gpt-5-nano", api_key=os.getenv("GMS_API_KEY"), base_url="https://gms.ssafy.io/gmsapi/api.openai.com/v1/", temperature=0)


# ===== State =====
class State(TypedDict):
    topic: str
    joke: NotRequired[str]
    feedback: NotRequired[str]
    funny_or_not: NotRequired[str]


# ===== Structured Output 준비 =====
class Feedback(BaseModel):
    grade: Literal["funny", "not funny"] = Field(
        description="농담이 재밌는지, 재미가 없는지 결정한다.",
    )
    feedback: str = Field(
        description="농담이 재미 없는 경우, 어떻게 하면 더 재미있을지 피드백을 제공한다.",
    )
    
llm_evaluator = llm.with_structured_output(Feedback)


# ===== Generator(Optimizer) Node =====
def llm_call_generator(state: State):    
    prompt = f"{state['topic']}에 관련되어 웃긴 농담 1개만 해줘 (3줄 이내)\n"
    
    if state.get("feedback"):
        prompt += f"이전에 너가 시도했던 농담의 피드백인데, 반영해줘 : {state['feedback']}"

    result = llm.invoke(prompt)
    return {"joke": result.content}


# ===== Evaluator Node =====
def llm_call_evaluator(state: State):
    grade = llm_evaluator.invoke(f"다음 농담에 대해 재미있는지 판별해줘 : {state['joke']}")
    return {"funny_or_not": grade.grade, "feedback": grade.feedback}


# ===== 조건 분기 ======
def route_joke(state: State):
    if state["funny_or_not"] == "funny":
        return "Accepted"

    return "Rejected + Feedback"


# ===== Graph 생성 =====
graph = StateGraph(State)

graph.add_node("generator", llm_call_generator)
graph.add_node("evaluator", llm_call_evaluator)

graph.add_edge(START, "generator")
graph.add_edge("generator", "evaluator")
graph.add_conditional_edges(
    "evaluator",
    route_joke,
    {
        "Accepted": END,
        "Rejected + Feedback": "generator",
    },
)

agent = graph.compile()

state = agent.invoke({"topic": "KFC 햄버거"})
print(state["joke"])