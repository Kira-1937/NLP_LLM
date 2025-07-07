# app/main.py
import streamlit as st
from upload import handle_file_upload
from process import process_file
from search import search_case

def main():
    st.title("AI-powered Legal Assistant")
    uploaded_file = st.file_uploader("Upload Case File", type=["pdf", "docx"])

    if uploaded_file:
        file_path = handle_file_upload(uploaded_file)
        extracted_data = process_file(file_path)

        # Display extracted data or a summary
        st.subheader("Extracted Summary")
        st.write(extracted_data["summary"])

        # Search functionality
        search_query = st.text_input("Search Case File")
        if search_query:
            search_results = search_case(search_query, extracted_data)
            st.write("Search Results: ", search_results)

if __name__ == "__main__":
    main()

