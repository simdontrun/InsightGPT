from database.db_loader import SQLLoader


def execute_query(query):

    print("\n🔍 Attempting SQL Connection...")

    loader = SQLLoader()

    if not loader.cursor:
        print("❌ SQLLoader returned no cursor")
        return None

    print("✅ Connection Successful")

    loader.cursor.execute(query)

    rows = loader.cursor.fetchall()

    print(f"✅ Retrieved {len(rows)} rows")

    return rows