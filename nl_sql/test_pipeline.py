from nl_sql.sql_generator import generate_sql
from nl_sql.sql_validator import validate_sql
from nl_sql.sql_executor import execute_query


question = "What is total revenue?"


print(f"\n📝 Question: {question}")


# Generate SQL
query = generate_sql(question)

if not query:
    print("❌ Could not generate SQL")
    exit()

print("\n📄 Generated SQL:")
print(query)


# Validate SQL
if not validate_sql(query):
    print("❌ SQL validation failed")
    exit()

print("✅ SQL validated")


# Execute SQL
results = execute_query(query)

print("\n📊 Results:")

for row in results:
    print(row)