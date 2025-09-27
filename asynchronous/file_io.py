import aiofiles
import asyncio

async def read_file_async(filename):
    async with aiofiles.open(filename, 'r', encoding='utf-8' ) as f:
        content = await f.read()
    return content

async def main():
    content = await read_file_async("dummy_dataset.csv")
    print(content)


if __name__ == "__main__":
    asyncio.run(main())