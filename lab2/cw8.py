import asyncio
import aiohttp

async def fetch(url: str) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()
            
async def get_mean_temp(weather: dict):
    return sum(weather["hourly"]["temperature_2m"]) / len(weather["hourly"]["temperature_2m"])
            
async def sort_temp(response: dict):
     return 

async def build_result(cities: dict):
    city_mean_temp = []
    all_weather = await asyncio.gather(*(fetch(url) for url in cities.values()))
    for city, weather in zip(cities.keys(), all_weather):
        mean_temp = await get_mean_temp(weather)
        city_mean_temp.append((city, mean_temp))

    sorted_city_temp = sorted(city_mean_temp, key= lambda x: x[1], reverse=True)
    return {city: temp for city, temp in sorted_city_temp}
     

async def main() -> None:
     cities = {"London" : "https://api.open-meteo.com/v1/forecast?latitude=51.5085&longitude=-0.1257&hourly=temperature_2m&forecast_days=1",
               "Warsaw": "https://api.open-meteo.com/v1/forecast?latitude=52.2298&longitude=21.0118&hourly=temperature_2m&forecast_days=1",
               "Berlin": "https://api.open-meteo.com/v1/forecast?latitude=52.5244&longitude=13.4105&hourly=temperature_2m&forecast_days=1"}
     weather = await build_result(cities)
     print(weather)


if __name__ == "__main__":
    asyncio.run(main())