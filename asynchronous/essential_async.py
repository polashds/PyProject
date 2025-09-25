import asyncio

async def fetch_data():
    await asyncio.sleep(2)
    return 'data fetched' 

async def main():
    result = await fetch_data()
    print(result)

if __name__ == '__main__':
    asyncio.run(main())