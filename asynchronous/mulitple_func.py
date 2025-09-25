import asyncio
import time

async def task_one():
    await asyncio.sleep(1)
    print("Task One Done")

async def task_two():
    await asyncio.sleep(2)
    print("Task Two Done")

async def main():
    results = await asyncio.gather(task_one(),
                                   task_two())
    print(results)

asyncio.run(main())