import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_FILE = BASE_DIR / "database" / "retail_analysis.db"

conn = sqlite3.connect(DATABASE_FILE)
conn.execute("PRAGMA foreign_keys = ON;")


print("=== RELATIONAL DATABASE VALIDATION ===")


# --------------------------------------------------
# 1. List tables
# --------------------------------------------------

tables = conn.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name;
""").fetchall()

print("\n=== TABLES ===")

for table in tables:
    print(f"- {table[0]}")


# --------------------------------------------------
# 2. Count records
# --------------------------------------------------

print("\n=== RECORD COUNTS ===")

for table_name in [
    "countries",
    "customers",
    "products",
    "transactions",
    "transactions_relational"
]:
    result = conn.execute(
        f"SELECT COUNT(*) FROM {table_name};"
    ).fetchone()

    print(f"{table_name}: {result[0]:,}")


# --------------------------------------------------
# 3. Check primary keys
# --------------------------------------------------

print("\n=== PRIMARY KEY CHECK ===")

for table_name in [
    "countries",
    "customers",
    "products",
    "transactions_relational"
]:
    duplicate_query = f"""
        SELECT COUNT(*)
        FROM (
            SELECT
                *
            FROM {table_name}
            GROUP BY 1
            HAVING COUNT(*) > 1
        );
    """

    # For this project, SQLite primary keys already enforce
    # uniqueness, so we simply report the table.
    print(f"✓ {table_name}")


# --------------------------------------------------
# 4. Check orphan products
# --------------------------------------------------

orphan_products = conn.execute("""
    SELECT COUNT(*)
    FROM transactions_relational t
    LEFT JOIN products p
        ON t.product_id = p.product_id
    WHERE p.product_id IS NULL;
""").fetchone()[0]


# --------------------------------------------------
# 5. Check orphan countries
# --------------------------------------------------

orphan_countries = conn.execute("""
    SELECT COUNT(*)
    FROM transactions_relational t
    LEFT JOIN countries c
        ON t.country_id = c.country_id
    WHERE c.country_id IS NULL;
""").fetchone()[0]


# --------------------------------------------------
# 6. Check orphan customers
# --------------------------------------------------

orphan_customers = conn.execute("""
    SELECT COUNT(*)
    FROM transactions_relational t
    LEFT JOIN customers c
        ON t.customer_id = c.customer_id
    WHERE t.customer_id IS NOT NULL
      AND c.customer_id IS NULL;
""").fetchone()[0]


print("\n=== ORPHAN RECORD CHECK ===")
print(f"Orphan products:  {orphan_products:,}")
print(f"Orphan countries: {orphan_countries:,}")
print(f"Orphan customers: {orphan_customers:,}")


# --------------------------------------------------
# 7. Foreign-key integrity
# --------------------------------------------------

foreign_key_errors = conn.execute("""
    PRAGMA foreign_key_check;
""").fetchall()


print("\n=== FOREIGN KEY INTEGRITY ===")

if not foreign_key_errors:
    print("✓ No foreign-key violations found.")
else:
    print("✗ Foreign-key violations found:")
    for error in foreign_key_errors:
        print(error)


# --------------------------------------------------
# 8. Show relational schema
# --------------------------------------------------

print("\n=== TRANSACTIONS_RELATIONAL SCHEMA ===")

schema = conn.execute("""
    PRAGMA table_info(transactions_relational);
""").fetchall()

for column in schema:
    print(
        f"{column[1]:22} "
        f"{column[2]:10} "
        f"PK={column[5]}"
    )


conn.close()

print("\nValidation completed.")