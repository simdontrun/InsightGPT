import pandas as pd

from ingestion.validator import DataValidator


df = pd.read_csv("data/raw/sample_sales.csv")

validator = DataValidator(df)

required_columns = [
    "Order_ID",
    "Order_Date",
    "Product",
    "Sales",
    "Region"
]

print("Missing Values:")
print(validator.check_missing_values())

print("\nDuplicate Rows:")
print(validator.check_duplicates())

print("\nMissing Required Columns:")
print(
    validator.check_required_columns(required_columns)
)

print("\nDate Validation:")
print(validator.validate_date_column("Order_Date"))