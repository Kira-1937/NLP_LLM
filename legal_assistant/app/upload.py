# app/upload.py
import os
import tempfile

def handle_file_upload(uploaded_file):
    # Save the uploaded file temporarily
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path
