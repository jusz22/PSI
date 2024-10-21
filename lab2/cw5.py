import asyncio
import aiohttp

async def fetch_multiple(url: str, name: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result_data = await response.json()
    return {result_data["hourly"]["temperature_2m"][0] : name}

async def main() -> None:
    urls = {"https://api.open-meteo.com/v1/forecast?latitude=10.9577&longitude=-63.8697&hourly=temperature_2m&timezone=Europe%2FBerlin&forecast_hours=1" : "Porlamar",
    "https://api.open-meteo.com/v1/forecast?latitude=-11.7022&longitude=43.2551&hourly=temperature_2m&timezone=Europe%2FBerlin&forecast_hours=1" : "Moroni",
    "https://api.open-meteo.com/v1/forecast?latitude=60.1100964&longitude=24.6890595&hourly=temperature_2m&timezone=Europe%2FBerlin&forecast_hours=1" : "Helsinki"}
    weather_data = await asyncio.gather(*(fetch_multiple(url, name) for url, name in urls.items()))
    print(weather_data)
    

if __name__ == "__main__":
    asyncio.run(main())