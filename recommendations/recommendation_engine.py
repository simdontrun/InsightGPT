import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_recommendations(results):

    prompt = f"""
You are a senior business consultant.

The following products are LOSS-MAKING products.

Evidence:

{results}

Each row contains:

(Sub_Category, Revenue, Profit, AvgDiscount, Quantity)

Tasks:

1. Explain why these products may be unprofitable.
2. Identify products requiring immediate attention.
3. Recommend actions to improve profitability.
4. Prioritize recommendations by business impact.

Rules:

- Focus on PROFITABILITY.
- Focus on LOSS REDUCTION.
- Use only the provided evidence.
- Do not invent numbers.
- Do not assume any currency.
- Do not add currency symbols.
- Maximum 5 recommendations.
- Write in executive style.
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