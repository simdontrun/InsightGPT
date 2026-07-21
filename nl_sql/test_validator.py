from nl_sql.sql_validator import validate_sql


safe_query = """
SELECT * FROM Superstore
"""


dangerous_query = """
DROP TABLE Superstore
"""


print("Safe Query:", validate_sql(safe_query))

print("Dangerous Query:", validate_sql(dangerous_query))