from nl_sql.explanation_generator import generate_explanation


question = "Which region has highest sales?"

results = [('West',)]


explanation = generate_explanation(
    question,
    results
)

print("\n🤖 Explanation:\n")
print(explanation)