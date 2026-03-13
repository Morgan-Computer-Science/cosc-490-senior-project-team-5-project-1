from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

with open("data/catalog_chunks.txt", "r", encoding="utf-8") as f:
    chunks = f.read().split("\n\n")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_texts(
    chunks,
    embeddings
)

vectorstore.save_local("vector_db")

print("Vector database created.")