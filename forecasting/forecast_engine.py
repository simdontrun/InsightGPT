import os
import pandas as pd
from prophet import Prophet


# Path to the forecast CSV — used directly, no database required
FORECAST_CSV = os.path.join(
    os.path.dirname(__file__), "..", "data", "cleaned", "forecast_sales.csv"
)
FORECAST_CSV = os.path.normpath(FORECAST_CSV)


def generate_forecast():
    """
    Load the forecast dataset from CSV, fit a Prophet model,
    and return a 30-day forward forecast with confidence intervals.
    """
    if not os.path.exists(FORECAST_CSV):
        print(f"❌ Forecast CSV not found at: {FORECAST_CSV}")
        return None

    df = pd.read_csv(FORECAST_CSV)

    # Prophet requires columns named 'ds' (date) and 'y' (target)
    df = df.rename(columns={"Order_Date": "ds", "Sales": "y"})
    df["ds"] = pd.to_datetime(df["ds"])

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]
