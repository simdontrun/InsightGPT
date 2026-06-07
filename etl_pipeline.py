import pandas as pd

from ingestion.validator import DataValidator
from ingestion.cleaner import DataCleaner


def run_pipeline():

    print("Loading dataset...")

    df = pd.read_csv("data/raw/sample_sales.csv")

    print("Running validation checks...")

    validator = DataValidator(df)

    validator.check_missing_values()
    validator.check_duplicates()

    required_columns = [
        "Order_ID",
        "Order_Date",
        "Product",
        "Sales",
        "Region"
    ]

    validator.check_required_columns(required_columns)

    validator.validate_date_column("Order_Date")

    print("Cleaning data...")

    cleaner = DataCleaner(df)

    cleaner.remove_duplicates()
    cleaner.fill_missing_values()
    cleaner.standardize_dates("Order_Date")

    cleaner.save_cleaned_data(
        "data/cleaned/clean_sales.csv"
    )

    print("ETL Pipeline Completed Successfully")


if __name__ == "__main__":
    run_pipeline()