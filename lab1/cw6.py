import asyncio
import random

async def fetch(delay: int) -> int:
    await asyncio.sleep(delay)
    return random.randint(0, 10)

async def main() -> None:
    result = await asyncio.gather(*(fetch(i) for i in range(1, 4)))
    print(result)

if __name__ == "__main__":
    asyncio.run(main())