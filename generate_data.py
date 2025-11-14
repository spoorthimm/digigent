import os
import random
from datetime import datetime, timedelta

import pandas as pd
from faker import Faker


def ensure_dependencies():
    try:
        import pandas  # noqa: F401
        import faker  # noqa: F401
    except ModuleNotFoundError as exc:
        missing = str(exc).split("'")[1]
        raise SystemExit(
            f"Missing dependency '{missing}'. Run 'pip install pandas faker'."
        ) from exc


def main():
    print("Script started...")

    fake = Faker()
    random.seed(42)

    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)

    num_users = 50
    num_products = 30
    num_orders = 70

    users = [
        {
            "user_id": uid,
            "name": fake.name(),
            "email": fake.email(),
            "city": fake.city(),
            "signup_date": fake.date_between(
                start_date="-2y", end_date="today"
            ),
        }
        for uid in range(1, num_users + 1)
    ]
    pd.DataFrame(users).to_csv(f"{data_dir}/users.csv", index=False)

    categories = ["Electronics", "Fashion", "Home", "Toys", "Sports"]
    products = [
        {
            "product_id": pid,
            "name": fake.word().title(),
            "category": random.choice(categories),
            "price": round(random.uniform(10, 500), 2),
        }
        for pid in range(1, num_products + 1)
    ]
    pd.DataFrame(products).to_csv(f"{data_dir}/products.csv", index=False)

    orders = []
    order_items = []
    payments = []
    order_id = 1
    item_id = 1

    for _ in range(num_orders):
        uid = random.randint(1, num_users)
        order_date = fake.date_between(start_date="-1y", end_date="today")
        orders.append(
            {"order_id": order_id, "user_id": uid, "order_date": order_date}
        )

        num_items = random.randint(1, 4)
        order_total = 0.0

        for _ in range(num_items):
            pid = random.randint(1, num_products)
            qty = random.randint(1, 5)
            price = products[pid - 1]["price"]

            order_items.append(
                {
                    "item_id": item_id,
                    "order_id": order_id,
                    "product_id": pid,
                    "quantity": qty,
                }
            )

            order_total += qty * price
            item_id += 1

        payments.append(
            {
                "payment_id": order_id,
                "order_id": order_id,
                "amount": round(order_total, 2),
                "payment_method": random.choice(["card", "upi", "wallet"]),
                "status": random.choice(
                    ["completed", "pending", "failed"]
                ),
            }
        )

        order_id += 1

    pd.DataFrame(orders).to_csv(f"{data_dir}/orders.csv", index=False)
    pd.DataFrame(order_items).to_csv(f"{data_dir}/order_items.csv", index=False)
    pd.DataFrame(payments).to_csv(f"{data_dir}/payments.csv", index=False)

    print("CSV data generated in data folder!")


if __name__ == "__main__":
    ensure_dependencies()
    main()
