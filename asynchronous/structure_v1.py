import asyncio
import json
from datetime import datetime

# =========================
# Step 1: Fetch data
# =========================

async def fetch_users():
    await asyncio.sleep(1)  # simulate API call
    return ["Alice", "Bob"]

async def fetch_products():
    await asyncio.sleep(1.5)  # simulate API call
    return ["Laptop", "Phone"]

async def fetch_orders():
    await asyncio.sleep(0.5)  # simulate API call
    return ["Order1", "Order2"]

# =========================
# Step 2: Process data
# =========================

async def process_data(raw_data):
    users, products, orders = raw_data

    # Example transformation
    summary = {
        "timestamp": datetime.utcnow().isoformat(),
        "users_count": len(users),
        "products_count": len(products),
        "orders_count": len(orders),
        "users": users,
        "products": products,
        "orders": orders,
    }

    # Simulate some CPU-bound work (could be AI model, parsing, etc.)
    await asyncio.sleep(0.5)
    return summary

# =========================
# Step 3: Save processed data
# =========================

async def save_data(data, filename="pipeline_output.json"):
    # Simulate I/O (writing to file or database)
    await asyncio.sleep(0.5)

    # Here we'll just write to a JSON file
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f" Data saved to {filename}")

# =========================
# Pipeline Runner
# =========================

async def data_pipeline():
    print(" Starting data pipeline...")

    # Step 1: Fetch concurrently
    raw_data = await asyncio.gather(
        fetch_users(),
        fetch_products(),
        fetch_orders()
    )

    # Step 2: Process
    processed = await process_data(raw_data)
    print(" Data processed.")

    # Step 3: Save
    await save_data(processed)
    print(" Pipeline complete.")

    return processed

# =========================
# Entry point
# =========================

if __name__ == "__main__":
    result = asyncio.run(data_pipeline())
    print(" Final Result:", result)
