from langchain_text_splitters import RecursiveCharacterTextSplitter

with open("data/morgan_cs_catalog.txt", "r", encoding="utf-8") as f:
    text = f.read()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_text(text)

with open("data/catalog_chunks.txt", "w", encoding="utf-8") as f:
    for chunk in chunks:
        f.write(chunk + "\n\n")

print("Chunks created:", len(chunks))