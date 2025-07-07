# utils/nlp_utils.py
import openai
from config import GEMINI_API_KEY

openai.api_key = GEMINI_API_KEY

def process_text(text):
    # Use Gemini API or other NLP models for fact extraction and summarization
    summary = openai.Completion.create(
        model="text-davinci-003", 
        prompt=f"Summarize the following legal text: {text}",
        max_tokens=500
    )

    extracted_facts = extract_facts_from_text(text)

    return {
        "summary": summary["choices"][0]["text"],
        "facts": extracted_facts
    }

def extract_facts_from_text(text):
    # Implement a simple rule-based extraction or use an LLM for more advanced extraction
    facts = []
    # Example: Extract dates, names, and legal terms (using regex or LLM)
    return facts
