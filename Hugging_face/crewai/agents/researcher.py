from crewai import Agent
from crewai_tools import SerperDevTool
from langchain_community.llms import Ollama

llm = Ollama(model="openhermes")
search_tool = SerperDevTool()

researcher = Agent(
    llm=llm,
    role="Health Article Researcher",
    goal="Find relevant health articles based on blood test results.",
    backstory="You are an expert in finding health-related information online.",
    allow_delegation=False,
    tools=[search_tool],
    verbose=True,
)
