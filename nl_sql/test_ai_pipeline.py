from nl_sql.gemini_sql_generator import generate_sql
from nl_sql.sql_validator import validate_sql
from nl_sql.sql_executor import execute_query


question = "What is the total revenue?"

print(f"\n📝 Question: {question}")

query = generate_sql(question)

print("\n📄 Generated SQL:")
print(query)


if not validate_sql(query):
    print("❌ SQL validation failed")
    exit()

print("✅ SQL validated")


results = execute_query(query)

if results is None:
    print("❌ Database query failed")
    exit()

print("\n📊 Results:")

for row in results:
    print(row)