import pandas as pd

from database.db_loader import SQLLoader


def load_forecast_data():

    # Read forecast dataset

    df = pd.read_csv(
        "data/cleaned/forecast_sales.csv"
    )

    # Connect to SQL Server

    loader = SQLLoader()

    if not loader.cursor:
        print("Database connection failed")
        return

    # Create forecasting table if it doesn't exist

    create_table_query = """
    IF OBJECT_ID('SalesForecastData', 'U') IS NULL
    CREATE TABLE SalesForecastData (
        Order_ID INT,
        Order_Date DATE,
        Product VARCHAR(255),
        Sales FLOAT,
        Region VARCHAR(100)
    )
    """

    loader.cursor.execute(
        create_table_query
    )

    loader.conn.commit()

    print(
        "Forecast table created successfully"
    )

    # Remove old forecast records

    loader.cursor.execute(
        "DELETE FROM SalesForecastData"
    )

    loader.conn.commit()

    print(
        "Existing forecast data cleared"
    )

    # Insert forecast dataset

    for _, row in df.iterrows():

        loader.cursor.execute(
            """
            INSERT INTO SalesForecastData
            (
                Order_ID,
                Order_Date,
                Product,
                Sales,
                Region
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                int(row["Order_ID"]),
                row["Order_Date"],
                row["Product"],
                float(row["Sales"]),
                row["Region"]
            )
        )

    loader.conn.commit()

    print(
        f"Inserted {len(df)} rows into SalesForecastData"
    )
