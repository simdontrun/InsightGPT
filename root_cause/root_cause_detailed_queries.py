LOSS_PRODUCT_DETAILS_QUERY = """
SELECT
    Sub_Category,
    SUM(Sales) AS Revenue,
    SUM(Profit) AS Profit,
    AVG(Discount) AS AvgDiscount,
    SUM(Quantity) AS TotalQuantity
FROM Superstore
GROUP BY Sub_Category
HAVING SUM(Profit) < 0
ORDER BY Profit ASC
"""