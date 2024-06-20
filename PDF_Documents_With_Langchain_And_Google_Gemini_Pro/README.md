### PDF Answering AI

Welcome to the PDF Answering AI project repository! This project enables you to interactively query PDF documents using natural language processing techniques. The AI system extracts text from uploaded PDFs, processes it into chunks for efficient analysis, generates embeddings for semantic understanding, and provides accurate responses to user queries.

### Usage

#### Streamlit Web Application

To interact with the PDF Answering AI, visit the [Streamlit Web App](https://nlpllm-r9w5wijk5demb38yzrnpks.streamlit.app/) (open in white mode only).

#### Installation and Setup

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd PDF_Documents_With_Langchain_And_Google_Gemini_Pro
   ```

2. **Install Dependencies**

   Ensure you have Python 3.10 installed. Then, install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your Google API key:

   ```plaintext
   GOOGLE_API_KEY="your-google-api-key"
   ```

   Replace `"your-google-api-key"` with your actual Google API key.

4. **Run the Application**

   Start the Streamlit application:

   ```bash
   streamlit run app.py
   ```

   This will launch the application locally. Open your browser and go to `http://localhost:8501` to interact with the PDF Answering AI.

### Project Structure

The project structure is organized as follows:

- `.streamlit/`: Configuration folder for Streamlit settings.
- `faiss_index/`: Directory where FAISS index files are stored.
- `.env`: Environment variables configuration file (not included in repository for security reasons).
- `.gitignore`: Git ignore file to exclude sensitive or unnecessary files from version control.
- `app.py`: Main application file containing the Streamlit app code.
- `requirements.txt`: List of Python dependencies required for the project.
- `README.md`: This readme file providing project information and setup instructions.

### Additional Notes

- Ensure that your system has adequate permissions and configurations to run Streamlit applications.
- For any issues or improvements, feel free to create a GitHub issue or pull request.

### References

- Streamlit Documentation: [https://docs.streamlit.io/](https://docs.streamlit.io/)
- PyPDF2 Documentation: [https://pythonhosted.org/PyPDF2/](https://pythonhosted.org/PyPDF2/)
- FAISS GitHub Repository: [https://github.com/facebookresearch/faiss](https://github.com/facebookresearch/faiss)
- Google Generative AI: [https://github.com/google/generativeai](https://github.com/google/generativeai)

Thank you for exploring the PDF Answering AI project! If you have any questions or feedback, please reach out.