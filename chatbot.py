from rag.retrieve import get_retriever
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

retriever = get_retriever()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


def ask_question(question):

    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an academic advisor for Morgan State University Computer Science students.

Use the catalog context below to answer the student question.

If the answer is not in the catalog, say you are not sure.

Catalog Context:
{context}

Student Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content


while True:

    question = input("\nStudent: ")

    if question.lower() == "exit":
        break

    answer = ask_question(question)

    print("\nAdvisor:", answer)