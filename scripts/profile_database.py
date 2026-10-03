import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_FILE = BASE_DIR / "database" / "retail_analysis.db"

conn = sqlite3.connect(DATABASE_FILE)


queries = {
    "unique_products": """
        SELECT COUNT(DISTINCT StockCode) AS unique_products
        FROM transactions;
    """,

    "unique_customers": """
        SELECT COUNT(DISTINCT CustomerID) AS unique_customers
        FROM transactions
        WHERE CustomerID IS NOT NULL;
    """,

    "unique_countries": """
        SELECT COUNT(DISTINCT Country) AS unique_countries
        FROM transactions;
    """,

    "missing_customer_ids": """
        SELECT COUNT(*) AS missing_customer_ids
        FROM transactions
        WHERE CustomerID IS NULL;
    """,

    "multiple_descriptions": """
        SELECT
            StockCode,
            COUNT(DISTINCT Description) AS description_count
        FROM transactions
        GROUP BY StockCode
        HAVING COUNT(DISTINCT Description) > 1;
    """,

    "customers_multiple_countries": """
    SELECT
        CustomerID,
        COUNT(DISTINCT Country) AS country_count
    FROM transactions
    WHERE CustomerID IS NOT NULL
    GROUP BY CustomerID
    HAVING COUNT(DISTINCT Country) > 1;
"""
}


for name, query in queries.items():
    print(f"\n=== {name.upper()} ===")

    result = pd.read_sql_query(query, conn)
    print(result)

conn.close()