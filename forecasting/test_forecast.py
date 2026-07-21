from forecasting.forecast_engine import (
    generate_forecast
)

forecast = generate_forecast()

print(
    forecast.tail()
)