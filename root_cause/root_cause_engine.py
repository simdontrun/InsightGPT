from database.db_loader import SQLLoader

from root_cause.root_cause_queries import (
    LOSS_MAKING_PRODUCTS_QUERY
)


def get_loss_making_products():

    loader = SQLLoader()

    if not loader.cursor:
        return None

    loader.cursor.execute(
        LOSS_MAKING_PRODUCTS_QUERY
    )

    rows = loader.cursor.fetchall()

    return rows