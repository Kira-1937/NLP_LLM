from crewai import Task
from agents.advisor import advisor

task3 = Task(
    description="Provide personalized health recommendations based on the summarized blood test results and found articles.",
    expected_output="""A list of personalized health recommendations based on the blood test results and the articles found.
    
    Example:
    - Reduce intake of saturated fats to manage high cholesterol.
    - Increase physical activity to maintain healthy blood sugar levels.
    - Consider taking iron supplements to address low hemoglobin levels.
    - Read the following articles for more information: [List of article titles with links]
    """,
    agent=advisor,
    output_file="output/health_recommendations.txt",
)
