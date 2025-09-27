import aiofiles
import asyncio
import os

async def read_file_async(filename):
    # Always resolve relative to this script's directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_dir, filename)

    async with aiofiles.open(filepath, 'r', encoding='utf-8') as f:
        content = await f.read()
    return content

async def main():
    content = await read_file_async("dummy_dataset.csv")
    print(content)

if __name__ == "__main__":
    asyncio.run(main())
