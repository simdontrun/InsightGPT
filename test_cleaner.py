import pandas as pd

from ingestion.cleaner import DataCleaner

df = pd.read_csv("data/raw/sample_sales.csv")

cleaner = DataCleaner(df)

cleaner.remove_duplicates()

cleaner.fill_missing_values()

cleaned_df = cleaner.standardize_dates("Order_Date")

print(cleaned_df)