import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_FILE = BASE_DIR / "database" / "retail_analysis.db"


conn = sqlite3.connect(DATABASE_FILE)

# Enable foreign-key enforcement
conn.execute("PRAGMA foreign_keys = ON;")


print("=== BUILDING RELATIONAL DATABASE ===")


# --------------------------------------------------
# 1. Create tables
# --------------------------------------------------

conn.executescript("""
DROP TABLE IF EXISTS transactions_relational;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS countries;


CREATE TABLE countries (
    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_name TEXT NOT NULL UNIQUE
);


CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY
);


CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    stock_code TEXT NOT NULL,
    description TEXT
);


CREATE TABLE transactions_relational (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_no TEXT,
    product_id INTEGER,
    customer_id INTEGER,
    country_id INTEGER,
    invoice_date TEXT,
    quantity INTEGER,
    unit_price REAL,
    is_zero_quantity INTEGER,
    is_return INTEGER,
    is_zero_price INTEGER,
    is_negative_price INTEGER,
    is_cancelled INTEGER,

    FOREIGN KEY (product_id)
        REFERENCES products(product_id),

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    FOREIGN KEY (country_id)
        REFERENCES countries(country_id)
);
""")


# --------------------------------------------------
# 2. Populate countries
# --------------------------------------------------

conn.execute("""
INSERT INTO countries (country_name)
SELECT DISTINCT Country
FROM transactions
WHERE Country IS NOT NULL;
""")


# --------------------------------------------------
# 3. Populate customers
# --------------------------------------------------

conn.execute("""
INSERT INTO customers (customer_id)
SELECT DISTINCT CAST(CustomerID AS INTEGER)
FROM transactions
WHERE CustomerID IS NOT NULL;
""")


# --------------------------------------------------
# 4. Populate products
# --------------------------------------------------
#
# StockCode + Description is preserved from the source
# because some StockCodes have multiple descriptions.
#

conn.execute("""
INSERT INTO products (stock_code, description)
SELECT DISTINCT
    StockCode,
    Description
FROM transactions
WHERE StockCode IS NOT NULL;
""")


# --------------------------------------------------
# 5. Populate transaction lines
# --------------------------------------------------

conn.execute("""
INSERT INTO transactions_relational (
    invoice_no,
    product_id,
    customer_id,
    country_id,
    invoice_date,
    quantity,
    unit_price,
    is_zero_quantity,
    is_return,
    is_zero_price,
    is_negative_price,
    is_cancelled
)
SELECT
    t.InvoiceNo,

    p.product_id,

    CASE
        WHEN t.CustomerID IS NOT NULL
        THEN CAST(t.CustomerID AS INTEGER)
        ELSE NULL
    END,

    c.country_id,

    t.InvoiceDate,
    t.Quantity,
    t.UnitPrice,
    t.is_zero_quantity,
    t.is_return,
    t.is_zero_price,
    t.is_negative_price,
    t.is_cancelled

FROM transactions AS t

LEFT JOIN products AS p
    ON t.StockCode = p.stock_code
    AND (
        t.Description = p.description
        OR (t.Description IS NULL AND p.description IS NULL)
    )

LEFT JOIN countries AS c
    ON t.Country = c.country_name;
""")


conn.commit()


# --------------------------------------------------
# 6. Validate migration
# --------------------------------------------------

source_count = conn.execute("""
    SELECT COUNT(*)
    FROM transactions;
""").fetchone()[0]


relational_count = conn.execute("""
    SELECT COUNT(*)
    FROM transactions_relational;
""").fetchone()[0]


product_count = conn.execute("""
    SELECT COUNT(*)
    FROM products;
""").fetchone()[0]


customer_count = conn.execute("""
    SELECT COUNT(*)
    FROM customers;
""").fetchone()[0]


country_count = conn.execute("""
    SELECT COUNT(*)
    FROM countries;
""").fetchone()[0]


print()
print("=== MIGRATION RESULTS ===")
print(f"Source transactions:       {source_count:,}")
print(f"Relational transactions:   {relational_count:,}")
print(f"Products:                  {product_count:,}")
print(f"Customers:                 {customer_count:,}")
print(f"Countries:                 {country_count:,}")


if source_count == relational_count:
    print("✓ Transaction row count matches.")
else:
    print("✗ WARNING: Transaction row count does not match!")


# --------------------------------------------------
# 7. Check missing foreign-key mappings
# --------------------------------------------------

missing_products = conn.execute("""
    SELECT COUNT(*)
    FROM transactions_relational
    WHERE product_id IS NULL;
""").fetchone()[0]


missing_countries = conn.execute("""
    SELECT COUNT(*)
    FROM transactions_relational
    WHERE country_id IS NULL;
""").fetchone()[0]


missing_customers = conn.execute("""
    SELECT COUNT(*)
    FROM transactions_relational
    WHERE customer_id IS NULL;
""").fetchone()[0]


print()
print("=== FOREIGN KEY CHECK ===")
print(f"Transactions without product:  {missing_products:,}")
print(f"Transactions without country:  {missing_countries:,}")
print(f"Transactions without customer: {missing_customers:,}")


# --------------------------------------------------
# 8. Check foreign-key integrity
# --------------------------------------------------

foreign_key_errors = conn.execute("""
    PRAGMA foreign_key_check;
""").fetchall()


print()
print("=== FOREIGN KEY INTEGRITY ===")

if not foreign_key_errors:
    print("✓ No foreign-key violations found.")
else:
    print("✗ Foreign-key violations found:")
    for error in foreign_key_errors:
        print(error)


conn.close()

print()
print("Database build completed.")