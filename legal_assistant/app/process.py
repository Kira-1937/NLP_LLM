# app/process.py
import os
from utils.file_utils import extract_text
from utils.nlp_utils import process_text

def process_file(file_path):
    # Extract text from uploaded file (PDF, DOCX)
    text = extract_text(file_path)

    # Use LangChain and Gemini for fact extraction and summarization
    extracted_data = process_text(text)
    
    # Save the extracted data (e.g., as JSON or text) for later use
    output_path = os.path.join("extracted_data", os.path.basename(file_path) + "_extracted.json")
    with open(output_path, "w") as f:
        f.write(extracted_data)
    
    return extracted_data
