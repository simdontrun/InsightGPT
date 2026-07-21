from nl_sql.sql_executor import execute_query


query = """
SELECT TOP 5
    Category,
    Sales
FROM Superstore
"""


rows = execute_query(query)

for row in rows:
    print(row)