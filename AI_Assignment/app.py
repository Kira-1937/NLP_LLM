import streamlit as st
import os
from dotenv import load_dotenv
from transformers import pipeline
from analyze_report import analyze_blood_test
from search_articles import search_health_articles
from make_recommendations import generate_recommendations

# Load environment variables
load_dotenv()

# Load the summarization model
model_name = os.getenv("HUGGING_FACE_MODEL", "t5-large")
summarizer = pipeline("summarization", model=model_name)

# Streamlit interface
st.title("Medical Report Analyzer and Health Recommendations")

# File uploader for blood test report
uploaded_file = st.file_uploader("Upload a blood test report", type=["txt"])

if uploaded_file is not None:
    # Read the uploaded file
    report_content = uploaded_file.read().decode("utf-8")
    
    # Analyze the report
    analysis = analyze_blood_test(report_content)
    st.subheader("Blood Test Report Analysis")
    st.write(analysis["summary"])

    # Search for health articles based on the analysis
    articles = search_health_articles(analysis)
    st.subheader("Relevant Health Articles")
    for i, article in enumerate(articles):
        st.write(f"{i+1}. {article}")

    # Generate health recommendations based on the articles
    recommendations = generate_recommendations(articles)
    st.subheader("Health Recommendations")
    for i, recommendation in enumerate(recommendations):
        st.write(f"{i+1}. {recommendation}")
