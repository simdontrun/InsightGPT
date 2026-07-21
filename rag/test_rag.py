from rag.rag_engine import (
    ask_document
)


question = (
    "What was the biggest business risk?"
)

answer = ask_document(
    question
)

print(
    "\nQUESTION:\n"
)

print(question)

print(
    "\nANSWER:\n"
)

print(answer)