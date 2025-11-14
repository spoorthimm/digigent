import sqlite3
from pathlib import Path

import pandas as pd


DB_FILE = Path("ecommerce.db")
DATA_DIR = Path("data")
TABLE_FILES = {
    "users": "users.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "payments": "payments.csv",
}


def validate_inputs():
    if not DATA_DIR.exists():
        raise SystemExit(
            f"Input folder '{DATA_DIR}' not found. Run generate_data.py first."
        )

    missing = [
        table
        for table, filename in TABLE_FILES.items()
        if not (DATA_DIR / filename).exists()
    ]
    if missing:
        raise SystemExit(
            f"Missing CSV files for tables: {', '.join(missing)}. "
            "Re-run generate_data.py."
        )


def main():
    with sqlite3.connect(DB_FILE) as conn:
        for table, filename in TABLE_FILES.items():
            csv_path = DATA_DIR / filename
            df = pd.read_csv(csv_path)
            df.to_sql(table, conn, if_exists="replace", index=False)

    print(f"Data successfully loaded into {DB_FILE}!")


if __name__ == "__main__":
    validate_inputs()
    main()
