import asyncio
import aiosqlite
from datetime import datetime
import random

DB_NAME = "pipelines.db"

# =========================
# DB Initialization
# =========================
async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS pipeline_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT,
                timestamp TEXT,
                users_count INTEGER,
                products_count INTEGER,
                orders_count INTEGER
            )
        """)
        await db.commit()
    print(" Database initialized.")

# =========================
# Retry Wrapper
# =========================
async def retry(coro_func, *args, retries=3, delay=1):
    """Retry a coroutine up to `retries` times with `delay` seconds between attempts."""
    for attempt in range(1, retries + 1):
        try:
            return await coro_func(*args)
        except Exception as e:
            print(f" Attempt {attempt} failed for {args}: {e}")
            if attempt == retries:
                raise
            await asyncio.sleep(delay)

# =========================
# Simulated Fetch Functions
# =========================
async def fetch_users(source_id):
    await asyncio.sleep(random.uniform(0.5, 1.5))
    if random.random() < 0.3:  # 30% chance to fail
        raise RuntimeError(f"User API failed for {source_id}")
    return [f"{source_id}-Alice", f"{source_id}-Bob"]

async def fetch_products(source_id):
    await asyncio.sleep(random.uniform(0.5, 1.5))
    return [f"{source_id}-Laptop", f"{source_id}-Phone"]

async def fetch_orders(source_id):
    await asyncio.sleep(random.uniform(0.5, 1.5))
    return [f"{source_id}-Order1", f"{source_id}-Order2"]

# =========================
# Process Function
# =========================
async def process_data(raw_data, source_id):
    users, products, orders = raw_data
    await asyncio.sleep(0.2)
    return {
        "source": source_id,
        "timestamp": datetime.utcnow().isoformat(),
        "users_count": len(users),
        "products_count": len(products),
        "orders_count": len(orders)
    }

# =========================
# Save to DB
# =========================
async def save_to_db(data):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            INSERT INTO pipeline_results (source, timestamp, users_count, products_count, orders_count)
            VALUES (?, ?, ?, ?, ?)
        """, (
            data["source"],
            data["timestamp"],
            data["users_count"],
            data["products_count"],
            data["orders_count"]
        ))
        await db.commit()
    print(f" [{data['source']}] Saved to DB.")

# =========================
# Single Pipeline with Retry
# =========================
async def data_pipeline(source_id):
    print(f" Starting pipeline for {source_id}...")
    try:
        # Step 1: Fetch concurrently with retry
        raw_data = await asyncio.gather(
            retry(fetch_users, source_id, retries=3, delay=1),
            retry(fetch_products, source_id, retries=3, delay=1),
            retry(fetch_orders, source_id, retries=3, delay=1)
        )

        # Step 2: Process
        processed = await process_data(raw_data, source_id)
        print(f" [{source_id}] Data processed.")

        # Step 3: Save
        await save_to_db(processed)
        print(f" [{source_id}] Pipeline complete.")

        return processed

    except Exception as e:
        print(f" [{source_id}] Pipeline failed after retries: {e}")
        return None

# =========================
# Run Multiple Pipelines
# =========================
async def run_multiple_pipelines():
    sources = ["ShopA", "ShopB", "ShopC", "ShopD"]
    results = await asyncio.gather(
        *(data_pipeline(src) for src in sources)
    )
    results = [r for r in results if r is not None]
    print("\n All pipelines finished.")
    return results

# =========================
# Show DB Contents
# =========================
async def show_db_contents():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT * FROM pipeline_results") as cursor:
            rows = await cursor.fetchall()
            print("\n DB Contents:")
            for row in rows:
                print(row)

# =========================
# Entry Point
# =========================
if __name__ == "__main__":
    asyncio.run(init_db())
    results = asyncio.run(run_multiple_pipelines())
    asyncio.run(show_db_contents())
