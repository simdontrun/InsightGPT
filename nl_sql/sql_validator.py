def validate_sql(query):

    query = query.strip().upper()

    forbidden_keywords = [
        "DROP",
        "DELETE",
        "UPDATE",
        "INSERT",
        "ALTER",
        "TRUNCATE",
        "CREATE"
    ]

    for keyword in forbidden_keywords:

        if keyword in query:
            return False

    if not query.startswith("SELECT"):
        return False

    return True