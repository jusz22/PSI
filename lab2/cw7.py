import asyncio
import aiohttp

async def download_save_file(url: str, path: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(path, 'wb') as f:
                f.write(await response.read())

async def main() -> None:
    await download_save_file("https://gratisography.com/wp-content/uploads/2024/10/gratisography-birthday-dog-sunglasses-1036x780.jpg", "D:/downloads/image.jpg")

if __name__ == "__main__":
    asyncio.run(main())