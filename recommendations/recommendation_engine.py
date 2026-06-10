import os

from dotenv import load_dotenv
from google import genai

from recommendations.risk_analyzer import (
    analyze_risk
)


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_recommendations(results):

    risk_summary = analyze_risk(
        results
    )

    prompt = f"""
You are a senior business consultant.

The following products are LOSS-MAKING products.

Evidence:

{results}

Risk Summary:

{risk_summary}

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

        print(
            "Gemini Error:",
            e
        )

        return """
Recommendations temporarily unavailable.

The AI recommendation service has exceeded its current quota.
Please retry later or upgrade the API plan.
"""