import asyncio
import aiohttp

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
        

async def main() -> None:
    html = await fetch("https://uwm.edu.pl/")
    print(html)

if __name__ == "__main__":
    asyncio.run(main())
