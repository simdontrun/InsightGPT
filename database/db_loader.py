import pyodbc


class SQLLoader:
    def __init__(self):
        try:
            self.conn = pyodbc.connect(
                "Driver={ODBC Driver 17 for SQL Server};"
                "Server=tcp:insightgpt-server-12345.database.windows.net,1433;"
                "Database=InsightGPTDB;"
                "Uid=sqladmin;"
                "Pwd=#eerrttyy07;"
                "Encrypt=yes;"
                "TrustServerCertificate=no;"
                "Connection Timeout=30;"
            )

            self.cursor = self.conn.cursor()
            print("✅ Database connection established")

        except Exception as e:
            print("❌ Connection failed:")
            print(e)
            self.cursor = None

    def test_connection(self):
        if not self.cursor:
            print("❌ Cursor not available (connection failed)")
            return
        
            self.cursor.execute("SELECT 1")
            result = self.cursor.fetchone()
            print("✅ Connection test result:", result[0])
        
    def create_table(self):

        if not self.cursor:
             print("❌ No database connection")
             return

        self.cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Superstore' AND xtype='U')
        CREATE TABLE Superstore (
          Ship_Mode VARCHAR(50),
          Segment VARCHAR(50),
          Country VARCHAR(50),
          City VARCHAR(100),
          State VARCHAR(100),
          Postal_Code INT,
          Region VARCHAR(50),
          Category VARCHAR(50),
          Sub_Category VARCHAR(50),
          Sales FLOAT,
          Quantity INT,
          Discount FLOAT,
          Profit FLOAT
        )
        """)
        self.conn.commit()
        print("✅ Table created successfully (or already exists)")

        self.cursor.execute("SELECT COUNT(*) FROM Superstore")

        count = self.cursor.fetchone()[0]

        print(f"📊 Rows currently in table: {count}")

        self.cursor.execute("DELETE FROM Superstore")
        self.conn.commit()

        print("🗑️ Existing data cleared")

    
    def insert_data(self, csv_path):
        import pandas as pd

        df = pd.read_csv(csv_path)

        print(f"📊 Loading {len(df)} rows...")

        data = list(df.itertuples(index=False, name=None))

        self.cursor.fast_executemany = True

        self.cursor.executemany("""
            INSERT INTO Superstore
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, data)

        self.conn.commit()

        print(f"✅ Inserted {len(df)} rows into Azure SQL")
    
