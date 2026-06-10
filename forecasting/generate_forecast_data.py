import pandas as pd
import numpy as np


dates = pd.date_range(
    start="2023-01-01",
    end="2023-12-31"
)

sales = []

for i in range(len(dates)):

    base_sales = 1000

    trend = i * 2

    seasonality = 200 * np.sin(i / 30)

    noise = np.random.randint(
        -100,
        100
    )

    revenue = (
        base_sales
        + trend
        + seasonality
        + noise
    )

    sales.append(
        round(revenue, 2)
    )

df = pd.DataFrame(
    {
        "Order_Date": dates,
        "Sales": sales
    }
)

df.to_csv(
    "data/cleaned/forecast_sales.csv",
    index=False
)

print(
    f"Generated {len(df)} rows"
)