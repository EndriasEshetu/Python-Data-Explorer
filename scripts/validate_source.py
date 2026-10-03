import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "cleaned_transactions.csv"


df = pd.read_csv(DATA_FILE)


print("=== SOURCE CSV VALIDATION ===")
print(f"CSV records: {len(df):,}")
print(f"CSV columns: {len(df.columns)}")
print()
print("Columns:")
for column in df.columns:
    print(f" - {column}")