import os
from crewai import Crew
from tasks.analyze_blood_test import task1
from tasks.find_health_articles import task2
from tasks.provide_recommendations import task3

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Ensure the output directory exists
if not os.path.exists("output"):
    os.makedirs("output")

# Create the crew with all agents and tasks
crew = Crew(agents=[task1.agent, task2.agent, task3.agent], tasks=[task1, task2, task3], verbose=2)

def run_tasks():
    task_output = crew.kickoff()
    print(task_output)

if __name__ == "__main__":
    run_tasks()
