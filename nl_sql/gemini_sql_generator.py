import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_sql(question):

    prompt = f"""
You are a SQL Server expert.

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
4. Never generate DELETE, UPDATE, DROP, INSERT, ALTER, or TRUNCATE.
5. Return SQL only.

User Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    if response.text:
        sql = response.text.strip()

        sql = sql.replace("```sql", "")
        sql = sql.replace("```", "")

        return sql.strip()

    return None