import pandas as pd

from ingestion.cleaner import DataCleaner

df = pd.read_csv("data/raw/sample_sales.csv")

cleaner = DataCleaner(df)

cleaner.remove_duplicates()

cleaner.fill_missing_values()

cleaner.standardize_dates("Order_Date")

cleaner.save_cleaned_data(
    "data/cleaned/clean_sales.csv"
)