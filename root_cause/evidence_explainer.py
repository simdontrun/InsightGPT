import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def explain_evidence(results):

    prompt = f"""
You are a senior business analyst.

Evidence:

{results}

Analyze:

1. Which products are causing losses?
2. Which products have unusually high discounts?
3. What patterns do you observe?
4. What business risks should management investigate?

Rules:

- Use only the provided evidence.
- Do not invent numbers.
- Keep answer under 8 sentences.
- Write like an executive business analyst.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:

        print("Gemini Error:", e)

        return """
Executive analysis temporarily unavailable.

The AI service quota has been exceeded.
Business evidence is still displayed above and can be reviewed manually.
"""