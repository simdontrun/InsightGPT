import os

from dotenv import load_dotenv
from utils.gemini_client import get_gemini_client

from rag.pdf_loader import load_pdf
from rag.vector_store import split_documents, create_vector_store, retrieve_documents

load_dotenv()

client = get_gemini_client()


def ask_document(question):

    documents = load_pdf(
        "data/documents/InsightGPT_Quarterly_Report.pdf"
    )

    chunks = split_documents(documents)
    vector_store = create_vector_store(chunks)
    retrieved_docs = retrieve_documents(vector_store, question)

    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    prompt = f"""
You are a business analyst.

Answer the user's question ONLY using the context below.

Context:

{context}

Question:

{question}

Rules:

- Use only the provided context.
- Do not invent information.
- Keep answers concise.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )
        return response.text

    except Exception:
        return (
            "Document Intelligence is temporarily unavailable.\n\n"
            "The Gemini API quota has been exceeded. "
            "The retrieval system is functioning correctly, but the language model "
            "cannot generate a response at this time."
        )
