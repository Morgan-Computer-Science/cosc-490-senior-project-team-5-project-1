from pathlib import Path
import json
import re

RAW_FILES = [
    Path("data/raw/morgan_cs_clean.txt"),
]
OUT_FILE = Path("data/chunks.json")

def split_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s.strip() for s in sentences if s.strip()]

def chunk_sentences(sentences, max_sentences=3):
    chunks = []
    for i in range(0, len(sentences), max_sentences):
        chunk = " ".join(sentences[i:i + max_sentences]).strip()
        if chunk:
            chunks.append(chunk)
    return chunks

def main():
    documents = []

    for file_path in RAW_FILES:
        if not file_path.exists():
            continue

        text = file_path.read_text(encoding="utf-8")
        sentences = split_sentences(text)
        chunks = chunk_sentences(sentences, max_sentences=3)

        for i, chunk in enumerate(chunks):
            documents.append({
                "source": file_path.name,
                "chunk_id": i,
                "text": chunk
            })

    OUT_FILE.write_text(json.dumps(documents, indent=2), encoding="utf-8")
    print(f"Saved {len(documents)} chunks to {OUT_FILE}")

if __name__ == "__main__":
    main()
