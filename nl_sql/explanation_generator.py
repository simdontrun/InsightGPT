import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_explanation(question, results):

    prompt = f"""
You are a business analyst.

User Question:
{question}

Database Results:
{results}

Rules:
1. Use ONLY the provided results.
2. Do not invent numbers.
3. Explain the result in simple business language.
4. Keep the explanation under 3 sentences.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text.strip()