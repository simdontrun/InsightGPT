import pandas as pd


class DataValidator:

    def __init__(self, dataframe):
        self.df = dataframe

    def check_missing_values(self):
        return self.df.isnull().sum()

    def check_duplicates(self):
        return self.df.duplicated().sum()

    def check_required_columns(self, required_columns):
        missing_columns = []

        for column in required_columns:
            if column not in self.df.columns:
                missing_columns.append(column)

        return missing_columns
    
    def validate_date_column(self, column_name):
        try:
            pd.to_datetime(self.df[column_name], format="mixed")
            return True
        
        except Exception as e:
            print("Data Error:", e)
            return False

