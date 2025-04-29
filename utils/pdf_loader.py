from PyPDF2 import PdfReader
import os
def extract_text_from_pdfs(pdf_folder):
    text=""
    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.endswith(".pdf"):
            reader=PdfReader(os.path.join(pdf_folder,pdf_file))
            for page in reader.pages:
                text = text + page.extract_text()
    return text