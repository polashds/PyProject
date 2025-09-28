import asyncio
import json
from datetime import datetime

# ==========================================
# STEP 1 — Fetch Functions (Simulated APIs)
# ==========================================
async def fetch_users(source_id):
    await asyncio.sleep(1)  # simulate I/O
    return [f"{source_id}-Alice", f"{source_id}-Bob"]

async def fetch_products(source_id):
    await asyncio.sleep(1.5)
    return [f"{source_id}-Laptop", f"{source_id}-Phone"]

async def fetch_orders(source_id):
    await asyncio.sleep(0.5)
    return [f"{source_id}-Order1", f"{source_id}-Order2"]

# ==========================================
# STEP 2 — Process Function
# ==========================================
async def process_data(raw_data, source_id):
    users, products, orders = raw_data
    await asyncio.sleep(0.3)  # simulate processing time

    return {
        "source": source_id,
        "timestamp": datetime.utcnow().isoformat(),
        "users_count": len(users),
        "products_count": len(products),
        "orders_count": len(orders),
        "users": users,
        "products": products,
        "orders": orders,
    }

# ==========================================
# STEP 3 — Save Function (Simulated Storage)
# ==========================================
async def save_data(data, filename):
    await asyncio.sleep(0.2)  # simulate write delay
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f" [{data['source']}] Saved to {filename}")

# ==========================================
# SINGLE PIPELINE
# ==========================================
async def data_pipeline(source_id):
    print(f" Starting pipeline for {source_id}...")

    # Step 1: Fetch concurrently
    raw_data = await asyncio.gather(
        fetch_users(source_id),
        fetch_products(source_id),
        fetch_orders(source_id)
    )

    # Step 2: Process
    processed = await process_data(raw_data, source_id)
    print(f" [{source_id}] Data processed.")

    # Step 3: Save
    filename = f"output_{source_id}.json"
    await save_data(processed, filename)

    print(f" [{source_id}] Pipeline complete.")
    return processed

# ==========================================
# MULTIPLE PIPELINES RUNNER
# ==========================================
async def run_multiple_pipelines():
    sources = ["ShopA", "ShopB", "ShopC"]  # imagine different data sources

    # Launch pipelines concurrently
    results = await asyncio.gather(
        *(data_pipeline(source) for source in sources)
    )

    print("\n All pipelines finished!")
    return results

# ==========================================
# ENTRY POINT
# ==========================================
if __name__ == "__main__":
    all_results = asyncio.run(run_multiple_pipelines())

    print("\n Final aggregated results:")
    for result in all_results:
        print(f"• {result['source']} - users: {result['users_count']}, products: {result['products_count']}, orders: {result['orders_count']}")
