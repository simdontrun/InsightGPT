import os
from dotenv import load_dotenv
from utils.gemini_client import get_gemini_client

load_dotenv()
client = get_gemini_client()


def generate_sql(question):

    prompt = f"""
You are an expert SQLite analyst.

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
2. Use SQLite syntax.
3. Only generate SELECT statements.
4. Never generate DELETE, UPDATE, INSERT, DROP, ALTER, CREATE, or TRUNCATE.
5. Use LIMIT instead of TOP for limiting rows.
6. Do not explain anything.
7. Do not include markdown.
8. Do not include ```sql.
9. Return SQL only.

User Question:
{question}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        if not response.text:
            return None

        sql = response.text.strip()
        sql = sql.replace("```sql", "").replace("```", "")
        return sql.strip()

    except Exception as e:
        print("Gemini API Error:", e)
        return None
