import streamlit as st
from utils.pdf_loader import extract_text_from_pdfs
from utils.vectore_store import create_vectorstore
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import os
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()


text_data=extract_text_from_pdfs("docs/")
create_vectorstore(text_data)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectordb = FAISS.load_local("faiss_index", embeddings,allow_dangerous_deserialization=True)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",temperature=0.0, google_api_key=os.getenv("GOOGLE_API_KEY"))
retriver = vectordb.as_retriever()
prompt_template = """
You are an intelligent assistant who helps users understand insurance policies only.

If the question is unrelated to insurance, respond with: 
"❌ Please ask me about insurance only."

If you do not know the answer or are not confident, respond with:
"⚠️ I do not know the answer. For further queries, please contact xyz@example.com."

Context:
{context}

Question:
{question}

Helpful Answer:
"""

prompt = PromptTemplate(
    input_variables= ["context","question"],
    template = prompt_template,
)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever = retriver,
    chain_type_kwargs={"prompt":prompt}
    #return_source_documents= True
)

st.title("TATA Insurance Policy Info ChatBot 🤖")


if "history" not in st.session_state:
    st.session_state["history"]=[]

for q,a in st.session_state["history"]:
    with st.chat_message("user"):
        st.markdown(q)
    with st.chat_message("assistant"):
        st.markdown(a)
#"You are a helpful assistant who gives information about only insurance if the below query is not about insurance just say 'Please ask about Our insurance policy only!' "+
query= st.chat_input("Ask a question about Our insurance Policies:")

if query:
    with st.chat_message("user"):
        st.markdown(query)
    response = qa_chain.invoke({"query": query})
    answer = response["result"]

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state["history"].append((query, answer))
