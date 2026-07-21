from database.db_loader import SQLLoader

from analytics.kpi_queries import (
    REVENUE_QUERY,
    PROFIT_QUERY,
    MARGIN_QUERY
)


loader = SQLLoader()

if not loader.cursor:
    print("❌ Database connection failed")
    exit()


print("\n📊 BUSINESS KPIs")
print("-" * 40)


# Revenue KPI
loader.cursor.execute(REVENUE_QUERY)

revenue = loader.cursor.fetchone()[0]

print(f"💰 Total Revenue: {revenue:,.2f}")


# Profit KPI
loader.cursor.execute(PROFIT_QUERY)

profit = loader.cursor.fetchone()[0]

print(f"📈 Total Profit: {profit:,.2f}")


# Margin KPI
loader.cursor.execute(MARGIN_QUERY)

margin = loader.cursor.fetchone()[0]

print(f"🎯 Profit Margin: {margin:.2f}%")