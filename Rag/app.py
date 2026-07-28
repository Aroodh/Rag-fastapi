import streamlit as st
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader,TextLoader,Docx2txtLoader,WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

st.set_page_config(
    page_title="Python  Chatbot",
    page_icon="📚",
    layout="wide"
)


@st.cache_resource
def initialize_rag():
    # Load PDF
    pdf_loader = PyPDFLoader("data/pythonHandbook.pdf")
    pdf_docs = pdf_loader.load()
    
    txt_loader=TextLoader("data/javascrip.txt")
    txt_docs=txt_loader.load()
    
    docx_loader=Docx2txtLoader("data/Resume.docx")
    docx_docs=docx_loader.load()
    
    loader = WebBaseLoader("https://dheecodinglab.com/")
    web_docs = loader.load()
    
    
    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20
    )
    documents=[]
    documents.extend(pdf_docs)
    documents.extend(txt_docs)
    documents.extend(docx_docs)
    documents.extend(web_docs)

    chunks = splitter.split_documents(documents)

    # Embedding Model
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Vector Database
    vector_db = FAISS.from_documents(chunks, embedding)

    # Retriever
    retriever = vector_db.as_retriever(
        search_kwargs={"k": 3}
    )

    # LLM
    llm = ChatGroq(
        model_name="llama-3.3-70b-versatile"
    )

    # Prompt
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are an AI assistant.

Answer ONLY from the provided context and some additional information you may know .

If the answer is not available in the document,
reply exactly:

"Sorry, I couldn't find the answer in the document."

Context:
{context}

Question:
{question}

Answer:
"""
    )

    return retriever, llm, prompt


retriever, llm, prompt = initialize_rag()

st.title("😶‍🌫️ Python  RAG Chatbot")

st.write("Ask any question from the uploaded Python Handbook.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

question = st.chat_input("Ask your question...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("Searching document..."):

        docs = retriever.invoke(question)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        final_prompt = prompt.format(
            context=context,
            question=question
        )

        response = llm.invoke(final_prompt)

        answer = response.content
 
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)

        with st.expander("Retrieved Context"):
            st.write(context)