import os
from dotenv import load_dotenv
from utils.pdf_loader import extract_text_from_pdfs
from utils.vectore_store import create_vectorstore

def main():
    load_dotenv()
    print("[INFO] Extracting text from PDFs...")
    text_data = extract_text_from_pdfs("docs/")
    print("[INFO] Creating vectorstore with embeddings...")
    create_vectorstore(text_data)
    print("[SUCCESS] Vectorstore saved to 'faiss_index/'")

if __name__ == "__main__":
    main()