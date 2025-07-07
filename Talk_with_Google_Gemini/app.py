from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

import streamlit as st
import os
import google.generativeai as genai

# Configure the Gemini API with your key from the .env file
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini Pro model
model = genai.GenerativeModel(model_name="gemini-pro")

# Function to get Gemini response
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Streamlit app setup
st.set_page_config(page_title="Gemini Q&A")

st.header("💬 Gemini LLM ask anything")
user_input = st.text_input("🩺 Enter your question:", key="input")

if st.button("Ask Gemini"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            answer = get_gemini_response(user_input)
        st.subheader("💡 Gemini's Response:")
        st.write(answer)
    else:
        st.warning("Please enter a valid question.")
