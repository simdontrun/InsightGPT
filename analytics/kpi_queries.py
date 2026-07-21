REVENUE_QUERY = """
SELECT
    SUM(Sales) AS TotalRevenue
FROM Superstore
"""

PROFIT_QUERY = """
SELECT
    SUM(Profit) AS TotalProfit
FROM Superstore
"""

MARGIN_QUERY = """
SELECT
    (SUM(Profit) / SUM(Sales)) * 100 AS ProfitMargin
FROM Superstore
"""

REGION_QUERY = """
SELECT
    Region,
    SUM(Sales) AS Revenue,
    SUM(Profit) AS Profit
FROM Superstore
GROUP BY Region
ORDER BY Revenue DESC
"""

CATEGORY_QUERY = """
SELECT
    Category,
    SUM(Sales) AS Revenue,
    SUM(Profit) AS Profit
FROM Superstore
GROUP BY Category
ORDER BY Revenue DESC
"""

PRODUCT_QUERY = """
SELECT
    Sub_Category,
    SUM(Sales) AS Revenue,
    SUM(Profit) AS Profit
FROM Superstore
GROUP BY Sub_Category
ORDER BY Revenue DESC
LIMIT 10
"""
