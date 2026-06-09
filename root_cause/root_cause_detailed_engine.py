from database.db_loader import SQLLoader

from root_cause.root_cause_detailed_queries import (
    LOSS_PRODUCT_DETAILS_QUERY
)


def get_loss_product_details():

    loader = SQLLoader()

    if not loader.cursor:
        return None

    loader.cursor.execute(
        LOSS_PRODUCT_DETAILS_QUERY
    )

    rows = loader.cursor.fetchall()

    # Convert pyodbc Row objects to normal tuples
    return [tuple(row) for row in rows]