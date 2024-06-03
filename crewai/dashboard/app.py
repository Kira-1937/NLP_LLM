import streamlit as st
import sys
import os

# Add the project root directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import run_tasks

def main():
    st.title("Health Analysis Dashboard")

    uploaded_file = st.file_uploader("Upload a blood test report (.txt)", type="txt")

    if uploaded_file is not None:
        with open("uploaded_report.txt", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Run the tasks
        run_tasks()

        st.write("Blood Test Summary:")
        with open("output/blood_test_summary.txt", "r") as f:
            st.text(f.read())

        st.write("Health Articles:")
        with open("output/health_articles.txt", "r") as f:
            st.text(f.read())

        st.write("Health Recommendations:")
        with open("output/health_recommendations.txt", "r") as f:
            st.text(f.read())

if __name__ == "__main__":
    main()
