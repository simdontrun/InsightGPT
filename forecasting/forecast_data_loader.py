import os
import pandas as pd
from database.db_loader import SQLLoader


FORECAST_CSV = os.path.join(
    os.path.dirname(__file__), "..", "data", "cleaned", "forecast_sales.csv"
)
FORECAST_CSV = os.path.normpath(FORECAST_CSV)


def load_forecast_dataset():
    """
    Load the forecast CSV into the SQLite SalesForecastData table.
    Creates the table if it doesn't exist and replaces any existing data.
    """
    if not os.path.exists(FORECAST_CSV):
        print(f"❌ Forecast CSV not found at: {FORECAST_CSV}")
        return

    df = pd.read_csv(FORECAST_CSV)

    loader = SQLLoader()
    if not loader.conn:
        print("❌ Database connection failed")
        return

    # Use pandas to_sql for clean SQLite-compatible insert
    df.to_sql("SalesForecastData", loader.conn, if_exists="replace", index=False)
    loader.conn.commit()

    print(f"✅ Inserted {len(df)} rows into SalesForecastData")
