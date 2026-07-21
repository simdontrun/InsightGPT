from database.db_loader import SQLLoader

loader = SQLLoader()

loader.test_connection()
loader.create_table()

loader.insert_data("data/raw/SampleSuperstore.csv")