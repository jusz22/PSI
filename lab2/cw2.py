import asyncio
from multiprocessing.connection import Client
import aiohttp

async def add_user(url: str, header: dict, body: dict) -> dict:
    async with aiohttp.ClientSession(headers=header) as session:
        async with session.post(url, data=body) as response:
            return await response.json()
        

async def main() -> None:
    url = "https://670bef0e7e5a228ec1cf1824.mockapi.io/api/v1/user"
    header = {"Token": "Bearer SOME_CHARS"}
    body = {"name": "Jan Jusz", "avatar": "https://www.wp.pl"}
    status = await add_user(url, header, body)
    print(status)

if __name__ == "__main__":
    asyncio.run(main())