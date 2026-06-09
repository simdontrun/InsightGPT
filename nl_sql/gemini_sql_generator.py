import os

from dotenv import load_dotenv
from google import genai


# Load environment variables
load_dotenv()


# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_sql(question):

    prompt = f"""
You are an expert SQL Server analyst.

Database Table:
Superstore

Columns:
Ship_Mode
Segment
Country
City
State
Postal_Code
Region
Category
Sub_Category
Sales
Quantity
Discount
Profit

Rules:
1. Generate ONLY SQL.
2. Use SQL Server syntax.
3. Only generate SELECT statements.
4. Never generate DELETE, UPDATE, INSERT, DROP, ALTER, CREATE, or TRUNCATE.
5. Do not explain anything.
6. Do not include markdown.
7. Do not include ```sql.
8. Return SQL only.

User Question:
{question}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        if not response.text:
            print("❌ Gemini returned empty response")
            return None

        sql = response.text.strip()

        # Remove markdown if Gemini adds it anyway
        sql = sql.replace("```sql", "")
        sql = sql.replace("```", "")

        return sql.strip()

    except Exception as e:

        print("\n❌ Gemini API Error")
        print(e)

        return None