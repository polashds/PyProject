import asyncio

async def fetch_users():
    await asyncio.sleep(1)
    return ["Alice", "Bob"]

async def fetch_products():
    await asyncio.sleep(1.5)
    return ["Laptop", "Phone"]

async def fetch_orders():
    await asyncio.sleep(0.5)
    return ["Order1", "Order2"]

async def process_data(raw_data):
    users, products, orders = raw_data
    return {
        "users_count": len(users),
        "products_count": len(products),
        "orders_count": len(orders)
    }

async def data_pipeline():
    # Step 1: Fetch concurrently
    raw_data = await asyncio.gather(
        fetch_users(),
        fetch_products(),
        fetch_orders()
    )

    # Step 2: Process
    processed = await process_data(raw_data)
    return processed

if __name__ == "__main__":
    result = asyncio.run(data_pipeline())
    print("Processed Data:", result)
