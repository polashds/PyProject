import asyncio

async def fast_task():
    await asyncio.sleep(1)
    return "fast done"

async def slow_task():
    await asyncio.sleep(10)
    return "slow done"

async def common_patterns():
    # 1️⃣ Sleep
    await asyncio.sleep(0.1)
    print("Slept for 0.1 sec")

    # 2️⃣ Wait for first to complete
    task1 = asyncio.create_task(fast_task())
    task2 = asyncio.create_task(slow_task())
    done, pending = await asyncio.wait([task1, task2], return_when=asyncio.FIRST_COMPLETED)
    print(f"Done: {done}, Pending: {pending}")

    # 3️⃣ Wait with timeout
    try:
        result = await asyncio.wait_for(slow_task(), timeout=5.0)
        print(f"Result: {result}")
    except asyncio.TimeoutError:
        print("Task timed out!")

asyncio.run(common_patterns())
