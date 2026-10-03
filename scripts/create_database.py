import sqlite3
from pathlib import Path

import pandas as pd


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# File paths
DATA_FILE = BASE_DIR / "data" / "cleaned_transactions.csv"
DATABASE_DIR = BASE_DIR / "database"
DATABASE_FILE = DATABASE_DIR / "retail_analysis.db"


# Create database directory if it does not exist
DATABASE_DIR.mkdir(exist_ok=True)


# Load cleaned transaction data
df = pd.read_csv(DATA_FILE)

print(f"Loaded {len(df):,} records from cleaned_transactions.csv")


# Connect to SQLite
conn = sqlite3.connect(DATABASE_FILE)


# Load data into SQLite
df.to_sql(
    "transactions",
    conn,
    if_exists="replace",
    index=False
)


# Verify the table
result = pd.read_sql_query(
    """
    SELECT COUNT(*) AS total_records
    FROM transactions
    """,
    conn
)

total_records = result["total_records"].iloc[0]

print(f"Records in transactions table: {total_records:,}")
print(f"Database created: {DATABASE_FILE}")


# Close connection
conn.close()