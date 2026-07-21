from database.db_loader import SQLLoader
from analytics.kpi_queries import PRODUCT_QUERY

loader = SQLLoader()

if not loader.cursor:
    print("❌ Database connection failed")
    exit()

print("\n🏆 TOP PRODUCT PERFORMANCE")
print("-" * 70)

loader.cursor.execute(PRODUCT_QUERY)

rows = loader.cursor.fetchall()

for row in rows:
    product = row[0]
    revenue = row[1]
    profit = row[2]

    print(
        f"{product:<20} | Revenue: {revenue:,.2f} | Profit: {profit:,.2f}"
    )
    