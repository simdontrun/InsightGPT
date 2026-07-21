import pandas as pd


class DataCleaner:

    def __init__(self, dataframe):
        self.df = dataframe

    def remove_duplicates(self):
        """
        Remove duplicate rows from dataframe
        """

        before = len(self.df)

        self.df = self.df.drop_duplicates()

        after = len(self.df)

        removed = before - after

        print(f"Removed {removed} duplicate rows")

        return self.df
    
    def fill_missing_values(self):
         """
         Fill missing values in the dataframe
         """

         for column in self.df.columns:
               if self.df[column].dtype in ["int64", "float64"]:
                    
                    self.df[column] = self.df[column].fillna(self.df[column].mean())

               else:

                    self.df[column] = self.df[column].fillna(self.df[column].mode()[0])


         print("Missing Values Filled")

         return self.df
    
    def standardize_dates(self, column_name):
         """
         Convert dates into a standard format
         """

         self.df[column_name] = pd.to_datetime(self.df[column_name], format="mixed", errors="coerce")

         self.df[column_name] = self.df[column_name].dt.strftime("%Y-%m-%d")

         print(f"{column_name} standardized")

         return self.df
    
    def save_cleaned_data(self, output_path):
         """
         Save cleaned dataframe to CSV
         """

         self.df.to_csv(output_path, index=False)

         print(f"Cleaned data saved to {output_path}")
    

            
                     
           
   