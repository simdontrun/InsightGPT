LOSS_MAKING_PRODUCTS_QUERY = """
SELECT
    Sub_Category,
    SUM(Sales) AS Revenue,
    SUM(Profit) AS Profit
FROM Superstore
GROUP BY Sub_Category
HAVING SUM(Profit) < 0
ORDER BY Profit ASC
"""