from database.db_loader import SQLLoader
from analytics.kpi_queries import PRODUCT_QUERY


def get_product_data():

    loader = SQLLoader()

    if not loader.cursor:
        return []

    loader.cursor.execute(PRODUCT_QUERY)

    rows = loader.cursor.fetchall()

    data = []

    for row in rows:
        data.append({
            "Product": row[0],
            "Revenue": float(row[1]),
            "Profit": float(row[2])
        })

    return data