import pandas as pd

from ingestion.validator import DataValidator
from ingestion.business_validator import BusinessValidator
from ingestion.cleaner import DataCleaner

# ----------------------
# STEP 1: LOAD DATA
# ----------------------
df = pd.read_csv("data/raw/SampleSuperstore.csv")

print("\n📥 DATA LOADED:", df.shape)

# ----------------------
# STEP 2: BASIC VALIDATION
# ----------------------
validator = DataValidator(df)
validator.run_checks()

# ----------------------
# STEP 3: BUSINESS VALIDATION
# ----------------------
business_validator = BusinessValidator(df)
issues = business_validator.run_all_checks()

# STOP PIPELINE IF CRITICAL ISSUES EXIST
if issues:
    print("\n❌ Pipeline stopped due to business rule violations.")
    exit()

# ----------------------
# STEP 4: CLEANING
# ----------------------
cleaner = DataCleaner(df)

df = cleaner.remove_duplicates()
df = cleaner.fill_missing_values()
df = cleaner.standardize_dates()

# ----------------------
# STEP 5: SAVE OUTPUT
# ----------------------
cleaner.save_cleaned_data("data/processed/cleaned_superstore.csv")

print("\n🎉 ETL PIPELINE COMPLETED SUCCESSFULLY")