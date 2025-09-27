import aiofiles
import asyncio
from pathlib import Path

# Define your parent dir once
BASE_DIR = Path(r"e:\Py-Projects-Vault\PyProject\asynchronous")

async def read_file_async(filename):
    filepath = BASE_DIR / filename
    async with aiofiles.open(filepath, 'r', encoding='utf-8') as f:
        content = await f.read()
    return content

async def main():
    content = await read_file_async("dummy_dataset.csv")
    print(content)

if __name__ == "__main__":
    asyncio.run(main())
