import pandas as pd

from prophet import Prophet

from database.db_loader import SQLLoader


def generate_forecast():

    loader = SQLLoader()

    if not loader.cursor:
        print("Database connection failed")
        return None

    query = """
    SELECT
        Order_Date,
        Sales
    FROM SalesForecastData
    ORDER BY Order_Date
    """

    df = pd.read_sql(
        query,
        loader.conn
    )

    # Prophet requires:
    # ds = date column
    # y = target column

    df = df.rename(
        columns={
            "Order_Date": "ds",
            "Sales": "y"
        }
    )

    model = Prophet()

    model.fit(df)

    future = model.make_future_dataframe(
        periods=30
    )

    forecast = model.predict(
        future
    )

    return forecast[
        [
            "ds",
            "yhat",
            "yhat_lower",
            "yhat_upper"
        ]
    ]