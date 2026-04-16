import json
import re
from pathlib import Path
from collections import Counter

CHUNKS_FILE = Path("data/chunks.json")

SOURCE_LABELS = {
    "morgan_cs_clean.txt": "Morgan State University Computer Science Advising Knowledge Base",
    "curriculum_sequence.txt": "Morgan State University Computer Science Curriculum Sequence",
    "computer_science_bs.txt": "Morgan State University Computer Science Program Information",
    "bs_computerscience.txt": "Morgan State University Computer Science Program Information",
}

def pretty_source_name(source):
    return SOURCE_LABELS.get(source, source)

def tokenize(text):
    return re.findall(r"\b[a-zA-Z0-9]+\b", text.lower())

def score_chunk(query_tokens, chunk_text):
    chunk_tokens = tokenize(chunk_text)
    chunk_counter = Counter(chunk_tokens)
    score = 0
    for token in query_tokens:
        score += chunk_counter[token]
    return score

def load_chunks():
    if not CHUNKS_FILE.exists():
        return []
    return json.loads(CHUNKS_FILE.read_text(encoding="utf-8"))

def retrieve_chunks(query, top_k=2):
    chunks = load_chunks()
    query_tokens = tokenize(query)

    scored = []
    for chunk in chunks:
        score = score_chunk(query_tokens, chunk["text"])
        if score > 0:
            scored.append((score, chunk))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [item[1] for item in scored[:top_k]]

def clean_answer_from_chunks(top_chunks):
    combined = " ".join(chunk["text"] for chunk in top_chunks)
    sentences = re.split(r'(?<=[.!?])\s+', combined)
    selected = []

    for sentence in sentences:
        sentence = sentence.strip()
        if sentence and sentence not in selected:
            selected.append(sentence)
        if len(selected) == 3:
            break

    return " ".join(selected)

def build_response(query, agent_name):
    top_chunks = retrieve_chunks(query)

    if not top_chunks:
        return {
            "agent": agent_name,
            "answer": "I could not find a strong match in the Morgan CS advising materials. Please verify with the department or an academic advisor.",
            "sources": []
        }

    answer = clean_answer_from_chunks(top_chunks)
    sources = list(dict.fromkeys(pretty_source_name(chunk["source"]) for chunk in top_chunks))

    return {
        "agent": agent_name,
        "answer": answer,
        "sources": sources
    }

def degree_planning_agent(query):
    return build_response(query, "Degree Planning Agent")

def prerequisite_agent(query):
    return build_response(query, "Prerequisite Checking Agent")

def advising_policy_agent(query):
    return build_response(query, "Advising and Policy Agent")

def resources_agent(query):
    return build_response(query, "Student Resources Agent")

def general_agent(query):
    return build_response(query, "General Advising Agent")

def route_query(query: str):
    q = query.lower()

    if (
        "prereq" in q or
        "prerequisite" in q or
        "before" in q or
        "can i take" in q or
        "take before" in q
    ):
        return prerequisite_agent(query)

    if (
        "credits" in q or
        "graduate" in q or
        "graduation" in q or
        "semester" in q or
        "sequence" in q or
        "plan" in q or
        "freshman" in q or
        "sophomore" in q or
        "junior" in q or
        "senior" in q or
        "cosc 490" in q
    ):
        return degree_planning_agent(query)

    if (
        "advisor" in q or
        "advising" in q or
        "policy" in q or
        "registration" in q
    ):
        return advising_policy_agent(query)

    if (
        "tutoring" in q or
        "resource" in q or
        "support" in q or
        "internship" in q or
        "help" in q
    ):
        return resources_agent(query)

    if "cosc 112" in q or "cosc 111" in q:
        return prerequisite_agent(query)

    return general_agent(query)

def answer_question(query: str):
    return route_query(query)
