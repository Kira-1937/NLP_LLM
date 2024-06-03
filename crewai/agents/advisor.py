from crewai import Agent
from langchain_community.llms import Ollama

llm = Ollama(model="openhermes")

advisor = Agent(
    llm=llm,
    role="Health Advisor",
    goal="Provide health recommendations based on the blood test summary and found articles.",
    backstory="You are a health advisor who provides personalized recommendations based on medical data.",
    allow_delegation=False,
    verbose=True,
)
