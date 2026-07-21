from database.db_loader import SQLLoader
from analytics.kpi_queries import REGION_QUERY

loader = SQLLoader()

if not loader.cursor:
    print("❌ Database connection failed")
    exit()

print("\n🌍 REGIONAL PERFORMANCE")
print("-" * 50)

loader.cursor.execute(REGION_QUERY)

rows = loader.cursor.fetchall()

for row in rows:
    region = row[0]
    revenue = row[1]
    profit = row[2]

    print(
        f"{region:<10} | Revenue: {revenue:,.2f} | Profit: {profit:,.2f}"
    )