from crewai import Task
from agents.analyst import analyst

task1 = Task(
    description="Analyze the provided blood test report and summarize the findings in an easy-to-understand manner.",
    expected_output="""A summarized report of the blood test should include key findings such as:
    
    - Cholesterol Levels: [Normal/High/Low]
    - Blood Sugar Levels: [Normal/High/Low]
    - Hemoglobin Levels: [Normal/High/Low]
    - Any other significant markers with their levels and interpretations.
    
    Example:
    Cholesterol Levels: High
    Blood Sugar Levels: Normal
    Hemoglobin Levels: Low
    Additional Notes: Patient shows signs of anemia. Recommendations for further tests and lifestyle changes are advised.
    """,
    agent=analyst,
    output_file="output/blood_test_summary.txt",
)
