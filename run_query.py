import sqlite3
from pathlib import Path

import pandas as pd


DB_PATH = Path("ecommerce.db")
QUERY_FILE = Path("query.sql")


def ensure_assets():
    if not DB_PATH.exists():
        raise SystemExit(
            f"Database '{DB_PATH}' not found. Run import_data.py first."
        )
    if not QUERY_FILE.exists():
        raise SystemExit(f"Query file '{QUERY_FILE}' is missing.")


def main():
    query = QUERY_FILE.read_text(encoding="utf-8")
    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query(query, conn)

    if df.empty:
        print("Query returned no rows.")
    else:
        print(df.head(20).to_string(index=False))


if __name__ == "__main__":
    ensure_assets()
    main()
