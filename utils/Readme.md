# 🛡️ AI-Powered Insurance Details Chatbot

An AI-powered chatbot that helps users interact with insurance policy documents through natural language queries. Built using **Python**, **Streamlit**, **LangChain**, and **Google Gemini**, this tool allows users to upload PDF policy files and ask questions like:

- "What is covered in this policy?"
- "What are the exclusions?"
- "When does the policy expire?"

---

## 🚀 Features

- 📄 Upload insurance policy PDFs
- 💬 Ask natural language questions and receive instant answers
- 🧠 Context-aware conversations using LangChain and Gemini
- ⚡ Simple and interactive UI via Streamlit
- 🛠️ Modular and extensible codebase

---

## 🧰 Tech Stack

- **Python 3.9+**
- **Streamlit** – Frontend web app framework
- **LangChain** – Language model orchestration
- **Google Gemini** – Large language model API
- **PyMuPDF / pdfplumber** – PDF parsing
- **FAISS / Chroma** – Document embedding and vector search

---

## 🛠️ Installation

1. Clone the repository

git clone https://github.com/your-username/insurance-chatbot.git
cd insurance-chatbot

2. Create a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Set up environment variables

Create a .env file with your API keys:

GEMINI_API_KEY=your_google_gemini_api_key

5. Run the app

streamlit run app.py

6. To add PDF and update the Vector database 

Create Docs folder
put the PDFs inside the Docs folder and run setup.py
