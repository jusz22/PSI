import asyncio
import aiohttp

async def fetch(url: str):
    async with aiohttp.ClientSession() as session:
        for _ in range(3):
            async with session.get(url) as response:
                if 200 <= response.status <= 299:
                    return await response.json()
                elif 500 <= response.status <= 599:
                    await asyncio.sleep(.5)
                else:
                    return None
    return None
                
async def main() -> None:
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.5244&longitude=13.4105&forecast_days=1"
    results = await asyncio.gather(*(fetch(url) for _ in range(100)))
    successful_responses = [result for result in results if result is not None]
    for response in successful_responses:
        print(response)

if __name__ == "__main__":
    asyncio.run(main())