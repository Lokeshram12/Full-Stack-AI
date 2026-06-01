from pathlib import Path 
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore

import os
from dotenv import load_dotenv

# Load key-value pairs from the .env file into the system environment
load_dotenv()

# Retrieve the variables
api_key = os.getenv("GOOGLE_API_KEY")

pdf_path = Path(__file__).parent/"Functional-Programming-in-Scala.pdf"

# load this file
loader = PyPDFLoader(file_path = pdf_path)
docs = loader.load()

# print(docs[2])

# Split the docs into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)

chunks = text_splitter.split_documents(documents=docs)

# embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

# vector = embedding_model.embed_query("hello, world!")
# print(vector[:5])
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag",
    force_recreate=True
)

print("Indexing of documents done....")