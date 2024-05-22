import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from PyPDF2 import PdfReader
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.runnables import RunnablePassthrough

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

key = st.secrets["OPENAI_API_KEY"]
model = ChatOpenAI(model="gpt-4o", openai_api_key=key)

message = """
Kamu adalah seorang komedian.
Kamu akan diberikan CV / resume sebagai context.
Roast CV / resume dengan sangat lucu.
Gunakan bahasa indonesia kasual anak tongkrongan.
Maksimum 200 karakter.
{question}

Context:
{context}
"""
prompt = ChatPromptTemplate.from_messages([("human", message)])

st.set_page_config(page_title="Kang Roasting", page_icon=":smiling_imp:")
st.title("Mana CV lo? sini gua roasting :smiling_imp:")

uploaded_file = st.file_uploader("Choose a file", type='pdf')

if uploaded_file is not None:
    text = ""
    reader = PdfReader(uploaded_file)
    for page in reader.pages:
      text += page.extract_text()
    doc = Document(
        page_content=text
    )
    
    vectorstore = Chroma.from_documents(
        [doc],
        embedding=OpenAIEmbeddings(openai_api_key=key),
    )
    
    retriever = vectorstore.as_retriever()
    rag_chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | model

    with st.spinner("Lagi dimasak :fire: sabar yak"):
        result = rag_chain.invoke("roast my CV").content
        st.write(result)
    