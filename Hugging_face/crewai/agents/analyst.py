from crewai import Agent
from langchain_community.llms import Ollama

llm = Ollama(model="openhermes")

analyst = Agent(
    llm=llm,
    role="Medical Analyst",
    goal="Analyze the blood test report and summarize it.",
    backstory="You are an experienced medical analyst tasked with interpreting blood test results.",
    allow_delegation=False,
    tools=[],
    verbose=True,
)
