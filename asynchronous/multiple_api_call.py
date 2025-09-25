import aiohttp
import asyncio
import time
import json

async def fetch(seeion, url):
    async with seeion.get(url) as response:
        return await response.text()
    
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['http://example.com', 'http://example.org']
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

if __name__ == "__main__":
    html_pages = asyncio.run(main())
    for i, page in enumerate(html_pages, start=1):
        print(f"Page {i} length:", len(page))
