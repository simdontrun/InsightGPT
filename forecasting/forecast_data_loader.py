import pandas as pd

from database.db_loader import SQLLoader


def load_forecast_dataset():

    # Read forecasting dataset

    df = pd.read_csv(
        "data/cleaned/forecast_sales.csv"
    )

    # Connect to SQL Server

    loader = SQLLoader()

    if not loader.cursor:
        print("Database connection failed")
        return

    # Create forecasting table

    create_table_query = """
    IF OBJECT_ID('SalesForecastData', 'U') IS NULL
    CREATE TABLE SalesForecastData (
        Order_Date DATE,
        Sales FLOAT
    )
    """

    loader.cursor.execute(
        create_table_query
    )

    loader.conn.commit()

    print(
        "Forecast table ready"
    )

    # Clear old data

    loader.cursor.execute(
        "DELETE FROM SalesForecastData"
    )

    loader.conn.commit()

    print(
        "Existing forecast data cleared"
    )

    # Insert new dataset

    for _, row in df.iterrows():

        loader.cursor.execute(
            """
            INSERT INTO SalesForecastData
            (
                Order_Date,
                Sales
            )
            VALUES (?, ?)
            """,
            (
                row["Order_Date"],
                float(row["Sales"])
            )
        )

    loader.conn.commit()

    print(
        f"Inserted {len(df)} rows into SalesForecastData"
    )