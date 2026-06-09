import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def explain_loss_products(results):

    prompt = f"""
You are a senior business analyst.

The following products are generating negative profit:

{results}

Rules:

1. Use only the provided data.
2. Do not invent numbers.
3. Explain what the data suggests.
4. Keep the explanation under 5 sentences.
5. Focus on business implications.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:

        print("Gemini Error:", e)

        return None