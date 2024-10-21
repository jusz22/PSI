import asyncio
import aiohttp

async def fetch(url: str) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()

async def parse_data(data: dict) -> list:
    return [user["name"] for user in data]

async def save_data(data: list) -> None:
    with open("D:/downloads/data.txt", 'w') as f:
        for name in data:
            f.write(name + "\n")

async def main() -> None:
    url = "https://jsonplaceholder.typicode.com/users"
    
    
    data = await fetch(url)

    parsed_data = await parse_data(data)

    await save_data(parsed_data)

if __name__ == "__main__":
    asyncio.run(main())