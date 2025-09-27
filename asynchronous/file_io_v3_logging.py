import aiofiles
import asyncio
import logging
from pathlib import Path

# logging setup
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Define your parent dir once
BASE_DIR = Path(r"e:\Py-Projects-Vault\PyProject\asynchronous")

async def read_file_async(filename):
    filepath = BASE_DIR / filename
    logging.info(f"Reading file: {filepath}")

    async with aiofiles.open(filepath, 'r', encoding='utf-8') as f:
        content = await f.read()
    return content

async def main():
    logging.info("proram started")
    content = await read_file_async("dummy_dataset.csv")
    print(content)


if __name__ == "__main__":
    asyncio.run(main())