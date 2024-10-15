import asyncio
import aiohttp

async def fetch(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
        

async def main() -> None:
    url = "https://api.open-meteo.com/v1/forecast?latitude=49.299&longitude=19.9489&hourly=temperature_2m&timezone=Europe%2FBerlin&forecast_days=1&forecast_hours=1"
    weather_data = await fetch(url)
    print(weather_data["hourly"]["temperature_2m"])

if __name__ == "__main__":
    asyncio.run(main())