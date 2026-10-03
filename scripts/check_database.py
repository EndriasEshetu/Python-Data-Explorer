import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_FILE = BASE_DIR / "database" / "retail_analysis.db"

conn = sqlite3.connect(DATABASE_FILE)


# Check table structure
schema = pd.read_sql_query(
    "PRAGMA table_info(transactions);",
    conn
)

print("=== TABLE STRUCTURE ===")
print(schema)


# Check first 10 records
records = pd.read_sql_query(
    """
    SELECT *
    FROM transactions
    LIMIT 10;
    """,
    conn
)

print("\n=== FIRST 10 RECORDS ===")
print(records)


conn.close()