from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from pdf_processor import PDFProcessor
from image_processor import ImageProcessor
from external_search import ExternalSearch
from database_manager import DatabaseManager

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pdf_processor = PDFProcessor()
image_processor = ImageProcessor()
external_search = ExternalSearch()
database_manager = DatabaseManager()

@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    pdf_content = await file.read()
    pdf_processor.process_pdf(pdf_content)
    return {"status": "PDF uploaded successfully"}

@app.post("/ask_question/")
async def ask_question(user_id: str, question: str):
    answer = pdf_processor.answer_query(question)
    if not answer:
        answer = external_search.perform_search(question)
    database_manager.save_interaction(user_id, question, answer)
    return {"answer": answer}

@app.post("/upload_image/")
async def upload_image(file: UploadFile = File(...)):
    image_content = await file.read()
    description = image_processor.describe_image(image_content)
    return {"description": description}
