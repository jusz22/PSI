import asyncio
import aiohttp

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
        

async def main() -> None:
    urls = ["https://github.com", "https://encyklopedia.pwn.pl", "https://pl.wikipedia.org", "https://www.urbandictionary.com", "https://uwm.edu.pl"]
    html = await asyncio.gather(*(fetch(url) for url in urls))
    print(html)

if __name__ == "__main__":
    asyncio.run(main())
