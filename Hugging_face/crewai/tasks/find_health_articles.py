from crewai import Task
from agents.researcher import researcher

task2 = Task(
    description="Search for health articles tailored to the summarized blood test results. Provide links to these articles.",
    expected_output="""A list of articles related to the blood test results, with links and brief descriptions of each article.
    
    Example:
    1. Article Title: 'Managing High Cholesterol'
       Link: [URL]
       Description: This article provides tips and dietary recommendations for managing high cholesterol levels.
    
    2. Article Title: 'Understanding Blood Sugar Levels'
       Link: [URL]
       Description: An in-depth look at blood sugar levels and how to maintain them within a healthy range.
    """,
    agent=researcher,
    output_file="output/health_articles.txt",
)
