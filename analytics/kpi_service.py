from database.db_loader import SQLLoader

from analytics.kpi_queries import (
    REVENUE_QUERY,
    PROFIT_QUERY,
    MARGIN_QUERY
)


def get_kpis():

    loader = SQLLoader()

    if not loader.cursor:
        return None

    loader.cursor.execute(REVENUE_QUERY)
    revenue = loader.cursor.fetchone()[0]

    loader.cursor.execute(PROFIT_QUERY)
    profit = loader.cursor.fetchone()[0]

    loader.cursor.execute(MARGIN_QUERY)
    margin = loader.cursor.fetchone()[0]

    return {
        "revenue": revenue,
        "profit": profit,
        "margin": margin
    }