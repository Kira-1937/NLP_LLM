import os
from dotenv import load_dotenv
from transformers import pipeline

# Load the environment variables
load_dotenv()

# Load the summarization model from Hugging Face
model_name = os.getenv("HUGGING_FACE_MODEL", "t5-large")
recommender = pipeline("summarization", model=model_name)

def generate_recommendations(articles):
    articles_content = "\n".join(articles)
    
    # Use the summarizer to generate recommendations
    recommendations = recommender(articles_content, max_length=2000, min_length=5, do_sample=False)[0]['summary_text'].split('\n')
    
    return recommendations
