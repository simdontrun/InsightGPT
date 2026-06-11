import os

from dotenv import load_dotenv
from google import genai

from rag.pdf_loader import (
    load_pdf
)

from rag.vector_store import (
    split_documents,
    create_vector_store,
    retrieve_documents
)


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_document(question):

    documents = load_pdf(
        "data/documents/InsightGPT_Quarterly_Report.pdf"
    )

    chunks = split_documents(
        documents
    )

    vector_store = create_vector_store(
        chunks
    )

    retrieved_docs = retrieve_documents(
        vector_store,
        question
    )

    context = "\n\n".join(
        [
            doc.page_content
            for doc in retrieved_docs
        ]
    )

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

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text