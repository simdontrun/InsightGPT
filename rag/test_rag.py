from rag.pdf_loader import (
    load_pdf
)

from rag.vector_store import (
    split_documents,
    create_vector_store,
    retrieve_documents
)


documents = load_pdf(
    "data/documents/InsightGPT_Quarterly_Report.pdf"
)

chunks = split_documents(
    documents
)

vector_store = create_vector_store(
    chunks
)

question = (
    "What was the biggest business risk?"
)

results = retrieve_documents(
    vector_store,
    question
)

print(
    "\nQUESTION:\n"
)

print(question)

print(
    "\nRETRIEVED DOCUMENT:\n"
)

print(
    results[0].page_content
)