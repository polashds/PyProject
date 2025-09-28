import asyncio
import aiosqlite   # async wrapper around sqlite3
from datetime import datetime
import random

# ==========================================
# STEP 0 — Database Setup (one-time)
# ==========================================
DB_NAME = "pipelines.db"

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

# ==========================================
# STEP 1 — Simulated Fetch Functions
# ==========================================
async def fetch_users(source_id):
    await asyncio.sleep(random.uniform(0.5, 1.5))
    # Random failure simulation
    if random.random() < 0.2:
        raise RuntimeError(f"User API failed for {source_id}")
    return [f"{source_id}-Alice", f"{source_id}-Bob"]

async def fetch_products(source_id):
    await asyncio.sleep(random.uniform(0.5, 1.5))
    return [f"{source_id}-Laptop", f"{source_id}-Phone"]

async def fetch_orders(source_id):
    await asyncio.sleep(random.uniform(0.5, 1.5))
    return [f"{source_id}-Order1", f"{source_id}-Order2"]

# ==========================================
# STEP 2 — Processing Function
# ==========================================
async def process_data(raw_data, source_id):
    users, products, orders = raw_data
    await asyncio.sleep(0.2)  # simulate processing time
    return {
        "source": source_id,
        "timestamp": datetime.utcnow().isoformat(),
        "users_count": len(users),
        "products_count": len(products),
        "orders_count": len(orders)
    }

# ==========================================
# STEP 3 — Save to SQLite
# ==========================================
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

# ==========================================
# SINGLE PIPELINE (with error handling)
# ==========================================
async def data_pipeline(source_id):
    print(f" Starting pipeline for {source_id}...")

    try:
        # Step 1: Fetch concurrently
        raw_data = await asyncio.gather(
            fetch_users(source_id),
            fetch_products(source_id),
            fetch_orders(source_id)
        )

        # Step 2: Process
        processed = await process_data(raw_data, source_id)
        print(f" [{source_id}] Data processed.")

        # Step 3: Save to DB
        await save_to_db(processed)
        print(f" [{source_id}] Pipeline complete.")

        return processed

    except Exception as e:
        # Handle failures gracefully per pipeline
        print(f" [{source_id}] Pipeline failed: {e}")
        return None

# ==========================================
# MULTIPLE PIPELINES RUNNER
# ==========================================
async def run_multiple_pipelines():
    sources = ["ShopA", "ShopB", "ShopC", "ShopD"]  # Multiple sources

    # Run pipelines concurrently
    results = await asyncio.gather(
        *(data_pipeline(src) for src in sources)
    )

    # Filter out failed pipelines
    results = [r for r in results if r is not None]

    print("\n All pipelines finished.")
    return results

# ==========================================
# DB INSPECTION HELPER
# ==========================================
async def show_db_contents():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT * FROM pipeline_results") as cursor:
            rows = await cursor.fetchall()
            print("\n DB Contents:")
            for row in rows:
                print(row)

# ==========================================
# ENTRY POINT
# ==========================================
if __name__ == "__main__":
    asyncio.run(init_db())              # Create table if not exists
    results = asyncio.run(run_multiple_pipelines())  # Run pipelines
    asyncio.run(show_db_contents())     # Inspect DB
