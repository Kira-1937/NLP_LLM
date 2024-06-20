# import streamlit as st
# from PyPDF2 import PdfReader


# from langchain.text_splitter import RecursiveCharacterTextSplitter

# import os

# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# import google.generativeai as genai


# # from langchain.vectorstores import FAISS
# from langchain_community.vectorstores import FAISS
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.chains.question_answering import load_qa_chain
# from langchain.prompts import PromptTemplate

# from dotenv import load_dotenv

# load_dotenv()

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# #-----------------------------------------------------------------
# def get_pdf_text(pdf_docs):
#     text=""
#     for pdf in pdf_docs:
#       pdf_reader=PdfReader(pdf)
#     for page in pdf_reader.pages:
#         text+=page.extract_text()

#     return text



# #------------------------------------------------------------------


# def get_text_chunks(text):
#     text_splitter=RecursiveCharacterTextSplitter(chunk_size=10000,chunk_overlap=1000)
#     chunks=text_splitter.split_text(text)
#     return chunks

# #------------------------------------------------------------------

# def get_vector_store(text_chunks):
#     embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
#     vector_store=FAISS.from_texts(text_chunks,embedding=embeddings )
#     vector_store.save_local("faiss_index")


# #------------------------------------------------------------------
    
# def get_conversational_chain():
#     prompt_template="""   
#     Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
#     provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
#     Context:\n {context}?\n
#     Question: \n{question}\n
#     Answer:
#     """
#     model=ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3)


#     prompt=PromptTemplate(template=prompt_template, input_variables=["context","question"])
    
#     chain=load_qa_chain(model,chain_type="stuff",prompt=prompt)
#     return chain







# #----------------------------------------------------------------
# # user input is taken here 

# def user_input(user_question):
#     embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
#     # new_db = FAISS.load_local("faiss_index", embeddings)
#     new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

#     docs = new_db.similarity_search(user_question)
    
#     chain = get_conversational_chain()

    
#     response = chain(
#         {"input_documents":docs, "question": user_question}
#         , return_only_outputs=True)

#     print(response)
#     st.write("Reply: ", response["output_text"])




    
# def main():
#     st.set_page_config("Chat PDF")
#     st.header("Chat with PDF using Gemini💁")

#     user_question = st.text_input("Ask a Question from the PDF Files")

#     if user_question:
#         user_input(user_question)

#     with st.sidebar:
#         st.title("Menu:")
#         pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
#         if st.button("Submit & Process"):
#             with st.spinner("Processing..."):
#                 raw_text = get_pdf_text(pdf_docs)
#                 text_chunks = get_text_chunks(raw_text)
#                 get_vector_store(text_chunks)
#                 st.success("Done")



# if __name__ == "__main__":
#     main()

import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="Chat with PDF using Gemini", page_icon="💁")

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template = """   
    Answer the question as detailed as possible from the provided context. If the answer is not in
    the provided context, just say, "answer is not available in the context". Do not provide a wrong answer.\n\n
    Context:\n {context}?\n
    Question: \n{question}\n
    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    st.write("Reply: ", response["output_text"])

def main():
    st.title("Chat with PDF using Gemini 💁")
    st.markdown(
        """
        <style>
        .main {background-color: #f8f9fa;}
        .stButton>button {background-color: #007bff; color: white; border-radius: 5px;}
        .stButton>button:hover {background-color: #0056b3;}
        .footer {position: fixed; bottom: 0; width: 100%; text-align: center; padding: 10px; background-color: #f8f9fa;}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Upload PDF files and ask questions using Gemini Pro AI.")
    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu 📜")
        pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Processing Complete")

        st.markdown("---")
        st.markdown("### About the App")
        st.markdown(
            """
            This app allows you to interact with PDF documents using advanced language models.
            - Upload PDF files.
            - Ask questions about the content.
            - Get detailed answers powered by Gemini Pro AI.
            """
        )
        
        with st.expander("📘 Explanation of Project"):
            st.markdown(
                """
                **Step-by-Step Explanation:**
                
                1. **Upload PDF Files**: 
                   - You can upload one or multiple PDF files using the file uploader.
                
                2. **Process the PDF Files**:
                   - Once you upload the files, click on the "Submit & Process" button.
                   - The app will read and extract text from all the pages in the uploaded PDF files.
                
                3. **Text Chunking**:
                   - The extracted text is then split into smaller chunks using a text splitter. This is necessary to handle large texts effectively.
                
                4. **Vector Store Creation**:
                   - These text chunks are then converted into embeddings (vector representations) using Google Generative AI embeddings.
                   - The embeddings are stored in a FAISS (Facebook AI Similarity Search) vector store for efficient similarity search.
                
                5. **Ask Questions**:
                   - You can type in a question related to the content of the uploaded PDF files.
                
                6. **Retrieve Relevant Information**:
                   - The app searches the vector store to find the most relevant chunks of text that can answer your question.
                
                7. **Generate Answer**:
                   - The relevant chunks are then passed to a conversational chain powered by Gemini Pro AI to generate a detailed answer to your question.
                
                8. **Display Answer**:
                   - The generated answer is displayed on the app.
                
                This app leverages advanced AI models to provide accurate and detailed answers based on the content of your PDF documents.
                """
            )

    st.markdown('<div class="footer">Made with ❤ by Vikram</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

