from database.db_loader import SQLLoader
from analytics.kpi_queries import REGION_QUERY


def get_region_data():

    loader = SQLLoader()

    if not loader.cursor:
        return []

    loader.cursor.execute(REGION_QUERY)

    rows = loader.cursor.fetchall()

    data = []

    for row in rows:
        data.append({
            "Region": row[0],
            "Revenue": float(row[1]),
            "Profit": float(row[2])
        })

    return data