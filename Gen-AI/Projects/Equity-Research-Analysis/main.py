import streamlit as st
import os
import pickle
import time
import langchain
from langchain.llms import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import UnstructuredURLLoader
from dotenv import load_dotenv

load_dotenv()

# Load the OpenAI LLM

openai_api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=openai_api_key,temperature=0.9, max_tokens=500)

main_placeholder = st.empty()

st.sidebar.title("Equity-Research-Analysis")

st.sidebar.subheader("Enter your URLS...")

urls = []

for i in range(3):
  url = st.sidebar.text_input(f"URL {i+1}")
  urls.append(url)

proces_button = st.sidebar.button("Process URL's")

if proces_button:
  loader = UnstructuredURLLoader(urls=urls)
  main_placeholder.text("Data Loading...Started...✅✅✅")
  data = loader.load()
  # split data
  text_splitter = RecursiveCharacterTextSplitter(
      separators=['\n\n', '\n', '.', ','], chunk_size=1000)
  main_placeholder.text("Text Splitter...Started...✅✅✅")
  docs = text_splitter.split_documents(data)
  # create embeddings and save it to FAISS index
  embeddings = OpenAIEmbeddings()
  vectorstore_openai = FAISS.from_documents(docs, embeddings)
  main_placeholder.text("Embedding Vector Started Building...✅✅✅")
  time.sleep(2)

  with open("faiss_store_openai.pkl", "wb") as f:
    pickle.dump(vectorstore_openai, f)

query = main_placeholder.text_input("Question: ")

if query:
  if os.path.exists("faiss_store_openai.pkl"):
    with open("faiss_store_openai.pkl", "rb") as f:
      vectorstore = pickle.load(f)
      chain = RetrievalQAWithSourcesChain.from_llm(
          llm=llm, retriever=vectorstore.as_retriever())
      result = chain({"question": query}, return_only_outputs=True)
      # result will be a dictionary of this format --> {"answer": "", "sources": [] }
      st.header("Answer")
      st.write(result["answer"])

      # Display sources, if available
      sources = result.get("sources", "")
      if sources:
        st.subheader("Sources:")
        sources_list = sources.split("\n")  # Split the sources by newline
        for source in sources_list:
          st.write(source)
