from database.db_loader import SQLLoader
from analytics.kpi_queries import CATEGORY_QUERY


def get_category_data():

    loader = SQLLoader()

    if not loader.cursor:
        return []

    loader.cursor.execute(CATEGORY_QUERY)

    rows = loader.cursor.fetchall()

    data = []

    for row in rows:
        data.append({
            "Category": row[0],
            "Revenue": float(row[1]),
            "Profit": float(row[2])
        })

    return data