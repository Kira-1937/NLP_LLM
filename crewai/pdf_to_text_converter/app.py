from flask import Flask, request, redirect, url_for, render_template, send_file
import fitz  # PyMuPDF
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def pdf_to_text(pdf_path, txt_path):
    pdf_document = fitz.open(pdf_path)
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        pdf_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(pdf_path)
        txt_path = os.path.splitext(pdf_path)[0] + '.txt'
        pdf_to_text(pdf_path, txt_path)
        return send_file(txt_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
