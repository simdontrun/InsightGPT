from nl_sql.gemini_sql_generator import generate_sql


question = "What is the total revenue?"


sql = generate_sql(question)

print("\n📝 Question:")
print(question)

print("\n📄 Generated SQL:")
print(sql)