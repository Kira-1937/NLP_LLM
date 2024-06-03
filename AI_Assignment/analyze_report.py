import os
from dotenv import load_dotenv
from transformers import pipeline

# Load the environment variables
load_dotenv()

# Load the summarization model from Hugging Face
model_name = os.getenv("HUGGING_FACE_MODEL", "t5-large")
summarizer = pipeline("summarization", model=model_name)

def analyze_blood_test(report_content):
    # Use the summarizer to analyze the report
    summary = summarizer(report_content, max_length=200, min_length=50, do_sample=False)[0]['summary_text']
    
    return {
        "summary": summary,
        "details": report_content  # Include original report content for reference
    }
