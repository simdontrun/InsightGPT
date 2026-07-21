def generate_sql(question):

    question = question.lower()

    if "revenue" in question:
        return """
        SELECT SUM(Sales) AS Revenue
        FROM Superstore
        """

    elif "profit" in question:
        return """
        SELECT SUM(Profit) AS Profit
        FROM Superstore
        """

    else:
        return None