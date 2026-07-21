import sqlite3
import os
import pandas as pd


# Path to the SQLite database file (created automatically on first run)
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "insightgpt.db")
DB_PATH = os.path.normpath(DB_PATH)

# Path to the source CSV used to seed the database
CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "raw", "SampleSuperstore.csv")
CSV_PATH = os.path.normpath(CSV_PATH)


def _seed_database(conn):
    """
    Create and populate the Superstore table from the raw CSV.
    Called automatically when the database file does not yet exist.
    """
    df = pd.read_csv(CSV_PATH)

    # Normalise column names: strip spaces, replace spaces/hyphens with underscores
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
    )

    # Write to SQLite — replaces the table if it somehow already exists
    df.to_sql("Superstore", conn, if_exists="replace", index=False)
    conn.commit()
    print(f"✅ Database seeded: {len(df)} rows loaded into Superstore table")


class SQLLoader:
    def __init__(self):
        db_exists = os.path.exists(DB_PATH)

        try:
            self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
            self.cursor = self.conn.cursor()

            if not db_exists:
                print("📦 First run — seeding SQLite database from CSV…")
                _seed_database(self.conn)

            print("✅ Database connection established")

        except Exception as e:
            print("❌ Database connection failed:")
            print(e)
            self.conn = None
            self.cursor = None

    def test_connection(self):
        """Return True if the connection is alive, False otherwise."""
        if not self.cursor:
            print("❌ Cursor not available (connection failed)")
            return False

        self.cursor.execute("SELECT 1")
        result = self.cursor.fetchone()
        print("✅ Connection test result:", result[0])
        return True
