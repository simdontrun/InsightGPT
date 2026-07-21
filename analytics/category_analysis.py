from database.db_loader import SQLLoader
from analytics.kpi_queries import CATEGORY_QUERY

loader = SQLLoader()

if not loader.cursor:
    print("❌ Database connection failed")
    exit()

print("\n📦 CATEGORY PERFORMANCE")
print("-" * 50)

loader.cursor.execute(CATEGORY_QUERY)

rows = loader.cursor.fetchall()

for row in rows:
    category = row[0]
    revenue = row[1]
    profit = row[2]

    print(
        f"{category:<20} | Revenue: {revenue:,.2f} | Profit: {profit:,.2f}"
    )